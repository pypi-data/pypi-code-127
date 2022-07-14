# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserPoolUICustomizationAttachmentArgs', 'UserPoolUICustomizationAttachment']

@pulumi.input_type
class UserPoolUICustomizationAttachmentArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[str],
                 user_pool_id: pulumi.Input[str],
                 c_ss: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UserPoolUICustomizationAttachment resource.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "user_pool_id", user_pool_id)
        if c_ss is not None:
            pulumi.set(__self__, "c_ss", c_ss)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "user_pool_id")

    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_pool_id", value)

    @property
    @pulumi.getter(name="cSS")
    def c_ss(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "c_ss")

    @c_ss.setter
    def c_ss(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "c_ss", value)


warnings.warn("""UserPoolUICustomizationAttachment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class UserPoolUICustomizationAttachment(pulumi.CustomResource):
    warnings.warn("""UserPoolUICustomizationAttachment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 c_ss: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 user_pool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Cognito::UserPoolUICustomizationAttachment

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserPoolUICustomizationAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Cognito::UserPoolUICustomizationAttachment

        :param str resource_name: The name of the resource.
        :param UserPoolUICustomizationAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserPoolUICustomizationAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 c_ss: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 user_pool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""UserPoolUICustomizationAttachment is deprecated: UserPoolUICustomizationAttachment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = UserPoolUICustomizationAttachmentArgs.__new__(UserPoolUICustomizationAttachmentArgs)

            __props__.__dict__["c_ss"] = c_ss
            if client_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_id'")
            __props__.__dict__["client_id"] = client_id
            if user_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_pool_id'")
            __props__.__dict__["user_pool_id"] = user_pool_id
        super(UserPoolUICustomizationAttachment, __self__).__init__(
            'aws-native:cognito:UserPoolUICustomizationAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UserPoolUICustomizationAttachment':
        """
        Get an existing UserPoolUICustomizationAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserPoolUICustomizationAttachmentArgs.__new__(UserPoolUICustomizationAttachmentArgs)

        __props__.__dict__["c_ss"] = None
        __props__.__dict__["client_id"] = None
        __props__.__dict__["user_pool_id"] = None
        return UserPoolUICustomizationAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cSS")
    def c_ss(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "c_ss")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "user_pool_id")

