# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetPlacementResult',
    'AwaitableGetPlacementResult',
    'get_placement',
    'get_placement_output',
]

@pulumi.output_type
class GetPlacementResult:
    def __init__(__self__, attributes=None, id=None):
        if attributes and not isinstance(attributes, dict):
            raise TypeError("Expected argument 'attributes' to be a dict")
        pulumi.set(__self__, "attributes", attributes)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[Any]:
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetPlacementResult(GetPlacementResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPlacementResult(
            attributes=self.attributes,
            id=self.id)


def get_placement(id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPlacementResult:
    """
    Resource Type definition for AWS::IoT1Click::Placement
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:iot1click:getPlacement', __args__, opts=opts, typ=GetPlacementResult).value

    return AwaitableGetPlacementResult(
        attributes=__ret__.attributes,
        id=__ret__.id)


@_utilities.lift_output_func(get_placement)
def get_placement_output(id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPlacementResult]:
    """
    Resource Type definition for AWS::IoT1Click::Placement
    """
    ...
