# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetDebugTokenResult',
    'AwaitableGetDebugTokenResult',
    'get_debug_token',
    'get_debug_token_output',
]

@pulumi.output_type
class GetDebugTokenResult:
    def __init__(__self__, display_name=None, name=None, token=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A human readable display name used to identify this debug token.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The relative resource name of the debug token, in the format: ``` projects/{project_number}/apps/{app_id}/debugTokens/{debug_token_id} ```
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def token(self) -> str:
        """
        Input only. Immutable. The secret token itself. Must be provided during creation, and must be a UUID4, case insensitive. This field is immutable once set, and cannot be provided during an UpdateDebugToken request. You can, however, delete this debug token using DeleteDebugToken to revoke it. For security reasons, this field will never be populated in any response.
        """
        return pulumi.get(self, "token")


class AwaitableGetDebugTokenResult(GetDebugTokenResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDebugTokenResult(
            display_name=self.display_name,
            name=self.name,
            token=self.token)


def get_debug_token(app_id: Optional[str] = None,
                    debug_token_id: Optional[str] = None,
                    project: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDebugTokenResult:
    """
    Gets the specified DebugToken. For security reasons, the `token` field is never populated in the response.
    """
    __args__ = dict()
    __args__['appId'] = app_id
    __args__['debugTokenId'] = debug_token_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:firebaseappcheck/v1beta:getDebugToken', __args__, opts=opts, typ=GetDebugTokenResult).value

    return AwaitableGetDebugTokenResult(
        display_name=__ret__.display_name,
        name=__ret__.name,
        token=__ret__.token)


@_utilities.lift_output_func(get_debug_token)
def get_debug_token_output(app_id: Optional[pulumi.Input[str]] = None,
                           debug_token_id: Optional[pulumi.Input[str]] = None,
                           project: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDebugTokenResult]:
    """
    Gets the specified DebugToken. For security reasons, the `token` field is never populated in the response.
    """
    ...
