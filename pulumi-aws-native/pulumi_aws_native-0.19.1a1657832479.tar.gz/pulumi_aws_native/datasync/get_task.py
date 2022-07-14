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
    'GetTaskResult',
    'AwaitableGetTaskResult',
    'get_task',
    'get_task_output',
]

@pulumi.output_type
class GetTaskResult:
    def __init__(__self__, cloud_watch_log_group_arn=None, destination_network_interface_arns=None, error_code=None, error_detail=None, excludes=None, includes=None, name=None, options=None, schedule=None, source_network_interface_arns=None, status=None, tags=None, task_arn=None):
        if cloud_watch_log_group_arn and not isinstance(cloud_watch_log_group_arn, str):
            raise TypeError("Expected argument 'cloud_watch_log_group_arn' to be a str")
        pulumi.set(__self__, "cloud_watch_log_group_arn", cloud_watch_log_group_arn)
        if destination_network_interface_arns and not isinstance(destination_network_interface_arns, list):
            raise TypeError("Expected argument 'destination_network_interface_arns' to be a list")
        pulumi.set(__self__, "destination_network_interface_arns", destination_network_interface_arns)
        if error_code and not isinstance(error_code, str):
            raise TypeError("Expected argument 'error_code' to be a str")
        pulumi.set(__self__, "error_code", error_code)
        if error_detail and not isinstance(error_detail, str):
            raise TypeError("Expected argument 'error_detail' to be a str")
        pulumi.set(__self__, "error_detail", error_detail)
        if excludes and not isinstance(excludes, list):
            raise TypeError("Expected argument 'excludes' to be a list")
        pulumi.set(__self__, "excludes", excludes)
        if includes and not isinstance(includes, list):
            raise TypeError("Expected argument 'includes' to be a list")
        pulumi.set(__self__, "includes", includes)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if options and not isinstance(options, dict):
            raise TypeError("Expected argument 'options' to be a dict")
        pulumi.set(__self__, "options", options)
        if schedule and not isinstance(schedule, dict):
            raise TypeError("Expected argument 'schedule' to be a dict")
        pulumi.set(__self__, "schedule", schedule)
        if source_network_interface_arns and not isinstance(source_network_interface_arns, list):
            raise TypeError("Expected argument 'source_network_interface_arns' to be a list")
        pulumi.set(__self__, "source_network_interface_arns", source_network_interface_arns)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if task_arn and not isinstance(task_arn, str):
            raise TypeError("Expected argument 'task_arn' to be a str")
        pulumi.set(__self__, "task_arn", task_arn)

    @property
    @pulumi.getter(name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> Optional[str]:
        """
        The ARN of the Amazon CloudWatch log group that is used to monitor and log events in the task.
        """
        return pulumi.get(self, "cloud_watch_log_group_arn")

    @property
    @pulumi.getter(name="destinationNetworkInterfaceArns")
    def destination_network_interface_arns(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "destination_network_interface_arns")

    @property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> Optional[str]:
        """
        Errors that AWS DataSync encountered during execution of the task. You can use this error code to help troubleshoot issues.
        """
        return pulumi.get(self, "error_code")

    @property
    @pulumi.getter(name="errorDetail")
    def error_detail(self) -> Optional[str]:
        """
        Detailed description of an error that was encountered during the task execution.
        """
        return pulumi.get(self, "error_detail")

    @property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence['outputs.TaskFilterRule']]:
        return pulumi.get(self, "excludes")

    @property
    @pulumi.getter
    def includes(self) -> Optional[Sequence['outputs.TaskFilterRule']]:
        return pulumi.get(self, "includes")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of a task. This value is a text reference that is used to identify the task in the console.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def options(self) -> Optional['outputs.TaskOptions']:
        return pulumi.get(self, "options")

    @property
    @pulumi.getter
    def schedule(self) -> Optional['outputs.TaskSchedule']:
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="sourceNetworkInterfaceArns")
    def source_network_interface_arns(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "source_network_interface_arns")

    @property
    @pulumi.getter
    def status(self) -> Optional['TaskStatus']:
        """
        The status of the task that was described.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.TaskTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="taskArn")
    def task_arn(self) -> Optional[str]:
        """
        The ARN of the task.
        """
        return pulumi.get(self, "task_arn")


class AwaitableGetTaskResult(GetTaskResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTaskResult(
            cloud_watch_log_group_arn=self.cloud_watch_log_group_arn,
            destination_network_interface_arns=self.destination_network_interface_arns,
            error_code=self.error_code,
            error_detail=self.error_detail,
            excludes=self.excludes,
            includes=self.includes,
            name=self.name,
            options=self.options,
            schedule=self.schedule,
            source_network_interface_arns=self.source_network_interface_arns,
            status=self.status,
            tags=self.tags,
            task_arn=self.task_arn)


def get_task(task_arn: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTaskResult:
    """
    Resource schema for AWS::DataSync::Task.


    :param str task_arn: The ARN of the task.
    """
    __args__ = dict()
    __args__['taskArn'] = task_arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:datasync:getTask', __args__, opts=opts, typ=GetTaskResult).value

    return AwaitableGetTaskResult(
        cloud_watch_log_group_arn=__ret__.cloud_watch_log_group_arn,
        destination_network_interface_arns=__ret__.destination_network_interface_arns,
        error_code=__ret__.error_code,
        error_detail=__ret__.error_detail,
        excludes=__ret__.excludes,
        includes=__ret__.includes,
        name=__ret__.name,
        options=__ret__.options,
        schedule=__ret__.schedule,
        source_network_interface_arns=__ret__.source_network_interface_arns,
        status=__ret__.status,
        tags=__ret__.tags,
        task_arn=__ret__.task_arn)


@_utilities.lift_output_func(get_task)
def get_task_output(task_arn: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTaskResult]:
    """
    Resource schema for AWS::DataSync::Task.


    :param str task_arn: The ARN of the task.
    """
    ...
