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
    'GetProjectResult',
    'AwaitableGetProjectResult',
    'get_project',
    'get_project_output',
]

@pulumi.output_type
class GetProjectResult:
    def __init__(__self__, create_time=None, delete_time=None, display_name=None, etag=None, labels=None, name=None, parent=None, project_id=None, state=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if delete_time and not isinstance(delete_time, str):
            raise TypeError("Expected argument 'delete_time' to be a str")
        pulumi.set(__self__, "delete_time", delete_time)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parent and not isinstance(parent, str):
            raise TypeError("Expected argument 'parent' to be a str")
        pulumi.set(__self__, "parent", parent)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Creation time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> str:
        """
        The time at which this resource was requested for deletion.
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Optional. A user-assigned display name of the project. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point. Example: `My Project`
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A checksum computed by the server based on the current value of the Project resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Optional. The labels associated with this project. Label keys must be between 1 and 63 characters long and must conform to the following regular expression: \[a-z\](\[-a-z0-9\]*\[a-z0-9\])?. Label values must be between 0 and 63 characters long and must conform to the regular expression (\[a-z\](\[-a-z0-9\]*\[a-z0-9\])?)?. No more than 256 labels can be associated with a given resource. Clients should store labels in a representation such as JSON that does not depend on specific characters being disallowed. Example: `"myBusinessDimension" : "businessValue"`
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The unique resource name of the project. It is an int64 generated number prefixed by "projects/". Example: `projects/415104041262`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parent(self) -> str:
        """
        Optional. A reference to a parent Resource. eg., `organizations/123` or `folders/876`.
        """
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        Immutable. The unique, user-assigned id of the project. It must be 6 to 30 lowercase ASCII letters, digits, or hyphens. It must start with a letter. Trailing hyphens are prohibited. Example: `tokyo-rain-123`
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The project lifecycle state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The most recent time this resource was modified.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetProjectResult(GetProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectResult(
            create_time=self.create_time,
            delete_time=self.delete_time,
            display_name=self.display_name,
            etag=self.etag,
            labels=self.labels,
            name=self.name,
            parent=self.parent,
            project_id=self.project_id,
            state=self.state,
            update_time=self.update_time)


def get_project(project: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectResult:
    """
    Retrieves the project identified by the specified `name` (for example, `projects/415104041262`). The caller must have `resourcemanager.projects.get` permission for this project.
    """
    __args__ = dict()
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:cloudresourcemanager/v3:getProject', __args__, opts=opts, typ=GetProjectResult).value

    return AwaitableGetProjectResult(
        create_time=__ret__.create_time,
        delete_time=__ret__.delete_time,
        display_name=__ret__.display_name,
        etag=__ret__.etag,
        labels=__ret__.labels,
        name=__ret__.name,
        parent=__ret__.parent,
        project_id=__ret__.project_id,
        state=__ret__.state,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_project)
def get_project_output(project: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectResult]:
    """
    Retrieves the project identified by the specified `name` (for example, `projects/415104041262`). The caller must have `resourcemanager.projects.get` permission for this project.
    """
    ...
