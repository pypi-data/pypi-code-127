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

__all__ = ['ConformancePackArgs', 'ConformancePack']

@pulumi.input_type
class ConformancePackArgs:
    def __init__(__self__, *,
                 conformance_pack_input_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['ConformancePackInputParameterArgs']]]] = None,
                 conformance_pack_name: Optional[pulumi.Input[str]] = None,
                 delivery_s3_bucket: Optional[pulumi.Input[str]] = None,
                 delivery_s3_key_prefix: Optional[pulumi.Input[str]] = None,
                 template_body: Optional[pulumi.Input[str]] = None,
                 template_s3_uri: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConformancePack resource.
        :param pulumi.Input[Sequence[pulumi.Input['ConformancePackInputParameterArgs']]] conformance_pack_input_parameters: A list of ConformancePackInputParameter objects.
        :param pulumi.Input[str] conformance_pack_name: Name of the conformance pack which will be assigned as the unique identifier.
        :param pulumi.Input[str] delivery_s3_bucket: AWS Config stores intermediate files while processing conformance pack template.
        :param pulumi.Input[str] delivery_s3_key_prefix: The prefix for delivery S3 bucket.
        :param pulumi.Input[str] template_body: A string containing full conformance pack template body. You can only specify one of the template body or template S3Uri fields.
        :param pulumi.Input[str] template_s3_uri: Location of file containing the template body which points to the conformance pack template that is located in an Amazon S3 bucket. You can only specify one of the template body or template S3Uri fields.
        """
        if conformance_pack_input_parameters is not None:
            pulumi.set(__self__, "conformance_pack_input_parameters", conformance_pack_input_parameters)
        if conformance_pack_name is not None:
            pulumi.set(__self__, "conformance_pack_name", conformance_pack_name)
        if delivery_s3_bucket is not None:
            pulumi.set(__self__, "delivery_s3_bucket", delivery_s3_bucket)
        if delivery_s3_key_prefix is not None:
            pulumi.set(__self__, "delivery_s3_key_prefix", delivery_s3_key_prefix)
        if template_body is not None:
            pulumi.set(__self__, "template_body", template_body)
        if template_s3_uri is not None:
            pulumi.set(__self__, "template_s3_uri", template_s3_uri)

    @property
    @pulumi.getter(name="conformancePackInputParameters")
    def conformance_pack_input_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConformancePackInputParameterArgs']]]]:
        """
        A list of ConformancePackInputParameter objects.
        """
        return pulumi.get(self, "conformance_pack_input_parameters")

    @conformance_pack_input_parameters.setter
    def conformance_pack_input_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConformancePackInputParameterArgs']]]]):
        pulumi.set(self, "conformance_pack_input_parameters", value)

    @property
    @pulumi.getter(name="conformancePackName")
    def conformance_pack_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the conformance pack which will be assigned as the unique identifier.
        """
        return pulumi.get(self, "conformance_pack_name")

    @conformance_pack_name.setter
    def conformance_pack_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "conformance_pack_name", value)

    @property
    @pulumi.getter(name="deliveryS3Bucket")
    def delivery_s3_bucket(self) -> Optional[pulumi.Input[str]]:
        """
        AWS Config stores intermediate files while processing conformance pack template.
        """
        return pulumi.get(self, "delivery_s3_bucket")

    @delivery_s3_bucket.setter
    def delivery_s3_bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delivery_s3_bucket", value)

    @property
    @pulumi.getter(name="deliveryS3KeyPrefix")
    def delivery_s3_key_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The prefix for delivery S3 bucket.
        """
        return pulumi.get(self, "delivery_s3_key_prefix")

    @delivery_s3_key_prefix.setter
    def delivery_s3_key_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delivery_s3_key_prefix", value)

    @property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> Optional[pulumi.Input[str]]:
        """
        A string containing full conformance pack template body. You can only specify one of the template body or template S3Uri fields.
        """
        return pulumi.get(self, "template_body")

    @template_body.setter
    def template_body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_body", value)

    @property
    @pulumi.getter(name="templateS3Uri")
    def template_s3_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Location of file containing the template body which points to the conformance pack template that is located in an Amazon S3 bucket. You can only specify one of the template body or template S3Uri fields.
        """
        return pulumi.get(self, "template_s3_uri")

    @template_s3_uri.setter
    def template_s3_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_s3_uri", value)


