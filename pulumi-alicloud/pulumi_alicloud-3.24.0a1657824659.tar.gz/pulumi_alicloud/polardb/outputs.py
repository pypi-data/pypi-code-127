# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'ClusterDbClusterIpArray',
    'ClusterParameter',
    'GetAccountsAccountResult',
    'GetAccountsAccountDatabasePrivilegeResult',
    'GetClustersClusterResult',
    'GetClustersClusterDbNodeResult',
    'GetDatabasesDatabaseResult',
    'GetDatabasesDatabaseAccountResult',
    'GetEndpointsEndpointResult',
    'GetEndpointsEndpointAddressItemResult',
    'GetNodeClassesClassResult',
    'GetNodeClassesClassSupportedEngineResult',
    'GetNodeClassesClassSupportedEngineAvailableResourceResult',
    'GetZonesZoneResult',
]

@pulumi.output_type
class ClusterDbClusterIpArray(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dbClusterIpArrayName":
            suggest = "db_cluster_ip_array_name"
        elif key == "modifyMode":
            suggest = "modify_mode"
        elif key == "securityIps":
            suggest = "security_ips"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterDbClusterIpArray. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterDbClusterIpArray.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterDbClusterIpArray.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 db_cluster_ip_array_name: Optional[str] = None,
                 modify_mode: Optional[str] = None,
                 security_ips: Optional[Sequence[str]] = None):
        """
        :param str db_cluster_ip_array_name: The name of the IP whitelist group. The group name must be 2 to 120 characters in length and consists of lowercase letters and digits. It must start with a letter, and end with a letter or a digit.
               **NOTE:** If the specified whitelist group name does not exist, the whitelist group is created. If the specified whitelist group name exists, the whitelist group is modified. If you do not specify this parameter, the default group is modified. You can create a maximum of 50 IP whitelist groups for a cluster.
        :param str modify_mode: The method for modifying the IP whitelist. Valid values are `Cover`, `Append`, `Delete`.
               **NOTE:** There does not recommend setting modify_mode to `Append` or `Delete` and it will bring a potential diff error.
        :param Sequence[str] security_ips: List of IP addresses allowed to access all databases of a cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
        """
        if db_cluster_ip_array_name is not None:
            pulumi.set(__self__, "db_cluster_ip_array_name", db_cluster_ip_array_name)
        if modify_mode is not None:
            pulumi.set(__self__, "modify_mode", modify_mode)
        if security_ips is not None:
            pulumi.set(__self__, "security_ips", security_ips)

    @property
    @pulumi.getter(name="dbClusterIpArrayName")
    def db_cluster_ip_array_name(self) -> Optional[str]:
        """
        The name of the IP whitelist group. The group name must be 2 to 120 characters in length and consists of lowercase letters and digits. It must start with a letter, and end with a letter or a digit.
        **NOTE:** If the specified whitelist group name does not exist, the whitelist group is created. If the specified whitelist group name exists, the whitelist group is modified. If you do not specify this parameter, the default group is modified. You can create a maximum of 50 IP whitelist groups for a cluster.
        """
        return pulumi.get(self, "db_cluster_ip_array_name")

    @property
    @pulumi.getter(name="modifyMode")
    def modify_mode(self) -> Optional[str]:
        """
        The method for modifying the IP whitelist. Valid values are `Cover`, `Append`, `Delete`.
        **NOTE:** There does not recommend setting modify_mode to `Append` or `Delete` and it will bring a potential diff error.
        """
        return pulumi.get(self, "modify_mode")

    @property
    @pulumi.getter(name="securityIps")
    def security_ips(self) -> Optional[Sequence[str]]:
        """
        List of IP addresses allowed to access all databases of a cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
        """
        return pulumi.get(self, "security_ips")


