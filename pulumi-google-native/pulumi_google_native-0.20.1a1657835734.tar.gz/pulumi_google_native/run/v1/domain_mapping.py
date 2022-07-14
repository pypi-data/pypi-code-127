# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['DomainMappingArgs', 'DomainMapping']

@pulumi.input_type
class DomainMappingArgs:
    def __init__(__self__, *,
                 api_version: Optional[pulumi.Input[str]] = None,
                 dry_run: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['ObjectMetaArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input['DomainMappingSpecArgs']] = None):
        """
        The set of arguments for constructing a DomainMapping resource.
        :param pulumi.Input[str] api_version: The API version for this call such as "domains.cloudrun.com/v1".
        :param pulumi.Input[str] dry_run: Indicates that the server should validate the request and populate default values without persisting the request. Supported values: `all`
        :param pulumi.Input[str] kind: The kind of resource, in this case "DomainMapping".
        :param pulumi.Input['ObjectMetaArgs'] metadata: Metadata associated with this BuildTemplate.
        :param pulumi.Input['DomainMappingSpecArgs'] spec: The spec for this DomainMapping.
        """
        if api_version is not None:
            pulumi.set(__self__, "api_version", api_version)
        if dry_run is not None:
            pulumi.set(__self__, "dry_run", dry_run)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if spec is not None:
            pulumi.set(__self__, "spec", spec)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        """
        The API version for this call such as "domains.cloudrun.com/v1".
        """
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates that the server should validate the request and populate default values without persisting the request. Supported values: `all`
        """
        return pulumi.get(self, "dry_run")

    @dry_run.setter
    def dry_run(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dry_run", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        The kind of resource, in this case "DomainMapping".
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['ObjectMetaArgs']]:
        """
        Metadata associated with this BuildTemplate.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['ObjectMetaArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input['DomainMappingSpecArgs']]:
        """
        The spec for this DomainMapping.
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: Optional[pulumi.Input['DomainMappingSpecArgs']]):
        pulumi.set(self, "spec", value)


class DomainMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 dry_run: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['ObjectMetaArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['DomainMappingSpecArgs']]] = None,
                 __props__=None):
        """
        Create a new domain mapping.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_version: The API version for this call such as "domains.cloudrun.com/v1".
        :param pulumi.Input[str] dry_run: Indicates that the server should validate the request and populate default values without persisting the request. Supported values: `all`
        :param pulumi.Input[str] kind: The kind of resource, in this case "DomainMapping".
        :param pulumi.Input[pulumi.InputType['ObjectMetaArgs']] metadata: Metadata associated with this BuildTemplate.
        :param pulumi.Input[pulumi.InputType['DomainMappingSpecArgs']] spec: The spec for this DomainMapping.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DomainMappingArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a new domain mapping.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param DomainMappingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainMappingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 dry_run: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['ObjectMetaArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['DomainMappingSpecArgs']]] = None,
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
            __props__ = DomainMappingArgs.__new__(DomainMappingArgs)

            __props__.__dict__["api_version"] = api_version
            __props__.__dict__["dry_run"] = dry_run
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["project"] = project
            __props__.__dict__["spec"] = spec
            __props__.__dict__["status"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DomainMapping, __self__).__init__(
            'google-native:run/v1:DomainMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DomainMapping':
        """
        Get an existing DomainMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DomainMappingArgs.__new__(DomainMappingArgs)

        __props__.__dict__["api_version"] = None
        __props__.__dict__["dry_run"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["spec"] = None
        __props__.__dict__["status"] = None
        return DomainMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Output[str]:
        """
        The API version for this call such as "domains.cloudrun.com/v1".
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates that the server should validate the request and populate default values without persisting the request. Supported values: `all`
        """
        return pulumi.get(self, "dry_run")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of resource, in this case "DomainMapping".
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['outputs.ObjectMetaResponse']:
        """
        Metadata associated with this BuildTemplate.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output['outputs.DomainMappingSpecResponse']:
        """
        The spec for this DomainMapping.
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.DomainMappingStatusResponse']:
        """
        The current status of the DomainMapping.
        """
        return pulumi.get(self, "status")

