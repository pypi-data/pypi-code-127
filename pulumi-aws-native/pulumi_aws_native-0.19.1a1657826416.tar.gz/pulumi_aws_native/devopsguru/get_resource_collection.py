# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'GetResourceCollectionResult',
    'AwaitableGetResourceCollectionResult',
    'get_resource_collection',
    'get_resource_collection_output',
]

@pulumi.output_type
class GetResourceCollectionResult:
    def __init__(__self__, resource_collection_filter=None, resource_collection_type=None):
        if resource_collection_filter and not isinstance(resource_collection_filter, dict):
            raise TypeError("Expected argument 'resource_collection_filter' to be a dict")
        pulumi.set(__self__, "resource_collection_filter", resource_collection_filter)
        if resource_collection_type and not isinstance(resource_collection_type, str):
            raise TypeError("Expected argument 'resource_collection_type' to be a str")
        pulumi.set(__self__, "resource_collection_type", resource_collection_type)

    @property
    @pulumi.getter(name="resourceCollectionFilter")
    def resource_collection_filter(self) -> Optional['outputs.ResourceCollectionFilter']:
        return pulumi.get(self, "resource_collection_filter")

    @property
    @pulumi.getter(name="resourceCollectionType")
    def resource_collection_type(self) -> Optional['ResourceCollectionType']:
        """
        The type of ResourceCollection
        """
        return pulumi.get(self, "resource_collection_type")


class AwaitableGetResourceCollectionResult(GetResourceCollectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceCollectionResult(
            resource_collection_filter=self.resource_collection_filter,
            resource_collection_type=self.resource_collection_type)


def get_resource_collection(resource_collection_type: Optional['ResourceCollectionType'] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceCollectionResult:
    """
    This resource schema represents the ResourceCollection resource in the Amazon DevOps Guru.


    :param 'ResourceCollectionType' resource_collection_type: The type of ResourceCollection
    """
    __args__ = dict()
    __args__['resourceCollectionType'] = resource_collection_type
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:devopsguru:getResourceCollection', __args__, opts=opts, typ=GetResourceCollectionResult).value

    return AwaitableGetResourceCollectionResult(
        resource_collection_filter=__ret__.resource_collection_filter,
        resource_collection_type=__ret__.resource_collection_type)


@_utilities.lift_output_func(get_resource_collection)
def get_resource_collection_output(resource_collection_type: Optional[pulumi.Input['ResourceCollectionType']] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceCollectionResult]:
    """
    This resource schema represents the ResourceCollection resource in the Amazon DevOps Guru.


    :param 'ResourceCollectionType' resource_collection_type: The type of ResourceCollection
    """
    ...
