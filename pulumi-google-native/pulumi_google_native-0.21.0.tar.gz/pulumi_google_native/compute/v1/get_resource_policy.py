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
    'GetResourcePolicyResult',
    'AwaitableGetResourcePolicyResult',
    'get_resource_policy',
    'get_resource_policy_output',
]

@pulumi.output_type
class GetResourcePolicyResult:
    def __init__(__self__, creation_timestamp=None, description=None, group_placement_policy=None, instance_schedule_policy=None, kind=None, name=None, region=None, resource_status=None, self_link=None, snapshot_schedule_policy=None, status=None):
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if group_placement_policy and not isinstance(group_placement_policy, dict):
            raise TypeError("Expected argument 'group_placement_policy' to be a dict")
        pulumi.set(__self__, "group_placement_policy", group_placement_policy)
        if instance_schedule_policy and not isinstance(instance_schedule_policy, dict):
            raise TypeError("Expected argument 'instance_schedule_policy' to be a dict")
        pulumi.set(__self__, "instance_schedule_policy", instance_schedule_policy)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if resource_status and not isinstance(resource_status, dict):
            raise TypeError("Expected argument 'resource_status' to be a dict")
        pulumi.set(__self__, "resource_status", resource_status)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if snapshot_schedule_policy and not isinstance(snapshot_schedule_policy, dict):
            raise TypeError("Expected argument 'snapshot_schedule_policy' to be a dict")
        pulumi.set(__self__, "snapshot_schedule_policy", snapshot_schedule_policy)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="groupPlacementPolicy")
    def group_placement_policy(self) -> 'outputs.ResourcePolicyGroupPlacementPolicyResponse':
        """
        Resource policy for instances for placement configuration.
        """
        return pulumi.get(self, "group_placement_policy")

    @property
    @pulumi.getter(name="instanceSchedulePolicy")
    def instance_schedule_policy(self) -> 'outputs.ResourcePolicyInstanceSchedulePolicyResponse':
        """
        Resource policy for scheduling instance operations.
        """
        return pulumi.get(self, "instance_schedule_policy")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of the resource. Always compute#resource_policies for resource policies.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="resourceStatus")
    def resource_status(self) -> 'outputs.ResourcePolicyResourceStatusResponse':
        """
        The system status of the resource policy.
        """
        return pulumi.get(self, "resource_status")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        Server-defined fully-qualified URL for this resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="snapshotSchedulePolicy")
    def snapshot_schedule_policy(self) -> 'outputs.ResourcePolicySnapshotSchedulePolicyResponse':
        """
        Resource policy for persistent disks for creating snapshots.
        """
        return pulumi.get(self, "snapshot_schedule_policy")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of resource policy creation.
        """
        return pulumi.get(self, "status")


class AwaitableGetResourcePolicyResult(GetResourcePolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourcePolicyResult(
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            group_placement_policy=self.group_placement_policy,
            instance_schedule_policy=self.instance_schedule_policy,
            kind=self.kind,
            name=self.name,
            region=self.region,
            resource_status=self.resource_status,
            self_link=self.self_link,
            snapshot_schedule_policy=self.snapshot_schedule_policy,
            status=self.status)


def get_resource_policy(project: Optional[str] = None,
                        region: Optional[str] = None,
                        resource_policy: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourcePolicyResult:
    """
    Retrieves all information of the specified resource policy.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['region'] = region
    __args__['resourcePolicy'] = resource_policy
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/v1:getResourcePolicy', __args__, opts=opts, typ=GetResourcePolicyResult).value

    return AwaitableGetResourcePolicyResult(
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        group_placement_policy=__ret__.group_placement_policy,
        instance_schedule_policy=__ret__.instance_schedule_policy,
        kind=__ret__.kind,
        name=__ret__.name,
        region=__ret__.region,
        resource_status=__ret__.resource_status,
        self_link=__ret__.self_link,
        snapshot_schedule_policy=__ret__.snapshot_schedule_policy,
        status=__ret__.status)


@_utilities.lift_output_func(get_resource_policy)
def get_resource_policy_output(project: Optional[pulumi.Input[Optional[str]]] = None,
                               region: Optional[pulumi.Input[str]] = None,
                               resource_policy: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourcePolicyResult]:
    """
    Retrieves all information of the specified resource policy.
    """
    ...
