# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetCustomClassResult',
    'AwaitableGetCustomClassResult',
    'get_custom_class',
    'get_custom_class_output',
]

@pulumi.output_type
class GetCustomClassResult:
    def __init__(__self__, custom_class_id=None, items=None, name=None):
        if custom_class_id and not isinstance(custom_class_id, str):
            raise TypeError("Expected argument 'custom_class_id' to be a str")
        pulumi.set(__self__, "custom_class_id", custom_class_id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="customClassId")
    def custom_class_id(self) -> str:
        """
        If this custom class is a resource, the custom_class_id is the resource id of the CustomClass. Case sensitive.
        """
        return pulumi.get(self, "custom_class_id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.ClassItemResponse']:
        """
        A collection of class items.
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the custom class.
        """
        return pulumi.get(self, "name")


class AwaitableGetCustomClassResult(GetCustomClassResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCustomClassResult(
            custom_class_id=self.custom_class_id,
            items=self.items,
            name=self.name)


def get_custom_class(custom_class_id: Optional[str] = None,
                     location: Optional[str] = None,
                     project: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCustomClassResult:
    """
    Get a custom class.
    """
    __args__ = dict()
    __args__['customClassId'] = custom_class_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:speech/v1:getCustomClass', __args__, opts=opts, typ=GetCustomClassResult).value

    return AwaitableGetCustomClassResult(
        custom_class_id=__ret__.custom_class_id,
        items=__ret__.items,
        name=__ret__.name)


@_utilities.lift_output_func(get_custom_class)
def get_custom_class_output(custom_class_id: Optional[pulumi.Input[str]] = None,
                            location: Optional[pulumi.Input[str]] = None,
                            project: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCustomClassResult]:
    """
    Get a custom class.
    """
    ...