@pulumi.output_type
class ClusterParameter(dict):
    def __init__(__self__, *,
                 name: str,
                 value: str):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class GetAccountsAccountResult(dict):
    def __init__(__self__, *,
                 account_description: str,
                 account_lock_state: str,
                 account_name: str,
                 account_status: str,
                 account_type: str,
                 database_privileges: Sequence['outputs.GetAccountsAccountDatabasePrivilegeResult']):
        """
        :param str account_description: Account description.
        :param str account_lock_state: Account lock state, Valid values are `Lock`, `UnLock`.
        :param str account_name: Account name.
        :param str account_status: Cluster address type.`Cluster`: the default address of the Cluster.`Primary`: Primary address.`Custom`: Custom cluster addresses.
        :param str account_type: Account type, Valid values are `Normal`, `Super`.
        :param Sequence['GetAccountsAccountDatabasePrivilegeArgs'] database_privileges: A list of database privilege. Each element contains the following attributes.
        """
        pulumi.set(__self__, "account_description", account_description)
        pulumi.set(__self__, "account_lock_state", account_lock_state)
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "account_status", account_status)
        pulumi.set(__self__, "account_type", account_type)
        pulumi.set(__self__, "database_privileges", database_privileges)

    @property
    @pulumi.getter(name="accountDescription")
    def account_description(self) -> str:
        """
        Account description.
        """
        return pulumi.get(self, "account_description")

    @property
    @pulumi.getter(name="accountLockState")
    def account_lock_state(self) -> str:
        """
        Account lock state, Valid values are `Lock`, `UnLock`.
        """
        return pulumi.get(self, "account_lock_state")

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> str:
        """
        Account name.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="accountStatus")
    def account_status(self) -> str:
        """
        Cluster address type.`Cluster`: the default address of the Cluster.`Primary`: Primary address.`Custom`: Custom cluster addresses.
        """
        return pulumi.get(self, "account_status")

    @property
    @pulumi.getter(name="accountType")
    def account_type(self) -> str:
        """
        Account type, Valid values are `Normal`, `Super`.
        """
        return pulumi.get(self, "account_type")

    @property
    @pulumi.getter(name="databasePrivileges")
    def database_privileges(self) -> Sequence['outputs.GetAccountsAccountDatabasePrivilegeResult']:
        """
        A list of database privilege. Each element contains the following attributes.
        """
        return pulumi.get(self, "database_privileges")


@pulumi.output_type
class GetAccountsAccountDatabasePrivilegeResult(dict):
    def __init__(__self__, *,
                 account_privilege: str,
                 db_name: str):
        """
        :param str account_privilege: Account privilege of database
        :param str db_name: The account owned database name
        """
        pulumi.set(__self__, "account_privilege", account_privilege)
        pulumi.set(__self__, "db_name", db_name)

    @property
    @pulumi.getter(name="accountPrivilege")
    def account_privilege(self) -> str:
        """
        Account privilege of database
        """
        return pulumi.get(self, "account_privilege")

    @property
    @pulumi.getter(name="dbName")
    def db_name(self) -> str:
        """
        The account owned database name
        """
        return pulumi.get(self, "db_name")


@pulumi.output_type
class GetClustersClusterResult(dict):
    def __init__(__self__, *,
                 charge_type: str,
                 create_time: str,
                 db_node_class: str,
                 db_node_number: int,
                 db_nodes: Sequence['outputs.GetClustersClusterDbNodeResult'],
                 db_type: str,
                 db_version: str,
                 delete_lock: int,
                 description: str,
                 engine: str,
                 expire_time: str,
                 expired: str,
                 id: str,
                 lock_mode: str,
                 network_type: str,
                 region_id: str,
                 status: str,
                 storage_used: int,
                 vpc_id: str,
                 zone_id: str):
        """
        :param str charge_type: Billing method. Value options: `PostPaid` for Pay-As-You-Go and `PrePaid` for subscription.
        :param str create_time: The create_time of the db_nodes.
        :param str db_node_class: The db_node_class of the db_nodes.
        :param int db_node_number: The DBNodeNumber of the PolarDB cluster.
        :param Sequence['GetClustersClusterDbNodeArgs'] db_nodes: The DBNodes of the PolarDB cluster.
        :param str db_type: Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
        :param str db_version: The DBVersion of the PolarDB cluster.
        :param int delete_lock: The DeleteLock of the PolarDB cluster.
        :param str description: The description of the PolarDB cluster.
        :param str engine: Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
        :param str expire_time: Expiration time. Pay-As-You-Go clusters never expire.
        :param str expired: The expired of the PolarDB cluster.
        :param str id: The ID of the PolarDB cluster.
        :param str lock_mode: The LockMode of the PolarDB cluster.
        :param str network_type: The DBClusterNetworkType of the PolarDB cluster.
        :param str region_id: The region_id of the db_nodes.
        :param str status: status of the cluster.
        :param int storage_used: The StorageUsed of the PolarDB cluster.
        :param str vpc_id: ID of the VPC the cluster belongs to.
        :param str zone_id: The zone_id of the db_nodes.
        """
        pulumi.set(__self__, "charge_type", charge_type)
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "db_node_class", db_node_class)
        pulumi.set(__self__, "db_node_number", db_node_number)
        pulumi.set(__self__, "db_nodes", db_nodes)
        pulumi.set(__self__, "db_type", db_type)
        pulumi.set(__self__, "db_version", db_version)
        pulumi.set(__self__, "delete_lock", delete_lock)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "engine", engine)
        pulumi.set(__self__, "expire_time", expire_time)
        pulumi.set(__self__, "expired", expired)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "lock_mode", lock_mode)
        pulumi.set(__self__, "network_type", network_type)
        pulumi.set(__self__, "region_id", region_id)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "storage_used", storage_used)
        pulumi.set(__self__, "vpc_id", vpc_id)
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> str:
        """
        Billing method. Value options: `PostPaid` for Pay-As-You-Go and `PrePaid` for subscription.
        """
        return pulumi.get(self, "charge_type")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The create_time of the db_nodes.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dbNodeClass")
    def db_node_class(self) -> str:
        """
        The db_node_class of the db_nodes.
        """
        return pulumi.get(self, "db_node_class")

    @property
    @pulumi.getter(name="dbNodeNumber")
    def db_node_number(self) -> int:
        """
        The DBNodeNumber of the PolarDB cluster.
        """
        return pulumi.get(self, "db_node_number")

    @property
    @pulumi.getter(name="dbNodes")
    def db_nodes(self) -> Sequence['outputs.GetClustersClusterDbNodeResult']:
        """
        The DBNodes of the PolarDB cluster.
        """
        return pulumi.get(self, "db_nodes")

    @property
    @pulumi.getter(name="dbType")
    def db_type(self) -> str:
        """
        Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
        """
        return pulumi.get(self, "db_type")

    @property
    @pulumi.getter(name="dbVersion")
    def db_version(self) -> str:
        """
        The DBVersion of the PolarDB cluster.
        """
        return pulumi.get(self, "db_version")

    @property
    @pulumi.getter(name="deleteLock")
    def delete_lock(self) -> int:
        """
        The DeleteLock of the PolarDB cluster.
        """
        return pulumi.get(self, "delete_lock")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the PolarDB cluster.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def engine(self) -> str:
        """
        Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> str:
        """
        Expiration time. Pay-As-You-Go clusters never expire.
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter
    def expired(self) -> str:
        """
        The expired of the PolarDB cluster.
        """
        return pulumi.get(self, "expired")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the PolarDB cluster.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lockMode")
    def lock_mode(self) -> str:
        """
        The LockMode of the PolarDB cluster.
        """
        return pulumi.get(self, "lock_mode")

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> str:
        """
        The DBClusterNetworkType of the PolarDB cluster.
        """
        return pulumi.get(self, "network_type")

    @property
    @pulumi.getter(name="regionId")
    def region_id(self) -> str:
        """
        The region_id of the db_nodes.
        """
        return pulumi.get(self, "region_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        status of the cluster.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageUsed")
    def storage_used(self) -> int:
        """
        The StorageUsed of the PolarDB cluster.
        """
        return pulumi.get(self, "storage_used")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        ID of the VPC the cluster belongs to.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        """
        The zone_id of the db_nodes.
        """
        return pulumi.get(self, "zone_id")


@pulumi.output_type
class GetClustersClusterDbNodeResult(dict):
    def __init__(__self__, *,
                 create_time: str,
                 db_node_class: str,
                 db_node_id: str,
                 db_node_role: str,
                 db_node_status: str,
                 max_connections: int,
                 max_iops: int,
                 region_id: str,
                 zone_id: str):
        """
        :param str create_time: The create_time of the db_nodes.
        :param str db_node_class: The db_node_class of the db_nodes.
        :param str db_node_id: The db_node_id of the db_nodes.
        :param str db_node_role: The db_node_role of the db_nodes.
        :param str db_node_status: The db_node_status of the db_nodes.
        :param int max_connections: The max_connections of the db_nodes.
        :param int max_iops: The max_iops of the db_nodes.
        :param str region_id: The region_id of the db_nodes.
        :param str zone_id: The zone_id of the db_nodes.
        """
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "db_node_class", db_node_class)
        pulumi.set(__self__, "db_node_id", db_node_id)
        pulumi.set(__self__, "db_node_role", db_node_role)
        pulumi.set(__self__, "db_node_status", db_node_status)
        pulumi.set(__self__, "max_connections", max_connections)
        pulumi.set(__self__, "max_iops", max_iops)
        pulumi.set(__self__, "region_id", region_id)
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The create_time of the db_nodes.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dbNodeClass")
    def db_node_class(self) -> str:
        """
        The db_node_class of the db_nodes.
        """
        return pulumi.get(self, "db_node_class")

    @property
    @pulumi.getter(name="dbNodeId")
    def db_node_id(self) -> str:
        """
        The db_node_id of the db_nodes.
        """
        return pulumi.get(self, "db_node_id")

    @property
    @pulumi.getter(name="dbNodeRole")
    def db_node_role(self) -> str:
        """
        The db_node_role of the db_nodes.
        """
        return pulumi.get(self, "db_node_role")

    @property
    @pulumi.getter(name="dbNodeStatus")
    def db_node_status(self) -> str:
        """
        The db_node_status of the db_nodes.
        """
        return pulumi.get(self, "db_node_status")

    @property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> int:
        """
        The max_connections of the db_nodes.
        """
        return pulumi.get(self, "max_connections")

    @property
    @pulumi.getter(name="maxIops")
    def max_iops(self) -> int:
        """
        The max_iops of the db_nodes.
        """
        return pulumi.get(self, "max_iops")

    @property
    @pulumi.getter(name="regionId")
    def region_id(self) -> str:
        """
        The region_id of the db_nodes.
        """
        return pulumi.get(self, "region_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        """
        The zone_id of the db_nodes.
        """
        return pulumi.get(self, "zone_id")


@pulumi.output_type
class GetDatabasesDatabaseResult(dict):
    def __init__(__self__, *,
                 accounts: Sequence['outputs.GetDatabasesDatabaseAccountResult'],
                 character_set_name: str,
                 db_description: str,
                 db_name: str,
                 db_status: str,
                 engine: str):
        """
        :param Sequence['GetDatabasesDatabaseAccountArgs'] accounts: A list of accounts of database. Each element contains the following attributes.
        :param str character_set_name: The character set name of database.
        :param str db_description: Database description.
        :param str db_name: Database name.
        :param str db_status: The status of database.
        :param str engine: The engine of database.
        """
        pulumi.set(__self__, "accounts", accounts)
        pulumi.set(__self__, "character_set_name", character_set_name)
        pulumi.set(__self__, "db_description", db_description)
        pulumi.set(__self__, "db_name", db_name)
        pulumi.set(__self__, "db_status", db_status)
        pulumi.set(__self__, "engine", engine)

    @property
    @pulumi.getter
    def accounts(self) -> Sequence['outputs.GetDatabasesDatabaseAccountResult']:
        """
        A list of accounts of database. Each element contains the following attributes.
        """
        return pulumi.get(self, "accounts")

    @property
    @pulumi.getter(name="characterSetName")
    def character_set_name(self) -> str:
        """
        The character set name of database.
        """
        return pulumi.get(self, "character_set_name")

    @property
    @pulumi.getter(name="dbDescription")
    def db_description(self) -> str:
        """
        Database description.
        """
        return pulumi.get(self, "db_description")

    @property
    @pulumi.getter(name="dbName")
    def db_name(self) -> str:
        """
        Database name.
        """
        return pulumi.get(self, "db_name")

    @property
    @pulumi.getter(name="dbStatus")
    def db_status(self) -> str:
        """
        The status of database.
        """
        return pulumi.get(self, "db_status")

    @property
    @pulumi.getter
    def engine(self) -> str:
        """
        The engine of database.
        """
        return pulumi.get(self, "engine")


@pulumi.output_type
class GetDatabasesDatabaseAccountResult(dict):
    def __init__(__self__, *,
                 account_name: str,
                 account_status: str,
                 privilege_status: str):
        """
        :param str account_name: Account name.
        :param str account_status: Account status.
        :param str privilege_status: The privilege status of account.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "account_status", account_status)
        pulumi.set(__self__, "privilege_status", privilege_status)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> str:
        """
        Account name.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="accountStatus")
    def account_status(self) -> str:
        """
        Account status.
        """
        return pulumi.get(self, "account_status")

    @property
    @pulumi.getter(name="privilegeStatus")
    def privilege_status(self) -> str:
        """
        The privilege status of account.
        """
        return pulumi.get(self, "privilege_status")


@pulumi.output_type
class GetEndpointsEndpointResult(dict):
    def __init__(__self__, *,
                 address_items: Sequence['outputs.GetEndpointsEndpointAddressItemResult'],
                 auto_add_new_nodes: str,
                 db_endpoint_id: str,
                 endpoint_config: str,
                 endpoint_type: str,
                 nodes: str,
                 read_write_mode: str):
        """
        :param Sequence['GetEndpointsEndpointAddressItemArgs'] address_items: A list of endpoint addresses. Each element contains the following attributes.
        :param str auto_add_new_nodes: Whether the new node is automatically added to the default cluster address.Options are `Enable` and `Disable`.
        :param str db_endpoint_id: endpoint of the cluster.
        :param str endpoint_config: The Endpoint configuration. `ConsistLevel`: session consistency level, value:`0`: final consistency,`1`: session consistency;`LoadBalanceStrategy`: load balancing strategy. Based on the automatic scheduling of load, the value is: `load`.
        :param str endpoint_type: Cluster address type.`Cluster`: the default address of the Cluster.`Primary`: Primary address.`Custom`: Custom cluster addresses.
        :param str nodes: A list of nodes that connect to the address configuration.
        :param str read_write_mode: Read-write mode:`ReadWrite`: readable and writable (automatic read-write separation).`ReadOnly`: ReadOnly.
        """
        pulumi.set(__self__, "address_items", address_items)
        pulumi.set(__self__, "auto_add_new_nodes", auto_add_new_nodes)
        pulumi.set(__self__, "db_endpoint_id", db_endpoint_id)
        pulumi.set(__self__, "endpoint_config", endpoint_config)
        pulumi.set(__self__, "endpoint_type", endpoint_type)
        pulumi.set(__self__, "nodes", nodes)
        pulumi.set(__self__, "read_write_mode", read_write_mode)

    @property
    @pulumi.getter(name="addressItems")
    def address_items(self) -> Sequence['outputs.GetEndpointsEndpointAddressItemResult']:
        """
        A list of endpoint addresses. Each element contains the following attributes.
        """
        return pulumi.get(self, "address_items")

    @property
    @pulumi.getter(name="autoAddNewNodes")
    def auto_add_new_nodes(self) -> str:
        """
        Whether the new node is automatically added to the default cluster address.Options are `Enable` and `Disable`.
        """
        return pulumi.get(self, "auto_add_new_nodes")

    @property
    @pulumi.getter(name="dbEndpointId")
    def db_endpoint_id(self) -> str:
        """
        endpoint of the cluster.
        """
        return pulumi.get(self, "db_endpoint_id")

    @property
    @pulumi.getter(name="endpointConfig")
    def endpoint_config(self) -> str:
        """
        The Endpoint configuration. `ConsistLevel`: session consistency level, value:`0`: final consistency,`1`: session consistency;`LoadBalanceStrategy`: load balancing strategy. Based on the automatic scheduling of load, the value is: `load`.
        """
        return pulumi.get(self, "endpoint_config")

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> str:
        """
        Cluster address type.`Cluster`: the default address of the Cluster.`Primary`: Primary address.`Custom`: Custom cluster addresses.
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter
    def nodes(self) -> str:
        """
        A list of nodes that connect to the address configuration.
        """
        return pulumi.get(self, "nodes")

    @property
    @pulumi.getter(name="readWriteMode")
    def read_write_mode(self) -> str:
        """
        Read-write mode:`ReadWrite`: readable and writable (automatic read-write separation).`ReadOnly`: ReadOnly.
        """
        return pulumi.get(self, "read_write_mode")


