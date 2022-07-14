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
    'GetEmailChannelResult',
    'AwaitableGetEmailChannelResult',
    'get_email_channel',
    'get_email_channel_output',
]

@pulumi.output_type
class GetEmailChannelResult:
    def __init__(__self__, configuration_set=None, enabled=None, from_address=None, id=None, identity=None, role_arn=None):
        if configuration_set and not isinstance(configuration_set, str):
            raise TypeError("Expected argument 'configuration_set' to be a str")
        pulumi.set(__self__, "configuration_set", configuration_set)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if from_address and not isinstance(from_address, str):
            raise TypeError("Expected argument 'from_address' to be a str")
        pulumi.set(__self__, "from_address", from_address)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, str):
            raise TypeError("Expected argument 'identity' to be a str")
        pulumi.set(__self__, "identity", identity)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="configurationSet")
    def configuration_set(self) -> Optional[str]:
        return pulumi.get(self, "configuration_set")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="fromAddress")
    def from_address(self) -> Optional[str]:
        return pulumi.get(self, "from_address")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional[str]:
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        return pulumi.get(self, "role_arn")


class AwaitableGetEmailChannelResult(GetEmailChannelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEmailChannelResult(
            configuration_set=self.configuration_set,
            enabled=self.enabled,
            from_address=self.from_address,
            id=self.id,
            identity=self.identity,
            role_arn=self.role_arn)


def get_email_channel(id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEmailChannelResult:
    """
    Resource Type definition for AWS::Pinpoint::EmailChannel
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:pinpoint:getEmailChannel', __args__, opts=opts, typ=GetEmailChannelResult).value

    return AwaitableGetEmailChannelResult(
        configuration_set=__ret__.configuration_set,
        enabled=__ret__.enabled,
        from_address=__ret__.from_address,
        id=__ret__.id,
        identity=__ret__.identity,
        role_arn=__ret__.role_arn)


@_utilities.lift_output_func(get_email_channel)
def get_email_channel_output(id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEmailChannelResult]:
    """
    Resource Type definition for AWS::Pinpoint::EmailChannel
    """
    ...
