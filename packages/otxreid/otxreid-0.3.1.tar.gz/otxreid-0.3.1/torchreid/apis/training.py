"""
 Copyright (c) 2021 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import sys
from copy import deepcopy
import shutil
from os import path as osp

import torchreid
from torchreid.engine import build_engine
from torchreid.integration.nncf.compression import is_accuracy_aware_training_set
from torchreid.integration.nncf.engine import run_acc_aware_training_loop
from torchreid.optim import LrFinder
from scripts.default_config import (lr_finder_run_kwargs,
                                    lr_scheduler_kwargs, model_kwargs,
                                    optimizer_kwargs, engine_run_kwargs)
from torchreid.utils import set_random_seed
from scripts.script_utils import (build_datamanager, build_auxiliary_model,
                                  put_main_model_on_the_device)


def run_lr_finder(cfg, datamanager, model, optimizer, scheduler, classes,
                  rebuild_model=True, gpu_num=1, split_models=False):
    if not rebuild_model:
        backup_model = deepcopy(model)

    engine = build_engine(cfg, datamanager, model, optimizer, scheduler, initial_lr=cfg.train.lr)
    lr_finder = LrFinder(engine=engine, **lr_finder_run_kwargs(cfg))
    aux_lr = lr_finder.process()

    print(f"Estimated learning rate: {aux_lr}")
    if cfg.lr_finder.stop_after:
        print("Finding learning rate finished. Terminate the training process")
        sys.exit(0)

    # reload all parts of the training
    # we do not check classification parameters
    # and do not get num_train_classes the second time
    # since it's done above and lr finder cannot change parameters of the datasets
    cfg.train.lr = aux_lr
    cfg.lr_finder.enable = False
    set_random_seed(cfg.train.seed, cfg.train.deterministic)
    datamanager = build_datamanager(cfg, classes)
    num_train_classes = datamanager.num_train_ids

    if rebuild_model:
        backup_model = torchreid.models.build_model(**model_kwargs(cfg, num_train_classes))
        num_aux_models = len(cfg.mutual_learning.aux_configs)
        backup_model, _ = put_main_model_on_the_device(backup_model, cfg.use_gpu, gpu_num, num_aux_models, split_models)

    optimizer = torchreid.optim.build_optimizer(backup_model, **optimizer_kwargs(cfg))
    scheduler = torchreid.optim.build_lr_scheduler(optimizer=optimizer,
                                                   num_iter=datamanager.num_iter,
                                                   **lr_scheduler_kwargs(cfg))

    return cfg.train.lr, backup_model, optimizer, scheduler


def run_training(cfg, datamanager, model, optimizer, scheduler, extra_device_ids, init_lr,
                 tb_writer=None, perf_monitor=None, stop_callback=None,
                 aux_config_opts=None,
                 aux_pretrained_dicts=None,
                 should_freeze_aux_models=None,
                 nncf_metainfo=None,
                 compression_ctrl=None):
    num_aux_models = len(cfg.mutual_learning.aux_configs)
    num_train_classes = datamanager.num_train_ids

    if num_aux_models > 0:
        print(f'Enabled mutual learning between {len(cfg.mutual_learning.aux_configs) + 1} models.')

        nncf_aux_config_changes = cfg.get('nncf_aux_config_changes', [None] * num_aux_models)
        if aux_pretrained_dicts is None:
            aux_pretrained_dicts = [None] * num_aux_models
        models, optimizers, schedulers = [model], [optimizer], [scheduler]
        aux_configs = []
        for config_file, device_ids, pretrained_dict, nncf_config_changes in zip(cfg.mutual_learning.aux_configs,
                                                                                 extra_device_ids,
                                                                                 aux_pretrained_dicts,
                                                                                 nncf_aux_config_changes):
            if aux_config_opts is None:
                aux_config_opts = []
            aux_config_opts.extend(['train.mix_precision', cfg.train.mix_precision])
            aux_model, aux_optimizer, aux_scheduler, aux_cfg = build_auxiliary_model(
                config_file, num_train_classes, cfg.use_gpu, device_ids, num_iter=datamanager.num_iter,
                lr=init_lr, nncf_aux_config_changes=nncf_config_changes,
                aux_config_opts=aux_config_opts, aux_pretrained_dict=pretrained_dict
            )

            models.append(aux_model)
            optimizers.append(aux_optimizer)
            schedulers.append(aux_scheduler)
            aux_configs.append(aux_cfg)
    else:
        models, optimizers, schedulers = model, optimizer, scheduler
    print(f'Building {cfg.loss.name}-engine')
    engine = build_engine(cfg, datamanager, models, optimizers, schedulers,
                          should_freeze_aux_models=should_freeze_aux_models,
                          nncf_metainfo=nncf_metainfo,
                          compression_ctrl=compression_ctrl,
                          initial_lr=init_lr)

    accuracy = None
    final_accuracy = None
    if (cfg.test.test_before_train or
        cfg.test.evaluate or
        cfg.test.save_initial_metric):
        if cfg.test.test_before_train:
            print('Test before training')
        accuracy = engine.test(0, test_only=True)[0]
        if cfg.test.evaluate:
            return accuracy, None

        if cfg.test.save_initial_metric:
            model_weight_file = None
            if cfg.model.resume:
                model_weight_file = cfg.model.resume
            elif cfg.model.load_weights:
                model_weight_file = cfg.model.load_weights
            if model_weight_file is not None:
                shutil.copy(model_weight_file,
                    osp.join(cfg.data.save_dir, "best.pth"))
            engine.best_metric = accuracy

    nncf_config = cfg.get('nncf_config')
    if nncf_config is not None and is_accuracy_aware_training_set(nncf_config):
        def configure_optimizers_fn():
            optimizer = torchreid.optim.build_optimizer(model, **optimizer_kwargs(cfg))
            scheduler = torchreid.optim.build_lr_scheduler(optimizer, num_iter=datamanager.num_iter,
                                                           **lr_scheduler_kwargs(cfg))

            optimizers = [optimizer]
            schedulers = [scheduler]
            if num_aux_models > 0:
                for aux_cfg in aux_configs:
                    aux_optimizer = torchreid.optim.build_optimizer(model, **optimizer_kwargs(aux_cfg))
                    aux_scheduler = torchreid.optim.build_lr_scheduler(optimizer=aux_optimizer,
                                                                       num_iter=datamanager.num_iter,
                                                                       **lr_scheduler_kwargs(aux_cfg))
                    optimizers.append(aux_optimizer)
                    schedulers.append(aux_scheduler)
            return optimizers, schedulers

        run_acc_aware_training_loop(engine, nncf_config, configure_optimizers_fn,
                                    stop_callback=stop_callback, perf_monitor=perf_monitor)
    else:
        _, final_accuracy = engine.run(**engine_run_kwargs(cfg), tb_writer=tb_writer,
                                       perf_monitor=perf_monitor, stop_callback=stop_callback)

    return accuracy, final_accuracy
