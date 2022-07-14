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
    'GetZoneQueuedResourceResult',
    'AwaitableGetZoneQueuedResourceResult',
    'get_zone_queued_resource',
    'get_zone_queued_resource_output',
]

@pulumi.output_type
class GetZoneQueuedResourceResult:
    def __init__(__self__, bulk_insert_instance_resource=None, creation_timestamp=None, description=None, kind=None, name=None, queuing_policy=None, region=None, self_link=None, self_link_with_id=None, state=None, status=None, zone=None):
        if bulk_insert_instance_resource and not isinstance(bulk_insert_instance_resource, dict):
            raise TypeError("Expected argument 'bulk_insert_instance_resource' to be a dict")
        pulumi.set(__self__, "bulk_insert_instance_resource", bulk_insert_instance_resource)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if queuing_policy and not isinstance(queuing_policy, dict):
            raise TypeError("Expected argument 'queuing_policy' to be a dict")
        pulumi.set(__self__, "queuing_policy", queuing_policy)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if self_link_with_id and not isinstance(self_link_with_id, str):
            raise TypeError("Expected argument 'self_link_with_id' to be a str")
        pulumi.set(__self__, "self_link_with_id", self_link_with_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="bulkInsertInstanceResource")
    def bulk_insert_instance_resource(self) -> 'outputs.BulkInsertInstanceResourceResponse':
        """
        Specification of VM instances to create.
        """
        return pulumi.get(self, "bulk_insert_instance_resource")

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
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of the resource. Always compute#queuedResource for QueuedResources.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="queuingPolicy")
    def queuing_policy(self) -> 'outputs.QueuingPolicyResponse':
        """
        Queuing parameters for the requested capacity.
        """
        return pulumi.get(self, "queuing_policy")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        URL of the region where the resource resides. Only applicable for regional resources. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        [Output only] Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> str:
        """
        Server-defined URL for this resource with the resource id.
        """
        return pulumi.get(self, "self_link_with_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        [Output only] High-level status of the request.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.QueuedResourceStatusResponse':
        """
        [Output only] Result of queuing and provisioning based on deferred capacity.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def zone(self) -> str:
        """
        URL of the zone where the resource resides. Only applicable for zonal resources. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "zone")


class AwaitableGetZoneQueuedResourceResult(GetZoneQueuedResourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZoneQueuedResourceResult(
            bulk_insert_instance_resource=self.bulk_insert_instance_resource,
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            kind=self.kind,
            name=self.name,
            queuing_policy=self.queuing_policy,
            region=self.region,
            self_link=self.self_link,
            self_link_with_id=self.self_link_with_id,
            state=self.state,
            status=self.status,
            zone=self.zone)


def get_zone_queued_resource(project: Optional[str] = None,
                             queued_resource: Optional[str] = None,
                             zone: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZoneQueuedResourceResult:
    """
    Returns the specified QueuedResource resource.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['queuedResource'] = queued_resource
    __args__['zone'] = zone
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/alpha:getZoneQueuedResource', __args__, opts=opts, typ=GetZoneQueuedResourceResult).value

    return AwaitableGetZoneQueuedResourceResult(
        bulk_insert_instance_resource=__ret__.bulk_insert_instance_resource,
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        kind=__ret__.kind,
        name=__ret__.name,
        queuing_policy=__ret__.queuing_policy,
        region=__ret__.region,
        self_link=__ret__.self_link,
        self_link_with_id=__ret__.self_link_with_id,
        state=__ret__.state,
        status=__ret__.status,
        zone=__ret__.zone)


@_utilities.lift_output_func(get_zone_queued_resource)
def get_zone_queued_resource_output(project: Optional[pulumi.Input[Optional[str]]] = None,
                                    queued_resource: Optional[pulumi.Input[str]] = None,
                                    zone: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZoneQueuedResourceResult]:
    """
    Returns the specified QueuedResource resource.
    """
    ...
