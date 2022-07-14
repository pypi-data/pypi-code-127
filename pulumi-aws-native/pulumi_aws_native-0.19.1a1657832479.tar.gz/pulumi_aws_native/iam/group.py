# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['GroupArgs', 'Group']

@pulumi.input_type
class GroupArgs:
    def __init__(__self__, *,
                 group_name: Optional[pulumi.Input[str]] = None,
                 managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input['GroupPolicyArgs']]]] = None):
        """
        The set of arguments for constructing a Group resource.
        """
        if group_name is not None:
            pulumi.set(__self__, "group_name", group_name)
        if managed_policy_arns is not None:
            pulumi.set(__self__, "managed_policy_arns", managed_policy_arns)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if policies is not None:
            pulumi.set(__self__, "policies", policies)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "managed_policy_arns")

    @managed_policy_arns.setter
    def managed_policy_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "managed_policy_arns", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GroupPolicyArgs']]]]:
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GroupPolicyArgs']]]]):
        pulumi.set(self, "policies", value)


warnings.warn("""Group is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Group(pulumi.CustomResource):
    warnings.warn("""Group is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GroupPolicyArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::IAM::Group

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[GroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::IAM::Group

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
                 group_name: Optional[pulumi.Input[str]] = None,
                 managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GroupPolicyArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""Group is deprecated: Group is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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

            __props__.__dict__["group_name"] = group_name
            __props__.__dict__["managed_policy_arns"] = managed_policy_arns
            __props__.__dict__["path"] = path
            __props__.__dict__["policies"] = policies
            __props__.__dict__["arn"] = None
        super(Group, __self__).__init__(
            'aws-native:iam:Group',
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

        __props__.__dict__["arn"] = None
        __props__.__dict__["group_name"] = None
        __props__.__dict__["managed_policy_arns"] = None
        __props__.__dict__["path"] = None
        __props__.__dict__["policies"] = None
        return Group(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "group_name")

    @property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "managed_policy_arns")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Optional[Sequence['outputs.GroupPolicy']]]:
        return pulumi.get(self, "policies")

