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

__all__ = ['DomainArgs', 'Domain']

@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *,
                 access_policies: Optional[Any] = None,
                 advanced_options: Optional[Any] = None,
                 advanced_security_options: Optional[pulumi.Input['DomainAdvancedSecurityOptionsInputArgs']] = None,
                 cognito_options: Optional[pulumi.Input['DomainCognitoOptionsArgs']] = None,
                 domain_endpoint_options: Optional[pulumi.Input['DomainEndpointOptionsArgs']] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 e_bs_options: Optional[pulumi.Input['DomainEBSOptionsArgs']] = None,
                 elasticsearch_cluster_config: Optional[pulumi.Input['DomainElasticsearchClusterConfigArgs']] = None,
                 elasticsearch_version: Optional[pulumi.Input[str]] = None,
                 encryption_at_rest_options: Optional[pulumi.Input['DomainEncryptionAtRestOptionsArgs']] = None,
                 log_publishing_options: Optional[Any] = None,
                 node_to_node_encryption_options: Optional[pulumi.Input['DomainNodeToNodeEncryptionOptionsArgs']] = None,
                 snapshot_options: Optional[pulumi.Input['DomainSnapshotOptionsArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]]] = None,
                 v_pc_options: Optional[pulumi.Input['DomainVPCOptionsArgs']] = None):
        """
        The set of arguments for constructing a Domain resource.
        """
        if access_policies is not None:
            pulumi.set(__self__, "access_policies", access_policies)
        if advanced_options is not None:
            pulumi.set(__self__, "advanced_options", advanced_options)
        if advanced_security_options is not None:
            pulumi.set(__self__, "advanced_security_options", advanced_security_options)
        if cognito_options is not None:
            pulumi.set(__self__, "cognito_options", cognito_options)
        if domain_endpoint_options is not None:
            pulumi.set(__self__, "domain_endpoint_options", domain_endpoint_options)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if e_bs_options is not None:
            pulumi.set(__self__, "e_bs_options", e_bs_options)
        if elasticsearch_cluster_config is not None:
            pulumi.set(__self__, "elasticsearch_cluster_config", elasticsearch_cluster_config)
        if elasticsearch_version is not None:
            pulumi.set(__self__, "elasticsearch_version", elasticsearch_version)
        if encryption_at_rest_options is not None:
            pulumi.set(__self__, "encryption_at_rest_options", encryption_at_rest_options)
        if log_publishing_options is not None:
            pulumi.set(__self__, "log_publishing_options", log_publishing_options)
        if node_to_node_encryption_options is not None:
            pulumi.set(__self__, "node_to_node_encryption_options", node_to_node_encryption_options)
        if snapshot_options is not None:
            pulumi.set(__self__, "snapshot_options", snapshot_options)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if v_pc_options is not None:
            pulumi.set(__self__, "v_pc_options", v_pc_options)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[Any]:
        return pulumi.get(self, "access_policies")

    @access_policies.setter
    def access_policies(self, value: Optional[Any]):
        pulumi.set(self, "access_policies", value)

    @property
    @pulumi.getter(name="advancedOptions")
    def advanced_options(self) -> Optional[Any]:
        return pulumi.get(self, "advanced_options")

    @advanced_options.setter
    def advanced_options(self, value: Optional[Any]):
        pulumi.set(self, "advanced_options", value)

    @property
    @pulumi.getter(name="advancedSecurityOptions")
    def advanced_security_options(self) -> Optional[pulumi.Input['DomainAdvancedSecurityOptionsInputArgs']]:
        return pulumi.get(self, "advanced_security_options")

    @advanced_security_options.setter
    def advanced_security_options(self, value: Optional[pulumi.Input['DomainAdvancedSecurityOptionsInputArgs']]):
        pulumi.set(self, "advanced_security_options", value)

    @property
    @pulumi.getter(name="cognitoOptions")
    def cognito_options(self) -> Optional[pulumi.Input['DomainCognitoOptionsArgs']]:
        return pulumi.get(self, "cognito_options")

    @cognito_options.setter
    def cognito_options(self, value: Optional[pulumi.Input['DomainCognitoOptionsArgs']]):
        pulumi.set(self, "cognito_options", value)

    @property
    @pulumi.getter(name="domainEndpointOptions")
    def domain_endpoint_options(self) -> Optional[pulumi.Input['DomainEndpointOptionsArgs']]:
        return pulumi.get(self, "domain_endpoint_options")

    @domain_endpoint_options.setter
    def domain_endpoint_options(self, value: Optional[pulumi.Input['DomainEndpointOptionsArgs']]):
        pulumi.set(self, "domain_endpoint_options", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="eBSOptions")
    def e_bs_options(self) -> Optional[pulumi.Input['DomainEBSOptionsArgs']]:
        return pulumi.get(self, "e_bs_options")

    @e_bs_options.setter
    def e_bs_options(self, value: Optional[pulumi.Input['DomainEBSOptionsArgs']]):
        pulumi.set(self, "e_bs_options", value)

    @property
    @pulumi.getter(name="elasticsearchClusterConfig")
    def elasticsearch_cluster_config(self) -> Optional[pulumi.Input['DomainElasticsearchClusterConfigArgs']]:
        return pulumi.get(self, "elasticsearch_cluster_config")

    @elasticsearch_cluster_config.setter
    def elasticsearch_cluster_config(self, value: Optional[pulumi.Input['DomainElasticsearchClusterConfigArgs']]):
        pulumi.set(self, "elasticsearch_cluster_config", value)

    @property
    @pulumi.getter(name="elasticsearchVersion")
    def elasticsearch_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "elasticsearch_version")

    @elasticsearch_version.setter
    def elasticsearch_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "elasticsearch_version", value)

    @property
    @pulumi.getter(name="encryptionAtRestOptions")
    def encryption_at_rest_options(self) -> Optional[pulumi.Input['DomainEncryptionAtRestOptionsArgs']]:
        return pulumi.get(self, "encryption_at_rest_options")

    @encryption_at_rest_options.setter
    def encryption_at_rest_options(self, value: Optional[pulumi.Input['DomainEncryptionAtRestOptionsArgs']]):
        pulumi.set(self, "encryption_at_rest_options", value)

    @property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> Optional[Any]:
        return pulumi.get(self, "log_publishing_options")

    @log_publishing_options.setter
    def log_publishing_options(self, value: Optional[Any]):
        pulumi.set(self, "log_publishing_options", value)

    @property
    @pulumi.getter(name="nodeToNodeEncryptionOptions")
    def node_to_node_encryption_options(self) -> Optional[pulumi.Input['DomainNodeToNodeEncryptionOptionsArgs']]:
        return pulumi.get(self, "node_to_node_encryption_options")

    @node_to_node_encryption_options.setter
    def node_to_node_encryption_options(self, value: Optional[pulumi.Input['DomainNodeToNodeEncryptionOptionsArgs']]):
        pulumi.set(self, "node_to_node_encryption_options", value)

    @property
    @pulumi.getter(name="snapshotOptions")
    def snapshot_options(self) -> Optional[pulumi.Input['DomainSnapshotOptionsArgs']]:
        return pulumi.get(self, "snapshot_options")

    @snapshot_options.setter
    def snapshot_options(self, value: Optional[pulumi.Input['DomainSnapshotOptionsArgs']]):
        pulumi.set(self, "snapshot_options", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vPCOptions")
    def v_pc_options(self) -> Optional[pulumi.Input['DomainVPCOptionsArgs']]:
        return pulumi.get(self, "v_pc_options")

    @v_pc_options.setter
    def v_pc_options(self, value: Optional[pulumi.Input['DomainVPCOptionsArgs']]):
        pulumi.set(self, "v_pc_options", value)


warnings.warn("""Domain is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Domain(pulumi.CustomResource):
    warnings.warn("""Domain is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_policies: Optional[Any] = None,
                 advanced_options: Optional[Any] = None,
                 advanced_security_options: Optional[pulumi.Input[pulumi.InputType['DomainAdvancedSecurityOptionsInputArgs']]] = None,
                 cognito_options: Optional[pulumi.Input[pulumi.InputType['DomainCognitoOptionsArgs']]] = None,
                 domain_endpoint_options: Optional[pulumi.Input[pulumi.InputType['DomainEndpointOptionsArgs']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 e_bs_options: Optional[pulumi.Input[pulumi.InputType['DomainEBSOptionsArgs']]] = None,
                 elasticsearch_cluster_config: Optional[pulumi.Input[pulumi.InputType['DomainElasticsearchClusterConfigArgs']]] = None,
                 elasticsearch_version: Optional[pulumi.Input[str]] = None,
                 encryption_at_rest_options: Optional[pulumi.Input[pulumi.InputType['DomainEncryptionAtRestOptionsArgs']]] = None,
                 log_publishing_options: Optional[Any] = None,
                 node_to_node_encryption_options: Optional[pulumi.Input[pulumi.InputType['DomainNodeToNodeEncryptionOptionsArgs']]] = None,
                 snapshot_options: Optional[pulumi.Input[pulumi.InputType['DomainSnapshotOptionsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTagArgs']]]]] = None,
                 v_pc_options: Optional[pulumi.Input[pulumi.InputType['DomainVPCOptionsArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Elasticsearch::Domain

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DomainArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Elasticsearch::Domain

        :param str resource_name: The name of the resource.
        :param DomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_policies: Optional[Any] = None,
                 advanced_options: Optional[Any] = None,
                 advanced_security_options: Optional[pulumi.Input[pulumi.InputType['DomainAdvancedSecurityOptionsInputArgs']]] = None,
                 cognito_options: Optional[pulumi.Input[pulumi.InputType['DomainCognitoOptionsArgs']]] = None,
                 domain_endpoint_options: Optional[pulumi.Input[pulumi.InputType['DomainEndpointOptionsArgs']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 e_bs_options: Optional[pulumi.Input[pulumi.InputType['DomainEBSOptionsArgs']]] = None,
                 elasticsearch_cluster_config: Optional[pulumi.Input[pulumi.InputType['DomainElasticsearchClusterConfigArgs']]] = None,
                 elasticsearch_version: Optional[pulumi.Input[str]] = None,
                 encryption_at_rest_options: Optional[pulumi.Input[pulumi.InputType['DomainEncryptionAtRestOptionsArgs']]] = None,
                 log_publishing_options: Optional[Any] = None,
                 node_to_node_encryption_options: Optional[pulumi.Input[pulumi.InputType['DomainNodeToNodeEncryptionOptionsArgs']]] = None,
                 snapshot_options: Optional[pulumi.Input[pulumi.InputType['DomainSnapshotOptionsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTagArgs']]]]] = None,
                 v_pc_options: Optional[pulumi.Input[pulumi.InputType['DomainVPCOptionsArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""Domain is deprecated: Domain is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = DomainArgs.__new__(DomainArgs)

            __props__.__dict__["access_policies"] = access_policies
            __props__.__dict__["advanced_options"] = advanced_options
            __props__.__dict__["advanced_security_options"] = advanced_security_options
            __props__.__dict__["cognito_options"] = cognito_options
            __props__.__dict__["domain_endpoint_options"] = domain_endpoint_options
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["e_bs_options"] = e_bs_options
            __props__.__dict__["elasticsearch_cluster_config"] = elasticsearch_cluster_config
            __props__.__dict__["elasticsearch_version"] = elasticsearch_version
            __props__.__dict__["encryption_at_rest_options"] = encryption_at_rest_options
            __props__.__dict__["log_publishing_options"] = log_publishing_options
            __props__.__dict__["node_to_node_encryption_options"] = node_to_node_encryption_options
            __props__.__dict__["snapshot_options"] = snapshot_options
            __props__.__dict__["tags"] = tags
            __props__.__dict__["v_pc_options"] = v_pc_options
            __props__.__dict__["arn"] = None
            __props__.__dict__["domain_arn"] = None
            __props__.__dict__["domain_endpoint"] = None
        super(Domain, __self__).__init__(
            'aws-native:elasticsearch:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DomainArgs.__new__(DomainArgs)

        __props__.__dict__["access_policies"] = None
        __props__.__dict__["advanced_options"] = None
        __props__.__dict__["advanced_security_options"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["cognito_options"] = None
        __props__.__dict__["domain_arn"] = None
        __props__.__dict__["domain_endpoint"] = None
        __props__.__dict__["domain_endpoint_options"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["e_bs_options"] = None
        __props__.__dict__["elasticsearch_cluster_config"] = None
        __props__.__dict__["elasticsearch_version"] = None
        __props__.__dict__["encryption_at_rest_options"] = None
        __props__.__dict__["log_publishing_options"] = None
        __props__.__dict__["node_to_node_encryption_options"] = None
        __props__.__dict__["snapshot_options"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["v_pc_options"] = None
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "access_policies")

    @property
    @pulumi.getter(name="advancedOptions")
    def advanced_options(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "advanced_options")

    @property
    @pulumi.getter(name="advancedSecurityOptions")
    def advanced_security_options(self) -> pulumi.Output[Optional['outputs.DomainAdvancedSecurityOptionsInput']]:
        return pulumi.get(self, "advanced_security_options")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="cognitoOptions")
    def cognito_options(self) -> pulumi.Output[Optional['outputs.DomainCognitoOptions']]:
        return pulumi.get(self, "cognito_options")

    @property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "domain_arn")

    @property
    @pulumi.getter(name="domainEndpoint")
    def domain_endpoint(self) -> pulumi.Output[str]:
        return pulumi.get(self, "domain_endpoint")

    @property
    @pulumi.getter(name="domainEndpointOptions")
    def domain_endpoint_options(self) -> pulumi.Output[Optional['outputs.DomainEndpointOptions']]:
        return pulumi.get(self, "domain_endpoint_options")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="eBSOptions")
    def e_bs_options(self) -> pulumi.Output[Optional['outputs.DomainEBSOptions']]:
        return pulumi.get(self, "e_bs_options")

    @property
    @pulumi.getter(name="elasticsearchClusterConfig")
    def elasticsearch_cluster_config(self) -> pulumi.Output[Optional['outputs.DomainElasticsearchClusterConfig']]:
        return pulumi.get(self, "elasticsearch_cluster_config")

    @property
    @pulumi.getter(name="elasticsearchVersion")
    def elasticsearch_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "elasticsearch_version")

    @property
    @pulumi.getter(name="encryptionAtRestOptions")
    def encryption_at_rest_options(self) -> pulumi.Output[Optional['outputs.DomainEncryptionAtRestOptions']]:
        return pulumi.get(self, "encryption_at_rest_options")

    @property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "log_publishing_options")

    @property
    @pulumi.getter(name="nodeToNodeEncryptionOptions")
    def node_to_node_encryption_options(self) -> pulumi.Output[Optional['outputs.DomainNodeToNodeEncryptionOptions']]:
        return pulumi.get(self, "node_to_node_encryption_options")

    @property
    @pulumi.getter(name="snapshotOptions")
    def snapshot_options(self) -> pulumi.Output[Optional['outputs.DomainSnapshotOptions']]:
        return pulumi.get(self, "snapshot_options")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DomainTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vPCOptions")
    def v_pc_options(self) -> pulumi.Output[Optional['outputs.DomainVPCOptions']]:
        return pulumi.get(self, "v_pc_options")

