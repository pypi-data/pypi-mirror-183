from .base import BaseScaler
import torch


class ScaleScaler(BaseScaler):

    def __init__(self):
        self.scale_ = None

    def _fit_params(self, x, dims=None):
        if isinstance(dims, tuple):
            scale_ = x.std(dims, keepdims=True)
        elif isinstance(dims, list):
            raise Exception('dims should be None or a tuple!')
        else:
            scale_ = x.std()
        params = {'scale_': scale_}
        return params

    def aggregate_param(self, name, param):
        if name == 'scale_':
            param_new = torch.mean(param, dim=0)
        else:
            raise NotImplementedError

        return param_new

    def fit_manual(self):
        self.scale_ = 1.0

    def _transform(self, x, inplace):
        return x / self.scale_

    def _inverse_transform(self, x_norm, inplace):
        return x_norm * self.scale_
