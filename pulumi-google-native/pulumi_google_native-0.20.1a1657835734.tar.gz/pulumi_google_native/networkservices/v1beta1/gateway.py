# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['GatewayArgs', 'Gateway']

@pulumi.input_type
class GatewayArgs:
    def __init__(__self__, *,
                 gateway_id: pulumi.Input[str],
                 ports: pulumi.Input[Sequence[pulumi.Input[int]]],
                 scope: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 server_tls_policy: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['GatewayType']] = None):
        """
        The set of arguments for constructing a Gateway resource.
        :param pulumi.Input[str] gateway_id: Required. Short name of the Gateway resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ports: One or more ports that the Gateway must receive traffic on. The proxy binds to the ports specified. Gateway listen on 0.0.0.0 on the ports specified below.
        :param pulumi.Input[str] scope: Immutable. Scope determines how configuration across multiple Gateway instances are merged. The configuration for multiple Gateway instances with the same scope will be merged as presented as a single coniguration to the proxy/load balancer. Max length 64 characters. Scope should start with a letter and can only have letters, numbers, hyphens.
        :param pulumi.Input[str] description: Optional. A free-text description of the resource. Max length 1024 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Set of label tags associated with the Gateway resource.
        :param pulumi.Input[str] name: Name of the Gateway resource. It matches pattern `projects/*/locations/*/gateways/`.
        :param pulumi.Input[str] server_tls_policy: Optional. A fully-qualified ServerTLSPolicy URL reference. Specifies how TLS traffic is terminated. If empty, TLS termination is disabled.
        :param pulumi.Input['GatewayType'] type: Immutable. The type of the customer managed gateway.
        """
        pulumi.set(__self__, "gateway_id", gateway_id)
        pulumi.set(__self__, "ports", ports)
        pulumi.set(__self__, "scope", scope)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if server_tls_policy is not None:
            pulumi.set(__self__, "server_tls_policy", server_tls_policy)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Input[str]:
        """
        Required. Short name of the Gateway resource to be created.
        """
        return pulumi.get(self, "gateway_id")

    @gateway_id.setter
    def gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "gateway_id", value)

    @property
    @pulumi.getter
    def ports(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        One or more ports that the Gateway must receive traffic on. The proxy binds to the ports specified. Gateway listen on 0.0.0.0 on the ports specified below.
        """
        return pulumi.get(self, "ports")

    @ports.setter
    def ports(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "ports", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        Immutable. Scope determines how configuration across multiple Gateway instances are merged. The configuration for multiple Gateway instances with the same scope will be merged as presented as a single coniguration to the proxy/load balancer. Max length 64 characters. Scope should start with a letter and can only have letters, numbers, hyphens.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

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
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. Set of label tags associated with the Gateway resource.
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
        Name of the Gateway resource. It matches pattern `projects/*/locations/*/gateways/`.
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

    @property
    @pulumi.getter(name="serverTlsPolicy")
    def server_tls_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. A fully-qualified ServerTLSPolicy URL reference. Specifies how TLS traffic is terminated. If empty, TLS termination is disabled.
        """
        return pulumi.get(self, "server_tls_policy")

    @server_tls_policy.setter
    def server_tls_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_tls_policy", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['GatewayType']]:
        """
        Immutable. The type of the customer managed gateway.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['GatewayType']]):
        pulumi.set(self, "type", value)


class Gateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ports: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 server_tls_policy: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['GatewayType']] = None,
                 __props__=None):
        """
        Creates a new Gateway in a given project and location.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Optional. A free-text description of the resource. Max length 1024 characters.
        :param pulumi.Input[str] gateway_id: Required. Short name of the Gateway resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Set of label tags associated with the Gateway resource.
        :param pulumi.Input[str] name: Name of the Gateway resource. It matches pattern `projects/*/locations/*/gateways/`.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ports: One or more ports that the Gateway must receive traffic on. The proxy binds to the ports specified. Gateway listen on 0.0.0.0 on the ports specified below.
        :param pulumi.Input[str] scope: Immutable. Scope determines how configuration across multiple Gateway instances are merged. The configuration for multiple Gateway instances with the same scope will be merged as presented as a single coniguration to the proxy/load balancer. Max length 64 characters. Scope should start with a letter and can only have letters, numbers, hyphens.
        :param pulumi.Input[str] server_tls_policy: Optional. A fully-qualified ServerTLSPolicy URL reference. Specifies how TLS traffic is terminated. If empty, TLS termination is disabled.
        :param pulumi.Input['GatewayType'] type: Immutable. The type of the customer managed gateway.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Gateway in a given project and location.

        :param str resource_name: The name of the resource.
        :param GatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ports: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 server_tls_policy: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['GatewayType']] = None,
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
            __props__ = GatewayArgs.__new__(GatewayArgs)

            __props__.__dict__["description"] = description
            if gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_id'")
            __props__.__dict__["gateway_id"] = gateway_id
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if ports is None and not opts.urn:
                raise TypeError("Missing required property 'ports'")
            __props__.__dict__["ports"] = ports
            __props__.__dict__["project"] = project
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["server_tls_policy"] = server_tls_policy
            __props__.__dict__["type"] = type
            __props__.__dict__["create_time"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["gateway_id", "location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Gateway, __self__).__init__(
            'google-native:networkservices/v1beta1:Gateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Gateway':
        """
        Get an existing Gateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GatewayArgs.__new__(GatewayArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["gateway_id"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["ports"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["server_tls_policy"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["update_time"] = None
        return Gateway(resource_name, opts=opts, __props__=__props__)

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
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Output[str]:
        """
        Required. Short name of the Gateway resource to be created.
        """
        return pulumi.get(self, "gateway_id")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. Set of label tags associated with the Gateway resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Gateway resource. It matches pattern `projects/*/locations/*/gateways/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def ports(self) -> pulumi.Output[Sequence[int]]:
        """
        One or more ports that the Gateway must receive traffic on. The proxy binds to the ports specified. Gateway listen on 0.0.0.0 on the ports specified below.
        """
        return pulumi.get(self, "ports")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        Immutable. Scope determines how configuration across multiple Gateway instances are merged. The configuration for multiple Gateway instances with the same scope will be merged as presented as a single coniguration to the proxy/load balancer. Max length 64 characters. Scope should start with a letter and can only have letters, numbers, hyphens.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        Server-defined URL of this resource
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="serverTlsPolicy")
    def server_tls_policy(self) -> pulumi.Output[str]:
        """
        Optional. A fully-qualified ServerTLSPolicy URL reference. Specifies how TLS traffic is terminated. If empty, TLS termination is disabled.
        """
        return pulumi.get(self, "server_tls_policy")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Immutable. The type of the customer managed gateway.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The timestamp when the resource was updated.
        """
        return pulumi.get(self, "update_time")

