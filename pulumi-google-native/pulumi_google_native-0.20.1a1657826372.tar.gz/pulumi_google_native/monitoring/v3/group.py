# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['GroupArgs', 'Group']

@pulumi.input_type
class GroupArgs:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 is_cluster: Optional[pulumi.Input[bool]] = None,
                 parent_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 validate_only: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Group resource.
        :param pulumi.Input[str] display_name: A user-assigned name for this group, used only for display purposes.
        :param pulumi.Input[str] filter: The filter used to determine which monitored resources belong to this group.
        :param pulumi.Input[bool] is_cluster: If true, the members of this group are considered to be a cluster. The system can perform additional analysis on groups that are clusters.
        :param pulumi.Input[str] parent_name: The name of the group's parent, if it has one. The format is: projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID] For groups with no parent, parent_name is the empty string, "".
        :param pulumi.Input[str] validate_only: If true, validate this request but do not create the group.
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if is_cluster is not None:
            pulumi.set(__self__, "is_cluster", is_cluster)
        if parent_name is not None:
            pulumi.set(__self__, "parent_name", parent_name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if validate_only is not None:
            pulumi.set(__self__, "validate_only", validate_only)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-assigned name for this group, used only for display purposes.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        """
        The filter used to determine which monitored resources belong to this group.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter(name="isCluster")
    def is_cluster(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, the members of this group are considered to be a cluster. The system can perform additional analysis on groups that are clusters.
        """
        return pulumi.get(self, "is_cluster")

    @is_cluster.setter
    def is_cluster(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_cluster", value)

    @property
    @pulumi.getter(name="parentName")
    def parent_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the group's parent, if it has one. The format is: projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID] For groups with no parent, parent_name is the empty string, "".
        """
        return pulumi.get(self, "parent_name")

    @parent_name.setter
    def parent_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="validateOnly")
    def validate_only(self) -> Optional[pulumi.Input[str]]:
        """
        If true, validate this request but do not create the group.
        """
        return pulumi.get(self, "validate_only")

    @validate_only.setter
    def validate_only(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "validate_only", value)


class Group(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 is_cluster: Optional[pulumi.Input[bool]] = None,
                 parent_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 validate_only: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new group.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: A user-assigned name for this group, used only for display purposes.
        :param pulumi.Input[str] filter: The filter used to determine which monitored resources belong to this group.
        :param pulumi.Input[bool] is_cluster: If true, the members of this group are considered to be a cluster. The system can perform additional analysis on groups that are clusters.
        :param pulumi.Input[str] parent_name: The name of the group's parent, if it has one. The format is: projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID] For groups with no parent, parent_name is the empty string, "".
        :param pulumi.Input[str] validate_only: If true, validate this request but do not create the group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[GroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new group.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param GroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 is_cluster: Optional[pulumi.Input[bool]] = None,
                 parent_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 validate_only: Optional[pulumi.Input[str]] = None,
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
            __props__ = GroupArgs.__new__(GroupArgs)

            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["filter"] = filter
            __props__.__dict__["is_cluster"] = is_cluster
            __props__.__dict__["parent_name"] = parent_name
            __props__.__dict__["project"] = project
            __props__.__dict__["validate_only"] = validate_only
            __props__.__dict__["name"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Group, __self__).__init__(
            'google-native:monitoring/v3:Group',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Group':
        """
        Get an existing Group resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GroupArgs.__new__(GroupArgs)

        __props__.__dict__["display_name"] = None
        __props__.__dict__["filter"] = None
        __props__.__dict__["is_cluster"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parent_name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["validate_only"] = None
        return Group(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        A user-assigned name for this group, used only for display purposes.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[str]:
        """
        The filter used to determine which monitored resources belong to this group.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="isCluster")
    def is_cluster(self) -> pulumi.Output[bool]:
        """
        If true, the members of this group are considered to be a cluster. The system can perform additional analysis on groups that are clusters.
        """
        return pulumi.get(self, "is_cluster")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of this group. The format is: projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID] When creating a group, this field is ignored and a new name is created consisting of the project specified in the call to CreateGroup and a unique [GROUP_ID] that is generated automatically.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentName")
    def parent_name(self) -> pulumi.Output[str]:
        """
        The name of the group's parent, if it has one. The format is: projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID] For groups with no parent, parent_name is the empty string, "".
        """
        return pulumi.get(self, "parent_name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="validateOnly")
    def validate_only(self) -> pulumi.Output[Optional[str]]:
        """
        If true, validate this request but do not create the group.
        """
        return pulumi.get(self, "validate_only")

