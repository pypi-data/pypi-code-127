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
    'GetWorkflowResult',
    'AwaitableGetWorkflowResult',
    'get_workflow',
    'get_workflow_output',
]

@pulumi.output_type
class GetWorkflowResult:
    def __init__(__self__, arn=None, tags=None, workflow_id=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if workflow_id and not isinstance(workflow_id, str):
            raise TypeError("Expected argument 'workflow_id' to be a str")
        pulumi.set(__self__, "workflow_id", workflow_id)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Specifies the unique Amazon Resource Name (ARN) for the workflow.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.WorkflowTag']]:
        """
        Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="workflowId")
    def workflow_id(self) -> Optional[str]:
        """
        A unique identifier for the workflow.
        """
        return pulumi.get(self, "workflow_id")


class AwaitableGetWorkflowResult(GetWorkflowResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkflowResult(
            arn=self.arn,
            tags=self.tags,
            workflow_id=self.workflow_id)


def get_workflow(workflow_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkflowResult:
    """
    Resource Type definition for AWS::Transfer::Workflow


    :param str workflow_id: A unique identifier for the workflow.
    """
    __args__ = dict()
    __args__['workflowId'] = workflow_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:transfer:getWorkflow', __args__, opts=opts, typ=GetWorkflowResult).value

    return AwaitableGetWorkflowResult(
        arn=__ret__.arn,
        tags=__ret__.tags,
        workflow_id=__ret__.workflow_id)


@_utilities.lift_output_func(get_workflow)
def get_workflow_output(workflow_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkflowResult]:
    """
    Resource Type definition for AWS::Transfer::Workflow


    :param str workflow_id: A unique identifier for the workflow.
    """
    ...
