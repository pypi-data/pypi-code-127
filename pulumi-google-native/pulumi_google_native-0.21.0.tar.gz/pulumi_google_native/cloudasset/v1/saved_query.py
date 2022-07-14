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
from ._inputs import *

__all__ = ['SavedQueryArgs', 'SavedQuery']

@pulumi.input_type
class SavedQueryArgs:
    def __init__(__self__, *,
                 saved_query_id: pulumi.Input[str],
                 v1_id: pulumi.Input[str],
                 v1_id1: pulumi.Input[str],
                 content: Optional[pulumi.Input['QueryContentArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SavedQuery resource.
        :param pulumi.Input[str] saved_query_id: Required. The ID to use for the saved query, which must be unique in the specified parent. It will become the final component of the saved query's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Notice that this field is required in the saved query creation, and the `name` field of the `saved_query` will be ignored.
        :param pulumi.Input['QueryContentArgs'] content: The query content.
        :param pulumi.Input[str] description: The description of this saved query. This value should be fewer than 255 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels applied on the resource. This value should not contain more than 10 entries. The key and value of each entry must be non-empty and fewer than 64 characters.
        :param pulumi.Input[str] name: The resource name of the saved query. The format must be: * projects/project_number/savedQueries/saved_query_id * folders/folder_number/savedQueries/saved_query_id * organizations/organization_number/savedQueries/saved_query_id
        """
        pulumi.set(__self__, "saved_query_id", saved_query_id)
        pulumi.set(__self__, "v1_id", v1_id)
        pulumi.set(__self__, "v1_id1", v1_id1)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="savedQueryId")
    def saved_query_id(self) -> pulumi.Input[str]:
        """
        Required. The ID to use for the saved query, which must be unique in the specified parent. It will become the final component of the saved query's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Notice that this field is required in the saved query creation, and the `name` field of the `saved_query` will be ignored.
        """
        return pulumi.get(self, "saved_query_id")

    @saved_query_id.setter
    def saved_query_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "saved_query_id", value)

    @property
    @pulumi.getter(name="v1Id")
    def v1_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "v1_id")

    @v1_id.setter
    def v1_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "v1_id", value)

    @property
    @pulumi.getter(name="v1Id1")
    def v1_id1(self) -> pulumi.Input[str]:
        return pulumi.get(self, "v1_id1")

    @v1_id1.setter
    def v1_id1(self, value: pulumi.Input[str]):
        pulumi.set(self, "v1_id1", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input['QueryContentArgs']]:
        """
        The query content.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input['QueryContentArgs']]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of this saved query. This value should be fewer than 255 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels applied on the resource. This value should not contain more than 10 entries. The key and value of each entry must be non-empty and fewer than 64 characters.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the saved query. The format must be: * projects/project_number/savedQueries/saved_query_id * folders/folder_number/savedQueries/saved_query_id * organizations/organization_number/savedQueries/saved_query_id
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class SavedQuery(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[pulumi.InputType['QueryContentArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 saved_query_id: Optional[pulumi.Input[str]] = None,
                 v1_id: Optional[pulumi.Input[str]] = None,
                 v1_id1: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a saved query in a parent project/folder/organization.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['QueryContentArgs']] content: The query content.
        :param pulumi.Input[str] description: The description of this saved query. This value should be fewer than 255 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels applied on the resource. This value should not contain more than 10 entries. The key and value of each entry must be non-empty and fewer than 64 characters.
        :param pulumi.Input[str] name: The resource name of the saved query. The format must be: * projects/project_number/savedQueries/saved_query_id * folders/folder_number/savedQueries/saved_query_id * organizations/organization_number/savedQueries/saved_query_id
        :param pulumi.Input[str] saved_query_id: Required. The ID to use for the saved query, which must be unique in the specified parent. It will become the final component of the saved query's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Notice that this field is required in the saved query creation, and the `name` field of the `saved_query` will be ignored.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SavedQueryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a saved query in a parent project/folder/organization.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param SavedQueryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SavedQueryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[pulumi.InputType['QueryContentArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 saved_query_id: Optional[pulumi.Input[str]] = None,
                 v1_id: Optional[pulumi.Input[str]] = None,
                 v1_id1: Optional[pulumi.Input[str]] = None,
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
            __props__ = SavedQueryArgs.__new__(SavedQueryArgs)

            __props__.__dict__["content"] = content
            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            if saved_query_id is None and not opts.urn:
                raise TypeError("Missing required property 'saved_query_id'")
            __props__.__dict__["saved_query_id"] = saved_query_id
            if v1_id is None and not opts.urn:
                raise TypeError("Missing required property 'v1_id'")
            __props__.__dict__["v1_id"] = v1_id
            if v1_id1 is None and not opts.urn:
                raise TypeError("Missing required property 'v1_id1'")
            __props__.__dict__["v1_id1"] = v1_id1
            __props__.__dict__["create_time"] = None
            __props__.__dict__["creator"] = None
            __props__.__dict__["last_update_time"] = None
            __props__.__dict__["last_updater"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["saved_query_id", "v1_id", "v1_id1"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(SavedQuery, __self__).__init__(
            'google-native:cloudasset/v1:SavedQuery',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SavedQuery':
        """
        Get an existing SavedQuery resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SavedQueryArgs.__new__(SavedQueryArgs)

        __props__.__dict__["content"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["creator"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["last_update_time"] = None
        __props__.__dict__["last_updater"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["saved_query_id"] = None
        __props__.__dict__["v1_id"] = None
        __props__.__dict__["v1_id1"] = None
        return SavedQuery(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output['outputs.QueryContentResponse']:
        """
        The query content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The create time of this saved query.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def creator(self) -> pulumi.Output[str]:
        """
        The account's email address who has created this saved query.
        """
        return pulumi.get(self, "creator")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of this saved query. This value should be fewer than 255 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels applied on the resource. This value should not contain more than 10 entries. The key and value of each entry must be non-empty and fewer than 64 characters.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> pulumi.Output[str]:
        """
        The last update time of this saved query.
        """
        return pulumi.get(self, "last_update_time")

    @property
    @pulumi.getter(name="lastUpdater")
    def last_updater(self) -> pulumi.Output[str]:
        """
        The account's email address who has updated this saved query most recently.
        """
        return pulumi.get(self, "last_updater")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the saved query. The format must be: * projects/project_number/savedQueries/saved_query_id * folders/folder_number/savedQueries/saved_query_id * organizations/organization_number/savedQueries/saved_query_id
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="savedQueryId")
    def saved_query_id(self) -> pulumi.Output[str]:
        """
        Required. The ID to use for the saved query, which must be unique in the specified parent. It will become the final component of the saved query's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Notice that this field is required in the saved query creation, and the `name` field of the `saved_query` will be ignored.
        """
        return pulumi.get(self, "saved_query_id")

    @property
    @pulumi.getter(name="v1Id")
    def v1_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "v1_id")

    @property
    @pulumi.getter(name="v1Id1")
    def v1_id1(self) -> pulumi.Output[str]:
        return pulumi.get(self, "v1_id1")

