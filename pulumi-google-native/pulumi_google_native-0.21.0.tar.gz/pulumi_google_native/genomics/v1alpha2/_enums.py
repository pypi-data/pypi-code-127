# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DiskType',
]


class DiskType(str, Enum):
    """
    Required. The type of the disk to create.
    """
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    """
    Default disk type. Use one of the other options below.
    """
    PERSISTENT_HDD = "PERSISTENT_HDD"
    """
    Specifies a Google Compute Engine persistent hard disk. See https://cloud.google.com/compute/docs/disks/#pdspecs for details.
    """
    PERSISTENT_SSD = "PERSISTENT_SSD"
    """
    Specifies a Google Compute Engine persistent solid-state disk. See https://cloud.google.com/compute/docs/disks/#pdspecs for details.
    """
    LOCAL_SSD = "LOCAL_SSD"
    """
    Specifies a Google Compute Engine local SSD. See https://cloud.google.com/compute/docs/disks/local-ssd for details.
    """
