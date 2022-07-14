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

__all__ = ['ServiceArgs', 'Service']

@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *,
                 application_identifier: pulumi.Input[str],
                 environment_identifier: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 endpoint_type: Optional[pulumi.Input['ServiceEndpointType']] = None,
                 lambda_endpoint: Optional[pulumi.Input['ServiceLambdaEndpointInputArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceTagArgs']]]] = None,
                 url_endpoint: Optional[pulumi.Input['ServiceUrlEndpointInputArgs']] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Service resource.
        :param pulumi.Input[Sequence[pulumi.Input['ServiceTagArgs']]] tags: Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
        """
        pulumi.set(__self__, "application_identifier", application_identifier)
        pulumi.set(__self__, "environment_identifier", environment_identifier)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if endpoint_type is not None:
            pulumi.set(__self__, "endpoint_type", endpoint_type)
        if lambda_endpoint is not None:
            pulumi.set(__self__, "lambda_endpoint", lambda_endpoint)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if url_endpoint is not None:
            pulumi.set(__self__, "url_endpoint", url_endpoint)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="applicationIdentifier")
    def application_identifier(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application_identifier")

    @application_identifier.setter
    def application_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_identifier", value)

    @property
    @pulumi.getter(name="environmentIdentifier")
    def environment_identifier(self) -> pulumi.Input[str]:
        return pulumi.get(self, "environment_identifier")

    @environment_identifier.setter
    def environment_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_identifier", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input['ServiceEndpointType']]:
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input['ServiceEndpointType']]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="lambdaEndpoint")
    def lambda_endpoint(self) -> Optional[pulumi.Input['ServiceLambdaEndpointInputArgs']]:
        return pulumi.get(self, "lambda_endpoint")

    @lambda_endpoint.setter
    def lambda_endpoint(self, value: Optional[pulumi.Input['ServiceLambdaEndpointInputArgs']]):
        pulumi.set(self, "lambda_endpoint", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceTagArgs']]]]:
        """
        Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="urlEndpoint")
    def url_endpoint(self) -> Optional[pulumi.Input['ServiceUrlEndpointInputArgs']]:
        return pulumi.get(self, "url_endpoint")

    @url_endpoint.setter
    def url_endpoint(self, value: Optional[pulumi.Input['ServiceUrlEndpointInputArgs']]):
        pulumi.set(self, "url_endpoint", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_identifier: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 endpoint_type: Optional[pulumi.Input['ServiceEndpointType']] = None,
                 environment_identifier: Optional[pulumi.Input[str]] = None,
                 lambda_endpoint: Optional[pulumi.Input[pulumi.InputType['ServiceLambdaEndpointInputArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceTagArgs']]]]] = None,
                 url_endpoint: Optional[pulumi.Input[pulumi.InputType['ServiceUrlEndpointInputArgs']]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of AWS::RefactorSpaces::Service Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceTagArgs']]]] tags: Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::RefactorSpaces::Service Resource Type

        :param str resource_name: The name of the resource.
        :param ServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_identifier: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 endpoint_type: Optional[pulumi.Input['ServiceEndpointType']] = None,
                 environment_identifier: Optional[pulumi.Input[str]] = None,
                 lambda_endpoint: Optional[pulumi.Input[pulumi.InputType['ServiceLambdaEndpointInputArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceTagArgs']]]]] = None,
                 url_endpoint: Optional[pulumi.Input[pulumi.InputType['ServiceUrlEndpointInputArgs']]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = ServiceArgs.__new__(ServiceArgs)

            if application_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'application_identifier'")
            __props__.__dict__["application_identifier"] = application_identifier
            __props__.__dict__["description"] = description
            __props__.__dict__["endpoint_type"] = endpoint_type
            if environment_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'environment_identifier'")
            __props__.__dict__["environment_identifier"] = environment_identifier
            __props__.__dict__["lambda_endpoint"] = lambda_endpoint
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["url_endpoint"] = url_endpoint
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["arn"] = None
            __props__.__dict__["service_identifier"] = None
        super(Service, __self__).__init__(
            'aws-native:refactorspaces:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceArgs.__new__(ServiceArgs)

        __props__.__dict__["application_identifier"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["endpoint_type"] = None
        __props__.__dict__["environment_identifier"] = None
        __props__.__dict__["lambda_endpoint"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["service_identifier"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["url_endpoint"] = None
        __props__.__dict__["vpc_id"] = None
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationIdentifier")
    def application_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_identifier")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Output[Optional['ServiceEndpointType']]:
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter(name="environmentIdentifier")
    def environment_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "environment_identifier")

    @property
    @pulumi.getter(name="lambdaEndpoint")
    def lambda_endpoint(self) -> pulumi.Output[Optional['outputs.ServiceLambdaEndpointInput']]:
        return pulumi.get(self, "lambda_endpoint")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serviceIdentifier")
    def service_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "service_identifier")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceTag']]]:
        """
        Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="urlEndpoint")
    def url_endpoint(self) -> pulumi.Output[Optional['outputs.ServiceUrlEndpointInput']]:
        return pulumi.get(self, "url_endpoint")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "vpc_id")

