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
    'GetMultiRegionAccessPointResult',
    'AwaitableGetMultiRegionAccessPointResult',
    'get_multi_region_access_point',
    'get_multi_region_access_point_output',
]

@pulumi.output_type
class GetMultiRegionAccessPointResult:
    def __init__(__self__, alias=None, created_at=None):
        if alias and not isinstance(alias, str):
            raise TypeError("Expected argument 'alias' to be a str")
        pulumi.set(__self__, "alias", alias)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)

    @property
    @pulumi.getter
    def alias(self) -> Optional[str]:
        """
        The alias is a unique identifier to, and is part of the public DNS name for this Multi Region Access Point
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of the when the Multi Region Access Point is created
        """
        return pulumi.get(self, "created_at")


class AwaitableGetMultiRegionAccessPointResult(GetMultiRegionAccessPointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMultiRegionAccessPointResult(
            alias=self.alias,
            created_at=self.created_at)


def get_multi_region_access_point(name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMultiRegionAccessPointResult:
    """
    AWS::S3::MultiRegionAccessPoint is an Amazon S3 resource type that dynamically routes S3 requests to easily satisfy geographic compliance requirements based on customer-defined routing policies.


    :param str name: The name you want to assign to this Multi Region Access Point.
    """
    __args__ = dict()
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:s3:getMultiRegionAccessPoint', __args__, opts=opts, typ=GetMultiRegionAccessPointResult).value

    return AwaitableGetMultiRegionAccessPointResult(
        alias=__ret__.alias,
        created_at=__ret__.created_at)


@_utilities.lift_output_func(get_multi_region_access_point)
def get_multi_region_access_point_output(name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMultiRegionAccessPointResult]:
    """
    AWS::S3::MultiRegionAccessPoint is an Amazon S3 resource type that dynamically routes S3 requests to easily satisfy geographic compliance requirements based on customer-defined routing policies.


    :param str name: The name you want to assign to this Multi Region Access Point.
    """
    ...
