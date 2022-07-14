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

__all__ = ['GameSessionQueueArgs', 'GameSessionQueue']

@pulumi.input_type
class GameSessionQueueArgs:
    def __init__(__self__, *,
                 custom_event_data: Optional[pulumi.Input[str]] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input['GameSessionQueueDestinationArgs']]]] = None,
                 filter_configuration: Optional[pulumi.Input['GameSessionQueueFilterConfigurationArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_target: Optional[pulumi.Input[str]] = None,
                 player_latency_policies: Optional[pulumi.Input[Sequence[pulumi.Input['GameSessionQueuePlayerLatencyPolicyArgs']]]] = None,
                 priority_configuration: Optional[pulumi.Input['GameSessionQueuePriorityConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['GameSessionQueueTagArgs']]]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a GameSessionQueue resource.
        """
        if custom_event_data is not None:
            pulumi.set(__self__, "custom_event_data", custom_event_data)
        if destinations is not None:
            pulumi.set(__self__, "destinations", destinations)
        if filter_configuration is not None:
            pulumi.set(__self__, "filter_configuration", filter_configuration)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_target is not None:
            pulumi.set(__self__, "notification_target", notification_target)
        if player_latency_policies is not None:
            pulumi.set(__self__, "player_latency_policies", player_latency_policies)
        if priority_configuration is not None:
            pulumi.set(__self__, "priority_configuration", priority_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if timeout_in_seconds is not None:
            pulumi.set(__self__, "timeout_in_seconds", timeout_in_seconds)

    @property
    @pulumi.getter(name="customEventData")
    def custom_event_data(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "custom_event_data")

    @custom_event_data.setter
    def custom_event_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_event_data", value)

    @property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GameSessionQueueDestinationArgs']]]]:
        return pulumi.get(self, "destinations")

    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GameSessionQueueDestinationArgs']]]]):
        pulumi.set(self, "destinations", value)

    @property
    @pulumi.getter(name="filterConfiguration")
    def filter_configuration(self) -> Optional[pulumi.Input['GameSessionQueueFilterConfigurationArgs']]:
        return pulumi.get(self, "filter_configuration")

    @filter_configuration.setter
    def filter_configuration(self, value: Optional[pulumi.Input['GameSessionQueueFilterConfigurationArgs']]):
        pulumi.set(self, "filter_configuration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationTarget")
    def notification_target(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "notification_target")

    @notification_target.setter
    def notification_target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notification_target", value)

    @property
    @pulumi.getter(name="playerLatencyPolicies")
    def player_latency_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GameSessionQueuePlayerLatencyPolicyArgs']]]]:
        return pulumi.get(self, "player_latency_policies")

    @player_latency_policies.setter
    def player_latency_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GameSessionQueuePlayerLatencyPolicyArgs']]]]):
        pulumi.set(self, "player_latency_policies", value)

    @property
    @pulumi.getter(name="priorityConfiguration")
    def priority_configuration(self) -> Optional[pulumi.Input['GameSessionQueuePriorityConfigurationArgs']]:
        return pulumi.get(self, "priority_configuration")

    @priority_configuration.setter
    def priority_configuration(self, value: Optional[pulumi.Input['GameSessionQueuePriorityConfigurationArgs']]):
        pulumi.set(self, "priority_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GameSessionQueueTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GameSessionQueueTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "timeout_in_seconds")

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout_in_seconds", value)


warnings.warn("""GameSessionQueue is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class GameSessionQueue(pulumi.CustomResource):
    warnings.warn("""GameSessionQueue is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_event_data: Optional[pulumi.Input[str]] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameSessionQueueDestinationArgs']]]]] = None,
                 filter_configuration: Optional[pulumi.Input[pulumi.InputType['GameSessionQueueFilterConfigurationArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_target: Optional[pulumi.Input[str]] = None,
                 player_latency_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameSessionQueuePlayerLatencyPolicyArgs']]]]] = None,
                 priority_configuration: Optional[pulumi.Input[pulumi.InputType['GameSessionQueuePriorityConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameSessionQueueTagArgs']]]]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::GameLift::GameSessionQueue

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[GameSessionQueueArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::GameLift::GameSessionQueue

        :param str resource_name: The name of the resource.
        :param GameSessionQueueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GameSessionQueueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_event_data: Optional[pulumi.Input[str]] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameSessionQueueDestinationArgs']]]]] = None,
                 filter_configuration: Optional[pulumi.Input[pulumi.InputType['GameSessionQueueFilterConfigurationArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_target: Optional[pulumi.Input[str]] = None,
                 player_latency_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameSessionQueuePlayerLatencyPolicyArgs']]]]] = None,
                 priority_configuration: Optional[pulumi.Input[pulumi.InputType['GameSessionQueuePriorityConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameSessionQueueTagArgs']]]]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        pulumi.log.warn("""GameSessionQueue is deprecated: GameSessionQueue is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = GameSessionQueueArgs.__new__(GameSessionQueueArgs)

            __props__.__dict__["custom_event_data"] = custom_event_data
            __props__.__dict__["destinations"] = destinations
            __props__.__dict__["filter_configuration"] = filter_configuration
            __props__.__dict__["name"] = name
            __props__.__dict__["notification_target"] = notification_target
            __props__.__dict__["player_latency_policies"] = player_latency_policies
            __props__.__dict__["priority_configuration"] = priority_configuration
            __props__.__dict__["tags"] = tags
            __props__.__dict__["timeout_in_seconds"] = timeout_in_seconds
            __props__.__dict__["arn"] = None
        super(GameSessionQueue, __self__).__init__(
            'aws-native:gamelift:GameSessionQueue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GameSessionQueue':
        """
        Get an existing GameSessionQueue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GameSessionQueueArgs.__new__(GameSessionQueueArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["custom_event_data"] = None
        __props__.__dict__["destinations"] = None
        __props__.__dict__["filter_configuration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notification_target"] = None
        __props__.__dict__["player_latency_policies"] = None
        __props__.__dict__["priority_configuration"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["timeout_in_seconds"] = None
        return GameSessionQueue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="customEventData")
    def custom_event_data(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "custom_event_data")

    @property
    @pulumi.getter
    def destinations(self) -> pulumi.Output[Optional[Sequence['outputs.GameSessionQueueDestination']]]:
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter(name="filterConfiguration")
    def filter_configuration(self) -> pulumi.Output[Optional['outputs.GameSessionQueueFilterConfiguration']]:
        return pulumi.get(self, "filter_configuration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationTarget")
    def notification_target(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "notification_target")

    @property
    @pulumi.getter(name="playerLatencyPolicies")
    def player_latency_policies(self) -> pulumi.Output[Optional[Sequence['outputs.GameSessionQueuePlayerLatencyPolicy']]]:
        return pulumi.get(self, "player_latency_policies")

    @property
    @pulumi.getter(name="priorityConfiguration")
    def priority_configuration(self) -> pulumi.Output[Optional['outputs.GameSessionQueuePriorityConfiguration']]:
        return pulumi.get(self, "priority_configuration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.GameSessionQueueTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "timeout_in_seconds")

