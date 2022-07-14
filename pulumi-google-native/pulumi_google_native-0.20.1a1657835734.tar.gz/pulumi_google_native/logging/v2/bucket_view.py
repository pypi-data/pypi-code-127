# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['BucketViewArgs', 'BucketView']

@pulumi.input_type
class BucketViewArgs:
    def __init__(__self__, *,
                 bucket_id: pulumi.Input[str],
                 view_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BucketView resource.
        :param pulumi.Input[str] view_id: Required. The id to use for this view.
        :param pulumi.Input[str] description: Describes this view.
        :param pulumi.Input[str] filter: Filter that restricts which log entries in a bucket are visible in this view.Filters are restricted to be a logical AND of ==/!= of any of the following: originating project/folder/organization/billing account. resource type log idFor example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND LOG_ID("stdout")
        :param pulumi.Input[str] name: The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view
        """
        pulumi.set(__self__, "bucket_id", bucket_id)
        pulumi.set(__self__, "view_id", view_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "bucket_id")

    @bucket_id.setter
    def bucket_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket_id", value)

    @property
    @pulumi.getter(name="viewId")
    def view_id(self) -> pulumi.Input[str]:
        """
        Required. The id to use for this view.
        """
        return pulumi.get(self, "view_id")

    @view_id.setter
    def view_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "view_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Describes this view.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        """
        Filter that restricts which log entries in a bucket are visible in this view.Filters are restricted to be a logical AND of ==/!= of any of the following: originating project/folder/organization/billing account. resource type log idFor example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND LOG_ID("stdout")
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class BucketView(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 view_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Describes this view.
        :param pulumi.Input[str] filter: Filter that restricts which log entries in a bucket are visible in this view.Filters are restricted to be a logical AND of ==/!= of any of the following: originating project/folder/organization/billing account. resource type log idFor example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND LOG_ID("stdout")
        :param pulumi.Input[str] name: The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view
        :param pulumi.Input[str] view_id: Required. The id to use for this view.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BucketViewArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views.

        :param str resource_name: The name of the resource.
        :param BucketViewArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BucketViewArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 view_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        else:
            opts = copy.copy(opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BucketViewArgs.__new__(BucketViewArgs)

            if bucket_id is None and not opts.urn:
                raise TypeError("Missing required property 'bucket_id'")
            __props__.__dict__["bucket_id"] = bucket_id
            __props__.__dict__["description"] = description
            __props__.__dict__["filter"] = filter
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            if view_id is None and not opts.urn:
                raise TypeError("Missing required property 'view_id'")
            __props__.__dict__["view_id"] = view_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["bucket_id", "location", "project", "view_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(BucketView, __self__).__init__(
            'google-native:logging/v2:BucketView',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BucketView':
        """
        Get an existing BucketView resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BucketViewArgs.__new__(BucketViewArgs)

        __props__.__dict__["bucket_id"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["filter"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["view_id"] = None
        return BucketView(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "bucket_id")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The creation timestamp of the view.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Describes this view.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[str]:
        """
        Filter that restricts which log entries in a bucket are visible in this view.Filters are restricted to be a logical AND of ==/!= of any of the following: originating project/folder/organization/billing account. resource type log idFor example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND LOG_ID("stdout")
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The last update timestamp of the view.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="viewId")
    def view_id(self) -> pulumi.Output[str]:
        """
        Required. The id to use for this view.
        """
        return pulumi.get(self, "view_id")

