# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AuditLogConfigLogType',
    'RestoreConfigClusterResourceConflictPolicy',
    'RestoreConfigNamespacedResourceRestoreMode',
    'RestoreConfigVolumeDataRestorePolicy',
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


class RestoreConfigClusterResourceConflictPolicy(str, Enum):
    """
    Defines the behavior for handling the situation where cluster-scoped resources being restored already exist in the target cluster. This MUST be set to a value other than CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED if cluster_resource_restore_scope is not empty.
    """
    CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED = "CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED"
    """
    Unspecified. Only allowed if no cluster-scoped resources will be restored.
    """
    USE_EXISTING_VERSION = "USE_EXISTING_VERSION"
    """
    Do not attempt to restore the conflicting resource.
    """
    USE_BACKUP_VERSION = "USE_BACKUP_VERSION"
    """
    Delete the existing version before re-creating it from the Backup. Note that this is a dangerous option which could cause unintentional data loss if used inappropriately - for example, deleting a CRD will cause Kubernetes to delete all CRs of that type.
    """


class RestoreConfigNamespacedResourceRestoreMode(str, Enum):
    """
    Defines the behavior for handling the situation where sets of namespaced resources being restored already exist in the target cluster. This MUST be set to a value other than NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED.
    """
    NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED = "NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED"
    """
    Unspecified (invalid).
    """
    DELETE_AND_RESTORE = "DELETE_AND_RESTORE"
    """
    When conflicting top-level resources (either Namespaces or ProtectedApplications, depending upon the scope) are encountered, this will first trigger a delete of the conflicting resource AND ALL OF ITS REFERENCED RESOURCES (e.g., all resources in the Namespace or all resources referenced by the ProtectedApplication) before restoring the resources from the Backup. This mode should only be used when you are intending to revert some portion of a cluster to an earlier state.
    """
    FAIL_ON_CONFLICT = "FAIL_ON_CONFLICT"
    """
    If conflicting top-level resources (either Namespaces or ProtectedApplications, depending upon the scope) are encountered at the beginning of a restore process, the Restore will fail. If a conflict occurs during the restore process itself (e.g., because an out of band process creates conflicting resources), a conflict will be reported.
    """


class RestoreConfigVolumeDataRestorePolicy(str, Enum):
    """
    Specifies the mechanism to be used to restore volume data. Default: VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED (will be treated as NO_VOLUME_DATA_RESTORATION).
    """
    VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED = "VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED"
    """
    Unspecified (illegal).
    """
    RESTORE_VOLUME_DATA_FROM_BACKUP = "RESTORE_VOLUME_DATA_FROM_BACKUP"
    """
    For each PVC to be restored, will create a new underlying volume (and PV) from the corresponding VolumeBackup contained within the Backup.
    """
    REUSE_VOLUME_HANDLE_FROM_BACKUP = "REUSE_VOLUME_HANDLE_FROM_BACKUP"
    """
    For each PVC to be restored, attempt to reuse the original PV contained in the Backup (with its original underlying volume). Note that option is likely only usable when restoring a workload to its original cluster.
    """
    NO_VOLUME_DATA_RESTORATION = "NO_VOLUME_DATA_RESTORATION"
    """
    For each PVC to be restored, PVCs will be created without any particular action to restore data. In this case, the normal Kubernetes provisioning logic would kick in, and this would likely result in either dynamically provisioning blank PVs or binding to statically provisioned PVs.
    """
