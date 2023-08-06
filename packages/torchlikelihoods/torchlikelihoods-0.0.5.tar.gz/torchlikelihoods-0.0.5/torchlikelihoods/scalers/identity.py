from .base import BaseScaler


class IdentityScaler(BaseScaler):
    def __init__(self):
        return

    def _fit_params(self, x, dims=None):
        return {}

    def aggregate_param(self, name, param):
        return param

    def fit_manual(self):
        return

    def fit_with_loader(self, loader):
        return

    def _transform(self, x, inplace):
        return x

    def _inverse_transform(self, x_norm, inplace):
        return x_norm
