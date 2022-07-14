# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['CustomDomainArgs', 'CustomDomain']

@pulumi.input_type
class CustomDomainArgs:
    def __init__(__self__, *,
                 domain: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        The set of arguments for constructing a CustomDomain resource.
        :param pulumi.Input[str] domain: String. Name of the custom domain.
        :param pulumi.Input[str] type: String. Provisioning type for the custom domain. Options include `auth0_managed_certs` and `self_managed_certs`.
        """
        pulumi.set(__self__, "domain", domain)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        String. Name of the custom domain.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        String. Provisioning type for the custom domain. Options include `auth0_managed_certs` and `self_managed_certs`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _CustomDomainState:
    def __init__(__self__, *,
                 domain: Optional[pulumi.Input[str]] = None,
                 origin_domain_name: Optional[pulumi.Input[str]] = None,
                 primary: Optional[pulumi.Input[bool]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 verifications: Optional[pulumi.Input[Sequence[pulumi.Input['CustomDomainVerificationArgs']]]] = None):
        """
        Input properties used for looking up and filtering CustomDomain resources.
        :param pulumi.Input[str] domain: String. Name of the custom domain.
        :param pulumi.Input[str] origin_domain_name: String. Once the configuration status is `ready`, the DNS name of the Auth0 origin server that handles traffic for the custom domain.
        :param pulumi.Input[bool] primary: Boolean. Indicates whether this is a primary domain.
        :param pulumi.Input[str] status: String. Configuration status for the custom domain. Options include `disabled`, `pending`, `pending_verification`, and `ready`.
        :param pulumi.Input[str] type: String. Provisioning type for the custom domain. Options include `auth0_managed_certs` and `self_managed_certs`.
        :param pulumi.Input[Sequence[pulumi.Input['CustomDomainVerificationArgs']]] verifications: List(Resource). Configuration settings for verification. For details, see Verification.
        """
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if origin_domain_name is not None:
            pulumi.set(__self__, "origin_domain_name", origin_domain_name)
        if primary is not None:
            pulumi.set(__self__, "primary", primary)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if verifications is not None:
            pulumi.set(__self__, "verifications", verifications)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        String. Name of the custom domain.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="originDomainName")
    def origin_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        String. Once the configuration status is `ready`, the DNS name of the Auth0 origin server that handles traffic for the custom domain.
        """
        return pulumi.get(self, "origin_domain_name")

    @origin_domain_name.setter
    def origin_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "origin_domain_name", value)

    @property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean. Indicates whether this is a primary domain.
        """
        return pulumi.get(self, "primary")

    @primary.setter
    def primary(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "primary", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        String. Configuration status for the custom domain. Options include `disabled`, `pending`, `pending_verification`, and `ready`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        String. Provisioning type for the custom domain. Options include `auth0_managed_certs` and `self_managed_certs`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def verifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomDomainVerificationArgs']]]]:
        """
        List(Resource). Configuration settings for verification. For details, see Verification.
        """
        return pulumi.get(self, "verifications")

    @verifications.setter
    def verifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomDomainVerificationArgs']]]]):
        pulumi.set(self, "verifications", value)


class CustomDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        With Auth0, you can use a custom domain to maintain a consistent user experience. This resource allows you to create and
        manage a custom domain within your Auth0 tenant.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_auth0 as auth0

        my_custom_domain = auth0.CustomDomain("myCustomDomain",
            domain="auth.example.com",
            type="auth0_managed_certs")
        ```

        ## Import

        Custom Domains can be imported using the id, e.g.

        ```sh
         $ pulumi import auth0:index/customDomain:CustomDomain my_custom_domain cd_XXXXXXXXXXXXXXXX
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain: String. Name of the custom domain.
        :param pulumi.Input[str] type: String. Provisioning type for the custom domain. Options include `auth0_managed_certs` and `self_managed_certs`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomDomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        With Auth0, you can use a custom domain to maintain a consistent user experience. This resource allows you to create and
        manage a custom domain within your Auth0 tenant.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_auth0 as auth0

        my_custom_domain = auth0.CustomDomain("myCustomDomain",
            domain="auth.example.com",
            type="auth0_managed_certs")
        ```

        ## Import

        Custom Domains can be imported using the id, e.g.

        ```sh
         $ pulumi import auth0:index/customDomain:CustomDomain my_custom_domain cd_XXXXXXXXXXXXXXXX
        ```

        :param str resource_name: The name of the resource.
        :param CustomDomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomDomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomDomainArgs.__new__(CustomDomainArgs)

            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["origin_domain_name"] = None
            __props__.__dict__["primary"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["verifications"] = None
        super(CustomDomain, __self__).__init__(
            'auth0:index/customDomain:CustomDomain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            domain: Optional[pulumi.Input[str]] = None,
            origin_domain_name: Optional[pulumi.Input[str]] = None,
            primary: Optional[pulumi.Input[bool]] = None,
            status: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            verifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomDomainVerificationArgs']]]]] = None) -> 'CustomDomain':
        """
        Get an existing CustomDomain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain: String. Name of the custom domain.
        :param pulumi.Input[str] origin_domain_name: String. Once the configuration status is `ready`, the DNS name of the Auth0 origin server that handles traffic for the custom domain.
        :param pulumi.Input[bool] primary: Boolean. Indicates whether this is a primary domain.
        :param pulumi.Input[str] status: String. Configuration status for the custom domain. Options include `disabled`, `pending`, `pending_verification`, and `ready`.
        :param pulumi.Input[str] type: String. Provisioning type for the custom domain. Options include `auth0_managed_certs` and `self_managed_certs`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomDomainVerificationArgs']]]] verifications: List(Resource). Configuration settings for verification. For details, see Verification.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CustomDomainState.__new__(_CustomDomainState)

        __props__.__dict__["domain"] = domain
        __props__.__dict__["origin_domain_name"] = origin_domain_name
        __props__.__dict__["primary"] = primary
        __props__.__dict__["status"] = status
        __props__.__dict__["type"] = type
        __props__.__dict__["verifications"] = verifications
        return CustomDomain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        String. Name of the custom domain.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="originDomainName")
    def origin_domain_name(self) -> pulumi.Output[str]:
        """
        String. Once the configuration status is `ready`, the DNS name of the Auth0 origin server that handles traffic for the custom domain.
        """
        return pulumi.get(self, "origin_domain_name")

    @property
    @pulumi.getter
    def primary(self) -> pulumi.Output[bool]:
        """
        Boolean. Indicates whether this is a primary domain.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        String. Configuration status for the custom domain. Options include `disabled`, `pending`, `pending_verification`, and `ready`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        String. Provisioning type for the custom domain. Options include `auth0_managed_certs` and `self_managed_certs`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def verifications(self) -> pulumi.Output[Sequence['outputs.CustomDomainVerification']]:
        """
        List(Resource). Configuration settings for verification. For details, see Verification.
        """
        return pulumi.get(self, "verifications")

