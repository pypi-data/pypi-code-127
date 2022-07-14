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

__all__ = ['LifecyclePolicyArgs', 'LifecyclePolicy']

@pulumi.input_type
class LifecyclePolicyArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 policy_details: Optional[pulumi.Input['LifecyclePolicyPolicyDetailsArgs']] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['LifecyclePolicyTagArgs']]]] = None):
        """
        The set of arguments for constructing a LifecyclePolicy resource.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if execution_role_arn is not None:
            pulumi.set(__self__, "execution_role_arn", execution_role_arn)
        if policy_details is not None:
            pulumi.set(__self__, "policy_details", policy_details)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "execution_role_arn")

    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "execution_role_arn", value)

    @property
    @pulumi.getter(name="policyDetails")
    def policy_details(self) -> Optional[pulumi.Input['LifecyclePolicyPolicyDetailsArgs']]:
        return pulumi.get(self, "policy_details")

    @policy_details.setter
    def policy_details(self, value: Optional[pulumi.Input['LifecyclePolicyPolicyDetailsArgs']]):
        pulumi.set(self, "policy_details", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LifecyclePolicyTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LifecyclePolicyTagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""LifecyclePolicy is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class LifecyclePolicy(pulumi.CustomResource):
    warnings.warn("""LifecyclePolicy is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 policy_details: Optional[pulumi.Input[pulumi.InputType['LifecyclePolicyPolicyDetailsArgs']]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LifecyclePolicyTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::DLM::LifecyclePolicy

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[LifecyclePolicyArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::DLM::LifecyclePolicy

        :param str resource_name: The name of the resource.
        :param LifecyclePolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LifecyclePolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 policy_details: Optional[pulumi.Input[pulumi.InputType['LifecyclePolicyPolicyDetailsArgs']]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LifecyclePolicyTagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""LifecyclePolicy is deprecated: LifecyclePolicy is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LifecyclePolicyArgs.__new__(LifecyclePolicyArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["execution_role_arn"] = execution_role_arn
            __props__.__dict__["policy_details"] = policy_details
            __props__.__dict__["state"] = state
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(LifecyclePolicy, __self__).__init__(
            'aws-native:dlm:LifecyclePolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LifecyclePolicy':
        """
        Get an existing LifecyclePolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LifecyclePolicyArgs.__new__(LifecyclePolicyArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["execution_role_arn"] = None
        __props__.__dict__["policy_details"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        return LifecyclePolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "execution_role_arn")

    @property
    @pulumi.getter(name="policyDetails")
    def policy_details(self) -> pulumi.Output[Optional['outputs.LifecyclePolicyPolicyDetails']]:
        return pulumi.get(self, "policy_details")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.LifecyclePolicyTag']]]:
        return pulumi.get(self, "tags")

