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

__all__ = ['RuntimeArgs', 'Runtime']

@pulumi.input_type
class RuntimeArgs:
    def __init__(__self__, *,
                 runtime_id: pulumi.Input[str],
                 access_config: Optional[pulumi.Input['RuntimeAccessConfigArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 software_config: Optional[pulumi.Input['RuntimeSoftwareConfigArgs']] = None,
                 virtual_machine: Optional[pulumi.Input['VirtualMachineArgs']] = None):
        """
        The set of arguments for constructing a Runtime resource.
        :param pulumi.Input[str] runtime_id: Required. User-defined unique ID of this Runtime.
        :param pulumi.Input['RuntimeAccessConfigArgs'] access_config: The config settings for accessing runtime.
        :param pulumi.Input[str] request_id: Idempotent request UUID.
        :param pulumi.Input['RuntimeSoftwareConfigArgs'] software_config: The config settings for software inside the runtime.
        :param pulumi.Input['VirtualMachineArgs'] virtual_machine: Use a Compute Engine VM image to start the managed notebook instance.
        """
        pulumi.set(__self__, "runtime_id", runtime_id)
        if access_config is not None:
            pulumi.set(__self__, "access_config", access_config)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if software_config is not None:
            pulumi.set(__self__, "software_config", software_config)
        if virtual_machine is not None:
            pulumi.set(__self__, "virtual_machine", virtual_machine)

    @property
    @pulumi.getter(name="runtimeId")
    def runtime_id(self) -> pulumi.Input[str]:
        """
        Required. User-defined unique ID of this Runtime.
        """
        return pulumi.get(self, "runtime_id")

    @runtime_id.setter
    def runtime_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "runtime_id", value)

    @property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> Optional[pulumi.Input['RuntimeAccessConfigArgs']]:
        """
        The config settings for accessing runtime.
        """
        return pulumi.get(self, "access_config")

    @access_config.setter
    def access_config(self, value: Optional[pulumi.Input['RuntimeAccessConfigArgs']]):
        pulumi.set(self, "access_config", value)

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
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        """
        Idempotent request UUID.
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)

    @property
    @pulumi.getter(name="softwareConfig")
    def software_config(self) -> Optional[pulumi.Input['RuntimeSoftwareConfigArgs']]:
        """
        The config settings for software inside the runtime.
        """
        return pulumi.get(self, "software_config")

    @software_config.setter
    def software_config(self, value: Optional[pulumi.Input['RuntimeSoftwareConfigArgs']]):
        pulumi.set(self, "software_config", value)

    @property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(self) -> Optional[pulumi.Input['VirtualMachineArgs']]:
        """
        Use a Compute Engine VM image to start the managed notebook instance.
        """
        return pulumi.get(self, "virtual_machine")

    @virtual_machine.setter
    def virtual_machine(self, value: Optional[pulumi.Input['VirtualMachineArgs']]):
        pulumi.set(self, "virtual_machine", value)


class Runtime(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_config: Optional[pulumi.Input[pulumi.InputType['RuntimeAccessConfigArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 runtime_id: Optional[pulumi.Input[str]] = None,
                 software_config: Optional[pulumi.Input[pulumi.InputType['RuntimeSoftwareConfigArgs']]] = None,
                 virtual_machine: Optional[pulumi.Input[pulumi.InputType['VirtualMachineArgs']]] = None,
                 __props__=None):
        """
        Creates a new Runtime in a given project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RuntimeAccessConfigArgs']] access_config: The config settings for accessing runtime.
        :param pulumi.Input[str] request_id: Idempotent request UUID.
        :param pulumi.Input[str] runtime_id: Required. User-defined unique ID of this Runtime.
        :param pulumi.Input[pulumi.InputType['RuntimeSoftwareConfigArgs']] software_config: The config settings for software inside the runtime.
        :param pulumi.Input[pulumi.InputType['VirtualMachineArgs']] virtual_machine: Use a Compute Engine VM image to start the managed notebook instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RuntimeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Runtime in a given project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param RuntimeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RuntimeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_config: Optional[pulumi.Input[pulumi.InputType['RuntimeAccessConfigArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 runtime_id: Optional[pulumi.Input[str]] = None,
                 software_config: Optional[pulumi.Input[pulumi.InputType['RuntimeSoftwareConfigArgs']]] = None,
                 virtual_machine: Optional[pulumi.Input[pulumi.InputType['VirtualMachineArgs']]] = None,
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
            __props__ = RuntimeArgs.__new__(RuntimeArgs)

            __props__.__dict__["access_config"] = access_config
            __props__.__dict__["location"] = location
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            if runtime_id is None and not opts.urn:
                raise TypeError("Missing required property 'runtime_id'")
            __props__.__dict__["runtime_id"] = runtime_id
            __props__.__dict__["software_config"] = software_config
            __props__.__dict__["virtual_machine"] = virtual_machine
            __props__.__dict__["create_time"] = None
            __props__.__dict__["health_state"] = None
            __props__.__dict__["metrics"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["location", "project", "runtime_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Runtime, __self__).__init__(
            'google-native:notebooks/v1:Runtime',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Runtime':
        """
        Get an existing Runtime resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RuntimeArgs.__new__(RuntimeArgs)

        __props__.__dict__["access_config"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["health_state"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metrics"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["request_id"] = None
        __props__.__dict__["runtime_id"] = None
        __props__.__dict__["software_config"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["virtual_machine"] = None
        return Runtime(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> pulumi.Output['outputs.RuntimeAccessConfigResponse']:
        """
        The config settings for accessing runtime.
        """
        return pulumi.get(self, "access_config")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Runtime creation time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="healthState")
    def health_state(self) -> pulumi.Output[str]:
        """
        Runtime health_state.
        """
        return pulumi.get(self, "health_state")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metrics(self) -> pulumi.Output['outputs.RuntimeMetricsResponse']:
        """
        Contains Runtime daemon metrics such as Service status and JupyterLab stats.
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the runtime. Format: `projects/{project}/locations/{location}/runtimes/{runtimeId}`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> pulumi.Output[Optional[str]]:
        """
        Idempotent request UUID.
        """
        return pulumi.get(self, "request_id")

    @property
    @pulumi.getter(name="runtimeId")
    def runtime_id(self) -> pulumi.Output[str]:
        """
        Required. User-defined unique ID of this Runtime.
        """
        return pulumi.get(self, "runtime_id")

    @property
    @pulumi.getter(name="softwareConfig")
    def software_config(self) -> pulumi.Output['outputs.RuntimeSoftwareConfigResponse']:
        """
        The config settings for software inside the runtime.
        """
        return pulumi.get(self, "software_config")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Runtime state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Runtime update time.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(self) -> pulumi.Output['outputs.VirtualMachineResponse']:
        """
        Use a Compute Engine VM image to start the managed notebook instance.
        """
        return pulumi.get(self, "virtual_machine")

