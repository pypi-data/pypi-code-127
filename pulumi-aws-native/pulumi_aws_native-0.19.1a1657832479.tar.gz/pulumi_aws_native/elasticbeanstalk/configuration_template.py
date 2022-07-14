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

__all__ = ['ConfigurationTemplateArgs', 'ConfigurationTemplate']

@pulumi.input_type
class ConfigurationTemplateArgs:
    def __init__(__self__, *,
                 application_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 option_settings: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationTemplateConfigurationOptionSettingArgs']]]] = None,
                 platform_arn: Optional[pulumi.Input[str]] = None,
                 solution_stack_name: Optional[pulumi.Input[str]] = None,
                 source_configuration: Optional[pulumi.Input['ConfigurationTemplateSourceConfigurationArgs']] = None):
        """
        The set of arguments for constructing a ConfigurationTemplate resource.
        """
        pulumi.set(__self__, "application_name", application_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if environment_id is not None:
            pulumi.set(__self__, "environment_id", environment_id)
        if option_settings is not None:
            pulumi.set(__self__, "option_settings", option_settings)
        if platform_arn is not None:
            pulumi.set(__self__, "platform_arn", platform_arn)
        if solution_stack_name is not None:
            pulumi.set(__self__, "solution_stack_name", solution_stack_name)
        if source_configuration is not None:
            pulumi.set(__self__, "source_configuration", source_configuration)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application_name")

    @application_name.setter
    def application_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "environment_id")

    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_id", value)

    @property
    @pulumi.getter(name="optionSettings")
    def option_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationTemplateConfigurationOptionSettingArgs']]]]:
        return pulumi.get(self, "option_settings")

    @option_settings.setter
    def option_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationTemplateConfigurationOptionSettingArgs']]]]):
        pulumi.set(self, "option_settings", value)

    @property
    @pulumi.getter(name="platformArn")
    def platform_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "platform_arn")

    @platform_arn.setter
    def platform_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "platform_arn", value)

    @property
    @pulumi.getter(name="solutionStackName")
    def solution_stack_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "solution_stack_name")

    @solution_stack_name.setter
    def solution_stack_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "solution_stack_name", value)

    @property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(self) -> Optional[pulumi.Input['ConfigurationTemplateSourceConfigurationArgs']]:
        return pulumi.get(self, "source_configuration")

    @source_configuration.setter
    def source_configuration(self, value: Optional[pulumi.Input['ConfigurationTemplateSourceConfigurationArgs']]):
        pulumi.set(self, "source_configuration", value)


warnings.warn("""ConfigurationTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ConfigurationTemplate(pulumi.CustomResource):
    warnings.warn("""ConfigurationTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 option_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationTemplateConfigurationOptionSettingArgs']]]]] = None,
                 platform_arn: Optional[pulumi.Input[str]] = None,
                 solution_stack_name: Optional[pulumi.Input[str]] = None,
                 source_configuration: Optional[pulumi.Input[pulumi.InputType['ConfigurationTemplateSourceConfigurationArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ElasticBeanstalk::ConfigurationTemplate

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigurationTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ElasticBeanstalk::ConfigurationTemplate

        :param str resource_name: The name of the resource.
        :param ConfigurationTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigurationTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 option_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationTemplateConfigurationOptionSettingArgs']]]]] = None,
                 platform_arn: Optional[pulumi.Input[str]] = None,
                 solution_stack_name: Optional[pulumi.Input[str]] = None,
                 source_configuration: Optional[pulumi.Input[pulumi.InputType['ConfigurationTemplateSourceConfigurationArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""ConfigurationTemplate is deprecated: ConfigurationTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = ConfigurationTemplateArgs.__new__(ConfigurationTemplateArgs)

            if application_name is None and not opts.urn:
                raise TypeError("Missing required property 'application_name'")
            __props__.__dict__["application_name"] = application_name
            __props__.__dict__["description"] = description
            __props__.__dict__["environment_id"] = environment_id
            __props__.__dict__["option_settings"] = option_settings
            __props__.__dict__["platform_arn"] = platform_arn
            __props__.__dict__["solution_stack_name"] = solution_stack_name
            __props__.__dict__["source_configuration"] = source_configuration
        super(ConfigurationTemplate, __self__).__init__(
            'aws-native:elasticbeanstalk:ConfigurationTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConfigurationTemplate':
        """
        Get an existing ConfigurationTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConfigurationTemplateArgs.__new__(ConfigurationTemplateArgs)

        __props__.__dict__["application_name"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["environment_id"] = None
        __props__.__dict__["option_settings"] = None
        __props__.__dict__["platform_arn"] = None
        __props__.__dict__["solution_stack_name"] = None
        __props__.__dict__["source_configuration"] = None
        return ConfigurationTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "environment_id")

    @property
    @pulumi.getter(name="optionSettings")
    def option_settings(self) -> pulumi.Output[Optional[Sequence['outputs.ConfigurationTemplateConfigurationOptionSetting']]]:
        return pulumi.get(self, "option_settings")

    @property
    @pulumi.getter(name="platformArn")
    def platform_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "platform_arn")

    @property
    @pulumi.getter(name="solutionStackName")
    def solution_stack_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "solution_stack_name")

    @property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(self) -> pulumi.Output[Optional['outputs.ConfigurationTemplateSourceConfiguration']]:
        return pulumi.get(self, "source_configuration")

