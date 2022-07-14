# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserVpcAuthorizationArgs', 'UserVpcAuthorization']

@pulumi.input_type
class UserVpcAuthorizationArgs:
    def __init__(__self__, *,
                 authorized_user_id: pulumi.Input[str],
                 auth_channel: Optional[pulumi.Input[str]] = None,
                 auth_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UserVpcAuthorization resource.
        :param pulumi.Input[str] authorized_user_id: The primary account ID of the user who authorizes the resource.
        :param pulumi.Input[str] auth_channel: The auth channel. Valid values: `RESOURCE_DIRECTORY`.
        :param pulumi.Input[str] auth_type: The type of Authorization. Valid values: `NORMAL` and `CLOUD_PRODUCT`.
        """
        pulumi.set(__self__, "authorized_user_id", authorized_user_id)
        if auth_channel is not None:
            pulumi.set(__self__, "auth_channel", auth_channel)
        if auth_type is not None:
            pulumi.set(__self__, "auth_type", auth_type)

    @property
    @pulumi.getter(name="authorizedUserId")
    def authorized_user_id(self) -> pulumi.Input[str]:
        """
        The primary account ID of the user who authorizes the resource.
        """
        return pulumi.get(self, "authorized_user_id")

    @authorized_user_id.setter
    def authorized_user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "authorized_user_id", value)

    @property
    @pulumi.getter(name="authChannel")
    def auth_channel(self) -> Optional[pulumi.Input[str]]:
        """
        The auth channel. Valid values: `RESOURCE_DIRECTORY`.
        """
        return pulumi.get(self, "auth_channel")

    @auth_channel.setter
    def auth_channel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_channel", value)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of Authorization. Valid values: `NORMAL` and `CLOUD_PRODUCT`.
        """
        return pulumi.get(self, "auth_type")

    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_type", value)


@pulumi.input_type
class _UserVpcAuthorizationState:
    def __init__(__self__, *,
                 auth_channel: Optional[pulumi.Input[str]] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 authorized_user_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UserVpcAuthorization resources.
        :param pulumi.Input[str] auth_channel: The auth channel. Valid values: `RESOURCE_DIRECTORY`.
        :param pulumi.Input[str] auth_type: The type of Authorization. Valid values: `NORMAL` and `CLOUD_PRODUCT`.
        :param pulumi.Input[str] authorized_user_id: The primary account ID of the user who authorizes the resource.
        """
        if auth_channel is not None:
            pulumi.set(__self__, "auth_channel", auth_channel)
        if auth_type is not None:
            pulumi.set(__self__, "auth_type", auth_type)
        if authorized_user_id is not None:
            pulumi.set(__self__, "authorized_user_id", authorized_user_id)

    @property
    @pulumi.getter(name="authChannel")
    def auth_channel(self) -> Optional[pulumi.Input[str]]:
        """
        The auth channel. Valid values: `RESOURCE_DIRECTORY`.
        """
        return pulumi.get(self, "auth_channel")

    @auth_channel.setter
    def auth_channel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_channel", value)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of Authorization. Valid values: `NORMAL` and `CLOUD_PRODUCT`.
        """
        return pulumi.get(self, "auth_type")

    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_type", value)

    @property
    @pulumi.getter(name="authorizedUserId")
    def authorized_user_id(self) -> Optional[pulumi.Input[str]]:
        """
        The primary account ID of the user who authorizes the resource.
        """
        return pulumi.get(self, "authorized_user_id")

    @authorized_user_id.setter
    def authorized_user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorized_user_id", value)


class UserVpcAuthorization(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_channel: Optional[pulumi.Input[str]] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 authorized_user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Private Zone User Vpc Authorization resource.

        > **NOTE:** Available in v1.138.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.pvtz.UserVpcAuthorization("example",
            auth_channel="RESOURCE_DIRECTORY",
            auth_type="NORMAL",
            authorized_user_id="example_value")
        ```

        ## Import

        Private Zone User Vpc Authorization can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:pvtz/userVpcAuthorization:UserVpcAuthorization example <authorized_user_id>:<auth_type>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_channel: The auth channel. Valid values: `RESOURCE_DIRECTORY`.
        :param pulumi.Input[str] auth_type: The type of Authorization. Valid values: `NORMAL` and `CLOUD_PRODUCT`.
        :param pulumi.Input[str] authorized_user_id: The primary account ID of the user who authorizes the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserVpcAuthorizationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Private Zone User Vpc Authorization resource.

        > **NOTE:** Available in v1.138.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.pvtz.UserVpcAuthorization("example",
            auth_channel="RESOURCE_DIRECTORY",
            auth_type="NORMAL",
            authorized_user_id="example_value")
        ```

        ## Import

        Private Zone User Vpc Authorization can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:pvtz/userVpcAuthorization:UserVpcAuthorization example <authorized_user_id>:<auth_type>
        ```

        :param str resource_name: The name of the resource.
        :param UserVpcAuthorizationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserVpcAuthorizationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_channel: Optional[pulumi.Input[str]] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 authorized_user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserVpcAuthorizationArgs.__new__(UserVpcAuthorizationArgs)

            __props__.__dict__["auth_channel"] = auth_channel
            __props__.__dict__["auth_type"] = auth_type
            if authorized_user_id is None and not opts.urn:
                raise TypeError("Missing required property 'authorized_user_id'")
            __props__.__dict__["authorized_user_id"] = authorized_user_id
        super(UserVpcAuthorization, __self__).__init__(
            'alicloud:pvtz/userVpcAuthorization:UserVpcAuthorization',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auth_channel: Optional[pulumi.Input[str]] = None,
            auth_type: Optional[pulumi.Input[str]] = None,
            authorized_user_id: Optional[pulumi.Input[str]] = None) -> 'UserVpcAuthorization':
        """
        Get an existing UserVpcAuthorization resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_channel: The auth channel. Valid values: `RESOURCE_DIRECTORY`.
        :param pulumi.Input[str] auth_type: The type of Authorization. Valid values: `NORMAL` and `CLOUD_PRODUCT`.
        :param pulumi.Input[str] authorized_user_id: The primary account ID of the user who authorizes the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserVpcAuthorizationState.__new__(_UserVpcAuthorizationState)

        __props__.__dict__["auth_channel"] = auth_channel
        __props__.__dict__["auth_type"] = auth_type
        __props__.__dict__["authorized_user_id"] = authorized_user_id
        return UserVpcAuthorization(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authChannel")
    def auth_channel(self) -> pulumi.Output[Optional[str]]:
        """
        The auth channel. Valid values: `RESOURCE_DIRECTORY`.
        """
        return pulumi.get(self, "auth_channel")

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of Authorization. Valid values: `NORMAL` and `CLOUD_PRODUCT`.
        """
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter(name="authorizedUserId")
    def authorized_user_id(self) -> pulumi.Output[str]:
        """
        The primary account ID of the user who authorizes the resource.
        """
        return pulumi.get(self, "authorized_user_id")

