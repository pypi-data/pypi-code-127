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

__all__ = ['JobDefinitionArgs', 'JobDefinition']

@pulumi.input_type
class JobDefinitionArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 container_properties: Optional[pulumi.Input['JobDefinitionContainerPropertiesArgs']] = None,
                 job_definition_name: Optional[pulumi.Input[str]] = None,
                 node_properties: Optional[pulumi.Input['JobDefinitionNodePropertiesArgs']] = None,
                 parameters: Optional[Any] = None,
                 platform_capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 propagate_tags: Optional[pulumi.Input[bool]] = None,
                 retry_strategy: Optional[pulumi.Input['JobDefinitionRetryStrategyArgs']] = None,
                 scheduling_priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[Any] = None,
                 timeout: Optional[pulumi.Input['JobDefinitionTimeoutArgs']] = None):
        """
        The set of arguments for constructing a JobDefinition resource.
        """
        pulumi.set(__self__, "type", type)
        if container_properties is not None:
            pulumi.set(__self__, "container_properties", container_properties)
        if job_definition_name is not None:
            pulumi.set(__self__, "job_definition_name", job_definition_name)
        if node_properties is not None:
            pulumi.set(__self__, "node_properties", node_properties)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if platform_capabilities is not None:
            pulumi.set(__self__, "platform_capabilities", platform_capabilities)
        if propagate_tags is not None:
            pulumi.set(__self__, "propagate_tags", propagate_tags)
        if retry_strategy is not None:
            pulumi.set(__self__, "retry_strategy", retry_strategy)
        if scheduling_priority is not None:
            pulumi.set(__self__, "scheduling_priority", scheduling_priority)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="containerProperties")
    def container_properties(self) -> Optional[pulumi.Input['JobDefinitionContainerPropertiesArgs']]:
        return pulumi.get(self, "container_properties")

    @container_properties.setter
    def container_properties(self, value: Optional[pulumi.Input['JobDefinitionContainerPropertiesArgs']]):
        pulumi.set(self, "container_properties", value)

    @property
    @pulumi.getter(name="jobDefinitionName")
    def job_definition_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "job_definition_name")

    @job_definition_name.setter
    def job_definition_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_definition_name", value)

    @property
    @pulumi.getter(name="nodeProperties")
    def node_properties(self) -> Optional[pulumi.Input['JobDefinitionNodePropertiesArgs']]:
        return pulumi.get(self, "node_properties")

    @node_properties.setter
    def node_properties(self, value: Optional[pulumi.Input['JobDefinitionNodePropertiesArgs']]):
        pulumi.set(self, "node_properties", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[Any]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="platformCapabilities")
    def platform_capabilities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "platform_capabilities")

    @platform_capabilities.setter
    def platform_capabilities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "platform_capabilities", value)

    @property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "propagate_tags")

    @propagate_tags.setter
    def propagate_tags(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "propagate_tags", value)

    @property
    @pulumi.getter(name="retryStrategy")
    def retry_strategy(self) -> Optional[pulumi.Input['JobDefinitionRetryStrategyArgs']]:
        return pulumi.get(self, "retry_strategy")

    @retry_strategy.setter
    def retry_strategy(self, value: Optional[pulumi.Input['JobDefinitionRetryStrategyArgs']]):
        pulumi.set(self, "retry_strategy", value)

    @property
    @pulumi.getter(name="schedulingPriority")
    def scheduling_priority(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "scheduling_priority")

    @scheduling_priority.setter
    def scheduling_priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scheduling_priority", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input['JobDefinitionTimeoutArgs']]:
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input['JobDefinitionTimeoutArgs']]):
        pulumi.set(self, "timeout", value)


warnings.warn("""JobDefinition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class JobDefinition(pulumi.CustomResource):
    warnings.warn("""JobDefinition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_properties: Optional[pulumi.Input[pulumi.InputType['JobDefinitionContainerPropertiesArgs']]] = None,
                 job_definition_name: Optional[pulumi.Input[str]] = None,
                 node_properties: Optional[pulumi.Input[pulumi.InputType['JobDefinitionNodePropertiesArgs']]] = None,
                 parameters: Optional[Any] = None,
                 platform_capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 propagate_tags: Optional[pulumi.Input[bool]] = None,
                 retry_strategy: Optional[pulumi.Input[pulumi.InputType['JobDefinitionRetryStrategyArgs']]] = None,
                 scheduling_priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[Any] = None,
                 timeout: Optional[pulumi.Input[pulumi.InputType['JobDefinitionTimeoutArgs']]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Batch::JobDefinition

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JobDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Batch::JobDefinition

        :param str resource_name: The name of the resource.
        :param JobDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JobDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_properties: Optional[pulumi.Input[pulumi.InputType['JobDefinitionContainerPropertiesArgs']]] = None,
                 job_definition_name: Optional[pulumi.Input[str]] = None,
                 node_properties: Optional[pulumi.Input[pulumi.InputType['JobDefinitionNodePropertiesArgs']]] = None,
                 parameters: Optional[Any] = None,
                 platform_capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 propagate_tags: Optional[pulumi.Input[bool]] = None,
                 retry_strategy: Optional[pulumi.Input[pulumi.InputType['JobDefinitionRetryStrategyArgs']]] = None,
                 scheduling_priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[Any] = None,
                 timeout: Optional[pulumi.Input[pulumi.InputType['JobDefinitionTimeoutArgs']]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""JobDefinition is deprecated: JobDefinition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = JobDefinitionArgs.__new__(JobDefinitionArgs)

            __props__.__dict__["container_properties"] = container_properties
            __props__.__dict__["job_definition_name"] = job_definition_name
            __props__.__dict__["node_properties"] = node_properties
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["platform_capabilities"] = platform_capabilities
            __props__.__dict__["propagate_tags"] = propagate_tags
            __props__.__dict__["retry_strategy"] = retry_strategy
            __props__.__dict__["scheduling_priority"] = scheduling_priority
            __props__.__dict__["tags"] = tags
            __props__.__dict__["timeout"] = timeout
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(JobDefinition, __self__).__init__(
            'aws-native:batch:JobDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'JobDefinition':
        """
        Get an existing JobDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = JobDefinitionArgs.__new__(JobDefinitionArgs)

        __props__.__dict__["container_properties"] = None
        __props__.__dict__["job_definition_name"] = None
        __props__.__dict__["node_properties"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["platform_capabilities"] = None
        __props__.__dict__["propagate_tags"] = None
        __props__.__dict__["retry_strategy"] = None
        __props__.__dict__["scheduling_priority"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["timeout"] = None
        __props__.__dict__["type"] = None
        return JobDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerProperties")
    def container_properties(self) -> pulumi.Output[Optional['outputs.JobDefinitionContainerProperties']]:
        return pulumi.get(self, "container_properties")

    @property
    @pulumi.getter(name="jobDefinitionName")
    def job_definition_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "job_definition_name")

    @property
    @pulumi.getter(name="nodeProperties")
    def node_properties(self) -> pulumi.Output[Optional['outputs.JobDefinitionNodeProperties']]:
        return pulumi.get(self, "node_properties")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="platformCapabilities")
    def platform_capabilities(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "platform_capabilities")

    @property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "propagate_tags")

    @property
    @pulumi.getter(name="retryStrategy")
    def retry_strategy(self) -> pulumi.Output[Optional['outputs.JobDefinitionRetryStrategy']]:
        return pulumi.get(self, "retry_strategy")

    @property
    @pulumi.getter(name="schedulingPriority")
    def scheduling_priority(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "scheduling_priority")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional['outputs.JobDefinitionTimeout']]:
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "type")

