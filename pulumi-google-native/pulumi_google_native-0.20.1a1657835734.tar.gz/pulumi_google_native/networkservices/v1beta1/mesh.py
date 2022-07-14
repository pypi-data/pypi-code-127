# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['MeshArgs', 'Mesh']

@pulumi.input_type
class MeshArgs:
    def __init__(__self__, *,
                 mesh_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 interception_port: Optional[pulumi.Input[int]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Mesh resource.
        :param pulumi.Input[str] mesh_id: Required. Short name of the Mesh resource to be created.
        :param pulumi.Input[str] description: Optional. A free-text description of the resource. Max length 1024 characters.
        :param pulumi.Input[int] interception_port: Optional. If set to a valid TCP port (1-65535), instructs the SIDECAR proxy to listen on the specified port of localhost (127.0.0.1) address. The SIDECAR proxy will expect all traffic to be redirected to this port regardless of its actual ip:port destination. If unset, a port '15001' is used as the interception port. This will is applicable only for sidecar proxy deployments.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Set of label tags associated with the Mesh resource.
        :param pulumi.Input[str] name: Name of the Mesh resource. It matches pattern `projects/*/locations/global/meshes/`.
        """
        pulumi.set(__self__, "mesh_id", mesh_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if interception_port is not None:
            pulumi.set(__self__, "interception_port", interception_port)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="meshId")
    def mesh_id(self) -> pulumi.Input[str]:
        """
        Required. Short name of the Mesh resource to be created.
        """
        return pulumi.get(self, "mesh_id")

    @mesh_id.setter
    def mesh_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "mesh_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. A free-text description of the resource. Max length 1024 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="interceptionPort")
    def interception_port(self) -> Optional[pulumi.Input[int]]:
        """
        Optional. If set to a valid TCP port (1-65535), instructs the SIDECAR proxy to listen on the specified port of localhost (127.0.0.1) address. The SIDECAR proxy will expect all traffic to be redirected to this port regardless of its actual ip:port destination. If unset, a port '15001' is used as the interception port. This will is applicable only for sidecar proxy deployments.
        """
        return pulumi.get(self, "interception_port")

    @interception_port.setter
    def interception_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "interception_port", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. Set of label tags associated with the Mesh resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Mesh resource. It matches pattern `projects/*/locations/global/meshes/`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class Mesh(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 interception_port: Optional[pulumi.Input[int]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mesh_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new Mesh in a given project and location.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Optional. A free-text description of the resource. Max length 1024 characters.
        :param pulumi.Input[int] interception_port: Optional. If set to a valid TCP port (1-65535), instructs the SIDECAR proxy to listen on the specified port of localhost (127.0.0.1) address. The SIDECAR proxy will expect all traffic to be redirected to this port regardless of its actual ip:port destination. If unset, a port '15001' is used as the interception port. This will is applicable only for sidecar proxy deployments.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Set of label tags associated with the Mesh resource.
        :param pulumi.Input[str] mesh_id: Required. Short name of the Mesh resource to be created.
        :param pulumi.Input[str] name: Name of the Mesh resource. It matches pattern `projects/*/locations/global/meshes/`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MeshArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Mesh in a given project and location.

        :param str resource_name: The name of the resource.
        :param MeshArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MeshArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 interception_port: Optional[pulumi.Input[int]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mesh_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
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
            __props__ = MeshArgs.__new__(MeshArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["interception_port"] = interception_port
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            if mesh_id is None and not opts.urn:
                raise TypeError("Missing required property 'mesh_id'")
            __props__.__dict__["mesh_id"] = mesh_id
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["create_time"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["location", "mesh_id", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Mesh, __self__).__init__(
            'google-native:networkservices/v1beta1:Mesh',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Mesh':
        """
        Get an existing Mesh resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MeshArgs.__new__(MeshArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["interception_port"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mesh_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["update_time"] = None
        return Mesh(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The timestamp when the resource was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. A free-text description of the resource. Max length 1024 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="interceptionPort")
    def interception_port(self) -> pulumi.Output[int]:
        """
        Optional. If set to a valid TCP port (1-65535), instructs the SIDECAR proxy to listen on the specified port of localhost (127.0.0.1) address. The SIDECAR proxy will expect all traffic to be redirected to this port regardless of its actual ip:port destination. If unset, a port '15001' is used as the interception port. This will is applicable only for sidecar proxy deployments.
        """
        return pulumi.get(self, "interception_port")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. Set of label tags associated with the Mesh resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="meshId")
    def mesh_id(self) -> pulumi.Output[str]:
        """
        Required. Short name of the Mesh resource to be created.
        """
        return pulumi.get(self, "mesh_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Mesh resource. It matches pattern `projects/*/locations/global/meshes/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        Server-defined URL of this resource
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The timestamp when the resource was updated.
        """
        return pulumi.get(self, "update_time")

