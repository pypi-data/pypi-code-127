# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AcceleratorAcceleratorType',
    'AuditLogConfigLogType',
    'InstanceType',
    'VersionType',
]


class AcceleratorAcceleratorType(str, Enum):
    """
    The type of an accelator for a CDF instance.
    """
    ACCELERATOR_TYPE_UNSPECIFIED = "ACCELERATOR_TYPE_UNSPECIFIED"
    """
    Default value, if unspecified.
    """
    CDC = "CDC"
    """
    Change Data Capture accelerator for CDF.
    """
    HEALTHCARE = "HEALTHCARE"
    """
    Cloud Healthcare accelerator for CDF. This accelerator is to enable Cloud Healthcare specific CDF plugins developed by Healthcare team.
    """


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


class InstanceType(str, Enum):
    """
    Required. Instance type.
    """
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    """
    No type specified. The instance creation will fail.
    """
    BASIC = "BASIC"
    """
    Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines using point and click UI. However, there are certain limitations, such as fewer number of concurrent pipelines, no support for streaming pipelines, etc.
    """
    ENTERPRISE = "ENTERPRISE"
    """
    Enterprise Data Fusion instance. In Enterprise type, the user will have all features available, such as support for streaming pipelines, unlimited number of concurrent pipelines, etc.
    """
    DEVELOPER = "DEVELOPER"
    """
    Developer Data Fusion instance. In Developer type, the user will have all features available but with restrictive capabilities. This is to help enterprises design and develop their data ingestion and integration pipelines at low cost.
    """


class VersionType(str, Enum):
    """
    Type represents the release availability of the version
    """
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    """
    Version does not have availability yet
    """
    TYPE_PREVIEW = "TYPE_PREVIEW"
    """
    Version is under development and not considered stable
    """
    TYPE_GENERAL_AVAILABILITY = "TYPE_GENERAL_AVAILABILITY"
    """
    Version is available for public use
    """
