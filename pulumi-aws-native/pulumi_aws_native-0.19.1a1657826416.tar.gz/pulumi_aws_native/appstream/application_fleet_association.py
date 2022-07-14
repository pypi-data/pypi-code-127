# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ApplicationFleetAssociationArgs', 'ApplicationFleetAssociation']

@pulumi.input_type
class ApplicationFleetAssociationArgs:
    def __init__(__self__, *,
                 application_arn: pulumi.Input[str],
                 fleet_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a ApplicationFleetAssociation resource.
        """
        pulumi.set(__self__, "application_arn", application_arn)
        pulumi.set(__self__, "fleet_name", fleet_name)

    @property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application_arn")

    @application_arn.setter
    def application_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_arn", value)

    @property
    @pulumi.getter(name="fleetName")
    def fleet_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "fleet_name")

    @fleet_name.setter
    def fleet_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "fleet_name", value)


class ApplicationFleetAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_arn: Optional[pulumi.Input[str]] = None,
                 fleet_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppStream::ApplicationFleetAssociation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationFleetAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppStream::ApplicationFleetAssociation

        :param str resource_name: The name of the resource.
        :param ApplicationFleetAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationFleetAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_arn: Optional[pulumi.Input[str]] = None,
                 fleet_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ApplicationFleetAssociationArgs.__new__(ApplicationFleetAssociationArgs)

            if application_arn is None and not opts.urn:
                raise TypeError("Missing required property 'application_arn'")
            __props__.__dict__["application_arn"] = application_arn
            if fleet_name is None and not opts.urn:
                raise TypeError("Missing required property 'fleet_name'")
            __props__.__dict__["fleet_name"] = fleet_name
        super(ApplicationFleetAssociation, __self__).__init__(
            'aws-native:appstream:ApplicationFleetAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApplicationFleetAssociation':
        """
        Get an existing ApplicationFleetAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationFleetAssociationArgs.__new__(ApplicationFleetAssociationArgs)

        __props__.__dict__["application_arn"] = None
        __props__.__dict__["fleet_name"] = None
        return ApplicationFleetAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_arn")

    @property
    @pulumi.getter(name="fleetName")
    def fleet_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "fleet_name")

