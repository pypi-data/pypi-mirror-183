# Copyright (c) 2018-2021 Kaiyang Zhou
# SPDX-License-Identifier: MIT
#
# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
#

# pylint: disable=too-many-branches

from __future__ import print_function, absolute_import
import torch
from torch import nn

import warnings

from .sam import SAM
from .radam import RAdam
from torchreid.integration.nncf.compression import get_compression_parameter
from torchreid.utils import get_model_attr

AVAI_OPTIMS = {'adam', 'amsgrad', 'sgd', 'rmsprop', 'radam', 'sam'}

def build_optimizer(model, optim, base_optim, lr_finder, **kwargs):
    """A wrapper function for building an optimizer.

    Args:
        model (nn.Module): model.
        optim (str, optional): optimizer. Default is "adam".
        lr (float, optional): learning rate. Default is 0.0003.
        weight_decay (float, optional): weight decay (L2 penalty). Default is 5e-04.
        momentum (float, optional): momentum factor in sgd. Default is 0.9,
        sgd_dampening (float, optional): dampening for momentum. Default is 0.
        sgd_nesterov (bool, optional): enables Nesterov momentum. Default is False.
        rmsprop_alpha (float, optional): smoothing constant for rmsprop. Default is 0.99.
        adam_beta1 (float, optional): beta-1 value in adam. Default is 0.9.
        adam_beta2 (float, optional): beta-2 value in adam. Default is 0.99,
        staged_lr (bool, optional): uses different learning rates for base and new layers. Base
            layers are pretrained layers while new layers are randomly initialized, e.g. the
            identity classification layer. Enabling ``staged_lr`` can allow the base layers to
            be trained with a smaller learning rate determined by ``base_lr_mult``, while the new
            layers will take the ``lr``. Default is False.
        new_layers (str or list): attribute names in ``model``. Default is empty.
        base_lr_mult (float, optional): learning rate multiplier for base layers. Default is 0.1.
        sam_rho (float, optional): Scale factor for SAM optimizer

    Examples::
        >>> # A normal optimizer can be built by
        >>> optimizer = torchreid.optim.build_optimizer(model, optim='sgd', lr=0.01)
        >>> # If you want to use a smaller learning rate for pretrained layers
        >>> # and the attribute name for the randomly initialized layer is 'classifier',
        >>> # you can do
        >>> optimizer = torchreid.optim.build_optimizer(
        >>>     model, optim='sgd', lr=0.01, staged_lr=True,
        >>>     new_layers='classifier', base_lr_mult=0.1
        >>> )
        >>> # Now the `classifier` has learning rate 0.01 but the base layers
        >>> # have learning rate 0.01 * 0.1.
        >>> # new_layers can also take multiple attribute names. Say the new layers
        >>> # are 'fc' and 'classifier', you can do
        >>> optimizer = torchreid.optim.build_optimizer(
        >>>     model, optim='sgd', lr=0.01, staged_lr=True,
        >>>     new_layers=['fc', 'classifier'], base_lr_mult=0.1
        >>> )
    """
    if optim == 'sam':
        if lr_finder:
            optimizer = _build_optim(model, optim=base_optim, base_optim=None, lr_finder=lr_finder, **kwargs)
            return optimizer
        base_optim = _build_optim(model, optim=base_optim, base_optim=None, **kwargs)
        optimizer = _build_optim(model, optim=optim, base_optim=base_optim, **kwargs)
    else:
        optimizer = _build_optim(model, optim=optim, base_optim=None,  lr_finder=lr_finder, **kwargs)

    return optimizer

