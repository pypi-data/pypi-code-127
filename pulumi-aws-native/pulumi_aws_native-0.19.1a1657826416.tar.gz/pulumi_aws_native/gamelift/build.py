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

__all__ = ['BuildArgs', 'Build']

@pulumi.input_type
class BuildArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 operating_system: Optional[pulumi.Input[str]] = None,
                 storage_location: Optional[pulumi.Input['BuildS3LocationArgs']] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Build resource.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if operating_system is not None:
            pulumi.set(__self__, "operating_system", operating_system)
        if storage_location is not None:
            pulumi.set(__self__, "storage_location", storage_location)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "operating_system")

    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operating_system", value)

    @property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> Optional[pulumi.Input['BuildS3LocationArgs']]:
        return pulumi.get(self, "storage_location")

    @storage_location.setter
    def storage_location(self, value: Optional[pulumi.Input['BuildS3LocationArgs']]):
        pulumi.set(self, "storage_location", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


warnings.warn("""Build is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Build(pulumi.CustomResource):
    warnings.warn("""Build is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operating_system: Optional[pulumi.Input[str]] = None,
                 storage_location: Optional[pulumi.Input[pulumi.InputType['BuildS3LocationArgs']]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::GameLift::Build

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[BuildArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::GameLift::Build

        :param str resource_name: The name of the resource.
        :param BuildArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BuildArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operating_system: Optional[pulumi.Input[str]] = None,
                 storage_location: Optional[pulumi.Input[pulumi.InputType['BuildS3LocationArgs']]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Build is deprecated: Build is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = BuildArgs.__new__(BuildArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["operating_system"] = operating_system
            __props__.__dict__["storage_location"] = storage_location
            __props__.__dict__["version"] = version
        super(Build, __self__).__init__(
            'aws-native:gamelift:Build',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Build':
        """
        Get an existing Build resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BuildArgs.__new__(BuildArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["operating_system"] = None
        __props__.__dict__["storage_location"] = None
        __props__.__dict__["version"] = None
        return Build(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "operating_system")

    @property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> pulumi.Output[Optional['outputs.BuildS3Location']]:
        return pulumi.get(self, "storage_location")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "version")

