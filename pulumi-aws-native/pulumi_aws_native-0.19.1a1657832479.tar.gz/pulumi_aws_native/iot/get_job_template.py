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
    'GetJobTemplateResult',
    'AwaitableGetJobTemplateResult',
    'get_job_template',
    'get_job_template_output',
]

@pulumi.output_type
class GetJobTemplateResult:
    def __init__(__self__, arn=None, job_executions_retry_config=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if job_executions_retry_config and not isinstance(job_executions_retry_config, dict):
            raise TypeError("Expected argument 'job_executions_retry_config' to be a dict")
        pulumi.set(__self__, "job_executions_retry_config", job_executions_retry_config)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="jobExecutionsRetryConfig")
    def job_executions_retry_config(self) -> Optional['outputs.JobExecutionsRetryConfigProperties']:
        return pulumi.get(self, "job_executions_retry_config")


class AwaitableGetJobTemplateResult(GetJobTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJobTemplateResult(
            arn=self.arn,
            job_executions_retry_config=self.job_executions_retry_config)


def get_job_template(job_template_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJobTemplateResult:
    """
    Job templates enable you to preconfigure jobs so that you can deploy them to multiple sets of target devices.
    """
    __args__ = dict()
    __args__['jobTemplateId'] = job_template_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:iot:getJobTemplate', __args__, opts=opts, typ=GetJobTemplateResult).value

    return AwaitableGetJobTemplateResult(
        arn=__ret__.arn,
        job_executions_retry_config=__ret__.job_executions_retry_config)


@_utilities.lift_output_func(get_job_template)
def get_job_template_output(job_template_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetJobTemplateResult]:
    """
    Job templates enable you to preconfigure jobs so that you can deploy them to multiple sets of target devices.
    """
    ...
