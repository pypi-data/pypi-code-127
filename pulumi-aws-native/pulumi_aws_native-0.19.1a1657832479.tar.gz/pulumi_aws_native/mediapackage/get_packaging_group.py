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
    'GetPackagingGroupResult',
    'AwaitableGetPackagingGroupResult',
    'get_packaging_group',
    'get_packaging_group_output',
]

@pulumi.output_type
class GetPackagingGroupResult:
    def __init__(__self__, arn=None, authorization=None, domain_name=None, egress_access_logs=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if authorization and not isinstance(authorization, dict):
            raise TypeError("Expected argument 'authorization' to be a dict")
        pulumi.set(__self__, "authorization", authorization)
        if domain_name and not isinstance(domain_name, str):
            raise TypeError("Expected argument 'domain_name' to be a str")
        pulumi.set(__self__, "domain_name", domain_name)
        if egress_access_logs and not isinstance(egress_access_logs, dict):
            raise TypeError("Expected argument 'egress_access_logs' to be a dict")
        pulumi.set(__self__, "egress_access_logs", egress_access_logs)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the PackagingGroup.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def authorization(self) -> Optional['outputs.PackagingGroupAuthorization']:
        """
        CDN Authorization
        """
        return pulumi.get(self, "authorization")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[str]:
        """
        The fully qualified domain name for Assets in the PackagingGroup.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="egressAccessLogs")
    def egress_access_logs(self) -> Optional['outputs.PackagingGroupLogConfiguration']:
        """
        The configuration parameters for egress access logging.
        """
        return pulumi.get(self, "egress_access_logs")


class AwaitableGetPackagingGroupResult(GetPackagingGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPackagingGroupResult(
            arn=self.arn,
            authorization=self.authorization,
            domain_name=self.domain_name,
            egress_access_logs=self.egress_access_logs)


def get_packaging_group(id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPackagingGroupResult:
    """
    Resource schema for AWS::MediaPackage::PackagingGroup


    :param str id: The ID of the PackagingGroup.
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:mediapackage:getPackagingGroup', __args__, opts=opts, typ=GetPackagingGroupResult).value

    return AwaitableGetPackagingGroupResult(
        arn=__ret__.arn,
        authorization=__ret__.authorization,
        domain_name=__ret__.domain_name,
        egress_access_logs=__ret__.egress_access_logs)


@_utilities.lift_output_func(get_packaging_group)
def get_packaging_group_output(id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPackagingGroupResult]:
    """
    Resource schema for AWS::MediaPackage::PackagingGroup


    :param str id: The ID of the PackagingGroup.
    """
    ...
