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

__all__ = [
    'GetNetworkAclResult',
    'AwaitableGetNetworkAclResult',
    'get_network_acl',
    'get_network_acl_output',
]

@pulumi.output_type
class GetNetworkAclResult:
    def __init__(__self__, id=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.NetworkAclTag']]:
        """
        The tags to assign to the network ACL.
        """
        return pulumi.get(self, "tags")


class AwaitableGetNetworkAclResult(GetNetworkAclResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkAclResult(
            id=self.id,
            tags=self.tags)


def get_network_acl(id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkAclResult:
    """
    Resource Type definition for AWS::EC2::NetworkAcl
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getNetworkAcl', __args__, opts=opts, typ=GetNetworkAclResult).value

    return AwaitableGetNetworkAclResult(
        id=__ret__.id,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_network_acl)
def get_network_acl_output(id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkAclResult]:
    """
    Resource Type definition for AWS::EC2::NetworkAcl
    """
    ...
