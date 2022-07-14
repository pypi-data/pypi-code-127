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

__all__ = ['FileSystemArgs', 'FileSystem']

@pulumi.input_type
class FileSystemArgs:
    def __init__(__self__, *,
                 file_system_type: pulumi.Input[str],
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 backup_id: Optional[pulumi.Input[str]] = None,
                 file_system_type_version: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 lustre_configuration: Optional[pulumi.Input['FileSystemLustreConfigurationArgs']] = None,
                 ontap_configuration: Optional[pulumi.Input['FileSystemOntapConfigurationArgs']] = None,
                 open_zfs_configuration: Optional[pulumi.Input['FileSystemOpenZFSConfigurationArgs']] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 storage_capacity: Optional[pulumi.Input[int]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['FileSystemTagArgs']]]] = None,
                 windows_configuration: Optional[pulumi.Input['FileSystemWindowsConfigurationArgs']] = None):
        """
        The set of arguments for constructing a FileSystem resource.
        """
        pulumi.set(__self__, "file_system_type", file_system_type)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if backup_id is not None:
            pulumi.set(__self__, "backup_id", backup_id)
        if file_system_type_version is not None:
            pulumi.set(__self__, "file_system_type_version", file_system_type_version)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if lustre_configuration is not None:
            pulumi.set(__self__, "lustre_configuration", lustre_configuration)
        if ontap_configuration is not None:
            pulumi.set(__self__, "ontap_configuration", ontap_configuration)
        if open_zfs_configuration is not None:
            pulumi.set(__self__, "open_zfs_configuration", open_zfs_configuration)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if storage_capacity is not None:
            pulumi.set(__self__, "storage_capacity", storage_capacity)
        if storage_type is not None:
            pulumi.set(__self__, "storage_type", storage_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if windows_configuration is not None:
            pulumi.set(__self__, "windows_configuration", windows_configuration)

    @property
    @pulumi.getter(name="fileSystemType")
    def file_system_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "file_system_type")

    @file_system_type.setter
    def file_system_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "file_system_type", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "backup_id")

    @backup_id.setter
    def backup_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backup_id", value)

    @property
    @pulumi.getter(name="fileSystemTypeVersion")
    def file_system_type_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "file_system_type_version")

    @file_system_type_version.setter
    def file_system_type_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_system_type_version", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="lustreConfiguration")
    def lustre_configuration(self) -> Optional[pulumi.Input['FileSystemLustreConfigurationArgs']]:
        return pulumi.get(self, "lustre_configuration")

    @lustre_configuration.setter
    def lustre_configuration(self, value: Optional[pulumi.Input['FileSystemLustreConfigurationArgs']]):
        pulumi.set(self, "lustre_configuration", value)

    @property
    @pulumi.getter(name="ontapConfiguration")
    def ontap_configuration(self) -> Optional[pulumi.Input['FileSystemOntapConfigurationArgs']]:
        return pulumi.get(self, "ontap_configuration")

    @ontap_configuration.setter
    def ontap_configuration(self, value: Optional[pulumi.Input['FileSystemOntapConfigurationArgs']]):
        pulumi.set(self, "ontap_configuration", value)

    @property
    @pulumi.getter(name="openZFSConfiguration")
    def open_zfs_configuration(self) -> Optional[pulumi.Input['FileSystemOpenZFSConfigurationArgs']]:
        return pulumi.get(self, "open_zfs_configuration")

    @open_zfs_configuration.setter
    def open_zfs_configuration(self, value: Optional[pulumi.Input['FileSystemOpenZFSConfigurationArgs']]):
        pulumi.set(self, "open_zfs_configuration", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "storage_capacity")

    @storage_capacity.setter
    def storage_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "storage_capacity", value)

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "storage_type")

    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FileSystemTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FileSystemTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(self) -> Optional[pulumi.Input['FileSystemWindowsConfigurationArgs']]:
        return pulumi.get(self, "windows_configuration")

    @windows_configuration.setter
    def windows_configuration(self, value: Optional[pulumi.Input['FileSystemWindowsConfigurationArgs']]):
        pulumi.set(self, "windows_configuration", value)


