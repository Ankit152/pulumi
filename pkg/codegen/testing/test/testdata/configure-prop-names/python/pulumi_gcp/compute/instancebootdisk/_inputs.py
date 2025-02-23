# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ... import compute as _compute

__all__ = [
    'InstanceBootDiskArgs',
]

@pulumi.input_type
class InstanceBootDiskArgs:
    def __init__(__self__, *,
                 initialize_params: Optional[pulumi.Input['_compute.instancebootdiskinitializeparams.InstanceBootDiskInitializeParamsArgs']] = None):
        """
        :param pulumi.Input['_compute.instancebootdiskinitializeparams.InstanceBootDiskInitializeParamsArgs'] initialize_params: Parameters for a new disk that will be created
               alongside the new instance. Either `initialize_params` or `source` must be set.
               Structure is documented below.
        """
        InstanceBootDiskArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            initialize_params=initialize_params,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             initialize_params: Optional[pulumi.Input['_compute.instancebootdiskinitializeparams.InstanceBootDiskInitializeParamsArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'initializeParams' in kwargs:
            initialize_params = kwargs['initializeParams']

        if initialize_params is not None:
            _setter("initialize_params", initialize_params)

    @property
    @pulumi.getter(name="initializeParams")
    def initialize_params(self) -> Optional[pulumi.Input['_compute.instancebootdiskinitializeparams.InstanceBootDiskInitializeParamsArgs']]:
        """
        Parameters for a new disk that will be created
        alongside the new instance. Either `initialize_params` or `source` must be set.
        Structure is documented below.
        """
        return pulumi.get(self, "initialize_params")

    @initialize_params.setter
    def initialize_params(self, value: Optional[pulumi.Input['_compute.instancebootdiskinitializeparams.InstanceBootDiskInitializeParamsArgs']]):
        pulumi.set(self, "initialize_params", value)


