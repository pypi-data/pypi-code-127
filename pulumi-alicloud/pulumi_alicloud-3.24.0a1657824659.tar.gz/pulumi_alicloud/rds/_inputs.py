# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'InstanceBabelfishConfigArgs',
    'InstanceParameterArgs',
    'InstancePgHbaConfArgs',
    'RdsCloneDbInstanceParameterArgs',
    'RdsCloneDbInstancePgHbaConfArgs',
    'RdsParameterGroupParamDetailArgs',
    'RdsUpgradeDbInstanceParameterArgs',
    'RdsUpgradeDbInstancePgHbaConfArgs',
    'ReadOnlyInstanceParameterArgs',
]

@pulumi.input_type
class InstanceBabelfishConfigArgs:
    def __init__(__self__, *,
                 babelfish_enabled: pulumi.Input[str],
                 master_user_password: pulumi.Input[str],
                 master_username: pulumi.Input[str],
                 migration_mode: pulumi.Input[str]):
        """
        :param pulumi.Input[str] babelfish_enabled: specifies whether to enable the Babelfish for the instance. If you set this parameter to **true**, you enable Babelfish for the instance. If you leave this parameter empty, you disable Babelfish for the instance.
        :param pulumi.Input[str] master_user_password: The password of the administrator account. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It must be 8 to 32 characters in length. The password can contain any of the following characters:! @ # $ % ^ & * () _ + - =
        :param pulumi.Input[str] master_username: The name of the administrator account. The name can contain lowercase letters, digits, and underscores (_). It must start with a letter and end with a letter or digit. It can be up to 63 characters in length and cannot start with pg.
        :param pulumi.Input[str] migration_mode: The migration mode of the instance. Valid values: **single-db** and **multi-db**.
        """
        pulumi.set(__self__, "babelfish_enabled", babelfish_enabled)
        pulumi.set(__self__, "master_user_password", master_user_password)
        pulumi.set(__self__, "master_username", master_username)
        pulumi.set(__self__, "migration_mode", migration_mode)

    @property
    @pulumi.getter(name="babelfishEnabled")
    def babelfish_enabled(self) -> pulumi.Input[str]:
        """
        specifies whether to enable the Babelfish for the instance. If you set this parameter to **true**, you enable Babelfish for the instance. If you leave this parameter empty, you disable Babelfish for the instance.
        """
        return pulumi.get(self, "babelfish_enabled")

    @babelfish_enabled.setter
    def babelfish_enabled(self, value: pulumi.Input[str]):
        pulumi.set(self, "babelfish_enabled", value)

    @property
    @pulumi.getter(name="masterUserPassword")
    def master_user_password(self) -> pulumi.Input[str]:
        """
        The password of the administrator account. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It must be 8 to 32 characters in length. The password can contain any of the following characters:! @ # $ % ^ & * () _ + - =
        """
        return pulumi.get(self, "master_user_password")

    @master_user_password.setter
    def master_user_password(self, value: pulumi.Input[str]):
        pulumi.set(self, "master_user_password", value)

    @property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> pulumi.Input[str]:
        """
        The name of the administrator account. The name can contain lowercase letters, digits, and underscores (_). It must start with a letter and end with a letter or digit. It can be up to 63 characters in length and cannot start with pg.
        """
        return pulumi.get(self, "master_username")

    @master_username.setter
    def master_username(self, value: pulumi.Input[str]):
        pulumi.set(self, "master_username", value)

    @property
    @pulumi.getter(name="migrationMode")
    def migration_mode(self) -> pulumi.Input[str]:
        """
        The migration mode of the instance. Valid values: **single-db** and **multi-db**.
        """
        return pulumi.get(self, "migration_mode")

    @migration_mode.setter
    def migration_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "migration_mode", value)


