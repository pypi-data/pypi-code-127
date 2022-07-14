# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PolicyArgs', 'Policy']

@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *,
                 policy_document: Any,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Policy resource.
        """
        pulumi.set(__self__, "policy_document", policy_document)
        if groups is not None:
            pulumi.set(__self__, "groups", groups)
        if policy_name is not None:
            pulumi.set(__self__, "policy_name", policy_name)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if users is not None:
            pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Any:
        return pulumi.get(self, "policy_document")

    @policy_document.setter
    def policy_document(self, value: Any):
        pulumi.set(self, "policy_document", value)

    @property
    @pulumi.getter
    def groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "groups")

    @groups.setter
    def groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "groups", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter
    def users(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "users")

    @users.setter
    def users(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "users", value)


warnings.warn("""Policy is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Policy(pulumi.CustomResource):
    warnings.warn("""Policy is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_document: Optional[Any] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::IAM::Policy

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::IAM::Policy

        :param str resource_name: The name of the resource.
        :param PolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_document: Optional[Any] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        pulumi.log.warn("""Policy is deprecated: Policy is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = PolicyArgs.__new__(PolicyArgs)

            __props__.__dict__["groups"] = groups
            if policy_document is None and not opts.urn:
                raise TypeError("Missing required property 'policy_document'")
            __props__.__dict__["policy_document"] = policy_document
            __props__.__dict__["policy_name"] = policy_name
            __props__.__dict__["roles"] = roles
            __props__.__dict__["users"] = users
        super(Policy, __self__).__init__(
            'aws-native:iam:Policy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Policy':
        """
        Get an existing Policy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PolicyArgs.__new__(PolicyArgs)

        __props__.__dict__["groups"] = None
        __props__.__dict__["policy_document"] = None
        __props__.__dict__["policy_name"] = None
        __props__.__dict__["roles"] = None
        __props__.__dict__["users"] = None
        return Policy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def groups(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[Any]:
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def users(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "users")

