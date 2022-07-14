# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'GetLoggingResult',
    'AwaitableGetLoggingResult',
    'get_logging',
    'get_logging_output',
]

@pulumi.output_type
class GetLoggingResult:
    def __init__(__self__, default_log_level=None, role_arn=None):
        if default_log_level and not isinstance(default_log_level, str):
            raise TypeError("Expected argument 'default_log_level' to be a str")
        pulumi.set(__self__, "default_log_level", default_log_level)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="defaultLogLevel")
    def default_log_level(self) -> Optional['LoggingDefaultLogLevel']:
        """
        The log level to use. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.
        """
        return pulumi.get(self, "default_log_level")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        """
        The ARN of the role that allows IoT to write to Cloudwatch logs.
        """
        return pulumi.get(self, "role_arn")


class AwaitableGetLoggingResult(GetLoggingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoggingResult(
            default_log_level=self.default_log_level,
            role_arn=self.role_arn)


def get_logging(account_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLoggingResult:
    """
    Logging Options enable you to configure your IoT V2 logging role and default logging level so that you can monitor progress events logs as it passes from your devices through Iot core service.


    :param str account_id: Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:iot:getLogging', __args__, opts=opts, typ=GetLoggingResult).value

    return AwaitableGetLoggingResult(
        default_log_level=__ret__.default_log_level,
        role_arn=__ret__.role_arn)


@_utilities.lift_output_func(get_logging)
def get_logging_output(account_id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLoggingResult]:
    """
    Logging Options enable you to configure your IoT V2 logging role and default logging level so that you can monitor progress events logs as it passes from your devices through Iot core service.


    :param str account_id: Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).
    """
    ...
