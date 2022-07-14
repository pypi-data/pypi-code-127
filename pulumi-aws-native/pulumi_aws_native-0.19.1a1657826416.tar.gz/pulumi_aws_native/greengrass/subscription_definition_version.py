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

__all__ = ['SubscriptionDefinitionVersionInitArgs', 'SubscriptionDefinitionVersion']

@pulumi.input_type
class SubscriptionDefinitionVersionInitArgs:
    def __init__(__self__, *,
                 subscription_definition_id: pulumi.Input[str],
                 subscriptions: pulumi.Input[Sequence[pulumi.Input['SubscriptionDefinitionVersionSubscriptionArgs']]]):
        """
        The set of arguments for constructing a SubscriptionDefinitionVersion resource.
        """
        pulumi.set(__self__, "subscription_definition_id", subscription_definition_id)
        pulumi.set(__self__, "subscriptions", subscriptions)

    @property
    @pulumi.getter(name="subscriptionDefinitionId")
    def subscription_definition_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "subscription_definition_id")

    @subscription_definition_id.setter
    def subscription_definition_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subscription_definition_id", value)

    @property
    @pulumi.getter
    def subscriptions(self) -> pulumi.Input[Sequence[pulumi.Input['SubscriptionDefinitionVersionSubscriptionArgs']]]:
        return pulumi.get(self, "subscriptions")

    @subscriptions.setter
    def subscriptions(self, value: pulumi.Input[Sequence[pulumi.Input['SubscriptionDefinitionVersionSubscriptionArgs']]]):
        pulumi.set(self, "subscriptions", value)


warnings.warn("""SubscriptionDefinitionVersion is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class SubscriptionDefinitionVersion(pulumi.CustomResource):
    warnings.warn("""SubscriptionDefinitionVersion is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 subscription_definition_id: Optional[pulumi.Input[str]] = None,
                 subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionDefinitionVersionSubscriptionArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Greengrass::SubscriptionDefinitionVersion

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubscriptionDefinitionVersionInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Greengrass::SubscriptionDefinitionVersion

        :param str resource_name: The name of the resource.
        :param SubscriptionDefinitionVersionInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubscriptionDefinitionVersionInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 subscription_definition_id: Optional[pulumi.Input[str]] = None,
                 subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriptionDefinitionVersionSubscriptionArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""SubscriptionDefinitionVersion is deprecated: SubscriptionDefinitionVersion is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = SubscriptionDefinitionVersionInitArgs.__new__(SubscriptionDefinitionVersionInitArgs)

            if subscription_definition_id is None and not opts.urn:
                raise TypeError("Missing required property 'subscription_definition_id'")
            __props__.__dict__["subscription_definition_id"] = subscription_definition_id
            if subscriptions is None and not opts.urn:
                raise TypeError("Missing required property 'subscriptions'")
            __props__.__dict__["subscriptions"] = subscriptions
        super(SubscriptionDefinitionVersion, __self__).__init__(
            'aws-native:greengrass:SubscriptionDefinitionVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SubscriptionDefinitionVersion':
        """
        Get an existing SubscriptionDefinitionVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SubscriptionDefinitionVersionInitArgs.__new__(SubscriptionDefinitionVersionInitArgs)

        __props__.__dict__["subscription_definition_id"] = None
        __props__.__dict__["subscriptions"] = None
        return SubscriptionDefinitionVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="subscriptionDefinitionId")
    def subscription_definition_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "subscription_definition_id")

    @property
    @pulumi.getter
    def subscriptions(self) -> pulumi.Output[Sequence['outputs.SubscriptionDefinitionVersionSubscription']]:
        return pulumi.get(self, "subscriptions")

