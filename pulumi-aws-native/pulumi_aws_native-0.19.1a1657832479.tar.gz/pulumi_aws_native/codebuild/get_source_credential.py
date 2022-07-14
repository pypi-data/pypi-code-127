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
    'GetSourceCredentialResult',
    'AwaitableGetSourceCredentialResult',
    'get_source_credential',
    'get_source_credential_output',
]

@pulumi.output_type
class GetSourceCredentialResult:
    def __init__(__self__, auth_type=None, id=None, token=None, username=None):
        if auth_type and not isinstance(auth_type, str):
            raise TypeError("Expected argument 'auth_type' to be a str")
        pulumi.set(__self__, "auth_type", auth_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[str]:
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def token(self) -> Optional[str]:
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def username(self) -> Optional[str]:
        return pulumi.get(self, "username")


class AwaitableGetSourceCredentialResult(GetSourceCredentialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSourceCredentialResult(
            auth_type=self.auth_type,
            id=self.id,
            token=self.token,
            username=self.username)


def get_source_credential(id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSourceCredentialResult:
    """
    Resource Type definition for AWS::CodeBuild::SourceCredential
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:codebuild:getSourceCredential', __args__, opts=opts, typ=GetSourceCredentialResult).value

    return AwaitableGetSourceCredentialResult(
        auth_type=__ret__.auth_type,
        id=__ret__.id,
        token=__ret__.token,
        username=__ret__.username)


@_utilities.lift_output_func(get_source_credential)
def get_source_credential_output(id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSourceCredentialResult]:
    """
    Resource Type definition for AWS::CodeBuild::SourceCredential
    """
    ...