def _build_optim(model,
                 optim='adam',
                 base_optim='sgd',
                 lr=0.0003,
                 weight_decay=5e-04,
                 momentum=0.9,
                 sgd_dampening=0,
                 sgd_nesterov=False,
                 rmsprop_alpha=0.99,
                 adam_beta1=0.9,
                 adam_beta2=0.99,
                 staged_lr=False,
                 new_layers='',
                 base_lr_mult=0.1,
                 nbd=False,
                 lr_finder=False,
                 sam_rho = 0.05,
                 sam_adaptive=False):

    param_groups = []
    if optim not in AVAI_OPTIMS:
        raise ValueError(
            f'Unsupported optimizer: {optim}. Must be one of {AVAI_OPTIMS}'
        )

    if isinstance(base_optim, SAM):
        raise ValueError(
            'Invalid base optimizer. SAM cannot be the base one'
        )

    if not isinstance(model, nn.Module):
        raise TypeError(
            'model given to build_optimizer must be an instance of nn.Module'
        )

    if staged_lr:
        if isinstance(new_layers, str):
            if new_layers is None:
                warnings.warn(
                    'new_layers is empty, therefore, staged_lr is useless'
                )
            new_layers = [new_layers]

        base_params = []
        base_layers = []
        new_params = []

        for name, module in model.named_children():
            if name in new_layers:
                new_params += list(module.parameters())
            else:
                base_params += list(module.parameters())
                base_layers.append(name)

        param_groups = [
            {
                'params': base_params,
                'lr': lr * base_lr_mult
            },
            {
                'params': new_params
            },
        ]

    # we switch off nbd when lr_finder enabled
    # because optimizer builded once and lr in biases isn't changed
    elif nbd and not lr_finder:
        compression_params = set()
        CompressionParameter = get_compression_parameter()
        if CompressionParameter:
            for param_group in get_model_attr(model, 'get_config_optim')(lr):
                layer_params = param_group['params']
                for name, param in layer_params:
                    if param.requires_grad and isinstance(param, CompressionParameter):
                        compression_params.add(param)

        for param_group in get_model_attr(model, 'get_config_optim')(lr):
            if 'weight_decay' in param_group:
                # weight_decay is already set for these parameters
                param_groups.append(param_group)
                continue

            decay, bias_no_decay, weight_no_decay = [], [], []
            group_lr = param_group['lr']
            layer_params = param_group['params']
            for name, param in layer_params:
                if param in compression_params:
                    continue  # Param is already registered
                if not param.requires_grad:
                    continue  # frozen weights
                if name.endswith("bias"):
                    bias_no_decay.append(param)
                elif len(param.shape) == 1:
                    weight_no_decay.append(param)
                elif (name.endswith("weight") and ("norm" in name or "query_embed" in name)):
                    weight_no_decay.append(param)
                else:
                    decay.append(param)

            cur_params = [{'params': decay, 'lr': group_lr, 'weight_decay': weight_decay},
                          {'params': bias_no_decay, 'lr': 2 * group_lr, 'weight_decay': 0.0},
                          {'params': weight_no_decay, 'lr': group_lr, 'weight_decay': 0.0}]
            param_groups.extend(cur_params)

        if compression_params:
            param_groups.append({'params': list(compression_params), 'lr': lr, 'weight_decay': 0.0})
    else:
        for param_group in get_model_attr(model, 'get_config_optim')(lr):
            group_weight_decay = param_group['weight_decay'] if 'weight_decay' in param_group else weight_decay
            param_groups.append({'params': [param for _, param in param_group['params']],
                                 'lr': param_group['lr'],
                                 'weight_decay': group_weight_decay})

    if optim == 'adam':
        optimizer = torch.optim.AdamW(
            param_groups,
            betas=(adam_beta1, adam_beta2),
        )

    elif optim == 'amsgrad':
        optimizer = torch.optim.AdamW(
            param_groups,
            betas=(adam_beta1, adam_beta2),
            amsgrad=True,
        )

    elif optim == 'sgd':
        optimizer = torch.optim.SGD(
            param_groups,
            momentum=momentum,
            dampening=sgd_dampening,
            nesterov=sgd_nesterov,
        )

    elif optim == 'rmsprop':
        optimizer = torch.optim.RMSprop(
            param_groups,
            momentum=momentum,
            alpha=rmsprop_alpha,
        )

    elif optim == 'radam':
        optimizer = RAdam(
            param_groups,
            betas=(adam_beta1, adam_beta2)
        )

    if optim == 'sam':
        if not base_optim:
            raise ValueError("SAM cannot operate without base optimizer. "
                                "Please add it to configuration file")
        optimizer = SAM(
            params=param_groups,
            base_optimizer=base_optim,
            rho=sam_rho,
            adaptive=sam_adaptive
        )

    return optimizer
