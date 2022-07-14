# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 engine: pulumi.Input['UserEngine'],
                 user_id: pulumi.Input[str],
                 access_string: Optional[pulumi.Input[str]] = None,
                 no_password_required: Optional[pulumi.Input[bool]] = None,
                 passwords: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 user_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input['UserEngine'] engine: Must be redis.
        :param pulumi.Input[str] user_id: The ID of the user.
        :param pulumi.Input[str] access_string: Access permissions string used for this user account.
        :param pulumi.Input[bool] no_password_required: Indicates a password is not required for this user account.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] passwords: Passwords used for this user account. You can create up to two passwords for each user.
        :param pulumi.Input[str] user_name: The username of the user.
        """
        pulumi.set(__self__, "engine", engine)
        pulumi.set(__self__, "user_id", user_id)
        if access_string is not None:
            pulumi.set(__self__, "access_string", access_string)
        if no_password_required is not None:
            pulumi.set(__self__, "no_password_required", no_password_required)
        if passwords is not None:
            pulumi.set(__self__, "passwords", passwords)
        if user_name is not None:
            pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Input['UserEngine']:
        """
        Must be redis.
        """
        return pulumi.get(self, "engine")

    @engine.setter
    def engine(self, value: pulumi.Input['UserEngine']):
        pulumi.set(self, "engine", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[str]:
        """
        The ID of the user.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter(name="accessString")
    def access_string(self) -> Optional[pulumi.Input[str]]:
        """
        Access permissions string used for this user account.
        """
        return pulumi.get(self, "access_string")

    @access_string.setter
    def access_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_string", value)

    @property
    @pulumi.getter(name="noPasswordRequired")
    def no_password_required(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates a password is not required for this user account.
        """
        return pulumi.get(self, "no_password_required")

    @no_password_required.setter
    def no_password_required(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "no_password_required", value)

    @property
    @pulumi.getter
    def passwords(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Passwords used for this user account. You can create up to two passwords for each user.
        """
        return pulumi.get(self, "passwords")

    @passwords.setter
    def passwords(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "passwords", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        """
        The username of the user.
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)


class User(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_string: Optional[pulumi.Input[str]] = None,
                 engine: Optional[pulumi.Input['UserEngine']] = None,
                 no_password_required: Optional[pulumi.Input[bool]] = None,
                 passwords: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ElastiCache::User

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_string: Access permissions string used for this user account.
        :param pulumi.Input['UserEngine'] engine: Must be redis.
        :param pulumi.Input[bool] no_password_required: Indicates a password is not required for this user account.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] passwords: Passwords used for this user account. You can create up to two passwords for each user.
        :param pulumi.Input[str] user_id: The ID of the user.
        :param pulumi.Input[str] user_name: The username of the user.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ElastiCache::User

        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_string: Optional[pulumi.Input[str]] = None,
                 engine: Optional[pulumi.Input['UserEngine']] = None,
                 no_password_required: Optional[pulumi.Input[bool]] = None,
                 passwords: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserArgs.__new__(UserArgs)

            __props__.__dict__["access_string"] = access_string
            if engine is None and not opts.urn:
                raise TypeError("Missing required property 'engine'")
            __props__.__dict__["engine"] = engine
            __props__.__dict__["no_password_required"] = no_password_required
            __props__.__dict__["passwords"] = passwords
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
            __props__.__dict__["user_name"] = user_name
            __props__.__dict__["arn"] = None
            __props__.__dict__["status"] = None
        super(User, __self__).__init__(
            'aws-native:elasticache:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserArgs.__new__(UserArgs)

        __props__.__dict__["access_string"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["engine"] = None
        __props__.__dict__["no_password_required"] = None
        __props__.__dict__["passwords"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["user_id"] = None
        __props__.__dict__["user_name"] = None
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessString")
    def access_string(self) -> pulumi.Output[Optional[str]]:
        """
        Access permissions string used for this user account.
        """
        return pulumi.get(self, "access_string")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the user account.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Output['UserEngine']:
        """
        Must be redis.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="noPasswordRequired")
    def no_password_required(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates a password is not required for this user account.
        """
        return pulumi.get(self, "no_password_required")

    @property
    @pulumi.getter
    def passwords(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Passwords used for this user account. You can create up to two passwords for each user.
        """
        return pulumi.get(self, "passwords")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Indicates the user status. Can be "active", "modifying" or "deleting".
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        The ID of the user.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        The username of the user.
        """
        return pulumi.get(self, "user_name")

