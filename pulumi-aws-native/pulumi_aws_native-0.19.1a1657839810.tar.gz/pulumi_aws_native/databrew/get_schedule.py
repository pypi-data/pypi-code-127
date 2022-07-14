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
    'GetScheduleResult',
    'AwaitableGetScheduleResult',
    'get_schedule',
    'get_schedule_output',
]

@pulumi.output_type
class GetScheduleResult:
    def __init__(__self__, cron_expression=None, job_names=None):
        if cron_expression and not isinstance(cron_expression, str):
            raise TypeError("Expected argument 'cron_expression' to be a str")
        pulumi.set(__self__, "cron_expression", cron_expression)
        if job_names and not isinstance(job_names, list):
            raise TypeError("Expected argument 'job_names' to be a list")
        pulumi.set(__self__, "job_names", job_names)

    @property
    @pulumi.getter(name="cronExpression")
    def cron_expression(self) -> Optional[str]:
        """
        Schedule cron
        """
        return pulumi.get(self, "cron_expression")

    @property
    @pulumi.getter(name="jobNames")
    def job_names(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "job_names")


class AwaitableGetScheduleResult(GetScheduleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScheduleResult(
            cron_expression=self.cron_expression,
            job_names=self.job_names)


def get_schedule(name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScheduleResult:
    """
    Resource schema for AWS::DataBrew::Schedule.


    :param str name: Schedule Name
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:databrew:getSchedule', __args__, opts=opts, typ=GetScheduleResult).value

    return AwaitableGetScheduleResult(
        cron_expression=__ret__.cron_expression,
        job_names=__ret__.job_names)


@_utilities.lift_output_func(get_schedule)
def get_schedule_output(name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScheduleResult]:
    """
    Resource schema for AWS::DataBrew::Schedule.


    :param str name: Schedule Name
    """
    ...
