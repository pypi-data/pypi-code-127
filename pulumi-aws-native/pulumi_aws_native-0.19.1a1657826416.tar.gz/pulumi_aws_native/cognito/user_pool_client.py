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

__all__ = ['UserPoolClientArgs', 'UserPoolClient']

@pulumi.input_type
class UserPoolClientArgs:
    def __init__(__self__, *,
                 user_pool_id: pulumi.Input[str],
                 access_token_validity: Optional[pulumi.Input[int]] = None,
                 allowed_o_auth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 allowed_o_auth_flows_user_pool_client: Optional[pulumi.Input[bool]] = None,
                 allowed_o_auth_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 analytics_configuration: Optional[pulumi.Input['UserPoolClientAnalyticsConfigurationArgs']] = None,
                 callback_urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 client_name: Optional[pulumi.Input[str]] = None,
                 default_redirect_uri: Optional[pulumi.Input[str]] = None,
                 enable_propagate_additional_user_context_data: Optional[pulumi.Input[bool]] = None,
                 enable_token_revocation: Optional[pulumi.Input[bool]] = None,
                 explicit_auth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 generate_secret: Optional[pulumi.Input[bool]] = None,
                 id_token_validity: Optional[pulumi.Input[int]] = None,
                 logout_urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 prevent_user_existence_errors: Optional[pulumi.Input[str]] = None,
                 read_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 refresh_token_validity: Optional[pulumi.Input[int]] = None,
                 supported_identity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 token_validity_units: Optional[pulumi.Input['UserPoolClientTokenValidityUnitsArgs']] = None,
                 write_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a UserPoolClient resource.
        """
        pulumi.set(__self__, "user_pool_id", user_pool_id)
        if access_token_validity is not None:
            pulumi.set(__self__, "access_token_validity", access_token_validity)
        if allowed_o_auth_flows is not None:
            pulumi.set(__self__, "allowed_o_auth_flows", allowed_o_auth_flows)
        if allowed_o_auth_flows_user_pool_client is not None:
            pulumi.set(__self__, "allowed_o_auth_flows_user_pool_client", allowed_o_auth_flows_user_pool_client)
        if allowed_o_auth_scopes is not None:
            pulumi.set(__self__, "allowed_o_auth_scopes", allowed_o_auth_scopes)
        if analytics_configuration is not None:
            pulumi.set(__self__, "analytics_configuration", analytics_configuration)
        if callback_urls is not None:
            pulumi.set(__self__, "callback_urls", callback_urls)
        if client_name is not None:
            pulumi.set(__self__, "client_name", client_name)
        if default_redirect_uri is not None:
            pulumi.set(__self__, "default_redirect_uri", default_redirect_uri)
        if enable_propagate_additional_user_context_data is not None:
            pulumi.set(__self__, "enable_propagate_additional_user_context_data", enable_propagate_additional_user_context_data)
        if enable_token_revocation is not None:
            pulumi.set(__self__, "enable_token_revocation", enable_token_revocation)
        if explicit_auth_flows is not None:
            pulumi.set(__self__, "explicit_auth_flows", explicit_auth_flows)
        if generate_secret is not None:
            pulumi.set(__self__, "generate_secret", generate_secret)
        if id_token_validity is not None:
            pulumi.set(__self__, "id_token_validity", id_token_validity)
        if logout_urls is not None:
            pulumi.set(__self__, "logout_urls", logout_urls)
        if prevent_user_existence_errors is not None:
            pulumi.set(__self__, "prevent_user_existence_errors", prevent_user_existence_errors)
        if read_attributes is not None:
            pulumi.set(__self__, "read_attributes", read_attributes)
        if refresh_token_validity is not None:
            pulumi.set(__self__, "refresh_token_validity", refresh_token_validity)
        if supported_identity_providers is not None:
            pulumi.set(__self__, "supported_identity_providers", supported_identity_providers)
        if token_validity_units is not None:
            pulumi.set(__self__, "token_validity_units", token_validity_units)
        if write_attributes is not None:
            pulumi.set(__self__, "write_attributes", write_attributes)

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "user_pool_id")

    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_pool_id", value)

    @property
    @pulumi.getter(name="accessTokenValidity")
    def access_token_validity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "access_token_validity")

    @access_token_validity.setter
    def access_token_validity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "access_token_validity", value)

    @property
    @pulumi.getter(name="allowedOAuthFlows")
    def allowed_o_auth_flows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "allowed_o_auth_flows")

    @allowed_o_auth_flows.setter
    def allowed_o_auth_flows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_o_auth_flows", value)

    @property
    @pulumi.getter(name="allowedOAuthFlowsUserPoolClient")
    def allowed_o_auth_flows_user_pool_client(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allowed_o_auth_flows_user_pool_client")

    @allowed_o_auth_flows_user_pool_client.setter
    def allowed_o_auth_flows_user_pool_client(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allowed_o_auth_flows_user_pool_client", value)

    @property
    @pulumi.getter(name="allowedOAuthScopes")
    def allowed_o_auth_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "allowed_o_auth_scopes")

    @allowed_o_auth_scopes.setter
    def allowed_o_auth_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_o_auth_scopes", value)

    @property
    @pulumi.getter(name="analyticsConfiguration")
    def analytics_configuration(self) -> Optional[pulumi.Input['UserPoolClientAnalyticsConfigurationArgs']]:
        return pulumi.get(self, "analytics_configuration")

    @analytics_configuration.setter
    def analytics_configuration(self, value: Optional[pulumi.Input['UserPoolClientAnalyticsConfigurationArgs']]):
        pulumi.set(self, "analytics_configuration", value)

    @property
    @pulumi.getter(name="callbackURLs")
    def callback_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "callback_urls")

    @callback_urls.setter
    def callback_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "callback_urls", value)

    @property
    @pulumi.getter(name="clientName")
    def client_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "client_name")

    @client_name.setter
    def client_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_name", value)

    @property
    @pulumi.getter(name="defaultRedirectURI")
    def default_redirect_uri(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_redirect_uri")

    @default_redirect_uri.setter
    def default_redirect_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_redirect_uri", value)

    @property
    @pulumi.getter(name="enablePropagateAdditionalUserContextData")
    def enable_propagate_additional_user_context_data(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_propagate_additional_user_context_data")

    @enable_propagate_additional_user_context_data.setter
    def enable_propagate_additional_user_context_data(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_propagate_additional_user_context_data", value)

    @property
    @pulumi.getter(name="enableTokenRevocation")
    def enable_token_revocation(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_token_revocation")

    @enable_token_revocation.setter
    def enable_token_revocation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_token_revocation", value)

    @property
    @pulumi.getter(name="explicitAuthFlows")
    def explicit_auth_flows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "explicit_auth_flows")

    @explicit_auth_flows.setter
    def explicit_auth_flows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "explicit_auth_flows", value)

    @property
    @pulumi.getter(name="generateSecret")
    def generate_secret(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "generate_secret")

    @generate_secret.setter
    def generate_secret(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "generate_secret", value)

    @property
    @pulumi.getter(name="idTokenValidity")
    def id_token_validity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "id_token_validity")

    @id_token_validity.setter
    def id_token_validity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "id_token_validity", value)

    @property
    @pulumi.getter(name="logoutURLs")
    def logout_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "logout_urls")

    @logout_urls.setter
    def logout_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "logout_urls", value)

    @property
    @pulumi.getter(name="preventUserExistenceErrors")
    def prevent_user_existence_errors(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "prevent_user_existence_errors")

    @prevent_user_existence_errors.setter
    def prevent_user_existence_errors(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prevent_user_existence_errors", value)

    @property
    @pulumi.getter(name="readAttributes")
    def read_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "read_attributes")

    @read_attributes.setter
    def read_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "read_attributes", value)

    @property
    @pulumi.getter(name="refreshTokenValidity")
    def refresh_token_validity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "refresh_token_validity")

    @refresh_token_validity.setter
    def refresh_token_validity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "refresh_token_validity", value)

    @property
    @pulumi.getter(name="supportedIdentityProviders")
    def supported_identity_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "supported_identity_providers")

    @supported_identity_providers.setter
    def supported_identity_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "supported_identity_providers", value)

    @property
    @pulumi.getter(name="tokenValidityUnits")
    def token_validity_units(self) -> Optional[pulumi.Input['UserPoolClientTokenValidityUnitsArgs']]:
        return pulumi.get(self, "token_validity_units")

    @token_validity_units.setter
    def token_validity_units(self, value: Optional[pulumi.Input['UserPoolClientTokenValidityUnitsArgs']]):
        pulumi.set(self, "token_validity_units", value)

    @property
    @pulumi.getter(name="writeAttributes")
    def write_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "write_attributes")

    @write_attributes.setter
    def write_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "write_attributes", value)


warnings.warn("""UserPoolClient is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class UserPoolClient(pulumi.CustomResource):
    warnings.warn("""UserPoolClient is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_token_validity: Optional[pulumi.Input[int]] = None,
                 allowed_o_auth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 allowed_o_auth_flows_user_pool_client: Optional[pulumi.Input[bool]] = None,
                 allowed_o_auth_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 analytics_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolClientAnalyticsConfigurationArgs']]] = None,
                 callback_urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 client_name: Optional[pulumi.Input[str]] = None,
                 default_redirect_uri: Optional[pulumi.Input[str]] = None,
                 enable_propagate_additional_user_context_data: Optional[pulumi.Input[bool]] = None,
                 enable_token_revocation: Optional[pulumi.Input[bool]] = None,
                 explicit_auth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 generate_secret: Optional[pulumi.Input[bool]] = None,
                 id_token_validity: Optional[pulumi.Input[int]] = None,
                 logout_urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 prevent_user_existence_errors: Optional[pulumi.Input[str]] = None,
                 read_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 refresh_token_validity: Optional[pulumi.Input[int]] = None,
                 supported_identity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 token_validity_units: Optional[pulumi.Input[pulumi.InputType['UserPoolClientTokenValidityUnitsArgs']]] = None,
                 user_pool_id: Optional[pulumi.Input[str]] = None,
                 write_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Cognito::UserPoolClient

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserPoolClientArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Cognito::UserPoolClient

        :param str resource_name: The name of the resource.
        :param UserPoolClientArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserPoolClientArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_token_validity: Optional[pulumi.Input[int]] = None,
                 allowed_o_auth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 allowed_o_auth_flows_user_pool_client: Optional[pulumi.Input[bool]] = None,
                 allowed_o_auth_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 analytics_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolClientAnalyticsConfigurationArgs']]] = None,
                 callback_urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 client_name: Optional[pulumi.Input[str]] = None,
                 default_redirect_uri: Optional[pulumi.Input[str]] = None,
                 enable_propagate_additional_user_context_data: Optional[pulumi.Input[bool]] = None,
                 enable_token_revocation: Optional[pulumi.Input[bool]] = None,
                 explicit_auth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 generate_secret: Optional[pulumi.Input[bool]] = None,
                 id_token_validity: Optional[pulumi.Input[int]] = None,
                 logout_urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 prevent_user_existence_errors: Optional[pulumi.Input[str]] = None,
                 read_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 refresh_token_validity: Optional[pulumi.Input[int]] = None,
                 supported_identity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 token_validity_units: Optional[pulumi.Input[pulumi.InputType['UserPoolClientTokenValidityUnitsArgs']]] = None,
                 user_pool_id: Optional[pulumi.Input[str]] = None,
                 write_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        pulumi.log.warn("""UserPoolClient is deprecated: UserPoolClient is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = UserPoolClientArgs.__new__(UserPoolClientArgs)

            __props__.__dict__["access_token_validity"] = access_token_validity
            __props__.__dict__["allowed_o_auth_flows"] = allowed_o_auth_flows
            __props__.__dict__["allowed_o_auth_flows_user_pool_client"] = allowed_o_auth_flows_user_pool_client
            __props__.__dict__["allowed_o_auth_scopes"] = allowed_o_auth_scopes
            __props__.__dict__["analytics_configuration"] = analytics_configuration
            __props__.__dict__["callback_urls"] = callback_urls
            __props__.__dict__["client_name"] = client_name
            __props__.__dict__["default_redirect_uri"] = default_redirect_uri
            __props__.__dict__["enable_propagate_additional_user_context_data"] = enable_propagate_additional_user_context_data
            __props__.__dict__["enable_token_revocation"] = enable_token_revocation
            __props__.__dict__["explicit_auth_flows"] = explicit_auth_flows
            __props__.__dict__["generate_secret"] = generate_secret
            __props__.__dict__["id_token_validity"] = id_token_validity
            __props__.__dict__["logout_urls"] = logout_urls
            __props__.__dict__["prevent_user_existence_errors"] = prevent_user_existence_errors
            __props__.__dict__["read_attributes"] = read_attributes
            __props__.__dict__["refresh_token_validity"] = refresh_token_validity
            __props__.__dict__["supported_identity_providers"] = supported_identity_providers
            __props__.__dict__["token_validity_units"] = token_validity_units
            if user_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_pool_id'")
            __props__.__dict__["user_pool_id"] = user_pool_id
            __props__.__dict__["write_attributes"] = write_attributes
            __props__.__dict__["client_secret"] = None
            __props__.__dict__["name"] = None
        super(UserPoolClient, __self__).__init__(
            'aws-native:cognito:UserPoolClient',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UserPoolClient':
        """
        Get an existing UserPoolClient resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserPoolClientArgs.__new__(UserPoolClientArgs)

        __props__.__dict__["access_token_validity"] = None
        __props__.__dict__["allowed_o_auth_flows"] = None
        __props__.__dict__["allowed_o_auth_flows_user_pool_client"] = None
        __props__.__dict__["allowed_o_auth_scopes"] = None
        __props__.__dict__["analytics_configuration"] = None
        __props__.__dict__["callback_urls"] = None
        __props__.__dict__["client_name"] = None
        __props__.__dict__["client_secret"] = None
        __props__.__dict__["default_redirect_uri"] = None
        __props__.__dict__["enable_propagate_additional_user_context_data"] = None
        __props__.__dict__["enable_token_revocation"] = None
        __props__.__dict__["explicit_auth_flows"] = None
        __props__.__dict__["generate_secret"] = None
        __props__.__dict__["id_token_validity"] = None
        __props__.__dict__["logout_urls"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["prevent_user_existence_errors"] = None
        __props__.__dict__["read_attributes"] = None
        __props__.__dict__["refresh_token_validity"] = None
        __props__.__dict__["supported_identity_providers"] = None
        __props__.__dict__["token_validity_units"] = None
        __props__.__dict__["user_pool_id"] = None
        __props__.__dict__["write_attributes"] = None
        return UserPoolClient(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessTokenValidity")
    def access_token_validity(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "access_token_validity")

    @property
    @pulumi.getter(name="allowedOAuthFlows")
    def allowed_o_auth_flows(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "allowed_o_auth_flows")

    @property
    @pulumi.getter(name="allowedOAuthFlowsUserPoolClient")
    def allowed_o_auth_flows_user_pool_client(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "allowed_o_auth_flows_user_pool_client")

    @property
    @pulumi.getter(name="allowedOAuthScopes")
    def allowed_o_auth_scopes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "allowed_o_auth_scopes")

    @property
    @pulumi.getter(name="analyticsConfiguration")
    def analytics_configuration(self) -> pulumi.Output[Optional['outputs.UserPoolClientAnalyticsConfiguration']]:
        return pulumi.get(self, "analytics_configuration")

    @property
    @pulumi.getter(name="callbackURLs")
    def callback_urls(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "callback_urls")

    @property
    @pulumi.getter(name="clientName")
    def client_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "client_name")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Output[str]:
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter(name="defaultRedirectURI")
    def default_redirect_uri(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_redirect_uri")

    @property
    @pulumi.getter(name="enablePropagateAdditionalUserContextData")
    def enable_propagate_additional_user_context_data(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enable_propagate_additional_user_context_data")

    @property
    @pulumi.getter(name="enableTokenRevocation")
    def enable_token_revocation(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enable_token_revocation")

    @property
    @pulumi.getter(name="explicitAuthFlows")
    def explicit_auth_flows(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "explicit_auth_flows")

    @property
    @pulumi.getter(name="generateSecret")
    def generate_secret(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "generate_secret")

    @property
    @pulumi.getter(name="idTokenValidity")
    def id_token_validity(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "id_token_validity")

    @property
    @pulumi.getter(name="logoutURLs")
    def logout_urls(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "logout_urls")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="preventUserExistenceErrors")
    def prevent_user_existence_errors(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "prevent_user_existence_errors")

    @property
    @pulumi.getter(name="readAttributes")
    def read_attributes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "read_attributes")

    @property
    @pulumi.getter(name="refreshTokenValidity")
    def refresh_token_validity(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "refresh_token_validity")

    @property
    @pulumi.getter(name="supportedIdentityProviders")
    def supported_identity_providers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "supported_identity_providers")

    @property
    @pulumi.getter(name="tokenValidityUnits")
    def token_validity_units(self) -> pulumi.Output[Optional['outputs.UserPoolClientTokenValidityUnits']]:
        return pulumi.get(self, "token_validity_units")

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "user_pool_id")

    @property
    @pulumi.getter(name="writeAttributes")
    def write_attributes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "write_attributes")