@pulumi.input_type
class InstanceParameterArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class InstancePgHbaConfArgs:
    def __init__(__self__, *,
                 address: pulumi.Input[str],
                 database: pulumi.Input[str],
                 method: pulumi.Input[str],
                 priority_id: pulumi.Input[int],
                 type: pulumi.Input[str],
                 user: pulumi.Input[str],
                 mask: Optional[pulumi.Input[str]] = None,
                 option: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] address: The IP addresses from which the specified users can access the specified databases. If you set this parameter to 0.0.0.0/0, the specified users are allowed to access the specified databases from all IP addresses.
        :param pulumi.Input[str] database: The name of the database that the specified users are allowed to access. If you set this parameter to all, the specified users are allowed to access all databases in the instance. If you specify multiple databases, separate the database names with commas (,).
        :param pulumi.Input[str] method: The authentication method of Lightweight Directory Access Protocol (LDAP). Valid values: `trust`, `reject`, `scram-sha-256`, `md5`, `password`, `gss`, `sspi`, `ldap`, `radius`, `cert`, `pam`.
        :param pulumi.Input[int] priority_id: The priority of an AD domain. If you set this parameter to 0, the AD domain has the highest priority. Valid values: 0 to 10000. This parameter is used to identify each AD domain. When you add an AD domain, the value of the PriorityId parameter of the new AD domain cannot be the same as the value of the PriorityId parameter for any existing AD domain. When you modify or delete an AD domain, you must also modify or delete the value of the PriorityId parameter for this AD domain.
        :param pulumi.Input[str] type: The type of connection to the instance. Valid values:
               * **host**: specifies to verify TCP/IP connections, including SSL connections and non-SSL connections.
               * **hostssl**: specifies to verify only TCP/IP connections that are established over SSL connections.
               * **hostnossl**: specifies to verify only TCP/IP connections that are established over non-SSL connections.
        :param pulumi.Input[str] user: The user that is allowed to access the instance. If you specify multiple users, separate the usernames with commas (,).
        :param pulumi.Input[str] mask: The mask of the instance. If the value of the `Address` parameter is an IP address, you can use this parameter to specify the mask of the IP address.
        :param pulumi.Input[str] option: Optional. The value of this parameter is based on the value of the HbaItem.N.Method parameter. In this topic, LDAP is used as an example. You must configure this parameter. For more information, see [Authentication Methods](https://www.postgresql.org/docs/11/auth-methods.html).
        """
        pulumi.set(__self__, "address", address)
        pulumi.set(__self__, "database", database)
        pulumi.set(__self__, "method", method)
        pulumi.set(__self__, "priority_id", priority_id)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "user", user)
        if mask is not None:
            pulumi.set(__self__, "mask", mask)
        if option is not None:
            pulumi.set(__self__, "option", option)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Input[str]:
        """
        The IP addresses from which the specified users can access the specified databases. If you set this parameter to 0.0.0.0/0, the specified users are allowed to access the specified databases from all IP addresses.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: pulumi.Input[str]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Input[str]:
        """
        The name of the database that the specified users are allowed to access. If you set this parameter to all, the specified users are allowed to access all databases in the instance. If you specify multiple databases, separate the database names with commas (,).
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: pulumi.Input[str]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def method(self) -> pulumi.Input[str]:
        """
        The authentication method of Lightweight Directory Access Protocol (LDAP). Valid values: `trust`, `reject`, `scram-sha-256`, `md5`, `password`, `gss`, `sspi`, `ldap`, `radius`, `cert`, `pam`.
        """
        return pulumi.get(self, "method")

    @method.setter
    def method(self, value: pulumi.Input[str]):
        pulumi.set(self, "method", value)

    @property
    @pulumi.getter(name="priorityId")
    def priority_id(self) -> pulumi.Input[int]:
        """
        The priority of an AD domain. If you set this parameter to 0, the AD domain has the highest priority. Valid values: 0 to 10000. This parameter is used to identify each AD domain. When you add an AD domain, the value of the PriorityId parameter of the new AD domain cannot be the same as the value of the PriorityId parameter for any existing AD domain. When you modify or delete an AD domain, you must also modify or delete the value of the PriorityId parameter for this AD domain.
        """
        return pulumi.get(self, "priority_id")

    @priority_id.setter
    def priority_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "priority_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of connection to the instance. Valid values:
        * **host**: specifies to verify TCP/IP connections, including SSL connections and non-SSL connections.
        * **hostssl**: specifies to verify only TCP/IP connections that are established over SSL connections.
        * **hostnossl**: specifies to verify only TCP/IP connections that are established over non-SSL connections.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def user(self) -> pulumi.Input[str]:
        """
        The user that is allowed to access the instance. If you specify multiple users, separate the usernames with commas (,).
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: pulumi.Input[str]):
        pulumi.set(self, "user", value)

    @property
    @pulumi.getter
    def mask(self) -> Optional[pulumi.Input[str]]:
        """
        The mask of the instance. If the value of the `Address` parameter is an IP address, you can use this parameter to specify the mask of the IP address.
        """
        return pulumi.get(self, "mask")

    @mask.setter
    def mask(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mask", value)

    @property
    @pulumi.getter
    def option(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The value of this parameter is based on the value of the HbaItem.N.Method parameter. In this topic, LDAP is used as an example. You must configure this parameter. For more information, see [Authentication Methods](https://www.postgresql.org/docs/11/auth-methods.html).
        """
        return pulumi.get(self, "option")

    @option.setter
    def option(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "option", value)


@pulumi.input_type
class RdsCloneDbInstanceParameterArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class RdsCloneDbInstancePgHbaConfArgs:
    def __init__(__self__, *,
                 address: pulumi.Input[str],
                 database: pulumi.Input[str],
                 method: pulumi.Input[str],
                 priority_id: pulumi.Input[int],
                 type: pulumi.Input[str],
                 user: pulumi.Input[str],
                 mask: Optional[pulumi.Input[str]] = None,
                 option: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] address: The IP addresses from which the specified users can access the specified databases. If you set this parameter to 0.0.0.0/0, the specified users are allowed to access the specified databases from all IP addresses.
        :param pulumi.Input[str] database: The name of the database that the specified users are allowed to access. If you set this parameter to all, the specified users are allowed to access all databases in the instance. If you specify multiple databases, separate the database names with commas (,).
        :param pulumi.Input[str] method: The authentication method of Lightweight Directory Access Protocol (LDAP). Valid values: `trust`, `reject`, `scram-sha-256`, `md5`, `password`, `gss`, `sspi`, `ldap`, `radius`, `cert`, `pam`.
        :param pulumi.Input[int] priority_id: The priority of an AD domain. If you set this parameter to 0, the AD domain has the highest priority. Valid values: 0 to 10000. This parameter is used to identify each AD domain. When you add an AD domain, the value of the PriorityId parameter of the new AD domain cannot be the same as the value of the PriorityId parameter for any existing AD domain. When you modify or delete an AD domain, you must also modify or delete the value of the PriorityId parameter for this AD domain.
        :param pulumi.Input[str] type: The type of connection to the instance. Valid values:
               * **host**: specifies to verify TCP/IP connections, including SSL connections and non-SSL connections.
               * **hostssl**: specifies to verify only TCP/IP connections that are established over SSL connections.
               * **hostnossl**: specifies to verify only TCP/IP connections that are established over non-SSL connections.
        :param pulumi.Input[str] user: The user that is allowed to access the instance. If you specify multiple users, separate the usernames with commas (,).
        :param pulumi.Input[str] mask: The mask of the instance. If the value of the `Address` parameter is an IP address, you can use this parameter to specify the mask of the IP address.
        :param pulumi.Input[str] option: Optional. The value of this parameter is based on the value of the HbaItem.N.Method parameter. In this topic, LDAP is used as an example. You must configure this parameter. For more information, see [Authentication Methods](https://www.postgresql.org/docs/11/auth-methods.html).
        """
        pulumi.set(__self__, "address", address)
        pulumi.set(__self__, "database", database)
        pulumi.set(__self__, "method", method)
        pulumi.set(__self__, "priority_id", priority_id)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "user", user)
        if mask is not None:
            pulumi.set(__self__, "mask", mask)
        if option is not None:
            pulumi.set(__self__, "option", option)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Input[str]:
        """
        The IP addresses from which the specified users can access the specified databases. If you set this parameter to 0.0.0.0/0, the specified users are allowed to access the specified databases from all IP addresses.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: pulumi.Input[str]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Input[str]:
        """
        The name of the database that the specified users are allowed to access. If you set this parameter to all, the specified users are allowed to access all databases in the instance. If you specify multiple databases, separate the database names with commas (,).
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: pulumi.Input[str]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def method(self) -> pulumi.Input[str]:
        """
        The authentication method of Lightweight Directory Access Protocol (LDAP). Valid values: `trust`, `reject`, `scram-sha-256`, `md5`, `password`, `gss`, `sspi`, `ldap`, `radius`, `cert`, `pam`.
        """
        return pulumi.get(self, "method")

    @method.setter
    def method(self, value: pulumi.Input[str]):
        pulumi.set(self, "method", value)

    @property
    @pulumi.getter(name="priorityId")
    def priority_id(self) -> pulumi.Input[int]:
        """
        The priority of an AD domain. If you set this parameter to 0, the AD domain has the highest priority. Valid values: 0 to 10000. This parameter is used to identify each AD domain. When you add an AD domain, the value of the PriorityId parameter of the new AD domain cannot be the same as the value of the PriorityId parameter for any existing AD domain. When you modify or delete an AD domain, you must also modify or delete the value of the PriorityId parameter for this AD domain.
        """
        return pulumi.get(self, "priority_id")

    @priority_id.setter
    def priority_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "priority_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of connection to the instance. Valid values:
        * **host**: specifies to verify TCP/IP connections, including SSL connections and non-SSL connections.
        * **hostssl**: specifies to verify only TCP/IP connections that are established over SSL connections.
        * **hostnossl**: specifies to verify only TCP/IP connections that are established over non-SSL connections.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def user(self) -> pulumi.Input[str]:
        """
        The user that is allowed to access the instance. If you specify multiple users, separate the usernames with commas (,).
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: pulumi.Input[str]):
        pulumi.set(self, "user", value)

    @property
    @pulumi.getter
    def mask(self) -> Optional[pulumi.Input[str]]:
        """
        The mask of the instance. If the value of the `Address` parameter is an IP address, you can use this parameter to specify the mask of the IP address.
        """
        return pulumi.get(self, "mask")

    @mask.setter
    def mask(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mask", value)

    @property
    @pulumi.getter
    def option(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The value of this parameter is based on the value of the HbaItem.N.Method parameter. In this topic, LDAP is used as an example. You must configure this parameter. For more information, see [Authentication Methods](https://www.postgresql.org/docs/11/auth-methods.html).
        """
        return pulumi.get(self, "option")

    @option.setter
    def option(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "option", value)


@pulumi.input_type
class RdsParameterGroupParamDetailArgs:
    def __init__(__self__, *,
                 param_name: pulumi.Input[str],
                 param_value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] param_name: The name of a parameter.
        :param pulumi.Input[str] param_value: The value of a parameter.
        """
        pulumi.set(__self__, "param_name", param_name)
        pulumi.set(__self__, "param_value", param_value)

    @property
    @pulumi.getter(name="paramName")
    def param_name(self) -> pulumi.Input[str]:
        """
        The name of a parameter.
        """
        return pulumi.get(self, "param_name")

    @param_name.setter
    def param_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "param_name", value)

    @property
    @pulumi.getter(name="paramValue")
    def param_value(self) -> pulumi.Input[str]:
        """
        The value of a parameter.
        """
        return pulumi.get(self, "param_value")

    @param_value.setter
    def param_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "param_value", value)


@pulumi.input_type
class RdsUpgradeDbInstanceParameterArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class RdsUpgradeDbInstancePgHbaConfArgs:
    def __init__(__self__, *,
                 address: pulumi.Input[str],
                 database: pulumi.Input[str],
                 method: pulumi.Input[str],
                 priority_id: pulumi.Input[int],
                 type: pulumi.Input[str],
                 user: pulumi.Input[str],
                 mask: Optional[pulumi.Input[str]] = None,
                 option: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] address: The IP addresses from which the specified users can access the specified databases. If you set this parameter to 0.0.0.0/0, the specified users are allowed to access the specified databases from all IP addresses.
        :param pulumi.Input[str] database: The name of the database that the specified users are allowed to access. If you set this parameter to all, the specified users are allowed to access all databases in the instance. If you specify multiple databases, separate the database names with commas (,).
        :param pulumi.Input[str] method: The authentication method of Lightweight Directory Access Protocol (LDAP). Valid values: `trust`, `reject`, `scram-sha-256`, `md5`, `password`, `gss`, `sspi`, `ldap`, `radius`, `cert`, `pam`.
        :param pulumi.Input[int] priority_id: The priority of an AD domain. If you set this parameter to 0, the AD domain has the highest priority. Valid values: 0 to 10000. This parameter is used to identify each AD domain. When you add an AD domain, the value of the PriorityId parameter of the new AD domain cannot be the same as the value of the PriorityId parameter for any existing AD domain. When you modify or delete an AD domain, you must also modify or delete the value of the PriorityId parameter for this AD domain.
        :param pulumi.Input[str] type: The type of connection to the instance. Valid values:
               * **host**: specifies to verify TCP/IP connections, including SSL connections and non-SSL connections.
               * **hostssl**: specifies to verify only TCP/IP connections that are established over SSL connections.
               * **hostnossl**: specifies to verify only TCP/IP connections that are established over non-SSL connections.
        :param pulumi.Input[str] user: The user that is allowed to access the instance. If you specify multiple users, separate the usernames with commas (,).
        :param pulumi.Input[str] mask: The mask of the instance. If the value of the `Address` parameter is an IP address, you can use this parameter to specify the mask of the IP address.
        :param pulumi.Input[str] option: Optional. The value of this parameter is based on the value of the HbaItem.N.Method parameter. In this topic, LDAP is used as an example. You must configure this parameter. For more information, see [Authentication Methods](https://www.postgresql.org/docs/11/auth-methods.html).
        """
        pulumi.set(__self__, "address", address)
        pulumi.set(__self__, "database", database)
        pulumi.set(__self__, "method", method)
        pulumi.set(__self__, "priority_id", priority_id)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "user", user)
        if mask is not None:
            pulumi.set(__self__, "mask", mask)
        if option is not None:
            pulumi.set(__self__, "option", option)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Input[str]:
        """
        The IP addresses from which the specified users can access the specified databases. If you set this parameter to 0.0.0.0/0, the specified users are allowed to access the specified databases from all IP addresses.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: pulumi.Input[str]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Input[str]:
        """
        The name of the database that the specified users are allowed to access. If you set this parameter to all, the specified users are allowed to access all databases in the instance. If you specify multiple databases, separate the database names with commas (,).
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: pulumi.Input[str]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def method(self) -> pulumi.Input[str]:
        """
        The authentication method of Lightweight Directory Access Protocol (LDAP). Valid values: `trust`, `reject`, `scram-sha-256`, `md5`, `password`, `gss`, `sspi`, `ldap`, `radius`, `cert`, `pam`.
        """
        return pulumi.get(self, "method")

    @method.setter
    def method(self, value: pulumi.Input[str]):
        pulumi.set(self, "method", value)

    @property
    @pulumi.getter(name="priorityId")
    def priority_id(self) -> pulumi.Input[int]:
        """
        The priority of an AD domain. If you set this parameter to 0, the AD domain has the highest priority. Valid values: 0 to 10000. This parameter is used to identify each AD domain. When you add an AD domain, the value of the PriorityId parameter of the new AD domain cannot be the same as the value of the PriorityId parameter for any existing AD domain. When you modify or delete an AD domain, you must also modify or delete the value of the PriorityId parameter for this AD domain.
        """
        return pulumi.get(self, "priority_id")

    @priority_id.setter
    def priority_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "priority_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of connection to the instance. Valid values:
        * **host**: specifies to verify TCP/IP connections, including SSL connections and non-SSL connections.
        * **hostssl**: specifies to verify only TCP/IP connections that are established over SSL connections.
        * **hostnossl**: specifies to verify only TCP/IP connections that are established over non-SSL connections.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def user(self) -> pulumi.Input[str]:
        """
        The user that is allowed to access the instance. If you specify multiple users, separate the usernames with commas (,).
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: pulumi.Input[str]):
        pulumi.set(self, "user", value)

    @property
    @pulumi.getter
    def mask(self) -> Optional[pulumi.Input[str]]:
        """
        The mask of the instance. If the value of the `Address` parameter is an IP address, you can use this parameter to specify the mask of the IP address.
        """
        return pulumi.get(self, "mask")

    @mask.setter
    def mask(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mask", value)

    @property
    @pulumi.getter
    def option(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The value of this parameter is based on the value of the HbaItem.N.Method parameter. In this topic, LDAP is used as an example. You must configure this parameter. For more information, see [Authentication Methods](https://www.postgresql.org/docs/11/auth-methods.html).
        """
        return pulumi.get(self, "option")

    @option.setter
    def option(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "option", value)


@pulumi.input_type
class ReadOnlyInstanceParameterArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


