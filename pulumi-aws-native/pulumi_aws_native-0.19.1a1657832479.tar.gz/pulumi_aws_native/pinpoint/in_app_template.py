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
from ._enums import *
from ._inputs import *

__all__ = ['InAppTemplateArgs', 'InAppTemplate']

@pulumi.input_type
class InAppTemplateArgs:
    def __init__(__self__, *,
                 template_name: pulumi.Input[str],
                 content: Optional[pulumi.Input[Sequence[pulumi.Input['InAppTemplateInAppMessageContentArgs']]]] = None,
                 custom_config: Optional[Any] = None,
                 layout: Optional[pulumi.Input['InAppTemplateLayout']] = None,
                 tags: Optional[Any] = None,
                 template_description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InAppTemplate resource.
        """
        pulumi.set(__self__, "template_name", template_name)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if custom_config is not None:
            pulumi.set(__self__, "custom_config", custom_config)
        if layout is not None:
            pulumi.set(__self__, "layout", layout)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if template_description is not None:
            pulumi.set(__self__, "template_description", template_description)

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "template_name")

    @template_name.setter
    def template_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "template_name", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InAppTemplateInAppMessageContentArgs']]]]:
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InAppTemplateInAppMessageContentArgs']]]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="customConfig")
    def custom_config(self) -> Optional[Any]:
        return pulumi.get(self, "custom_config")

    @custom_config.setter
    def custom_config(self, value: Optional[Any]):
        pulumi.set(self, "custom_config", value)

    @property
    @pulumi.getter
    def layout(self) -> Optional[pulumi.Input['InAppTemplateLayout']]:
        return pulumi.get(self, "layout")

    @layout.setter
    def layout(self, value: Optional[pulumi.Input['InAppTemplateLayout']]):
        pulumi.set(self, "layout", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="templateDescription")
    def template_description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "template_description")

    @template_description.setter
    def template_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_description", value)


class InAppTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InAppTemplateInAppMessageContentArgs']]]]] = None,
                 custom_config: Optional[Any] = None,
                 layout: Optional[pulumi.Input['InAppTemplateLayout']] = None,
                 tags: Optional[Any] = None,
                 template_description: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Pinpoint::InAppTemplate

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InAppTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Pinpoint::InAppTemplate

        :param str resource_name: The name of the resource.
        :param InAppTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InAppTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InAppTemplateInAppMessageContentArgs']]]]] = None,
                 custom_config: Optional[Any] = None,
                 layout: Optional[pulumi.Input['InAppTemplateLayout']] = None,
                 tags: Optional[Any] = None,
                 template_description: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
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
            __props__ = InAppTemplateArgs.__new__(InAppTemplateArgs)

            __props__.__dict__["content"] = content
            __props__.__dict__["custom_config"] = custom_config
            __props__.__dict__["layout"] = layout
            __props__.__dict__["tags"] = tags
            __props__.__dict__["template_description"] = template_description
            if template_name is None and not opts.urn:
                raise TypeError("Missing required property 'template_name'")
            __props__.__dict__["template_name"] = template_name
            __props__.__dict__["arn"] = None
        super(InAppTemplate, __self__).__init__(
            'aws-native:pinpoint:InAppTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InAppTemplate':
        """
        Get an existing InAppTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InAppTemplateArgs.__new__(InAppTemplateArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["content"] = None
        __props__.__dict__["custom_config"] = None
        __props__.__dict__["layout"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["template_description"] = None
        __props__.__dict__["template_name"] = None
        return InAppTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[Optional[Sequence['outputs.InAppTemplateInAppMessageContent']]]:
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="customConfig")
    def custom_config(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "custom_config")

    @property
    @pulumi.getter
    def layout(self) -> pulumi.Output[Optional['InAppTemplateLayout']]:
        return pulumi.get(self, "layout")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateDescription")
    def template_description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "template_description")

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "template_name")

