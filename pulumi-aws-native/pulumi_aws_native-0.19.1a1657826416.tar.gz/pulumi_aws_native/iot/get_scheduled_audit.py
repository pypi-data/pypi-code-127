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
from ._enums import *

__all__ = [
    'GetScheduledAuditResult',
    'AwaitableGetScheduledAuditResult',
    'get_scheduled_audit',
    'get_scheduled_audit_output',
]

@pulumi.output_type
class GetScheduledAuditResult:
    def __init__(__self__, day_of_month=None, day_of_week=None, frequency=None, scheduled_audit_arn=None, tags=None, target_check_names=None):
        if day_of_month and not isinstance(day_of_month, str):
            raise TypeError("Expected argument 'day_of_month' to be a str")
        pulumi.set(__self__, "day_of_month", day_of_month)
        if day_of_week and not isinstance(day_of_week, str):
            raise TypeError("Expected argument 'day_of_week' to be a str")
        pulumi.set(__self__, "day_of_week", day_of_week)
        if frequency and not isinstance(frequency, str):
            raise TypeError("Expected argument 'frequency' to be a str")
        pulumi.set(__self__, "frequency", frequency)
        if scheduled_audit_arn and not isinstance(scheduled_audit_arn, str):
            raise TypeError("Expected argument 'scheduled_audit_arn' to be a str")
        pulumi.set(__self__, "scheduled_audit_arn", scheduled_audit_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if target_check_names and not isinstance(target_check_names, list):
            raise TypeError("Expected argument 'target_check_names' to be a list")
        pulumi.set(__self__, "target_check_names", target_check_names)

    @property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> Optional[str]:
        """
        The day of the month on which the scheduled audit takes place. Can be 1 through 31 or LAST. This field is required if the frequency parameter is set to MONTHLY.
        """
        return pulumi.get(self, "day_of_month")

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional['ScheduledAuditDayOfWeek']:
        """
        The day of the week on which the scheduled audit takes place. Can be one of SUN, MON, TUE,WED, THU, FRI, or SAT. This field is required if the frequency parameter is set to WEEKLY or BIWEEKLY.
        """
        return pulumi.get(self, "day_of_week")

    @property
    @pulumi.getter
    def frequency(self) -> Optional['ScheduledAuditFrequency']:
        """
        How often the scheduled audit takes place. Can be one of DAILY, WEEKLY, BIWEEKLY, or MONTHLY.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter(name="scheduledAuditArn")
    def scheduled_audit_arn(self) -> Optional[str]:
        """
        The ARN (Amazon resource name) of the scheduled audit.
        """
        return pulumi.get(self, "scheduled_audit_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ScheduledAuditTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetCheckNames")
    def target_check_names(self) -> Optional[Sequence[str]]:
        """
        Which checks are performed during the scheduled audit. Checks must be enabled for your account.
        """
        return pulumi.get(self, "target_check_names")


class AwaitableGetScheduledAuditResult(GetScheduledAuditResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScheduledAuditResult(
            day_of_month=self.day_of_month,
            day_of_week=self.day_of_week,
            frequency=self.frequency,
            scheduled_audit_arn=self.scheduled_audit_arn,
            tags=self.tags,
            target_check_names=self.target_check_names)


def get_scheduled_audit(scheduled_audit_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScheduledAuditResult:
    """
    Scheduled audits can be used to specify the checks you want to perform during an audit and how often the audit should be run.


    :param str scheduled_audit_name: The name you want to give to the scheduled audit.
    """
    __args__ = dict()
    __args__['scheduledAuditName'] = scheduled_audit_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:iot:getScheduledAudit', __args__, opts=opts, typ=GetScheduledAuditResult).value

    return AwaitableGetScheduledAuditResult(
        day_of_month=__ret__.day_of_month,
        day_of_week=__ret__.day_of_week,
        frequency=__ret__.frequency,
        scheduled_audit_arn=__ret__.scheduled_audit_arn,
        tags=__ret__.tags,
        target_check_names=__ret__.target_check_names)


@_utilities.lift_output_func(get_scheduled_audit)
def get_scheduled_audit_output(scheduled_audit_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScheduledAuditResult]:
    """
    Scheduled audits can be used to specify the checks you want to perform during an audit and how often the audit should be run.


    :param str scheduled_audit_name: The name you want to give to the scheduled audit.
    """
    ...