warnings.warn("""FileSystem is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class FileSystem(pulumi.CustomResource):
    warnings.warn("""FileSystem is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_id: Optional[pulumi.Input[str]] = None,
                 file_system_type: Optional[pulumi.Input[str]] = None,
                 file_system_type_version: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 lustre_configuration: Optional[pulumi.Input[pulumi.InputType['FileSystemLustreConfigurationArgs']]] = None,
                 ontap_configuration: Optional[pulumi.Input[pulumi.InputType['FileSystemOntapConfigurationArgs']]] = None,
                 open_zfs_configuration: Optional[pulumi.Input[pulumi.InputType['FileSystemOpenZFSConfigurationArgs']]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 storage_capacity: Optional[pulumi.Input[int]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FileSystemTagArgs']]]]] = None,
                 windows_configuration: Optional[pulumi.Input[pulumi.InputType['FileSystemWindowsConfigurationArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::FSx::FileSystem

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FileSystemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::FSx::FileSystem

        :param str resource_name: The name of the resource.
        :param FileSystemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FileSystemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_id: Optional[pulumi.Input[str]] = None,
                 file_system_type: Optional[pulumi.Input[str]] = None,
                 file_system_type_version: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 lustre_configuration: Optional[pulumi.Input[pulumi.InputType['FileSystemLustreConfigurationArgs']]] = None,
                 ontap_configuration: Optional[pulumi.Input[pulumi.InputType['FileSystemOntapConfigurationArgs']]] = None,
                 open_zfs_configuration: Optional[pulumi.Input[pulumi.InputType['FileSystemOpenZFSConfigurationArgs']]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 storage_capacity: Optional[pulumi.Input[int]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FileSystemTagArgs']]]]] = None,
                 windows_configuration: Optional[pulumi.Input[pulumi.InputType['FileSystemWindowsConfigurationArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""FileSystem is deprecated: FileSystem is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = FileSystemArgs.__new__(FileSystemArgs)

            __props__.__dict__["backup_id"] = backup_id
            if file_system_type is None and not opts.urn:
                raise TypeError("Missing required property 'file_system_type'")
            __props__.__dict__["file_system_type"] = file_system_type
            __props__.__dict__["file_system_type_version"] = file_system_type_version
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["lustre_configuration"] = lustre_configuration
            __props__.__dict__["ontap_configuration"] = ontap_configuration
            __props__.__dict__["open_zfs_configuration"] = open_zfs_configuration
            __props__.__dict__["security_group_ids"] = security_group_ids
            __props__.__dict__["storage_capacity"] = storage_capacity
            __props__.__dict__["storage_type"] = storage_type
            if subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_ids'")
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["tags"] = tags
            __props__.__dict__["windows_configuration"] = windows_configuration
            __props__.__dict__["d_ns_name"] = None
            __props__.__dict__["lustre_mount_name"] = None
            __props__.__dict__["root_volume_id"] = None
        super(FileSystem, __self__).__init__(
            'aws-native:fsx:FileSystem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FileSystem':
        """
        Get an existing FileSystem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FileSystemArgs.__new__(FileSystemArgs)

        __props__.__dict__["backup_id"] = None
        __props__.__dict__["d_ns_name"] = None
        __props__.__dict__["file_system_type"] = None
        __props__.__dict__["file_system_type_version"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["lustre_configuration"] = None
        __props__.__dict__["lustre_mount_name"] = None
        __props__.__dict__["ontap_configuration"] = None
        __props__.__dict__["open_zfs_configuration"] = None
        __props__.__dict__["root_volume_id"] = None
        __props__.__dict__["security_group_ids"] = None
        __props__.__dict__["storage_capacity"] = None
        __props__.__dict__["storage_type"] = None
        __props__.__dict__["subnet_ids"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["windows_configuration"] = None
        return FileSystem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "backup_id")

    @property
    @pulumi.getter(name="dNSName")
    def d_ns_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "d_ns_name")

    @property
    @pulumi.getter(name="fileSystemType")
    def file_system_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "file_system_type")

    @property
    @pulumi.getter(name="fileSystemTypeVersion")
    def file_system_type_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "file_system_type_version")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="lustreConfiguration")
    def lustre_configuration(self) -> pulumi.Output[Optional['outputs.FileSystemLustreConfiguration']]:
        return pulumi.get(self, "lustre_configuration")

    @property
    @pulumi.getter(name="lustreMountName")
    def lustre_mount_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "lustre_mount_name")

    @property
    @pulumi.getter(name="ontapConfiguration")
    def ontap_configuration(self) -> pulumi.Output[Optional['outputs.FileSystemOntapConfiguration']]:
        return pulumi.get(self, "ontap_configuration")

    @property
    @pulumi.getter(name="openZFSConfiguration")
    def open_zfs_configuration(self) -> pulumi.Output[Optional['outputs.FileSystemOpenZFSConfiguration']]:
        return pulumi.get(self, "open_zfs_configuration")

    @property
    @pulumi.getter(name="rootVolumeId")
    def root_volume_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "root_volume_id")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "storage_capacity")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.FileSystemTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(self) -> pulumi.Output[Optional['outputs.FileSystemWindowsConfiguration']]:
        return pulumi.get(self, "windows_configuration")

