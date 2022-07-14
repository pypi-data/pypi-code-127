# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ApplicationEntitlementAssociationArgs', 'ApplicationEntitlementAssociation']

@pulumi.input_type
class ApplicationEntitlementAssociationArgs:
    def __init__(__self__, *,
                 application_identifier: pulumi.Input[str],
                 entitlement_name: pulumi.Input[str],
                 stack_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a ApplicationEntitlementAssociation resource.
        """
        pulumi.set(__self__, "application_identifier", application_identifier)
        pulumi.set(__self__, "entitlement_name", entitlement_name)
        pulumi.set(__self__, "stack_name", stack_name)

    @property
    @pulumi.getter(name="applicationIdentifier")
    def application_identifier(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application_identifier")

    @application_identifier.setter
    def application_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_identifier", value)

    @property
    @pulumi.getter(name="entitlementName")
    def entitlement_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "entitlement_name")

    @entitlement_name.setter
    def entitlement_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "entitlement_name", value)

    @property
    @pulumi.getter(name="stackName")
    def stack_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "stack_name")

    @stack_name.setter
    def stack_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "stack_name", value)


class ApplicationEntitlementAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_identifier: Optional[pulumi.Input[str]] = None,
                 entitlement_name: Optional[pulumi.Input[str]] = None,
                 stack_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppStream::ApplicationEntitlementAssociation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationEntitlementAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppStream::ApplicationEntitlementAssociation

        :param str resource_name: The name of the resource.
        :param ApplicationEntitlementAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationEntitlementAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_identifier: Optional[pulumi.Input[str]] = None,
                 entitlement_name: Optional[pulumi.Input[str]] = None,
                 stack_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ApplicationEntitlementAssociationArgs.__new__(ApplicationEntitlementAssociationArgs)

            if application_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'application_identifier'")
            __props__.__dict__["application_identifier"] = application_identifier
            if entitlement_name is None and not opts.urn:
                raise TypeError("Missing required property 'entitlement_name'")
            __props__.__dict__["entitlement_name"] = entitlement_name
            if stack_name is None and not opts.urn:
                raise TypeError("Missing required property 'stack_name'")
            __props__.__dict__["stack_name"] = stack_name
        super(ApplicationEntitlementAssociation, __self__).__init__(
            'aws-native:appstream:ApplicationEntitlementAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApplicationEntitlementAssociation':
        """
        Get an existing ApplicationEntitlementAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationEntitlementAssociationArgs.__new__(ApplicationEntitlementAssociationArgs)

        __props__.__dict__["application_identifier"] = None
        __props__.__dict__["entitlement_name"] = None
        __props__.__dict__["stack_name"] = None
        return ApplicationEntitlementAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationIdentifier")
    def application_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_identifier")

    @property
    @pulumi.getter(name="entitlementName")
    def entitlement_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "entitlement_name")

    @property
    @pulumi.getter(name="stackName")
    def stack_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "stack_name")

