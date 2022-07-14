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

__all__ = ['DatacenterConnectorArgs', 'DatacenterConnector']

@pulumi.input_type
class DatacenterConnectorArgs:
    def __init__(__self__, *,
                 datacenter_connector_id: pulumi.Input[str],
                 source_id: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 registration_id: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 service_account: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DatacenterConnector resource.
        :param pulumi.Input[str] datacenter_connector_id: Required. The datacenterConnector identifier.
        :param pulumi.Input[str] registration_id: Immutable. A unique key for this connector. This key is internal to the OVA connector and is supplied with its creation during the registration process and can not be modified.
        :param pulumi.Input[str] request_id: A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        :param pulumi.Input[str] service_account: The service account to use in the connector when communicating with the cloud.
        :param pulumi.Input[str] version: The version running in the DatacenterConnector. This is supplied by the OVA connector during the registration process and can not be modified.
        """
        pulumi.set(__self__, "datacenter_connector_id", datacenter_connector_id)
        pulumi.set(__self__, "source_id", source_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if registration_id is not None:
            pulumi.set(__self__, "registration_id", registration_id)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if service_account is not None:
            pulumi.set(__self__, "service_account", service_account)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="datacenterConnectorId")
    def datacenter_connector_id(self) -> pulumi.Input[str]:
        """
        Required. The datacenterConnector identifier.
        """
        return pulumi.get(self, "datacenter_connector_id")

    @datacenter_connector_id.setter
    def datacenter_connector_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_connector_id", value)

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source_id")

    @source_id.setter
    def source_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="registrationId")
    def registration_id(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. A unique key for this connector. This key is internal to the OVA connector and is supplied with its creation during the registration process and can not be modified.
        """
        return pulumi.get(self, "registration_id")

    @registration_id.setter
    def registration_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registration_id", value)

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        """
        A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)

    @property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[str]]:
        """
        The service account to use in the connector when communicating with the cloud.
        """
        return pulumi.get(self, "service_account")

    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version running in the DatacenterConnector. This is supplied by the OVA connector during the registration process and can not be modified.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class DatacenterConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_connector_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 registration_id: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 service_account: Optional[pulumi.Input[str]] = None,
                 source_id: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new DatacenterConnector in a given Source.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_connector_id: Required. The datacenterConnector identifier.
        :param pulumi.Input[str] registration_id: Immutable. A unique key for this connector. This key is internal to the OVA connector and is supplied with its creation during the registration process and can not be modified.
        :param pulumi.Input[str] request_id: A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        :param pulumi.Input[str] service_account: The service account to use in the connector when communicating with the cloud.
        :param pulumi.Input[str] version: The version running in the DatacenterConnector. This is supplied by the OVA connector during the registration process and can not be modified.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatacenterConnectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new DatacenterConnector in a given Source.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param DatacenterConnectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatacenterConnectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_connector_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 registration_id: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 service_account: Optional[pulumi.Input[str]] = None,
                 source_id: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
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
            __props__ = DatacenterConnectorArgs.__new__(DatacenterConnectorArgs)

            if datacenter_connector_id is None and not opts.urn:
                raise TypeError("Missing required property 'datacenter_connector_id'")
            __props__.__dict__["datacenter_connector_id"] = datacenter_connector_id
            __props__.__dict__["location"] = location
            __props__.__dict__["project"] = project
            __props__.__dict__["registration_id"] = registration_id
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["service_account"] = service_account
            if source_id is None and not opts.urn:
                raise TypeError("Missing required property 'source_id'")
            __props__.__dict__["source_id"] = source_id
            __props__.__dict__["version"] = version
            __props__.__dict__["appliance_infrastructure_version"] = None
            __props__.__dict__["appliance_software_version"] = None
            __props__.__dict__["available_versions"] = None
            __props__.__dict__["bucket"] = None
            __props__.__dict__["create_time"] = None
            __props__.__dict__["error"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["state_time"] = None
            __props__.__dict__["update_time"] = None
            __props__.__dict__["upgrade_status"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["datacenter_connector_id", "location", "project", "source_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DatacenterConnector, __self__).__init__(
            'google-native:vmmigration/v1alpha1:DatacenterConnector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DatacenterConnector':
        """
        Get an existing DatacenterConnector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatacenterConnectorArgs.__new__(DatacenterConnectorArgs)

        __props__.__dict__["appliance_infrastructure_version"] = None
        __props__.__dict__["appliance_software_version"] = None
        __props__.__dict__["available_versions"] = None
        __props__.__dict__["bucket"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["datacenter_connector_id"] = None
        __props__.__dict__["error"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["registration_id"] = None
        __props__.__dict__["request_id"] = None
        __props__.__dict__["service_account"] = None
        __props__.__dict__["source_id"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["state_time"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["upgrade_status"] = None
        __props__.__dict__["version"] = None
        return DatacenterConnector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applianceInfrastructureVersion")
    def appliance_infrastructure_version(self) -> pulumi.Output[str]:
        """
        Appliance OVA version. This is the OVA which is manually installed by the user and contains the infrastructure for the automatically updatable components on the appliance.
        """
        return pulumi.get(self, "appliance_infrastructure_version")

    @property
    @pulumi.getter(name="applianceSoftwareVersion")
    def appliance_software_version(self) -> pulumi.Output[str]:
        """
        Appliance last installed update bundle version. This is the version of the automatically updatable components on the appliance.
        """
        return pulumi.get(self, "appliance_software_version")

    @property
    @pulumi.getter(name="availableVersions")
    def available_versions(self) -> pulumi.Output['outputs.AvailableUpdatesResponse']:
        """
        The available versions for updating this appliance.
        """
        return pulumi.get(self, "available_versions")

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        The communication channel between the datacenter connector and GCP.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time the connector was created (as an API call, not when it was actually installed).
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="datacenterConnectorId")
    def datacenter_connector_id(self) -> pulumi.Output[str]:
        """
        Required. The datacenterConnector identifier.
        """
        return pulumi.get(self, "datacenter_connector_id")

    @property
    @pulumi.getter
    def error(self) -> pulumi.Output['outputs.StatusResponse']:
        """
        Provides details on the state of the Datacenter Connector in case of an error.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The connector's name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="registrationId")
    def registration_id(self) -> pulumi.Output[str]:
        """
        Immutable. A unique key for this connector. This key is internal to the OVA connector and is supplied with its creation during the registration process and can not be modified.
        """
        return pulumi.get(self, "registration_id")

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> pulumi.Output[Optional[str]]:
        """
        A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        """
        return pulumi.get(self, "request_id")

    @property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[str]:
        """
        The service account to use in the connector when communicating with the cloud.
        """
        return pulumi.get(self, "service_account")

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the DatacenterConnector, as determined by the health checks.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateTime")
    def state_time(self) -> pulumi.Output[str]:
        """
        The time the state was last set.
        """
        return pulumi.get(self, "state_time")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The last time the connector was updated with an API call.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="upgradeStatus")
    def upgrade_status(self) -> pulumi.Output['outputs.UpgradeStatusResponse']:
        """
        The status of the current / last upgradeAppliance operation.
        """
        return pulumi.get(self, "upgrade_status")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The version running in the DatacenterConnector. This is supplied by the OVA connector during the registration process and can not be modified.
        """
        return pulumi.get(self, "version")

