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

__all__ = ['AccessPointArgs', 'AccessPoint']

@pulumi.input_type
class AccessPointArgs:
    def __init__(__self__, *,
                 file_system_id: pulumi.Input[str],
                 access_point_tags: Optional[pulumi.Input[Sequence[pulumi.Input['AccessPointTagArgs']]]] = None,
                 client_token: Optional[pulumi.Input[str]] = None,
                 posix_user: Optional[pulumi.Input['AccessPointPosixUserArgs']] = None,
                 root_directory: Optional[pulumi.Input['AccessPointRootDirectoryArgs']] = None):
        """
        The set of arguments for constructing a AccessPoint resource.
        :param pulumi.Input[str] file_system_id: The ID of the EFS file system that the access point provides access to.
        :param pulumi.Input[str] client_token: (optional) A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.
        :param pulumi.Input['AccessPointPosixUserArgs'] posix_user: The operating system user and group applied to all file system requests made using the access point.
        :param pulumi.Input['AccessPointRootDirectoryArgs'] root_directory: Specifies the directory on the Amazon EFS file system that the access point exposes as the root directory of your file system to NFS clients using the access point. The clients using the access point can only access the root directory and below. If the RootDirectory>Path specified does not exist, EFS creates it and applies the CreationInfo settings when a client connects to an access point. When specifying a RootDirectory, you need to provide the Path, and the CreationInfo is optional.
        """
        pulumi.set(__self__, "file_system_id", file_system_id)
        if access_point_tags is not None:
            pulumi.set(__self__, "access_point_tags", access_point_tags)
        if client_token is not None:
            pulumi.set(__self__, "client_token", client_token)
        if posix_user is not None:
            pulumi.set(__self__, "posix_user", posix_user)
        if root_directory is not None:
            pulumi.set(__self__, "root_directory", root_directory)

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[str]:
        """
        The ID of the EFS file system that the access point provides access to.
        """
        return pulumi.get(self, "file_system_id")

    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "file_system_id", value)

    @property
    @pulumi.getter(name="accessPointTags")
    def access_point_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessPointTagArgs']]]]:
        return pulumi.get(self, "access_point_tags")

    @access_point_tags.setter
    def access_point_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessPointTagArgs']]]]):
        pulumi.set(self, "access_point_tags", value)

    @property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> Optional[pulumi.Input[str]]:
        """
        (optional) A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.
        """
        return pulumi.get(self, "client_token")

    @client_token.setter
    def client_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_token", value)

    @property
    @pulumi.getter(name="posixUser")
    def posix_user(self) -> Optional[pulumi.Input['AccessPointPosixUserArgs']]:
        """
        The operating system user and group applied to all file system requests made using the access point.
        """
        return pulumi.get(self, "posix_user")

    @posix_user.setter
    def posix_user(self, value: Optional[pulumi.Input['AccessPointPosixUserArgs']]):
        pulumi.set(self, "posix_user", value)

    @property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> Optional[pulumi.Input['AccessPointRootDirectoryArgs']]:
        """
        Specifies the directory on the Amazon EFS file system that the access point exposes as the root directory of your file system to NFS clients using the access point. The clients using the access point can only access the root directory and below. If the RootDirectory>Path specified does not exist, EFS creates it and applies the CreationInfo settings when a client connects to an access point. When specifying a RootDirectory, you need to provide the Path, and the CreationInfo is optional.
        """
        return pulumi.get(self, "root_directory")

    @root_directory.setter
    def root_directory(self, value: Optional[pulumi.Input['AccessPointRootDirectoryArgs']]):
        pulumi.set(self, "root_directory", value)


class AccessPoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_point_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPointTagArgs']]]]] = None,
                 client_token: Optional[pulumi.Input[str]] = None,
                 file_system_id: Optional[pulumi.Input[str]] = None,
                 posix_user: Optional[pulumi.Input[pulumi.InputType['AccessPointPosixUserArgs']]] = None,
                 root_directory: Optional[pulumi.Input[pulumi.InputType['AccessPointRootDirectoryArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EFS::AccessPoint

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_token: (optional) A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.
        :param pulumi.Input[str] file_system_id: The ID of the EFS file system that the access point provides access to.
        :param pulumi.Input[pulumi.InputType['AccessPointPosixUserArgs']] posix_user: The operating system user and group applied to all file system requests made using the access point.
        :param pulumi.Input[pulumi.InputType['AccessPointRootDirectoryArgs']] root_directory: Specifies the directory on the Amazon EFS file system that the access point exposes as the root directory of your file system to NFS clients using the access point. The clients using the access point can only access the root directory and below. If the RootDirectory>Path specified does not exist, EFS creates it and applies the CreationInfo settings when a client connects to an access point. When specifying a RootDirectory, you need to provide the Path, and the CreationInfo is optional.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessPointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EFS::AccessPoint

        :param str resource_name: The name of the resource.
        :param AccessPointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessPointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_point_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPointTagArgs']]]]] = None,
                 client_token: Optional[pulumi.Input[str]] = None,
                 file_system_id: Optional[pulumi.Input[str]] = None,
                 posix_user: Optional[pulumi.Input[pulumi.InputType['AccessPointPosixUserArgs']]] = None,
                 root_directory: Optional[pulumi.Input[pulumi.InputType['AccessPointRootDirectoryArgs']]] = None,
                 __props__=None):
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
            __props__ = AccessPointArgs.__new__(AccessPointArgs)

            __props__.__dict__["access_point_tags"] = access_point_tags
            __props__.__dict__["client_token"] = client_token
            if file_system_id is None and not opts.urn:
                raise TypeError("Missing required property 'file_system_id'")
            __props__.__dict__["file_system_id"] = file_system_id
            __props__.__dict__["posix_user"] = posix_user
            __props__.__dict__["root_directory"] = root_directory
            __props__.__dict__["access_point_id"] = None
            __props__.__dict__["arn"] = None
        super(AccessPoint, __self__).__init__(
            'aws-native:efs:AccessPoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AccessPoint':
        """
        Get an existing AccessPoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccessPointArgs.__new__(AccessPointArgs)

        __props__.__dict__["access_point_id"] = None
        __props__.__dict__["access_point_tags"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["client_token"] = None
        __props__.__dict__["file_system_id"] = None
        __props__.__dict__["posix_user"] = None
        __props__.__dict__["root_directory"] = None
        return AccessPoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessPointId")
    def access_point_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "access_point_id")

    @property
    @pulumi.getter(name="accessPointTags")
    def access_point_tags(self) -> pulumi.Output[Optional[Sequence['outputs.AccessPointTag']]]:
        return pulumi.get(self, "access_point_tags")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> pulumi.Output[Optional[str]]:
        """
        (optional) A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.
        """
        return pulumi.get(self, "client_token")

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Output[str]:
        """
        The ID of the EFS file system that the access point provides access to.
        """
        return pulumi.get(self, "file_system_id")

    @property
    @pulumi.getter(name="posixUser")
    def posix_user(self) -> pulumi.Output[Optional['outputs.AccessPointPosixUser']]:
        """
        The operating system user and group applied to all file system requests made using the access point.
        """
        return pulumi.get(self, "posix_user")

    @property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> pulumi.Output[Optional['outputs.AccessPointRootDirectory']]:
        """
        Specifies the directory on the Amazon EFS file system that the access point exposes as the root directory of your file system to NFS clients using the access point. The clients using the access point can only access the root directory and below. If the RootDirectory>Path specified does not exist, EFS creates it and applies the CreationInfo settings when a client connects to an access point. When specifying a RootDirectory, you need to provide the Path, and the CreationInfo is optional.
        """
        return pulumi.get(self, "root_directory")

