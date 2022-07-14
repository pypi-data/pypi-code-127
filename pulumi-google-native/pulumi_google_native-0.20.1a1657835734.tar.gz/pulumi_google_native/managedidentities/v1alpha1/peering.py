# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['PeeringArgs', 'Peering']

@pulumi.input_type
class PeeringArgs:
    def __init__(__self__, *,
                 authorized_network: pulumi.Input[str],
                 domain_resource: pulumi.Input[str],
                 peering_id: pulumi.Input[str],
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Peering resource.
        :param pulumi.Input[str] authorized_network: The full names of the Google Compute Engine [networks](/compute/docs/networks-and-firewalls#networks) to which the instance is connected. Caller needs to make sure that CIDR subnets do not overlap between networks, else peering creation will fail.
        :param pulumi.Input[str] domain_resource: Full domain resource path for the Managed AD Domain involved in peering. The resource path should be in the form: `projects/{project_id}/locations/global/domains/{domain_name}`
        :param pulumi.Input[str] peering_id: Required. Peering Id, unique name to identify peering.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Resource labels to represent user provided metadata.
        """
        pulumi.set(__self__, "authorized_network", authorized_network)
        pulumi.set(__self__, "domain_resource", domain_resource)
        pulumi.set(__self__, "peering_id", peering_id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="authorizedNetwork")
    def authorized_network(self) -> pulumi.Input[str]:
        """
        The full names of the Google Compute Engine [networks](/compute/docs/networks-and-firewalls#networks) to which the instance is connected. Caller needs to make sure that CIDR subnets do not overlap between networks, else peering creation will fail.
        """
        return pulumi.get(self, "authorized_network")

    @authorized_network.setter
    def authorized_network(self, value: pulumi.Input[str]):
        pulumi.set(self, "authorized_network", value)

    @property
    @pulumi.getter(name="domainResource")
    def domain_resource(self) -> pulumi.Input[str]:
        """
        Full domain resource path for the Managed AD Domain involved in peering. The resource path should be in the form: `projects/{project_id}/locations/global/domains/{domain_name}`
        """
        return pulumi.get(self, "domain_resource")

    @domain_resource.setter
    def domain_resource(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_resource", value)

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> pulumi.Input[str]:
        """
        Required. Peering Id, unique name to identify peering.
        """
        return pulumi.get(self, "peering_id")

    @peering_id.setter
    def peering_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "peering_id", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. Resource labels to represent user provided metadata.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class Peering(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorized_network: Optional[pulumi.Input[str]] = None,
                 domain_resource: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 peering_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a Peering for Managed AD instance.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorized_network: The full names of the Google Compute Engine [networks](/compute/docs/networks-and-firewalls#networks) to which the instance is connected. Caller needs to make sure that CIDR subnets do not overlap between networks, else peering creation will fail.
        :param pulumi.Input[str] domain_resource: Full domain resource path for the Managed AD Domain involved in peering. The resource path should be in the form: `projects/{project_id}/locations/global/domains/{domain_name}`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Resource labels to represent user provided metadata.
        :param pulumi.Input[str] peering_id: Required. Peering Id, unique name to identify peering.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PeeringArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a Peering for Managed AD instance.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param PeeringArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PeeringArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorized_network: Optional[pulumi.Input[str]] = None,
                 domain_resource: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 peering_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = PeeringArgs.__new__(PeeringArgs)

            if authorized_network is None and not opts.urn:
                raise TypeError("Missing required property 'authorized_network'")
            __props__.__dict__["authorized_network"] = authorized_network
            if domain_resource is None and not opts.urn:
                raise TypeError("Missing required property 'domain_resource'")
            __props__.__dict__["domain_resource"] = domain_resource
            __props__.__dict__["labels"] = labels
            if peering_id is None and not opts.urn:
                raise TypeError("Missing required property 'peering_id'")
            __props__.__dict__["peering_id"] = peering_id
            __props__.__dict__["project"] = project
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["status_message"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["peering_id", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Peering, __self__).__init__(
            'google-native:managedidentities/v1alpha1:Peering',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Peering':
        """
        Get an existing Peering resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PeeringArgs.__new__(PeeringArgs)

        __props__.__dict__["authorized_network"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["domain_resource"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peering_id"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["status_message"] = None
        __props__.__dict__["update_time"] = None
        return Peering(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorizedNetwork")
    def authorized_network(self) -> pulumi.Output[str]:
        """
        The full names of the Google Compute Engine [networks](/compute/docs/networks-and-firewalls#networks) to which the instance is connected. Caller needs to make sure that CIDR subnets do not overlap between networks, else peering creation will fail.
        """
        return pulumi.get(self, "authorized_network")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time the instance was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="domainResource")
    def domain_resource(self) -> pulumi.Output[str]:
        """
        Full domain resource path for the Managed AD Domain involved in peering. The resource path should be in the form: `projects/{project_id}/locations/global/domains/{domain_name}`
        """
        return pulumi.get(self, "domain_resource")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. Resource labels to represent user provided metadata.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unique name of the peering in this scope including projects and location using the form: `projects/{project_id}/locations/global/peerings/{peering_id}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> pulumi.Output[str]:
        """
        Required. Peering Id, unique name to identify peering.
        """
        return pulumi.get(self, "peering_id")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of this Peering.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[str]:
        """
        Additional information about the current status of this peering, if available.
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Last update time.
        """
        return pulumi.get(self, "update_time")

