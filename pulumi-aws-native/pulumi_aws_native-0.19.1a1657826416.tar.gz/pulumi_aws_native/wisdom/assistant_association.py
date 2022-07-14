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

__all__ = ['AssistantAssociationArgs', 'AssistantAssociation']

@pulumi.input_type
class AssistantAssociationArgs:
    def __init__(__self__, *,
                 assistant_id: pulumi.Input[str],
                 association: pulumi.Input['AssistantAssociationAssociationDataArgs'],
                 association_type: pulumi.Input['AssistantAssociationAssociationType'],
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['AssistantAssociationTagArgs']]]] = None):
        """
        The set of arguments for constructing a AssistantAssociation resource.
        """
        pulumi.set(__self__, "assistant_id", assistant_id)
        pulumi.set(__self__, "association", association)
        pulumi.set(__self__, "association_type", association_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="assistantId")
    def assistant_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "assistant_id")

    @assistant_id.setter
    def assistant_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "assistant_id", value)

    @property
    @pulumi.getter
    def association(self) -> pulumi.Input['AssistantAssociationAssociationDataArgs']:
        return pulumi.get(self, "association")

    @association.setter
    def association(self, value: pulumi.Input['AssistantAssociationAssociationDataArgs']):
        pulumi.set(self, "association", value)

    @property
    @pulumi.getter(name="associationType")
    def association_type(self) -> pulumi.Input['AssistantAssociationAssociationType']:
        return pulumi.get(self, "association_type")

    @association_type.setter
    def association_type(self, value: pulumi.Input['AssistantAssociationAssociationType']):
        pulumi.set(self, "association_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssistantAssociationTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssistantAssociationTagArgs']]]]):
        pulumi.set(self, "tags", value)


class AssistantAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assistant_id: Optional[pulumi.Input[str]] = None,
                 association: Optional[pulumi.Input[pulumi.InputType['AssistantAssociationAssociationDataArgs']]] = None,
                 association_type: Optional[pulumi.Input['AssistantAssociationAssociationType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssistantAssociationTagArgs']]]]] = None,
                 __props__=None):
        """
        Definition of AWS::Wisdom::AssistantAssociation Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssistantAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::Wisdom::AssistantAssociation Resource Type

        :param str resource_name: The name of the resource.
        :param AssistantAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssistantAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assistant_id: Optional[pulumi.Input[str]] = None,
                 association: Optional[pulumi.Input[pulumi.InputType['AssistantAssociationAssociationDataArgs']]] = None,
                 association_type: Optional[pulumi.Input['AssistantAssociationAssociationType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssistantAssociationTagArgs']]]]] = None,
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
            __props__ = AssistantAssociationArgs.__new__(AssistantAssociationArgs)

            if assistant_id is None and not opts.urn:
                raise TypeError("Missing required property 'assistant_id'")
            __props__.__dict__["assistant_id"] = assistant_id
            if association is None and not opts.urn:
                raise TypeError("Missing required property 'association'")
            __props__.__dict__["association"] = association
            if association_type is None and not opts.urn:
                raise TypeError("Missing required property 'association_type'")
            __props__.__dict__["association_type"] = association_type
            __props__.__dict__["tags"] = tags
            __props__.__dict__["assistant_arn"] = None
            __props__.__dict__["assistant_association_arn"] = None
            __props__.__dict__["assistant_association_id"] = None
        super(AssistantAssociation, __self__).__init__(
            'aws-native:wisdom:AssistantAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AssistantAssociation':
        """
        Get an existing AssistantAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AssistantAssociationArgs.__new__(AssistantAssociationArgs)

        __props__.__dict__["assistant_arn"] = None
        __props__.__dict__["assistant_association_arn"] = None
        __props__.__dict__["assistant_association_id"] = None
        __props__.__dict__["assistant_id"] = None
        __props__.__dict__["association"] = None
        __props__.__dict__["association_type"] = None
        __props__.__dict__["tags"] = None
        return AssistantAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assistantArn")
    def assistant_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "assistant_arn")

    @property
    @pulumi.getter(name="assistantAssociationArn")
    def assistant_association_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "assistant_association_arn")

    @property
    @pulumi.getter(name="assistantAssociationId")
    def assistant_association_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "assistant_association_id")

    @property
    @pulumi.getter(name="assistantId")
    def assistant_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "assistant_id")

    @property
    @pulumi.getter
    def association(self) -> pulumi.Output['outputs.AssistantAssociationAssociationData']:
        return pulumi.get(self, "association")

    @property
    @pulumi.getter(name="associationType")
    def association_type(self) -> pulumi.Output['AssistantAssociationAssociationType']:
        return pulumi.get(self, "association_type")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.AssistantAssociationTag']]]:
        return pulumi.get(self, "tags")

