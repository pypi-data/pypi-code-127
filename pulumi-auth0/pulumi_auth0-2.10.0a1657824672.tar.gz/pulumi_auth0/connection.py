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

__all__ = ['ConnectionArgs', 'Connection']

@pulumi.input_type
class ConnectionArgs:
    def __init__(__self__, *,
                 strategy: pulumi.Input[str],
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled_clients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_domain_connection: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input['ConnectionOptionsArgs']] = None,
                 realms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 show_as_button: Optional[pulumi.Input[bool]] = None,
                 strategy_version: Optional[pulumi.Input[str]] = None,
                 validation: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Connection resource.
        :param pulumi.Input[str] strategy: Type of the connection, which indicates the identity provider. Options include `ad`, `adfs`, `amazon`, `aol`, `apple`, `auth0`, `auth0-adldap`, `auth0-oidc`, `baidu`, `bitbucket`, `bitly`, `box`, `custom`, `daccount`, `dropbox`, `dwolla`, `email`, `evernote`, `evernote-sandbox`, `exact`, `facebook`, `fitbit`, `flickr`, `github`, `google-apps`, `google-oauth2`, `guardian`, `instagram`, `ip`, `line`, `linkedin`, `miicard`, `oauth1`, `oauth2`, `office365`, `oidc`, `paypal`, `paypal-sandbox`, `pingfederate`, `planningcenter`, `renren`, `salesforce`, `salesforce-community`, `salesforce-sandbox` `samlp`, `sharepoint`, `shopify`, `sms`, `soundcloud`, `thecity`, `thecity-sandbox`, `thirtysevensignals`, `twitter`, `untappd`, `vkontakte`, `waad`, `weibo`, `windowslive`, `wordpress`, `yahoo`, `yammer`, `yandex`.
        :param pulumi.Input[str] display_name: Name used in login screen
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_clients: IDs of the clients for which the connection is enabled. If not specified, no clients are enabled.
        :param pulumi.Input[bool] is_domain_connection: Indicates whether the connection is domain level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Metadata associated with the connection, in the form of a map of string values (max 255 chars). Maximum of 10 metadata properties allowed.
        :param pulumi.Input[str] name: Name of the connection.
        :param pulumi.Input['ConnectionOptionsArgs'] options: Configuration settings for connection options. For details, see Options.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] realms: Defines the realms for which the connection will be used (i.e., email domains). If not specified, the connection name is added as the realm.
        :param pulumi.Input[bool] show_as_button: Display connection as a button. Only available for enterprise connections.
        :param pulumi.Input[str] strategy_version: Version 1 is deprecated, use version 2.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] validation: Validation of the minimum and maximum values allowed for a user to have as username. For details, see Validation.
        """
        pulumi.set(__self__, "strategy", strategy)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if enabled_clients is not None:
            pulumi.set(__self__, "enabled_clients", enabled_clients)
        if is_domain_connection is not None:
            pulumi.set(__self__, "is_domain_connection", is_domain_connection)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if options is not None:
            pulumi.set(__self__, "options", options)
        if realms is not None:
            pulumi.set(__self__, "realms", realms)
        if show_as_button is not None:
            pulumi.set(__self__, "show_as_button", show_as_button)
        if strategy_version is not None:
            pulumi.set(__self__, "strategy_version", strategy_version)
        if validation is not None:
            pulumi.set(__self__, "validation", validation)

    @property
    @pulumi.getter
    def strategy(self) -> pulumi.Input[str]:
        """
        Type of the connection, which indicates the identity provider. Options include `ad`, `adfs`, `amazon`, `aol`, `apple`, `auth0`, `auth0-adldap`, `auth0-oidc`, `baidu`, `bitbucket`, `bitly`, `box`, `custom`, `daccount`, `dropbox`, `dwolla`, `email`, `evernote`, `evernote-sandbox`, `exact`, `facebook`, `fitbit`, `flickr`, `github`, `google-apps`, `google-oauth2`, `guardian`, `instagram`, `ip`, `line`, `linkedin`, `miicard`, `oauth1`, `oauth2`, `office365`, `oidc`, `paypal`, `paypal-sandbox`, `pingfederate`, `planningcenter`, `renren`, `salesforce`, `salesforce-community`, `salesforce-sandbox` `samlp`, `sharepoint`, `shopify`, `sms`, `soundcloud`, `thecity`, `thecity-sandbox`, `thirtysevensignals`, `twitter`, `untappd`, `vkontakte`, `waad`, `weibo`, `windowslive`, `wordpress`, `yahoo`, `yammer`, `yandex`.
        """
        return pulumi.get(self, "strategy")

    @strategy.setter
    def strategy(self, value: pulumi.Input[str]):
        pulumi.set(self, "strategy", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name used in login screen
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="enabledClients")
    def enabled_clients(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        IDs of the clients for which the connection is enabled. If not specified, no clients are enabled.
        """
        return pulumi.get(self, "enabled_clients")

    @enabled_clients.setter
    def enabled_clients(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "enabled_clients", value)

    @property
    @pulumi.getter(name="isDomainConnection")
    def is_domain_connection(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the connection is domain level.
        """
        return pulumi.get(self, "is_domain_connection")

    @is_domain_connection.setter
    def is_domain_connection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_domain_connection", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Metadata associated with the connection, in the form of a map of string values (max 255 chars). Maximum of 10 metadata properties allowed.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the connection.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input['ConnectionOptionsArgs']]:
        """
        Configuration settings for connection options. For details, see Options.
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: Optional[pulumi.Input['ConnectionOptionsArgs']]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter
    def realms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Defines the realms for which the connection will be used (i.e., email domains). If not specified, the connection name is added as the realm.
        """
        return pulumi.get(self, "realms")

    @realms.setter
    def realms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "realms", value)

    @property
    @pulumi.getter(name="showAsButton")
    def show_as_button(self) -> Optional[pulumi.Input[bool]]:
        """
        Display connection as a button. Only available for enterprise connections.
        """
        return pulumi.get(self, "show_as_button")

    @show_as_button.setter
    def show_as_button(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "show_as_button", value)

    @property
    @pulumi.getter(name="strategyVersion")
    def strategy_version(self) -> Optional[pulumi.Input[str]]:
        """
        Version 1 is deprecated, use version 2.
        """
        return pulumi.get(self, "strategy_version")

    @strategy_version.setter
    def strategy_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "strategy_version", value)

    @property
    @pulumi.getter
    def validation(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Validation of the minimum and maximum values allowed for a user to have as username. For details, see Validation.
        """
        return pulumi.get(self, "validation")

    @validation.setter
    def validation(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "validation", value)


@pulumi.input_type
class _ConnectionState:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled_clients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_domain_connection: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input['ConnectionOptionsArgs']] = None,
                 realms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 show_as_button: Optional[pulumi.Input[bool]] = None,
                 strategy: Optional[pulumi.Input[str]] = None,
                 strategy_version: Optional[pulumi.Input[str]] = None,
                 validation: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Connection resources.
        :param pulumi.Input[str] display_name: Name used in login screen
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_clients: IDs of the clients for which the connection is enabled. If not specified, no clients are enabled.
        :param pulumi.Input[bool] is_domain_connection: Indicates whether the connection is domain level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Metadata associated with the connection, in the form of a map of string values (max 255 chars). Maximum of 10 metadata properties allowed.
        :param pulumi.Input[str] name: Name of the connection.
        :param pulumi.Input['ConnectionOptionsArgs'] options: Configuration settings for connection options. For details, see Options.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] realms: Defines the realms for which the connection will be used (i.e., email domains). If not specified, the connection name is added as the realm.
        :param pulumi.Input[bool] show_as_button: Display connection as a button. Only available for enterprise connections.
        :param pulumi.Input[str] strategy: Type of the connection, which indicates the identity provider. Options include `ad`, `adfs`, `amazon`, `aol`, `apple`, `auth0`, `auth0-adldap`, `auth0-oidc`, `baidu`, `bitbucket`, `bitly`, `box`, `custom`, `daccount`, `dropbox`, `dwolla`, `email`, `evernote`, `evernote-sandbox`, `exact`, `facebook`, `fitbit`, `flickr`, `github`, `google-apps`, `google-oauth2`, `guardian`, `instagram`, `ip`, `line`, `linkedin`, `miicard`, `oauth1`, `oauth2`, `office365`, `oidc`, `paypal`, `paypal-sandbox`, `pingfederate`, `planningcenter`, `renren`, `salesforce`, `salesforce-community`, `salesforce-sandbox` `samlp`, `sharepoint`, `shopify`, `sms`, `soundcloud`, `thecity`, `thecity-sandbox`, `thirtysevensignals`, `twitter`, `untappd`, `vkontakte`, `waad`, `weibo`, `windowslive`, `wordpress`, `yahoo`, `yammer`, `yandex`.
        :param pulumi.Input[str] strategy_version: Version 1 is deprecated, use version 2.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] validation: Validation of the minimum and maximum values allowed for a user to have as username. For details, see Validation.
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if enabled_clients is not None:
            pulumi.set(__self__, "enabled_clients", enabled_clients)
        if is_domain_connection is not None:
            pulumi.set(__self__, "is_domain_connection", is_domain_connection)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if options is not None:
            pulumi.set(__self__, "options", options)
        if realms is not None:
            pulumi.set(__self__, "realms", realms)
        if show_as_button is not None:
            pulumi.set(__self__, "show_as_button", show_as_button)
        if strategy is not None:
            pulumi.set(__self__, "strategy", strategy)
        if strategy_version is not None:
            pulumi.set(__self__, "strategy_version", strategy_version)
        if validation is not None:
            pulumi.set(__self__, "validation", validation)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name used in login screen
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="enabledClients")
    def enabled_clients(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        IDs of the clients for which the connection is enabled. If not specified, no clients are enabled.
        """
        return pulumi.get(self, "enabled_clients")

    @enabled_clients.setter
    def enabled_clients(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "enabled_clients", value)

    @property
    @pulumi.getter(name="isDomainConnection")
    def is_domain_connection(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the connection is domain level.
        """
        return pulumi.get(self, "is_domain_connection")

    @is_domain_connection.setter
    def is_domain_connection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_domain_connection", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Metadata associated with the connection, in the form of a map of string values (max 255 chars). Maximum of 10 metadata properties allowed.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the connection.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input['ConnectionOptionsArgs']]:
        """
        Configuration settings for connection options. For details, see Options.
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: Optional[pulumi.Input['ConnectionOptionsArgs']]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter
    def realms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Defines the realms for which the connection will be used (i.e., email domains). If not specified, the connection name is added as the realm.
        """
        return pulumi.get(self, "realms")

    @realms.setter
    def realms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "realms", value)

    @property
    @pulumi.getter(name="showAsButton")
    def show_as_button(self) -> Optional[pulumi.Input[bool]]:
        """
        Display connection as a button. Only available for enterprise connections.
        """
        return pulumi.get(self, "show_as_button")

    @show_as_button.setter
    def show_as_button(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "show_as_button", value)

    @property
    @pulumi.getter
    def strategy(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the connection, which indicates the identity provider. Options include `ad`, `adfs`, `amazon`, `aol`, `apple`, `auth0`, `auth0-adldap`, `auth0-oidc`, `baidu`, `bitbucket`, `bitly`, `box`, `custom`, `daccount`, `dropbox`, `dwolla`, `email`, `evernote`, `evernote-sandbox`, `exact`, `facebook`, `fitbit`, `flickr`, `github`, `google-apps`, `google-oauth2`, `guardian`, `instagram`, `ip`, `line`, `linkedin`, `miicard`, `oauth1`, `oauth2`, `office365`, `oidc`, `paypal`, `paypal-sandbox`, `pingfederate`, `planningcenter`, `renren`, `salesforce`, `salesforce-community`, `salesforce-sandbox` `samlp`, `sharepoint`, `shopify`, `sms`, `soundcloud`, `thecity`, `thecity-sandbox`, `thirtysevensignals`, `twitter`, `untappd`, `vkontakte`, `waad`, `weibo`, `windowslive`, `wordpress`, `yahoo`, `yammer`, `yandex`.
        """
        return pulumi.get(self, "strategy")

    @strategy.setter
    def strategy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "strategy", value)

    @property
    @pulumi.getter(name="strategyVersion")
    def strategy_version(self) -> Optional[pulumi.Input[str]]:
        """
        Version 1 is deprecated, use version 2.
        """
        return pulumi.get(self, "strategy_version")

    @strategy_version.setter
    def strategy_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "strategy_version", value)

    @property
    @pulumi.getter
    def validation(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Validation of the minimum and maximum values allowed for a user to have as username. For details, see Validation.
        """
        return pulumi.get(self, "validation")

    @validation.setter
    def validation(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "validation", value)


class Connection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled_clients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_domain_connection: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['ConnectionOptionsArgs']]] = None,
                 realms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 show_as_button: Optional[pulumi.Input[bool]] = None,
                 strategy: Optional[pulumi.Input[str]] = None,
                 strategy_version: Optional[pulumi.Input[str]] = None,
                 validation: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        With Auth0, you can define sources of users, otherwise known as connections, which may include identity providers
        (such as Google or LinkedIn), databases, or passwordless authentication methods. This resource allows you to configure
        and manage connections to be used with your clients and users.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_auth0 as auth0

        my_connection = auth0.Connection("myConnection",
            metadata={
                "key1": "foo",
                "key2": "bar",
            },
            options=auth0.ConnectionOptionsArgs(
                brute_force_protection=True,
                configuration={
                    "bar": "baz",
                    "foo": "bar",
                },
                custom_scripts={
                    "getUser": \"\"\"function getByEmail (email, callback) {
          return callback(new Error("Whoops!"))
        }

        \"\"\",
                },
                enabled_database_customization=True,
                password_histories=[auth0.ConnectionOptionsPasswordHistoryArgs(
                    enable=True,
                    size=3,
                )],
                password_policy="excellent",
            ),
            strategy="auth0")
        ```

        > The Auth0 dashboard displays only one connection per social provider. Although the Auth0 Management API allows the
        creation of multiple connections per strategy, the additional connections may not be visible in the Auth0 dashboard.

        ## Import

        Connections can be imported using their id, e.g.

        ```sh
         $ pulumi import auth0:index/connection:Connection google con_a17f21fdb24d48a0
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Name used in login screen
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_clients: IDs of the clients for which the connection is enabled. If not specified, no clients are enabled.
        :param pulumi.Input[bool] is_domain_connection: Indicates whether the connection is domain level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Metadata associated with the connection, in the form of a map of string values (max 255 chars). Maximum of 10 metadata properties allowed.
        :param pulumi.Input[str] name: Name of the connection.
        :param pulumi.Input[pulumi.InputType['ConnectionOptionsArgs']] options: Configuration settings for connection options. For details, see Options.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] realms: Defines the realms for which the connection will be used (i.e., email domains). If not specified, the connection name is added as the realm.
        :param pulumi.Input[bool] show_as_button: Display connection as a button. Only available for enterprise connections.
        :param pulumi.Input[str] strategy: Type of the connection, which indicates the identity provider. Options include `ad`, `adfs`, `amazon`, `aol`, `apple`, `auth0`, `auth0-adldap`, `auth0-oidc`, `baidu`, `bitbucket`, `bitly`, `box`, `custom`, `daccount`, `dropbox`, `dwolla`, `email`, `evernote`, `evernote-sandbox`, `exact`, `facebook`, `fitbit`, `flickr`, `github`, `google-apps`, `google-oauth2`, `guardian`, `instagram`, `ip`, `line`, `linkedin`, `miicard`, `oauth1`, `oauth2`, `office365`, `oidc`, `paypal`, `paypal-sandbox`, `pingfederate`, `planningcenter`, `renren`, `salesforce`, `salesforce-community`, `salesforce-sandbox` `samlp`, `sharepoint`, `shopify`, `sms`, `soundcloud`, `thecity`, `thecity-sandbox`, `thirtysevensignals`, `twitter`, `untappd`, `vkontakte`, `waad`, `weibo`, `windowslive`, `wordpress`, `yahoo`, `yammer`, `yandex`.
        :param pulumi.Input[str] strategy_version: Version 1 is deprecated, use version 2.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] validation: Validation of the minimum and maximum values allowed for a user to have as username. For details, see Validation.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        With Auth0, you can define sources of users, otherwise known as connections, which may include identity providers
        (such as Google or LinkedIn), databases, or passwordless authentication methods. This resource allows you to configure
        and manage connections to be used with your clients and users.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_auth0 as auth0

        my_connection = auth0.Connection("myConnection",
            metadata={
                "key1": "foo",
                "key2": "bar",
            },
            options=auth0.ConnectionOptionsArgs(
                brute_force_protection=True,
                configuration={
                    "bar": "baz",
                    "foo": "bar",
                },
                custom_scripts={
                    "getUser": \"\"\"function getByEmail (email, callback) {
          return callback(new Error("Whoops!"))
        }

        \"\"\",
                },
                enabled_database_customization=True,
                password_histories=[auth0.ConnectionOptionsPasswordHistoryArgs(
                    enable=True,
                    size=3,
                )],
                password_policy="excellent",
            ),
            strategy="auth0")
        ```

        > The Auth0 dashboard displays only one connection per social provider. Although the Auth0 Management API allows the
        creation of multiple connections per strategy, the additional connections may not be visible in the Auth0 dashboard.

        ## Import

        Connections can be imported using their id, e.g.

        ```sh
         $ pulumi import auth0:index/connection:Connection google con_a17f21fdb24d48a0
        ```

        :param str resource_name: The name of the resource.
        :param ConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled_clients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_domain_connection: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['ConnectionOptionsArgs']]] = None,
                 realms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 show_as_button: Optional[pulumi.Input[bool]] = None,
                 strategy: Optional[pulumi.Input[str]] = None,
                 strategy_version: Optional[pulumi.Input[str]] = None,
                 validation: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = ConnectionArgs.__new__(ConnectionArgs)

            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["enabled_clients"] = enabled_clients
            __props__.__dict__["is_domain_connection"] = is_domain_connection
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            __props__.__dict__["options"] = options
            __props__.__dict__["realms"] = realms
            __props__.__dict__["show_as_button"] = show_as_button
            if strategy is None and not opts.urn:
                raise TypeError("Missing required property 'strategy'")
            __props__.__dict__["strategy"] = strategy
            __props__.__dict__["strategy_version"] = strategy_version
            __props__.__dict__["validation"] = validation
        super(Connection, __self__).__init__(
            'auth0:index/connection:Connection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            enabled_clients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            is_domain_connection: Optional[pulumi.Input[bool]] = None,
            metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            options: Optional[pulumi.Input[pulumi.InputType['ConnectionOptionsArgs']]] = None,
            realms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            show_as_button: Optional[pulumi.Input[bool]] = None,
            strategy: Optional[pulumi.Input[str]] = None,
            strategy_version: Optional[pulumi.Input[str]] = None,
            validation: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Connection':
        """
        Get an existing Connection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Name used in login screen
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_clients: IDs of the clients for which the connection is enabled. If not specified, no clients are enabled.
        :param pulumi.Input[bool] is_domain_connection: Indicates whether the connection is domain level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Metadata associated with the connection, in the form of a map of string values (max 255 chars). Maximum of 10 metadata properties allowed.
        :param pulumi.Input[str] name: Name of the connection.
        :param pulumi.Input[pulumi.InputType['ConnectionOptionsArgs']] options: Configuration settings for connection options. For details, see Options.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] realms: Defines the realms for which the connection will be used (i.e., email domains). If not specified, the connection name is added as the realm.
        :param pulumi.Input[bool] show_as_button: Display connection as a button. Only available for enterprise connections.
        :param pulumi.Input[str] strategy: Type of the connection, which indicates the identity provider. Options include `ad`, `adfs`, `amazon`, `aol`, `apple`, `auth0`, `auth0-adldap`, `auth0-oidc`, `baidu`, `bitbucket`, `bitly`, `box`, `custom`, `daccount`, `dropbox`, `dwolla`, `email`, `evernote`, `evernote-sandbox`, `exact`, `facebook`, `fitbit`, `flickr`, `github`, `google-apps`, `google-oauth2`, `guardian`, `instagram`, `ip`, `line`, `linkedin`, `miicard`, `oauth1`, `oauth2`, `office365`, `oidc`, `paypal`, `paypal-sandbox`, `pingfederate`, `planningcenter`, `renren`, `salesforce`, `salesforce-community`, `salesforce-sandbox` `samlp`, `sharepoint`, `shopify`, `sms`, `soundcloud`, `thecity`, `thecity-sandbox`, `thirtysevensignals`, `twitter`, `untappd`, `vkontakte`, `waad`, `weibo`, `windowslive`, `wordpress`, `yahoo`, `yammer`, `yandex`.
        :param pulumi.Input[str] strategy_version: Version 1 is deprecated, use version 2.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] validation: Validation of the minimum and maximum values allowed for a user to have as username. For details, see Validation.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConnectionState.__new__(_ConnectionState)

        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["enabled_clients"] = enabled_clients
        __props__.__dict__["is_domain_connection"] = is_domain_connection
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["options"] = options
        __props__.__dict__["realms"] = realms
        __props__.__dict__["show_as_button"] = show_as_button
        __props__.__dict__["strategy"] = strategy
        __props__.__dict__["strategy_version"] = strategy_version
        __props__.__dict__["validation"] = validation
        return Connection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name used in login screen
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enabledClients")
    def enabled_clients(self) -> pulumi.Output[Sequence[str]]:
        """
        IDs of the clients for which the connection is enabled. If not specified, no clients are enabled.
        """
        return pulumi.get(self, "enabled_clients")

    @property
    @pulumi.getter(name="isDomainConnection")
    def is_domain_connection(self) -> pulumi.Output[bool]:
        """
        Indicates whether the connection is domain level.
        """
        return pulumi.get(self, "is_domain_connection")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Metadata associated with the connection, in the form of a map of string values (max 255 chars). Maximum of 10 metadata properties allowed.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the connection.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def options(self) -> pulumi.Output['outputs.ConnectionOptions']:
        """
        Configuration settings for connection options. For details, see Options.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter
    def realms(self) -> pulumi.Output[Sequence[str]]:
        """
        Defines the realms for which the connection will be used (i.e., email domains). If not specified, the connection name is added as the realm.
        """
        return pulumi.get(self, "realms")

    @property
    @pulumi.getter(name="showAsButton")
    def show_as_button(self) -> pulumi.Output[Optional[bool]]:
        """
        Display connection as a button. Only available for enterprise connections.
        """
        return pulumi.get(self, "show_as_button")

    @property
    @pulumi.getter
    def strategy(self) -> pulumi.Output[str]:
        """
        Type of the connection, which indicates the identity provider. Options include `ad`, `adfs`, `amazon`, `aol`, `apple`, `auth0`, `auth0-adldap`, `auth0-oidc`, `baidu`, `bitbucket`, `bitly`, `box`, `custom`, `daccount`, `dropbox`, `dwolla`, `email`, `evernote`, `evernote-sandbox`, `exact`, `facebook`, `fitbit`, `flickr`, `github`, `google-apps`, `google-oauth2`, `guardian`, `instagram`, `ip`, `line`, `linkedin`, `miicard`, `oauth1`, `oauth2`, `office365`, `oidc`, `paypal`, `paypal-sandbox`, `pingfederate`, `planningcenter`, `renren`, `salesforce`, `salesforce-community`, `salesforce-sandbox` `samlp`, `sharepoint`, `shopify`, `sms`, `soundcloud`, `thecity`, `thecity-sandbox`, `thirtysevensignals`, `twitter`, `untappd`, `vkontakte`, `waad`, `weibo`, `windowslive`, `wordpress`, `yahoo`, `yammer`, `yandex`.
        """
        return pulumi.get(self, "strategy")

    @property
    @pulumi.getter(name="strategyVersion")
    def strategy_version(self) -> pulumi.Output[str]:
        """
        Version 1 is deprecated, use version 2.
        """
        return pulumi.get(self, "strategy_version")

    @property
    @pulumi.getter
    def validation(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Validation of the minimum and maximum values allowed for a user to have as username. For details, see Validation.
        """
        return pulumi.get(self, "validation")

