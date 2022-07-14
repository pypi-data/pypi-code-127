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
    'GetEnvgroupResult',
    'AwaitableGetEnvgroupResult',
    'get_envgroup',
    'get_envgroup_output',
]

@pulumi.output_type
class GetEnvgroupResult:
    def __init__(__self__, created_at=None, hostnames=None, last_modified_at=None, name=None, state=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if hostnames and not isinstance(hostnames, list):
            raise TypeError("Expected argument 'hostnames' to be a list")
        pulumi.set(__self__, "hostnames", hostnames)
        if last_modified_at and not isinstance(last_modified_at, str):
            raise TypeError("Expected argument 'last_modified_at' to be a str")
        pulumi.set(__self__, "last_modified_at", last_modified_at)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The time at which the environment group was created as milliseconds since epoch.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def hostnames(self) -> Sequence[str]:
        """
        Host names for this environment group.
        """
        return pulumi.get(self, "hostnames")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> str:
        """
        The time at which the environment group was last updated as milliseconds since epoch.
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        ID of the environment group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of the environment group. Values other than ACTIVE means the resource is not ready to use.
        """
        return pulumi.get(self, "state")


class AwaitableGetEnvgroupResult(GetEnvgroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnvgroupResult(
            created_at=self.created_at,
            hostnames=self.hostnames,
            last_modified_at=self.last_modified_at,
            name=self.name,
            state=self.state)


def get_envgroup(envgroup_id: Optional[str] = None,
                 organization_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnvgroupResult:
    """
    Gets an environment group.
    """
    __args__ = dict()
    __args__['envgroupId'] = envgroup_id
    __args__['organizationId'] = organization_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:apigee/v1:getEnvgroup', __args__, opts=opts, typ=GetEnvgroupResult).value

    return AwaitableGetEnvgroupResult(
        created_at=__ret__.created_at,
        hostnames=__ret__.hostnames,
        last_modified_at=__ret__.last_modified_at,
        name=__ret__.name,
        state=__ret__.state)


@_utilities.lift_output_func(get_envgroup)
def get_envgroup_output(envgroup_id: Optional[pulumi.Input[str]] = None,
                        organization_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEnvgroupResult]:
    """
    Gets an environment group.
    """
    ...
