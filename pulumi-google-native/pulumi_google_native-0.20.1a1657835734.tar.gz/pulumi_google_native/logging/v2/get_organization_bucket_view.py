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
    'GetOrganizationBucketViewResult',
    'AwaitableGetOrganizationBucketViewResult',
    'get_organization_bucket_view',
    'get_organization_bucket_view_output',
]

@pulumi.output_type
class GetOrganizationBucketViewResult:
    def __init__(__self__, create_time=None, description=None, filter=None, name=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if filter and not isinstance(filter, str):
            raise TypeError("Expected argument 'filter' to be a str")
        pulumi.set(__self__, "filter", filter)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The creation timestamp of the view.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Describes this view.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filter(self) -> str:
        """
        Filter that restricts which log entries in a bucket are visible in this view.Filters are restricted to be a logical AND of ==/!= of any of the following: originating project/folder/organization/billing account. resource type log idFor example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND LOG_ID("stdout")
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The last update timestamp of the view.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetOrganizationBucketViewResult(GetOrganizationBucketViewResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrganizationBucketViewResult(
            create_time=self.create_time,
            description=self.description,
            filter=self.filter,
            name=self.name,
            update_time=self.update_time)


def get_organization_bucket_view(bucket_id: Optional[str] = None,
                                 location: Optional[str] = None,
                                 organization_id: Optional[str] = None,
                                 view_id: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrganizationBucketViewResult:
    """
    Gets a view on a log bucket..
    """
    __args__ = dict()
    __args__['bucketId'] = bucket_id
    __args__['location'] = location
    __args__['organizationId'] = organization_id
    __args__['viewId'] = view_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:logging/v2:getOrganizationBucketView', __args__, opts=opts, typ=GetOrganizationBucketViewResult).value

    return AwaitableGetOrganizationBucketViewResult(
        create_time=__ret__.create_time,
        description=__ret__.description,
        filter=__ret__.filter,
        name=__ret__.name,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_organization_bucket_view)
def get_organization_bucket_view_output(bucket_id: Optional[pulumi.Input[str]] = None,
                                        location: Optional[pulumi.Input[str]] = None,
                                        organization_id: Optional[pulumi.Input[str]] = None,
                                        view_id: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOrganizationBucketViewResult]:
    """
    Gets a view on a log bucket..
    """
    ...
