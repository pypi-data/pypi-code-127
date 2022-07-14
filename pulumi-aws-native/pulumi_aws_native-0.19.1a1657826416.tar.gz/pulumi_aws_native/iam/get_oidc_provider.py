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
    'GetOIDCProviderResult',
    'AwaitableGetOIDCProviderResult',
    'get_oidc_provider',
    'get_oidc_provider_output',
]

@pulumi.output_type
class GetOIDCProviderResult:
    def __init__(__self__, arn=None, client_id_list=None, tags=None, thumbprint_list=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if client_id_list and not isinstance(client_id_list, list):
            raise TypeError("Expected argument 'client_id_list' to be a list")
        pulumi.set(__self__, "client_id_list", client_id_list)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if thumbprint_list and not isinstance(thumbprint_list, list):
            raise TypeError("Expected argument 'thumbprint_list' to be a list")
        pulumi.set(__self__, "thumbprint_list", thumbprint_list)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of the OIDC provider
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clientIdList")
    def client_id_list(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "client_id_list")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.OIDCProviderTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="thumbprintList")
    def thumbprint_list(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "thumbprint_list")


class AwaitableGetOIDCProviderResult(GetOIDCProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOIDCProviderResult(
            arn=self.arn,
            client_id_list=self.client_id_list,
            tags=self.tags,
            thumbprint_list=self.thumbprint_list)


def get_oidc_provider(arn: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOIDCProviderResult:
    """
    Resource Type definition for AWS::IAM::OIDCProvider


    :param str arn: Amazon Resource Name (ARN) of the OIDC provider
    """
    __args__ = dict()
    __args__['arn'] = arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:iam:getOIDCProvider', __args__, opts=opts, typ=GetOIDCProviderResult).value

    return AwaitableGetOIDCProviderResult(
        arn=__ret__.arn,
        client_id_list=__ret__.client_id_list,
        tags=__ret__.tags,
        thumbprint_list=__ret__.thumbprint_list)


@_utilities.lift_output_func(get_oidc_provider)
def get_oidc_provider_output(arn: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOIDCProviderResult]:
    """
    Resource Type definition for AWS::IAM::OIDCProvider


    :param str arn: Amazon Resource Name (ARN) of the OIDC provider
    """
    ...