class ConformancePack(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 conformance_pack_input_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConformancePackInputParameterArgs']]]]] = None,
                 conformance_pack_name: Optional[pulumi.Input[str]] = None,
                 delivery_s3_bucket: Optional[pulumi.Input[str]] = None,
                 delivery_s3_key_prefix: Optional[pulumi.Input[str]] = None,
                 template_body: Optional[pulumi.Input[str]] = None,
                 template_s3_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed as a single entity in an account and a region or across an entire AWS Organization.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConformancePackInputParameterArgs']]]] conformance_pack_input_parameters: A list of ConformancePackInputParameter objects.
        :param pulumi.Input[str] conformance_pack_name: Name of the conformance pack which will be assigned as the unique identifier.
        :param pulumi.Input[str] delivery_s3_bucket: AWS Config stores intermediate files while processing conformance pack template.
        :param pulumi.Input[str] delivery_s3_key_prefix: The prefix for delivery S3 bucket.
        :param pulumi.Input[str] template_body: A string containing full conformance pack template body. You can only specify one of the template body or template S3Uri fields.
        :param pulumi.Input[str] template_s3_uri: Location of file containing the template body which points to the conformance pack template that is located in an Amazon S3 bucket. You can only specify one of the template body or template S3Uri fields.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ConformancePackArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed as a single entity in an account and a region or across an entire AWS Organization.

        :param str resource_name: The name of the resource.
        :param ConformancePackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConformancePackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 conformance_pack_input_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConformancePackInputParameterArgs']]]]] = None,
                 conformance_pack_name: Optional[pulumi.Input[str]] = None,
                 delivery_s3_bucket: Optional[pulumi.Input[str]] = None,
                 delivery_s3_key_prefix: Optional[pulumi.Input[str]] = None,
                 template_body: Optional[pulumi.Input[str]] = None,
                 template_s3_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConformancePackArgs.__new__(ConformancePackArgs)

            __props__.__dict__["conformance_pack_input_parameters"] = conformance_pack_input_parameters
            __props__.__dict__["conformance_pack_name"] = conformance_pack_name
            __props__.__dict__["delivery_s3_bucket"] = delivery_s3_bucket
            __props__.__dict__["delivery_s3_key_prefix"] = delivery_s3_key_prefix
            __props__.__dict__["template_body"] = template_body
            __props__.__dict__["template_s3_uri"] = template_s3_uri
        super(ConformancePack, __self__).__init__(
            'aws-native:configuration:ConformancePack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConformancePack':
        """
        Get an existing ConformancePack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConformancePackArgs.__new__(ConformancePackArgs)

        __props__.__dict__["conformance_pack_input_parameters"] = None
        __props__.__dict__["conformance_pack_name"] = None
        __props__.__dict__["delivery_s3_bucket"] = None
        __props__.__dict__["delivery_s3_key_prefix"] = None
        __props__.__dict__["template_body"] = None
        __props__.__dict__["template_s3_uri"] = None
        return ConformancePack(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="conformancePackInputParameters")
    def conformance_pack_input_parameters(self) -> pulumi.Output[Optional[Sequence['outputs.ConformancePackInputParameter']]]:
        """
        A list of ConformancePackInputParameter objects.
        """
        return pulumi.get(self, "conformance_pack_input_parameters")

    @property
    @pulumi.getter(name="conformancePackName")
    def conformance_pack_name(self) -> pulumi.Output[str]:
        """
        Name of the conformance pack which will be assigned as the unique identifier.
        """
        return pulumi.get(self, "conformance_pack_name")

    @property
    @pulumi.getter(name="deliveryS3Bucket")
    def delivery_s3_bucket(self) -> pulumi.Output[Optional[str]]:
        """
        AWS Config stores intermediate files while processing conformance pack template.
        """
        return pulumi.get(self, "delivery_s3_bucket")

    @property
    @pulumi.getter(name="deliveryS3KeyPrefix")
    def delivery_s3_key_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The prefix for delivery S3 bucket.
        """
        return pulumi.get(self, "delivery_s3_key_prefix")

    @property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> pulumi.Output[Optional[str]]:
        """
        A string containing full conformance pack template body. You can only specify one of the template body or template S3Uri fields.
        """
        return pulumi.get(self, "template_body")

    @property
    @pulumi.getter(name="templateS3Uri")
    def template_s3_uri(self) -> pulumi.Output[Optional[str]]:
        """
        Location of file containing the template body which points to the conformance pack template that is located in an Amazon S3 bucket. You can only specify one of the template body or template S3Uri fields.
        """
        return pulumi.get(self, "template_s3_uri")

