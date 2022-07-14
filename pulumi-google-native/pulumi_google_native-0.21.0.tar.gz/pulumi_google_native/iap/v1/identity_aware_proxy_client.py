# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['IdentityAwareProxyClientArgs', 'IdentityAwareProxyClient']

@pulumi.input_type
class IdentityAwareProxyClientArgs:
    def __init__(__self__, *,
                 brand_id: pulumi.Input[str],
                 display_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IdentityAwareProxyClient resource.
        :param pulumi.Input[str] display_name: Human-friendly name given to the OAuth client.
        """
        pulumi.set(__self__, "brand_id", brand_id)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="brandId")
    def brand_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "brand_id")

    @brand_id.setter
    def brand_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "brand_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Human-friendly name given to the OAuth client.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class IdentityAwareProxyClient(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 brand_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an Identity Aware Proxy (IAP) OAuth client. The client is owned by IAP. Requires that the brand for the project exists and that it is set for internal-only use.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Human-friendly name given to the OAuth client.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IdentityAwareProxyClientArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an Identity Aware Proxy (IAP) OAuth client. The client is owned by IAP. Requires that the brand for the project exists and that it is set for internal-only use.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param IdentityAwareProxyClientArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IdentityAwareProxyClientArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 brand_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
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
            __props__ = IdentityAwareProxyClientArgs.__new__(IdentityAwareProxyClientArgs)

            if brand_id is None and not opts.urn:
                raise TypeError("Missing required property 'brand_id'")
            __props__.__dict__["brand_id"] = brand_id
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["project"] = project
            __props__.__dict__["name"] = None
            __props__.__dict__["secret"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["brand_id", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(IdentityAwareProxyClient, __self__).__init__(
            'google-native:iap/v1:IdentityAwareProxyClient',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IdentityAwareProxyClient':
        """
        Get an existing IdentityAwareProxyClient resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IdentityAwareProxyClientArgs.__new__(IdentityAwareProxyClientArgs)

        __props__.__dict__["brand_id"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["secret"] = None
        return IdentityAwareProxyClient(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="brandId")
    def brand_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "brand_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Human-friendly name given to the OAuth client.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unique identifier of the OAuth client.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Output[str]:
        """
        Client secret of the OAuth client.
        """
        return pulumi.get(self, "secret")

