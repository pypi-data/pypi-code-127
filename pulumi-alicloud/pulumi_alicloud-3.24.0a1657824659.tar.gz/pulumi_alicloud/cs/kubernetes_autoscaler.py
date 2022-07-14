# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['KubernetesAutoscalerArgs', 'KubernetesAutoscaler']

@pulumi.input_type
class KubernetesAutoscalerArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 cool_down_duration: pulumi.Input[str],
                 defer_scale_in_duration: pulumi.Input[str],
                 utilization: pulumi.Input[str],
                 nodepools: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesAutoscalerNodepoolArgs']]]] = None,
                 use_ecs_ram_role_token: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a KubernetesAutoscaler resource.
        :param pulumi.Input[str] cluster_id: The id of kubernetes cluster.
        :param pulumi.Input[str] cool_down_duration: The cool_down_duration option of cluster-autoscaler.
        :param pulumi.Input[str] defer_scale_in_duration: The defer_scale_in_duration option of cluster-autoscaler.
        :param pulumi.Input[str] utilization: The utilization option of cluster-autoscaler.
        :param pulumi.Input[Sequence[pulumi.Input['KubernetesAutoscalerNodepoolArgs']]] nodepools: * `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
               * `nodepools.taints` - (Required) The taints for the nodes in scaling group.
               * `nodepools.labels` - (Required) The labels for the nodes in scaling group.
        :param pulumi.Input[bool] use_ecs_ram_role_token: Enable autoscaler access to alibabacloud service by ecs ramrole token. default: false
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "cool_down_duration", cool_down_duration)
        pulumi.set(__self__, "defer_scale_in_duration", defer_scale_in_duration)
        pulumi.set(__self__, "utilization", utilization)
        if nodepools is not None:
            pulumi.set(__self__, "nodepools", nodepools)
        if use_ecs_ram_role_token is not None:
            pulumi.set(__self__, "use_ecs_ram_role_token", use_ecs_ram_role_token)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The id of kubernetes cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="coolDownDuration")
    def cool_down_duration(self) -> pulumi.Input[str]:
        """
        The cool_down_duration option of cluster-autoscaler.
        """
        return pulumi.get(self, "cool_down_duration")

    @cool_down_duration.setter
    def cool_down_duration(self, value: pulumi.Input[str]):
        pulumi.set(self, "cool_down_duration", value)

    @property
    @pulumi.getter(name="deferScaleInDuration")
    def defer_scale_in_duration(self) -> pulumi.Input[str]:
        """
        The defer_scale_in_duration option of cluster-autoscaler.
        """
        return pulumi.get(self, "defer_scale_in_duration")

    @defer_scale_in_duration.setter
    def defer_scale_in_duration(self, value: pulumi.Input[str]):
        pulumi.set(self, "defer_scale_in_duration", value)

    @property
    @pulumi.getter
    def utilization(self) -> pulumi.Input[str]:
        """
        The utilization option of cluster-autoscaler.
        """
        return pulumi.get(self, "utilization")

    @utilization.setter
    def utilization(self, value: pulumi.Input[str]):
        pulumi.set(self, "utilization", value)

    @property
    @pulumi.getter
    def nodepools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesAutoscalerNodepoolArgs']]]]:
        """
        * `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
        * `nodepools.taints` - (Required) The taints for the nodes in scaling group.
        * `nodepools.labels` - (Required) The labels for the nodes in scaling group.
        """
        return pulumi.get(self, "nodepools")

    @nodepools.setter
    def nodepools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesAutoscalerNodepoolArgs']]]]):
        pulumi.set(self, "nodepools", value)

    @property
    @pulumi.getter(name="useEcsRamRoleToken")
    def use_ecs_ram_role_token(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable autoscaler access to alibabacloud service by ecs ramrole token. default: false
        """
        return pulumi.get(self, "use_ecs_ram_role_token")

    @use_ecs_ram_role_token.setter
    def use_ecs_ram_role_token(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_ecs_ram_role_token", value)


@pulumi.input_type
class _KubernetesAutoscalerState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cool_down_duration: Optional[pulumi.Input[str]] = None,
                 defer_scale_in_duration: Optional[pulumi.Input[str]] = None,
                 nodepools: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesAutoscalerNodepoolArgs']]]] = None,
                 use_ecs_ram_role_token: Optional[pulumi.Input[bool]] = None,
                 utilization: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering KubernetesAutoscaler resources.
        :param pulumi.Input[str] cluster_id: The id of kubernetes cluster.
        :param pulumi.Input[str] cool_down_duration: The cool_down_duration option of cluster-autoscaler.
        :param pulumi.Input[str] defer_scale_in_duration: The defer_scale_in_duration option of cluster-autoscaler.
        :param pulumi.Input[Sequence[pulumi.Input['KubernetesAutoscalerNodepoolArgs']]] nodepools: * `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
               * `nodepools.taints` - (Required) The taints for the nodes in scaling group.
               * `nodepools.labels` - (Required) The labels for the nodes in scaling group.
        :param pulumi.Input[bool] use_ecs_ram_role_token: Enable autoscaler access to alibabacloud service by ecs ramrole token. default: false
        :param pulumi.Input[str] utilization: The utilization option of cluster-autoscaler.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if cool_down_duration is not None:
            pulumi.set(__self__, "cool_down_duration", cool_down_duration)
        if defer_scale_in_duration is not None:
            pulumi.set(__self__, "defer_scale_in_duration", defer_scale_in_duration)
        if nodepools is not None:
            pulumi.set(__self__, "nodepools", nodepools)
        if use_ecs_ram_role_token is not None:
            pulumi.set(__self__, "use_ecs_ram_role_token", use_ecs_ram_role_token)
        if utilization is not None:
            pulumi.set(__self__, "utilization", utilization)

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
        The cool_down_duration option of cluster-autoscaler.
        """
        return pulumi.get(self, "cool_down_duration")

    @cool_down_duration.setter
    def cool_down_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cool_down_duration", value)

    @property
    @pulumi.getter(name="deferScaleInDuration")
    def defer_scale_in_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The defer_scale_in_duration option of cluster-autoscaler.
        """
        return pulumi.get(self, "defer_scale_in_duration")

    @defer_scale_in_duration.setter
    def defer_scale_in_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "defer_scale_in_duration", value)

    @property
    @pulumi.getter
    def nodepools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesAutoscalerNodepoolArgs']]]]:
        """
        * `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
        * `nodepools.taints` - (Required) The taints for the nodes in scaling group.
        * `nodepools.labels` - (Required) The labels for the nodes in scaling group.
        """
        return pulumi.get(self, "nodepools")

    @nodepools.setter
    def nodepools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesAutoscalerNodepoolArgs']]]]):
        pulumi.set(self, "nodepools", value)

    @property
    @pulumi.getter(name="useEcsRamRoleToken")
    def use_ecs_ram_role_token(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable autoscaler access to alibabacloud service by ecs ramrole token. default: false
        """
        return pulumi.get(self, "use_ecs_ram_role_token")

    @use_ecs_ram_role_token.setter
    def use_ecs_ram_role_token(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_ecs_ram_role_token", value)

    @property
    @pulumi.getter
    def utilization(self) -> Optional[pulumi.Input[str]]:
        """
        The utilization option of cluster-autoscaler.
        """
        return pulumi.get(self, "utilization")

    @utilization.setter
    def utilization(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "utilization", value)


class KubernetesAutoscaler(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cool_down_duration: Optional[pulumi.Input[str]] = None,
                 defer_scale_in_duration: Optional[pulumi.Input[str]] = None,
                 nodepools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KubernetesAutoscalerNodepoolArgs']]]]] = None,
                 use_ecs_ram_role_token: Optional[pulumi.Input[bool]] = None,
                 utilization: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        cluster-autoscaler in Kubernetes Cluster.

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "autoscaler"
        default_networks = alicloud.vpc.get_networks()
        default_images = alicloud.ecs.get_images(owners="system",
            name_regex="^centos_7",
            most_recent=True)
        default_managed_kubernetes_clusters = alicloud.cs.get_managed_kubernetes_clusters()
        default_instance_types = alicloud.ecs.get_instance_types(cpu_core_count=2,
            memory_size=4)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_networks.vpcs[0].id)
        default_scaling_group = alicloud.ess.ScalingGroup("defaultScalingGroup",
            scaling_group_name=name,
            min_size=var["min_size"],
            max_size=var["max_size"],
            vswitch_ids=[default_networks.vpcs[0].vswitch_ids[0]],
            removal_policies=[
                "OldestInstance",
                "NewestInstance",
            ])
        default_scaling_configuration = alicloud.ess.ScalingConfiguration("defaultScalingConfiguration",
            image_id=default_images.images[0].id,
            security_group_id=default_security_group.id,
            scaling_group_id=default_scaling_group.id,
            instance_type=default_instance_types.instance_types[0].id,
            internet_charge_type="PayByTraffic",
            force_delete=True,
            enable=True,
            active=True)
        default_kubernetes_autoscaler = alicloud.cs.KubernetesAutoscaler("defaultKubernetesAutoscaler",
            cluster_id=default_managed_kubernetes_clusters.clusters[0].id,
            nodepools=[alicloud.cs.KubernetesAutoscalerNodepoolArgs(
                id=default_scaling_group.id,
                labels="a=b",
            )],
            utilization=var["utilization"],
            cool_down_duration=var["cool_down_duration"],
            defer_scale_in_duration=var["defer_scale_in_duration"],
            opts=pulumi.ResourceOptions(depends_on=[
                    alicloud_ess_scaling_group["defalut"],
                    default_scaling_configuration,
                ]))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The id of kubernetes cluster.
        :param pulumi.Input[str] cool_down_duration: The cool_down_duration option of cluster-autoscaler.
        :param pulumi.Input[str] defer_scale_in_duration: The defer_scale_in_duration option of cluster-autoscaler.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KubernetesAutoscalerNodepoolArgs']]]] nodepools: * `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
               * `nodepools.taints` - (Required) The taints for the nodes in scaling group.
               * `nodepools.labels` - (Required) The labels for the nodes in scaling group.
        :param pulumi.Input[bool] use_ecs_ram_role_token: Enable autoscaler access to alibabacloud service by ecs ramrole token. default: false
        :param pulumi.Input[str] utilization: The utilization option of cluster-autoscaler.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KubernetesAutoscalerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        cluster-autoscaler in Kubernetes Cluster.

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "autoscaler"
        default_networks = alicloud.vpc.get_networks()
        default_images = alicloud.ecs.get_images(owners="system",
            name_regex="^centos_7",
            most_recent=True)
        default_managed_kubernetes_clusters = alicloud.cs.get_managed_kubernetes_clusters()
        default_instance_types = alicloud.ecs.get_instance_types(cpu_core_count=2,
            memory_size=4)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_networks.vpcs[0].id)
        default_scaling_group = alicloud.ess.ScalingGroup("defaultScalingGroup",
            scaling_group_name=name,
            min_size=var["min_size"],
            max_size=var["max_size"],
            vswitch_ids=[default_networks.vpcs[0].vswitch_ids[0]],
            removal_policies=[
                "OldestInstance",
                "NewestInstance",
            ])
        default_scaling_configuration = alicloud.ess.ScalingConfiguration("defaultScalingConfiguration",
            image_id=default_images.images[0].id,
            security_group_id=default_security_group.id,
            scaling_group_id=default_scaling_group.id,
            instance_type=default_instance_types.instance_types[0].id,
            internet_charge_type="PayByTraffic",
            force_delete=True,
            enable=True,
            active=True)
        default_kubernetes_autoscaler = alicloud.cs.KubernetesAutoscaler("defaultKubernetesAutoscaler",
            cluster_id=default_managed_kubernetes_clusters.clusters[0].id,
            nodepools=[alicloud.cs.KubernetesAutoscalerNodepoolArgs(
                id=default_scaling_group.id,
                labels="a=b",
            )],
            utilization=var["utilization"],
            cool_down_duration=var["cool_down_duration"],
            defer_scale_in_duration=var["defer_scale_in_duration"],
            opts=pulumi.ResourceOptions(depends_on=[
                    alicloud_ess_scaling_group["defalut"],
                    default_scaling_configuration,
                ]))
        ```

        :param str resource_name: The name of the resource.
        :param KubernetesAutoscalerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KubernetesAutoscalerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cool_down_duration: Optional[pulumi.Input[str]] = None,
                 defer_scale_in_duration: Optional[pulumi.Input[str]] = None,
                 nodepools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KubernetesAutoscalerNodepoolArgs']]]]] = None,
                 use_ecs_ram_role_token: Optional[pulumi.Input[bool]] = None,
                 utilization: Optional[pulumi.Input[str]] = None,
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
            __props__ = KubernetesAutoscalerArgs.__new__(KubernetesAutoscalerArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            if cool_down_duration is None and not opts.urn:
                raise TypeError("Missing required property 'cool_down_duration'")
            __props__.__dict__["cool_down_duration"] = cool_down_duration
            if defer_scale_in_duration is None and not opts.urn:
                raise TypeError("Missing required property 'defer_scale_in_duration'")
            __props__.__dict__["defer_scale_in_duration"] = defer_scale_in_duration
            __props__.__dict__["nodepools"] = nodepools
            __props__.__dict__["use_ecs_ram_role_token"] = use_ecs_ram_role_token
            if utilization is None and not opts.urn:
                raise TypeError("Missing required property 'utilization'")
            __props__.__dict__["utilization"] = utilization
        super(KubernetesAutoscaler, __self__).__init__(
            'alicloud:cs/kubernetesAutoscaler:KubernetesAutoscaler',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            cool_down_duration: Optional[pulumi.Input[str]] = None,
            defer_scale_in_duration: Optional[pulumi.Input[str]] = None,
            nodepools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KubernetesAutoscalerNodepoolArgs']]]]] = None,
            use_ecs_ram_role_token: Optional[pulumi.Input[bool]] = None,
            utilization: Optional[pulumi.Input[str]] = None) -> 'KubernetesAutoscaler':
        """
        Get an existing KubernetesAutoscaler resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The id of kubernetes cluster.
        :param pulumi.Input[str] cool_down_duration: The cool_down_duration option of cluster-autoscaler.
        :param pulumi.Input[str] defer_scale_in_duration: The defer_scale_in_duration option of cluster-autoscaler.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KubernetesAutoscalerNodepoolArgs']]]] nodepools: * `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
               * `nodepools.taints` - (Required) The taints for the nodes in scaling group.
               * `nodepools.labels` - (Required) The labels for the nodes in scaling group.
        :param pulumi.Input[bool] use_ecs_ram_role_token: Enable autoscaler access to alibabacloud service by ecs ramrole token. default: false
        :param pulumi.Input[str] utilization: The utilization option of cluster-autoscaler.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KubernetesAutoscalerState.__new__(_KubernetesAutoscalerState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["cool_down_duration"] = cool_down_duration
        __props__.__dict__["defer_scale_in_duration"] = defer_scale_in_duration
        __props__.__dict__["nodepools"] = nodepools
        __props__.__dict__["use_ecs_ram_role_token"] = use_ecs_ram_role_token
        __props__.__dict__["utilization"] = utilization
        return KubernetesAutoscaler(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The id of kubernetes cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="coolDownDuration")
    def cool_down_duration(self) -> pulumi.Output[str]:
        """
        The cool_down_duration option of cluster-autoscaler.
        """
        return pulumi.get(self, "cool_down_duration")

    @property
    @pulumi.getter(name="deferScaleInDuration")
    def defer_scale_in_duration(self) -> pulumi.Output[str]:
        """
        The defer_scale_in_duration option of cluster-autoscaler.
        """
        return pulumi.get(self, "defer_scale_in_duration")

    @property
    @pulumi.getter
    def nodepools(self) -> pulumi.Output[Optional[Sequence['outputs.KubernetesAutoscalerNodepool']]]:
        """
        * `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
        * `nodepools.taints` - (Required) The taints for the nodes in scaling group.
        * `nodepools.labels` - (Required) The labels for the nodes in scaling group.
        """
        return pulumi.get(self, "nodepools")

    @property
    @pulumi.getter(name="useEcsRamRoleToken")
    def use_ecs_ram_role_token(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable autoscaler access to alibabacloud service by ecs ramrole token. default: false
        """
        return pulumi.get(self, "use_ecs_ram_role_token")

    @property
    @pulumi.getter
    def utilization(self) -> pulumi.Output[str]:
        """
        The utilization option of cluster-autoscaler.
        """
        return pulumi.get(self, "utilization")

