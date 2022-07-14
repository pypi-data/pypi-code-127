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
    'GetMountTargetResult',
    'AwaitableGetMountTargetResult',
    'get_mount_target',
    'get_mount_target_output',
]

@pulumi.output_type
class GetMountTargetResult:
    def __init__(__self__, id=None, security_groups=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if security_groups and not isinstance(security_groups, list):
            raise TypeError("Expected argument 'security_groups' to be a list")
        pulumi.set(__self__, "security_groups", security_groups)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "security_groups")


class AwaitableGetMountTargetResult(GetMountTargetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMountTargetResult(
            id=self.id,
            security_groups=self.security_groups)


def get_mount_target(id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMountTargetResult:
    """
    Resource Type definition for AWS::EFS::MountTarget
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:efs:getMountTarget', __args__, opts=opts, typ=GetMountTargetResult).value

    return AwaitableGetMountTargetResult(
        id=__ret__.id,
        security_groups=__ret__.security_groups)


@_utilities.lift_output_func(get_mount_target)
def get_mount_target_output(id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMountTargetResult]:
    """
    Resource Type definition for AWS::EFS::MountTarget
    """
    ...
