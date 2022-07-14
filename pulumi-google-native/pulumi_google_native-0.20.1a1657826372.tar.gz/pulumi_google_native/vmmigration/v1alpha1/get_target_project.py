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
    'GetTargetProjectResult',
    'AwaitableGetTargetProjectResult',
    'get_target_project',
    'get_target_project_output',
]

@pulumi.output_type
class GetTargetProjectResult:
    def __init__(__self__, create_time=None, description=None, name=None, project=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time this target project resource was created (not related to when the Compute Engine project it points to was created).
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The target project's description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the target project.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> str:
        """
        The target project ID (number) or project name.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The last time the target project resource was updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetTargetProjectResult(GetTargetProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTargetProjectResult(
            create_time=self.create_time,
            description=self.description,
            name=self.name,
            project=self.project,
            update_time=self.update_time)


def get_target_project(location: Optional[str] = None,
                       project: Optional[str] = None,
                       target_project_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTargetProjectResult:
    """
    Gets details of a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['targetProjectId'] = target_project_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:vmmigration/v1alpha1:getTargetProject', __args__, opts=opts, typ=GetTargetProjectResult).value

    return AwaitableGetTargetProjectResult(
        create_time=__ret__.create_time,
        description=__ret__.description,
        name=__ret__.name,
        project=__ret__.project,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_target_project)
def get_target_project_output(location: Optional[pulumi.Input[str]] = None,
                              project: Optional[pulumi.Input[Optional[str]]] = None,
                              target_project_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTargetProjectResult]:
    """
    Gets details of a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`.
    """
    ...
