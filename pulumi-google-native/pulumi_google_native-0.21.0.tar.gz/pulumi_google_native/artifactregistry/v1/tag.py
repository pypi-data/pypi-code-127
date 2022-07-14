# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['TagArgs', 'Tag']

@pulumi.input_type
class TagArgs:
    def __init__(__self__, *,
                 package_id: pulumi.Input[str],
                 repository_id: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 tag_id: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Tag resource.
        :param pulumi.Input[str] name: The name of the tag, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/tags/tag1". If the package part contains slashes, the slashes are escaped. The tag part can only have characters in [a-zA-Z0-9\-._~:@], anything else must be URL encoded.
        :param pulumi.Input[str] tag_id: The tag id to use for this repository.
        :param pulumi.Input[str] version: The name of the version the tag refers to, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/sha256:5243811" If the package or version ID parts contain slashes, the slashes are escaped.
        """
        pulumi.set(__self__, "package_id", package_id)
        pulumi.set(__self__, "repository_id", repository_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if tag_id is not None:
            pulumi.set(__self__, "tag_id", tag_id)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="packageId")
    def package_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "package_id")

    @package_id.setter
    def package_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "package_id", value)

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "repository_id")

    @repository_id.setter
    def repository_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "repository_id", value)

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
        The name of the tag, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/tags/tag1". If the package part contains slashes, the slashes are escaped. The tag part can only have characters in [a-zA-Z0-9\-._~:@], anything else must be URL encoded.
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

    @property
    @pulumi.getter(name="tagId")
    def tag_id(self) -> Optional[pulumi.Input[str]]:
        """
        The tag id to use for this repository.
        """
        return pulumi.get(self, "tag_id")

    @tag_id.setter
    def tag_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tag_id", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the version the tag refers to, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/sha256:5243811" If the package or version ID parts contain slashes, the slashes are escaped.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Tag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 package_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 repository_id: Optional[pulumi.Input[str]] = None,
                 tag_id: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a tag.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the tag, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/tags/tag1". If the package part contains slashes, the slashes are escaped. The tag part can only have characters in [a-zA-Z0-9\-._~:@], anything else must be URL encoded.
        :param pulumi.Input[str] tag_id: The tag id to use for this repository.
        :param pulumi.Input[str] version: The name of the version the tag refers to, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/sha256:5243811" If the package or version ID parts contain slashes, the slashes are escaped.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TagArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a tag.

        :param str resource_name: The name of the resource.
        :param TagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 package_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 repository_id: Optional[pulumi.Input[str]] = None,
                 tag_id: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
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
            __props__ = TagArgs.__new__(TagArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if package_id is None and not opts.urn:
                raise TypeError("Missing required property 'package_id'")
            __props__.__dict__["package_id"] = package_id
            __props__.__dict__["project"] = project
            if repository_id is None and not opts.urn:
                raise TypeError("Missing required property 'repository_id'")
            __props__.__dict__["repository_id"] = repository_id
            __props__.__dict__["tag_id"] = tag_id
            __props__.__dict__["version"] = version
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["location", "package_id", "project", "repository_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Tag, __self__).__init__(
            'google-native:artifactregistry/v1:Tag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Tag':
        """
        Get an existing Tag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TagArgs.__new__(TagArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["package_id"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["repository_id"] = None
        __props__.__dict__["tag_id"] = None
        __props__.__dict__["version"] = None
        return Tag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the tag, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/tags/tag1". If the package part contains slashes, the slashes are escaped. The tag part can only have characters in [a-zA-Z0-9\-._~:@], anything else must be URL encoded.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="packageId")
    def package_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "package_id")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "repository_id")

    @property
    @pulumi.getter(name="tagId")
    def tag_id(self) -> pulumi.Output[Optional[str]]:
        """
        The tag id to use for this repository.
        """
        return pulumi.get(self, "tag_id")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The name of the version the tag refers to, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/sha256:5243811" If the package or version ID parts contain slashes, the slashes are escaped.
        """
        return pulumi.get(self, "version")

