# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserProfileArgs', 'UserProfile']

@pulumi.input_type
class UserProfileArgs:
    def __init__(__self__, *,
                 iam_user_arn: pulumi.Input[str],
                 allow_self_management: Optional[pulumi.Input[bool]] = None,
                 ssh_public_key: Optional[pulumi.Input[str]] = None,
                 ssh_username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UserProfile resource.
        """
        pulumi.set(__self__, "iam_user_arn", iam_user_arn)
        if allow_self_management is not None:
            pulumi.set(__self__, "allow_self_management", allow_self_management)
        if ssh_public_key is not None:
            pulumi.set(__self__, "ssh_public_key", ssh_public_key)
        if ssh_username is not None:
            pulumi.set(__self__, "ssh_username", ssh_username)

    @property
    @pulumi.getter(name="iamUserArn")
    def iam_user_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "iam_user_arn")

    @iam_user_arn.setter
    def iam_user_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "iam_user_arn", value)

    @property
    @pulumi.getter(name="allowSelfManagement")
    def allow_self_management(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_self_management")

    @allow_self_management.setter
    def allow_self_management(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_self_management", value)

    @property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ssh_public_key")

    @ssh_public_key.setter
    def ssh_public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssh_public_key", value)

    @property
    @pulumi.getter(name="sshUsername")
    def ssh_username(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ssh_username")

    @ssh_username.setter
    def ssh_username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssh_username", value)


warnings.warn("""UserProfile is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class UserProfile(pulumi.CustomResource):
    warnings.warn("""UserProfile is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_self_management: Optional[pulumi.Input[bool]] = None,
                 iam_user_arn: Optional[pulumi.Input[str]] = None,
                 ssh_public_key: Optional[pulumi.Input[str]] = None,
                 ssh_username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::OpsWorks::UserProfile

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::OpsWorks::UserProfile

        :param str resource_name: The name of the resource.
        :param UserProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_self_management: Optional[pulumi.Input[bool]] = None,
                 iam_user_arn: Optional[pulumi.Input[str]] = None,
                 ssh_public_key: Optional[pulumi.Input[str]] = None,
                 ssh_username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""UserProfile is deprecated: UserProfile is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = UserProfileArgs.__new__(UserProfileArgs)

            __props__.__dict__["allow_self_management"] = allow_self_management
            if iam_user_arn is None and not opts.urn:
                raise TypeError("Missing required property 'iam_user_arn'")
            __props__.__dict__["iam_user_arn"] = iam_user_arn
            __props__.__dict__["ssh_public_key"] = ssh_public_key
            __props__.__dict__["ssh_username"] = ssh_username
        super(UserProfile, __self__).__init__(
            'aws-native:opsworks:UserProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UserProfile':
        """
        Get an existing UserProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserProfileArgs.__new__(UserProfileArgs)

        __props__.__dict__["allow_self_management"] = None
        __props__.__dict__["iam_user_arn"] = None
        __props__.__dict__["ssh_public_key"] = None
        __props__.__dict__["ssh_username"] = None
        return UserProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowSelfManagement")
    def allow_self_management(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "allow_self_management")

    @property
    @pulumi.getter(name="iamUserArn")
    def iam_user_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "iam_user_arn")

    @property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ssh_public_key")

    @property
    @pulumi.getter(name="sshUsername")
    def ssh_username(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ssh_username")

