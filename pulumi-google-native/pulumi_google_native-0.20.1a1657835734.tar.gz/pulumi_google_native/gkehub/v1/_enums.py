# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AuditLogConfigLogType',
    'OnPremClusterClusterType',
]


class AuditLogConfigLogType(str, Enum):
    """
    The log type that this config enables.
    """
    LOG_TYPE_UNSPECIFIED = "LOG_TYPE_UNSPECIFIED"
    """
    Default case. Should never be this.
    """
    ADMIN_READ = "ADMIN_READ"
    """
    Admin reads. Example: CloudIAM getIamPolicy
    """
    DATA_WRITE = "DATA_WRITE"
    """
    Data writes. Example: CloudSQL Users create
    """
    DATA_READ = "DATA_READ"
    """
    Data reads. Example: CloudSQL Users list
    """


class OnPremClusterClusterType(str, Enum):
    """
    Immutable. The on prem cluster's type.
    """
    CLUSTERTYPE_UNSPECIFIED = "CLUSTERTYPE_UNSPECIFIED"
    """
    The ClusterType is not set.
    """
    BOOTSTRAP = "BOOTSTRAP"
    """
    The ClusterType is bootstrap cluster.
    """
    HYBRID = "HYBRID"
    """
    The ClusterType is baremetal hybrid cluster.
    """
    STANDALONE = "STANDALONE"
    """
    The ClusterType is baremetal standalone cluster.
    """
    USER = "USER"
    """
    The ClusterType is user cluster.
    """
