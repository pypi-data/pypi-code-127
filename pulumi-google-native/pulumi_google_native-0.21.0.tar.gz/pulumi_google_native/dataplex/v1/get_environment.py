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
    'GetEnvironmentResult',
    'AwaitableGetEnvironmentResult',
    'get_environment',
    'get_environment_output',
]

@pulumi.output_type
class GetEnvironmentResult:
    def __init__(__self__, create_time=None, description=None, display_name=None, endpoints=None, infrastructure_spec=None, labels=None, name=None, session_spec=None, session_status=None, state=None, uid=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if endpoints and not isinstance(endpoints, dict):
            raise TypeError("Expected argument 'endpoints' to be a dict")
        pulumi.set(__self__, "endpoints", endpoints)
        if infrastructure_spec and not isinstance(infrastructure_spec, dict):
            raise TypeError("Expected argument 'infrastructure_spec' to be a dict")
        pulumi.set(__self__, "infrastructure_spec", infrastructure_spec)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if session_spec and not isinstance(session_spec, dict):
            raise TypeError("Expected argument 'session_spec' to be a dict")
        pulumi.set(__self__, "session_spec", session_spec)
        if session_status and not isinstance(session_status, dict):
            raise TypeError("Expected argument 'session_status' to be a dict")
        pulumi.set(__self__, "session_status", session_status)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Environment creation time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional. Description of the environment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Optional. User friendly display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def endpoints(self) -> 'outputs.GoogleCloudDataplexV1EnvironmentEndpointsResponse':
        """
        URI Endpoints to access sessions associated with the Environment.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter(name="infrastructureSpec")
    def infrastructure_spec(self) -> 'outputs.GoogleCloudDataplexV1EnvironmentInfrastructureSpecResponse':
        """
        Infrastructure specification for the Environment.
        """
        return pulumi.get(self, "infrastructure_spec")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Optional. User defined labels for the environment.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The relative resource name of the environment, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/environment/{environment_id}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sessionSpec")
    def session_spec(self) -> 'outputs.GoogleCloudDataplexV1EnvironmentSessionSpecResponse':
        """
        Optional. Configuration for sessions created for this environment.
        """
        return pulumi.get(self, "session_spec")

    @property
    @pulumi.getter(name="sessionStatus")
    def session_status(self) -> 'outputs.GoogleCloudDataplexV1EnvironmentSessionStatusResponse':
        """
        Status of sessions created for this environment.
        """
        return pulumi.get(self, "session_status")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Current state of the environment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def uid(self) -> str:
        """
        System generated globally unique ID for the environment. This ID will be different if the environment is deleted and re-created with the same name.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time when the environment was last updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetEnvironmentResult(GetEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnvironmentResult(
            create_time=self.create_time,
            description=self.description,
            display_name=self.display_name,
            endpoints=self.endpoints,
            infrastructure_spec=self.infrastructure_spec,
            labels=self.labels,
            name=self.name,
            session_spec=self.session_spec,
            session_status=self.session_status,
            state=self.state,
            uid=self.uid,
            update_time=self.update_time)


def get_environment(environment_id: Optional[str] = None,
                    lake_id: Optional[str] = None,
                    location: Optional[str] = None,
                    project: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnvironmentResult:
    """
    Get environment resource.
    """
    __args__ = dict()
    __args__['environmentId'] = environment_id
    __args__['lakeId'] = lake_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:dataplex/v1:getEnvironment', __args__, opts=opts, typ=GetEnvironmentResult).value

    return AwaitableGetEnvironmentResult(
        create_time=__ret__.create_time,
        description=__ret__.description,
        display_name=__ret__.display_name,
        endpoints=__ret__.endpoints,
        infrastructure_spec=__ret__.infrastructure_spec,
        labels=__ret__.labels,
        name=__ret__.name,
        session_spec=__ret__.session_spec,
        session_status=__ret__.session_status,
        state=__ret__.state,
        uid=__ret__.uid,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_environment)
def get_environment_output(environment_id: Optional[pulumi.Input[str]] = None,
                           lake_id: Optional[pulumi.Input[str]] = None,
                           location: Optional[pulumi.Input[str]] = None,
                           project: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEnvironmentResult]:
    """
    Get environment resource.
    """
    ...
