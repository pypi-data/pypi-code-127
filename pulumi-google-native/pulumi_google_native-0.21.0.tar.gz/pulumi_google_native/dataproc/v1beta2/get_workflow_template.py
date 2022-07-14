# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetWorkflowTemplateResult',
    'AwaitableGetWorkflowTemplateResult',
    'get_workflow_template',
    'get_workflow_template_output',
]

@pulumi.output_type
class GetWorkflowTemplateResult:
    def __init__(__self__, create_time=None, dag_timeout=None, jobs=None, labels=None, name=None, parameters=None, placement=None, update_time=None, version=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if dag_timeout and not isinstance(dag_timeout, str):
            raise TypeError("Expected argument 'dag_timeout' to be a str")
        pulumi.set(__self__, "dag_timeout", dag_timeout)
        if jobs and not isinstance(jobs, list):
            raise TypeError("Expected argument 'jobs' to be a list")
        pulumi.set(__self__, "jobs", jobs)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parameters and not isinstance(parameters, list):
            raise TypeError("Expected argument 'parameters' to be a list")
        pulumi.set(__self__, "parameters", parameters)
        if placement and not isinstance(placement, dict):
            raise TypeError("Expected argument 'placement' to be a dict")
        pulumi.set(__self__, "placement", placement)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time template was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dagTimeout")
    def dag_timeout(self) -> str:
        """
        Optional. Timeout duration for the DAG of jobs, expressed in seconds (see JSON representation of duration (https://developers.google.com/protocol-buffers/docs/proto3#json)). The timeout duration must be from 10 minutes ("600s") to 24 hours ("86400s"). The timer begins when the first job is submitted. If the workflow is running at the end of the timeout period, any remaining jobs are cancelled, the workflow is ended, and if the workflow was running on a managed cluster, the cluster is deleted.
        """
        return pulumi.get(self, "dag_timeout")

    @property
    @pulumi.getter
    def jobs(self) -> Sequence['outputs.OrderedJobResponse']:
        """
        The Directed Acyclic Graph of Jobs to submit.
        """
        return pulumi.get(self, "jobs")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Optional. The labels to associate with this template. These labels will be propagated to all jobs and clusters created by the workflow instance.Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt).Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt).No more than 32 labels can be associated with a template.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the workflow template, as described in https://cloud.google.com/apis/design/resource_names. For projects.regions.workflowTemplates, the resource name of the template has the following format: projects/{project_id}/regions/{region}/workflowTemplates/{template_id} For projects.locations.workflowTemplates, the resource name of the template has the following format: projects/{project_id}/locations/{location}/workflowTemplates/{template_id}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Sequence['outputs.TemplateParameterResponse']:
        """
        Optional. Template parameters whose values are substituted into the template. Values for parameters must be provided when the template is instantiated.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def placement(self) -> 'outputs.WorkflowTemplatePlacementResponse':
        """
        WorkflowTemplate scheduling information.
        """
        return pulumi.get(self, "placement")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time template was last updated.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        Optional. Used to perform a consistent read-modify-write.This field should be left blank for a CreateWorkflowTemplate request. It is required for an UpdateWorkflowTemplate request, and must match the current server version. A typical update template flow would fetch the current template with a GetWorkflowTemplate request, which will return the current template with the version field filled in with the current server version. The user updates other fields in the template, then returns it as part of the UpdateWorkflowTemplate request.
        """
        return pulumi.get(self, "version")


class AwaitableGetWorkflowTemplateResult(GetWorkflowTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkflowTemplateResult(
            create_time=self.create_time,
            dag_timeout=self.dag_timeout,
            jobs=self.jobs,
            labels=self.labels,
            name=self.name,
            parameters=self.parameters,
            placement=self.placement,
            update_time=self.update_time,
            version=self.version)


def get_workflow_template(location: Optional[str] = None,
                          project: Optional[str] = None,
                          version: Optional[str] = None,
                          workflow_template_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkflowTemplateResult:
    """
    Retrieves the latest workflow template.Can retrieve previously instantiated template by specifying optional version parameter.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['version'] = version
    __args__['workflowTemplateId'] = workflow_template_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:dataproc/v1beta2:getWorkflowTemplate', __args__, opts=opts, typ=GetWorkflowTemplateResult).value

    return AwaitableGetWorkflowTemplateResult(
        create_time=__ret__.create_time,
        dag_timeout=__ret__.dag_timeout,
        jobs=__ret__.jobs,
        labels=__ret__.labels,
        name=__ret__.name,
        parameters=__ret__.parameters,
        placement=__ret__.placement,
        update_time=__ret__.update_time,
        version=__ret__.version)


@_utilities.lift_output_func(get_workflow_template)
def get_workflow_template_output(location: Optional[pulumi.Input[str]] = None,
                                 project: Optional[pulumi.Input[Optional[str]]] = None,
                                 version: Optional[pulumi.Input[Optional[str]]] = None,
                                 workflow_template_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkflowTemplateResult]:
    """
    Retrieves the latest workflow template.Can retrieve previously instantiated template by specifying optional version parameter.
    """
    ...