@pulumi.output_type
class GetEndpointsEndpointAddressItemResult(dict):
    def __init__(__self__, *,
                 connection_string: str,
                 ip_address: str,
                 net_type: str,
                 port: str,
                 vpc_id: str,
                 vswitch_id: str):
        """
        :param str connection_string: Connection instance string.
        :param str ip_address: The ip address of connection string.
        :param str net_type: IP network type:`Public` or `Private`.
        :param str port: Intranet connection port.
        :param str vpc_id: ID of the VPC the instance belongs to.
        :param str vswitch_id: ID of the VSwitch the cluster belongs to.
        """
        pulumi.set(__self__, "connection_string", connection_string)
        pulumi.set(__self__, "ip_address", ip_address)
        pulumi.set(__self__, "net_type", net_type)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "vpc_id", vpc_id)
        pulumi.set(__self__, "vswitch_id", vswitch_id)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> str:
        """
        Connection instance string.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        The ip address of connection string.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="netType")
    def net_type(self) -> str:
        """
        IP network type:`Public` or `Private`.
        """
        return pulumi.get(self, "net_type")

    @property
    @pulumi.getter
    def port(self) -> str:
        """
        Intranet connection port.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        ID of the VPC the instance belongs to.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> str:
        """
        ID of the VSwitch the cluster belongs to.
        """
        return pulumi.get(self, "vswitch_id")


