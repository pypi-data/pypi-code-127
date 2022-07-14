# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AutoscalingConfigArgs', 'AutoscalingConfig']

@pulumi.input_type
class AutoscalingConfigArgs:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cool_down_duration: Optional[pulumi.Input[str]] = None,
                 expander: Optional[pulumi.Input[str]] = None,
                 gpu_utilization_threshold: Optional[pulumi.Input[str]] = None,
                 scale_down_enabled: Optional[pulumi.Input[bool]] = None,
                 scan_interval: Optional[pulumi.Input[str]] = None,
                 unneeded_duration: Optional[pulumi.Input[str]] = None,
                 utilization_threshold: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AutoscalingConfig resource.
        :param pulumi.Input[str] cluster_id: The id of kubernetes cluster.
        :param pulumi.Input[str] cool_down_duration: The cool down duration. Default is `10m`. If the delay (cooldown) value is set too long, there could be complaints that the Horizontal Pod Autoscaler is not responsive to workload changes. However, if the delay value is set too short, the scale of the replicas set may keep thrashing as usual.
        :param pulumi.Input[str] expander: The policy for selecting which node pool to scale. Valid values: `least-waste`, `random`, `priority`. For more information on these policies, see [Configure auto scaling](https://www.alibabacloud.com/help/en/container-service-for-kubernetes/latest/auto-scaling-of-nodes#section-3bg-2ko-inl)
        :param pulumi.Input[str] gpu_utilization_threshold: The scale-in threshold for GPU instance. Default is `0.5`.
        :param pulumi.Input[bool] scale_down_enabled: Specify whether to allow the scale-in of nodes. Default is `true`.
        :param pulumi.Input[str] scan_interval: The interval at which the cluster is reevaluated for scaling. Default is `30s`.
        :param pulumi.Input[str] unneeded_duration: The unneeded duration. Default is `10m`.
        :param pulumi.Input[str] utilization_threshold: The scale-in threshold. Default is `0.5`.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if cool_down_duration is not None:
            pulumi.set(__self__, "cool_down_duration", cool_down_duration)
        if expander is not None:
            pulumi.set(__self__, "expander", expander)
        if gpu_utilization_threshold is not None:
            pulumi.set(__self__, "gpu_utilization_threshold", gpu_utilization_threshold)
        if scale_down_enabled is not None:
            pulumi.set(__self__, "scale_down_enabled", scale_down_enabled)
        if scan_interval is not None:
            pulumi.set(__self__, "scan_interval", scan_interval)
        if unneeded_duration is not None:
            pulumi.set(__self__, "unneeded_duration", unneeded_duration)
        if utilization_threshold is not None:
            pulumi.set(__self__, "utilization_threshold", utilization_threshold)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of kubernetes cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="coolDownDuration")
    def cool_down_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The cool down duration. Default is `10m`. If the delay (cooldown) value is set too long, there could be complaints that the Horizontal Pod Autoscaler is not responsive to workload changes. However, if the delay value is set too short, the scale of the replicas set may keep thrashing as usual.
        """
        return pulumi.get(self, "cool_down_duration")

    @cool_down_duration.setter
    def cool_down_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cool_down_duration", value)

    @property
    @pulumi.getter
    def expander(self) -> Optional[pulumi.Input[str]]:
        """
        The policy for selecting which node pool to scale. Valid values: `least-waste`, `random`, `priority`. For more information on these policies, see [Configure auto scaling](https://www.alibabacloud.com/help/en/container-service-for-kubernetes/latest/auto-scaling-of-nodes#section-3bg-2ko-inl)
        """
        return pulumi.get(self, "expander")

    @expander.setter
    def expander(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expander", value)

    @property
    @pulumi.getter(name="gpuUtilizationThreshold")
    def gpu_utilization_threshold(self) -> Optional[pulumi.Input[str]]:
        """
        The scale-in threshold for GPU instance. Default is `0.5`.
        """
        return pulumi.get(self, "gpu_utilization_threshold")

    @gpu_utilization_threshold.setter
    def gpu_utilization_threshold(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gpu_utilization_threshold", value)

    @property
    @pulumi.getter(name="scaleDownEnabled")
    def scale_down_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specify whether to allow the scale-in of nodes. Default is `true`.
        """
        return pulumi.get(self, "scale_down_enabled")

    @scale_down_enabled.setter
    def scale_down_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "scale_down_enabled", value)

    @property
    @pulumi.getter(name="scanInterval")
    def scan_interval(self) -> Optional[pulumi.Input[str]]:
        """
        The interval at which the cluster is reevaluated for scaling. Default is `30s`.
        """
        return pulumi.get(self, "scan_interval")

    @scan_interval.setter
    def scan_interval(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scan_interval", value)

    @property
    @pulumi.getter(name="unneededDuration")
    def unneeded_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The unneeded duration. Default is `10m`.
        """
        return pulumi.get(self, "unneeded_duration")

    @unneeded_duration.setter
    def unneeded_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unneeded_duration", value)

    @property
    @pulumi.getter(name="utilizationThreshold")
    def utilization_threshold(self) -> Optional[pulumi.Input[str]]:
        """
        The scale-in threshold. Default is `0.5`.
        """
        return pulumi.get(self, "utilization_threshold")

    @utilization_threshold.setter
    def utilization_threshold(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "utilization_threshold", value)


@pulumi.input_type
class _AutoscalingConfigState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cool_down_duration: Optional[pulumi.Input[str]] = None,
                 expander: Optional[pulumi.Input[str]] = None,
                 gpu_utilization_threshold: Optional[pulumi.Input[str]] = None,
                 scale_down_enabled: Optional[pulumi.Input[bool]] = None,
                 scan_interval: Optional[pulumi.Input[str]] = None,
                 unneeded_duration: Optional[pulumi.Input[str]] = None,
                 utilization_threshold: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AutoscalingConfig resources.
        :param pulumi.Input[str] cluster_id: The id of kubernetes cluster.
        :param pulumi.Input[str] cool_down_duration: The cool down duration. Default is `10m`. If the delay (cooldown) value is set too long, there could be complaints that the Horizontal Pod Autoscaler is not responsive to workload changes. However, if the delay value is set too short, the scale of the replicas set may keep thrashing as usual.
        :param pulumi.Input[str] expander: The policy for selecting which node pool to scale. Valid values: `least-waste`, `random`, `priority`. For more information on these policies, see [Configure auto scaling](https://www.alibabacloud.com/help/en/container-service-for-kubernetes/latest/auto-scaling-of-nodes#section-3bg-2ko-inl)
        :param pulumi.Input[str] gpu_utilization_threshold: The scale-in threshold for GPU instance. Default is `0.5`.
        :param pulumi.Input[bool] scale_down_enabled: Specify whether to allow the scale-in of nodes. Default is `true`.
        :param pulumi.Input[str] scan_interval: The interval at which the cluster is reevaluated for scaling. Default is `30s`.
        :param pulumi.Input[str] unneeded_duration: The unneeded duration. Default is `10m`.
        :param pulumi.Input[str] utilization_threshold: The scale-in threshold. Default is `0.5`.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if cool_down_duration is not None:
            pulumi.set(__self__, "cool_down_duration", cool_down_duration)
        if expander is not None:
            pulumi.set(__self__, "expander", expander)
        if gpu_utilization_threshold is not None:
            pulumi.set(__self__, "gpu_utilization_threshold", gpu_utilization_threshold)
        if scale_down_enabled is not None:
            pulumi.set(__self__, "scale_down_enabled", scale_down_enabled)
        if scan_interval is not None:
            pulumi.set(__self__, "scan_interval", scan_interval)
        if unneeded_duration is not None:
            pulumi.set(__self__, "unneeded_duration", unneeded_duration)
        if utilization_threshold is not None:
            pulumi.set(__self__, "utilization_threshold", utilization_threshold)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of kubernetes cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="coolDownDuration")
    def cool_down_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The cool down duration. Default is `10m`. If the delay (cooldown) value is set too long, there could be complaints that the Horizontal Pod Autoscaler is not responsive to workload changes. However, if the delay value is set too short, the scale of the replicas set may keep thrashing as usual.
        """
        return pulumi.get(self, "cool_down_duration")

    @cool_down_duration.setter
    def cool_down_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cool_down_duration", value)

    @property
    @pulumi.getter
    def expander(self) -> Optional[pulumi.Input[str]]:
        """
        The policy for selecting which node pool to scale. Valid values: `least-waste`, `random`, `priority`. For more information on these policies, see [Configure auto scaling](https://www.alibabacloud.com/help/en/container-service-for-kubernetes/latest/auto-scaling-of-nodes#section-3bg-2ko-inl)
        """
        return pulumi.get(self, "expander")

    @expander.setter
    def expander(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expander", value)

    @property
    @pulumi.getter(name="gpuUtilizationThreshold")
    def gpu_utilization_threshold(self) -> Optional[pulumi.Input[str]]:
        """
        The scale-in threshold for GPU instance. Default is `0.5`.
        """
        return pulumi.get(self, "gpu_utilization_threshold")

    @gpu_utilization_threshold.setter
    def gpu_utilization_threshold(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gpu_utilization_threshold", value)

    @property
    @pulumi.getter(name="scaleDownEnabled")
    def scale_down_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specify whether to allow the scale-in of nodes. Default is `true`.
        """
        return pulumi.get(self, "scale_down_enabled")

    @scale_down_enabled.setter
    def scale_down_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "scale_down_enabled", value)

    @property
    @pulumi.getter(name="scanInterval")
    def scan_interval(self) -> Optional[pulumi.Input[str]]:
        """
        The interval at which the cluster is reevaluated for scaling. Default is `30s`.
        """
        return pulumi.get(self, "scan_interval")

    @scan_interval.setter
    def scan_interval(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scan_interval", value)

    @property
    @pulumi.getter(name="unneededDuration")
    def unneeded_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The unneeded duration. Default is `10m`.
        """
        return pulumi.get(self, "unneeded_duration")

    @unneeded_duration.setter
    def unneeded_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unneeded_duration", value)

    @property
    @pulumi.getter(name="utilizationThreshold")
    def utilization_threshold(self) -> Optional[pulumi.Input[str]]:
        """
        The scale-in threshold. Default is `0.5`.
        """
        return pulumi.get(self, "utilization_threshold")

    @utilization_threshold.setter
    def utilization_threshold(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "utilization_threshold", value)


class AutoscalingConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cool_down_duration: Optional[pulumi.Input[str]] = None,
                 expander: Optional[pulumi.Input[str]] = None,
                 gpu_utilization_threshold: Optional[pulumi.Input[str]] = None,
                 scale_down_enabled: Optional[pulumi.Input[bool]] = None,
                 scan_interval: Optional[pulumi.Input[str]] = None,
                 unneeded_duration: Optional[pulumi.Input[str]] = None,
                 utilization_threshold: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a AutoscalingConfig resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The id of kubernetes cluster.
        :param pulumi.Input[str] cool_down_duration: The cool down duration. Default is `10m`. If the delay (cooldown) value is set too long, there could be complaints that the Horizontal Pod Autoscaler is not responsive to workload changes. However, if the delay value is set too short, the scale of the replicas set may keep thrashing as usual.
        :param pulumi.Input[str] expander: The policy for selecting which node pool to scale. Valid values: `least-waste`, `random`, `priority`. For more information on these policies, see [Configure auto scaling](https://www.alibabacloud.com/help/en/container-service-for-kubernetes/latest/auto-scaling-of-nodes#section-3bg-2ko-inl)
        :param pulumi.Input[str] gpu_utilization_threshold: The scale-in threshold for GPU instance. Default is `0.5`.
        :param pulumi.Input[bool] scale_down_enabled: Specify whether to allow the scale-in of nodes. Default is `true`.
        :param pulumi.Input[str] scan_interval: The interval at which the cluster is reevaluated for scaling. Default is `30s`.
        :param pulumi.Input[str] unneeded_duration: The unneeded duration. Default is `10m`.
        :param pulumi.Input[str] utilization_threshold: The scale-in threshold. Default is `0.5`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AutoscalingConfigArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AutoscalingConfig resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AutoscalingConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AutoscalingConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cool_down_duration: Optional[pulumi.Input[str]] = None,
                 expander: Optional[pulumi.Input[str]] = None,
                 gpu_utilization_threshold: Optional[pulumi.Input[str]] = None,
                 scale_down_enabled: Optional[pulumi.Input[bool]] = None,
                 scan_interval: Optional[pulumi.Input[str]] = None,
                 unneeded_duration: Optional[pulumi.Input[str]] = None,
                 utilization_threshold: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AutoscalingConfigArgs.__new__(AutoscalingConfigArgs)

            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["cool_down_duration"] = cool_down_duration
            __props__.__dict__["expander"] = expander
            __props__.__dict__["gpu_utilization_threshold"] = gpu_utilization_threshold
            __props__.__dict__["scale_down_enabled"] = scale_down_enabled
            __props__.__dict__["scan_interval"] = scan_interval
            __props__.__dict__["unneeded_duration"] = unneeded_duration
            __props__.__dict__["utilization_threshold"] = utilization_threshold
        super(AutoscalingConfig, __self__).__init__(
            'alicloud:cs/autoscalingConfig:AutoscalingConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            cool_down_duration: Optional[pulumi.Input[str]] = None,
            expander: Optional[pulumi.Input[str]] = None,
            gpu_utilization_threshold: Optional[pulumi.Input[str]] = None,
            scale_down_enabled: Optional[pulumi.Input[bool]] = None,
            scan_interval: Optional[pulumi.Input[str]] = None,
            unneeded_duration: Optional[pulumi.Input[str]] = None,
            utilization_threshold: Optional[pulumi.Input[str]] = None) -> 'AutoscalingConfig':
        """
        Get an existing AutoscalingConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The id of kubernetes cluster.
        :param pulumi.Input[str] cool_down_duration: The cool down duration. Default is `10m`. If the delay (cooldown) value is set too long, there could be complaints that the Horizontal Pod Autoscaler is not responsive to workload changes. However, if the delay value is set too short, the scale of the replicas set may keep thrashing as usual.
        :param pulumi.Input[str] expander: The policy for selecting which node pool to scale. Valid values: `least-waste`, `random`, `priority`. For more information on these policies, see [Configure auto scaling](https://www.alibabacloud.com/help/en/container-service-for-kubernetes/latest/auto-scaling-of-nodes#section-3bg-2ko-inl)
        :param pulumi.Input[str] gpu_utilization_threshold: The scale-in threshold for GPU instance. Default is `0.5`.
        :param pulumi.Input[bool] scale_down_enabled: Specify whether to allow the scale-in of nodes. Default is `true`.
        :param pulumi.Input[str] scan_interval: The interval at which the cluster is reevaluated for scaling. Default is `30s`.
        :param pulumi.Input[str] unneeded_duration: The unneeded duration. Default is `10m`.
        :param pulumi.Input[str] utilization_threshold: The scale-in threshold. Default is `0.5`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AutoscalingConfigState.__new__(_AutoscalingConfigState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["cool_down_duration"] = cool_down_duration
        __props__.__dict__["expander"] = expander
        __props__.__dict__["gpu_utilization_threshold"] = gpu_utilization_threshold
        __props__.__dict__["scale_down_enabled"] = scale_down_enabled
        __props__.__dict__["scan_interval"] = scan_interval
        __props__.__dict__["unneeded_duration"] = unneeded_duration
        __props__.__dict__["utilization_threshold"] = utilization_threshold
        return AutoscalingConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[Optional[str]]:
        """
        The id of kubernetes cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="coolDownDuration")
    def cool_down_duration(self) -> pulumi.Output[Optional[str]]:
        """
        The cool down duration. Default is `10m`. If the delay (cooldown) value is set too long, there could be complaints that the Horizontal Pod Autoscaler is not responsive to workload changes. However, if the delay value is set too short, the scale of the replicas set may keep thrashing as usual.
        """
        return pulumi.get(self, "cool_down_duration")

    @property
    @pulumi.getter
    def expander(self) -> pulumi.Output[Optional[str]]:
        """
        The policy for selecting which node pool to scale. Valid values: `least-waste`, `random`, `priority`. For more information on these policies, see [Configure auto scaling](https://www.alibabacloud.com/help/en/container-service-for-kubernetes/latest/auto-scaling-of-nodes#section-3bg-2ko-inl)
        """
        return pulumi.get(self, "expander")

    @property
    @pulumi.getter(name="gpuUtilizationThreshold")
    def gpu_utilization_threshold(self) -> pulumi.Output[Optional[str]]:
        """
        The scale-in threshold for GPU instance. Default is `0.5`.
        """
        return pulumi.get(self, "gpu_utilization_threshold")

    @property
    @pulumi.getter(name="scaleDownEnabled")
    def scale_down_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Specify whether to allow the scale-in of nodes. Default is `true`.
        """
        return pulumi.get(self, "scale_down_enabled")

    @property
    @pulumi.getter(name="scanInterval")
    def scan_interval(self) -> pulumi.Output[Optional[str]]:
        """
        The interval at which the cluster is reevaluated for scaling. Default is `30s`.
        """
        return pulumi.get(self, "scan_interval")

    @property
    @pulumi.getter(name="unneededDuration")
    def unneeded_duration(self) -> pulumi.Output[Optional[str]]:
        """
        The unneeded duration. Default is `10m`.
        """
        return pulumi.get(self, "unneeded_duration")

    @property
    @pulumi.getter(name="utilizationThreshold")
    def utilization_threshold(self) -> pulumi.Output[Optional[str]]:
        """
        The scale-in threshold. Default is `0.5`.
        """
        return pulumi.get(self, "utilization_threshold")

