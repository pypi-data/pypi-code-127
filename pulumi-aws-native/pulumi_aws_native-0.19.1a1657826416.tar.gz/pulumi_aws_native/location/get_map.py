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
    'GetMapResult',
    'AwaitableGetMapResult',
    'get_map',
    'get_map_output',
]

@pulumi.output_type
class GetMapResult:
    def __init__(__self__, arn=None, create_time=None, data_source=None, map_arn=None, update_time=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if data_source and not isinstance(data_source, str):
            raise TypeError("Expected argument 'data_source' to be a str")
        pulumi.set(__self__, "data_source", data_source)
        if map_arn and not isinstance(map_arn, str):
            raise TypeError("Expected argument 'map_arn' to be a str")
        pulumi.set(__self__, "map_arn", map_arn)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[str]:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[str]:
        return pulumi.get(self, "data_source")

    @property
    @pulumi.getter(name="mapArn")
    def map_arn(self) -> Optional[str]:
        return pulumi.get(self, "map_arn")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[str]:
        return pulumi.get(self, "update_time")


class AwaitableGetMapResult(GetMapResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMapResult(
            arn=self.arn,
            create_time=self.create_time,
            data_source=self.data_source,
            map_arn=self.map_arn,
            update_time=self.update_time)


def get_map(map_name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMapResult:
    """
    Definition of AWS::Location::Map Resource Type
    """
    __args__ = dict()
    __args__['mapName'] = map_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:location:getMap', __args__, opts=opts, typ=GetMapResult).value

    return AwaitableGetMapResult(
        arn=__ret__.arn,
        create_time=__ret__.create_time,
        data_source=__ret__.data_source,
        map_arn=__ret__.map_arn,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_map)
def get_map_output(map_name: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMapResult]:
    """
    Definition of AWS::Location::Map Resource Type
    """
    ...