@pulumi.output_type
class GetNodeClassesClassResult(dict):
    def __init__(__self__, *,
                 supported_engines: Sequence['outputs.GetNodeClassesClassSupportedEngineResult'],
                 zone_id: str):
        """
        :param Sequence['GetNodeClassesClassSupportedEngineArgs'] supported_engines: A list of PolarDB node classes in the zone.
        :param str zone_id: The Zone to launch the PolarDB cluster.
        """
        pulumi.set(__self__, "supported_engines", supported_engines)
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="supportedEngines")
    def supported_engines(self) -> Sequence['outputs.GetNodeClassesClassSupportedEngineResult']:
        """
        A list of PolarDB node classes in the zone.
        """
        return pulumi.get(self, "supported_engines")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        """
        The Zone to launch the PolarDB cluster.
        """
        return pulumi.get(self, "zone_id")


@pulumi.output_type
class GetNodeClassesClassSupportedEngineResult(dict):
    def __init__(__self__, *,
                 available_resources: Sequence['outputs.GetNodeClassesClassSupportedEngineAvailableResourceResult'],
                 engine: str):
        """
        :param Sequence['GetNodeClassesClassSupportedEngineAvailableResourceArgs'] available_resources: A list of PolarDB node available classes.
        :param str engine: In the zone, the database type supports classes in the following available_resources.
        """
        pulumi.set(__self__, "available_resources", available_resources)
        pulumi.set(__self__, "engine", engine)

    @property
    @pulumi.getter(name="availableResources")
    def available_resources(self) -> Sequence['outputs.GetNodeClassesClassSupportedEngineAvailableResourceResult']:
        """
        A list of PolarDB node available classes.
        """
        return pulumi.get(self, "available_resources")

    @property
    @pulumi.getter
    def engine(self) -> str:
        """
        In the zone, the database type supports classes in the following available_resources.
        """
        return pulumi.get(self, "engine")


@pulumi.output_type
class GetNodeClassesClassSupportedEngineAvailableResourceResult(dict):
    def __init__(__self__, *,
                 db_node_class: str):
        """
        :param str db_node_class: The PolarDB node class type by the user.
        """
        pulumi.set(__self__, "db_node_class", db_node_class)

    @property
    @pulumi.getter(name="dbNodeClass")
    def db_node_class(self) -> str:
        """
        The PolarDB node class type by the user.
        """
        return pulumi.get(self, "db_node_class")


@pulumi.output_type
class GetZonesZoneResult(dict):
    def __init__(__self__, *,
                 id: str,
                 multi_zone_ids: Sequence[str]):
        """
        :param str id: ID of the zone.
        :param Sequence[str] multi_zone_ids: A list of zone ids in which the multi zone.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "multi_zone_ids", multi_zone_ids)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ID of the zone.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="multiZoneIds")
    def multi_zone_ids(self) -> Sequence[str]:
        """
        A list of zone ids in which the multi zone.
        """
        return pulumi.get(self, "multi_zone_ids")


