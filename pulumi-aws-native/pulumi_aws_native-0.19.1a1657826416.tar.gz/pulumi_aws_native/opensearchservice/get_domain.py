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

__all__ = [
    'GetDomainResult',
    'AwaitableGetDomainResult',
    'get_domain',
    'get_domain_output',
]

@pulumi.output_type
class GetDomainResult:
    def __init__(__self__, access_policies=None, advanced_options=None, arn=None, cluster_config=None, cognito_options=None, domain_arn=None, domain_endpoint=None, domain_endpoint_options=None, domain_endpoints=None, e_bs_options=None, encryption_at_rest_options=None, engine_version=None, id=None, log_publishing_options=None, node_to_node_encryption_options=None, service_software_options=None, snapshot_options=None, tags=None, v_pc_options=None):
        if access_policies and not isinstance(access_policies, dict):
            raise TypeError("Expected argument 'access_policies' to be a dict")
        pulumi.set(__self__, "access_policies", access_policies)
        if advanced_options and not isinstance(advanced_options, dict):
            raise TypeError("Expected argument 'advanced_options' to be a dict")
        pulumi.set(__self__, "advanced_options", advanced_options)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if cluster_config and not isinstance(cluster_config, dict):
            raise TypeError("Expected argument 'cluster_config' to be a dict")
        pulumi.set(__self__, "cluster_config", cluster_config)
        if cognito_options and not isinstance(cognito_options, dict):
            raise TypeError("Expected argument 'cognito_options' to be a dict")
        pulumi.set(__self__, "cognito_options", cognito_options)
        if domain_arn and not isinstance(domain_arn, str):
            raise TypeError("Expected argument 'domain_arn' to be a str")
        pulumi.set(__self__, "domain_arn", domain_arn)
        if domain_endpoint and not isinstance(domain_endpoint, str):
            raise TypeError("Expected argument 'domain_endpoint' to be a str")
        pulumi.set(__self__, "domain_endpoint", domain_endpoint)
        if domain_endpoint_options and not isinstance(domain_endpoint_options, dict):
            raise TypeError("Expected argument 'domain_endpoint_options' to be a dict")
        pulumi.set(__self__, "domain_endpoint_options", domain_endpoint_options)
        if domain_endpoints and not isinstance(domain_endpoints, dict):
            raise TypeError("Expected argument 'domain_endpoints' to be a dict")
        pulumi.set(__self__, "domain_endpoints", domain_endpoints)
        if e_bs_options and not isinstance(e_bs_options, dict):
            raise TypeError("Expected argument 'e_bs_options' to be a dict")
        pulumi.set(__self__, "e_bs_options", e_bs_options)
        if encryption_at_rest_options and not isinstance(encryption_at_rest_options, dict):
            raise TypeError("Expected argument 'encryption_at_rest_options' to be a dict")
        pulumi.set(__self__, "encryption_at_rest_options", encryption_at_rest_options)
        if engine_version and not isinstance(engine_version, str):
            raise TypeError("Expected argument 'engine_version' to be a str")
        pulumi.set(__self__, "engine_version", engine_version)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if log_publishing_options and not isinstance(log_publishing_options, dict):
            raise TypeError("Expected argument 'log_publishing_options' to be a dict")
        pulumi.set(__self__, "log_publishing_options", log_publishing_options)
        if node_to_node_encryption_options and not isinstance(node_to_node_encryption_options, dict):
            raise TypeError("Expected argument 'node_to_node_encryption_options' to be a dict")
        pulumi.set(__self__, "node_to_node_encryption_options", node_to_node_encryption_options)
        if service_software_options and not isinstance(service_software_options, dict):
            raise TypeError("Expected argument 'service_software_options' to be a dict")
        pulumi.set(__self__, "service_software_options", service_software_options)
        if snapshot_options and not isinstance(snapshot_options, dict):
            raise TypeError("Expected argument 'snapshot_options' to be a dict")
        pulumi.set(__self__, "snapshot_options", snapshot_options)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if v_pc_options and not isinstance(v_pc_options, dict):
            raise TypeError("Expected argument 'v_pc_options' to be a dict")
        pulumi.set(__self__, "v_pc_options", v_pc_options)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[Any]:
        return pulumi.get(self, "access_policies")

    @property
    @pulumi.getter(name="advancedOptions")
    def advanced_options(self) -> Optional[Any]:
        return pulumi.get(self, "advanced_options")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clusterConfig")
    def cluster_config(self) -> Optional['outputs.DomainClusterConfig']:
        return pulumi.get(self, "cluster_config")

    @property
    @pulumi.getter(name="cognitoOptions")
    def cognito_options(self) -> Optional['outputs.DomainCognitoOptions']:
        return pulumi.get(self, "cognito_options")

    @property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> Optional[str]:
        return pulumi.get(self, "domain_arn")

    @property
    @pulumi.getter(name="domainEndpoint")
    def domain_endpoint(self) -> Optional[str]:
        return pulumi.get(self, "domain_endpoint")

    @property
    @pulumi.getter(name="domainEndpointOptions")
    def domain_endpoint_options(self) -> Optional['outputs.DomainEndpointOptions']:
        return pulumi.get(self, "domain_endpoint_options")

    @property
    @pulumi.getter(name="domainEndpoints")
    def domain_endpoints(self) -> Optional[Any]:
        return pulumi.get(self, "domain_endpoints")

    @property
    @pulumi.getter(name="eBSOptions")
    def e_bs_options(self) -> Optional['outputs.DomainEBSOptions']:
        return pulumi.get(self, "e_bs_options")

    @property
    @pulumi.getter(name="encryptionAtRestOptions")
    def encryption_at_rest_options(self) -> Optional['outputs.DomainEncryptionAtRestOptions']:
        return pulumi.get(self, "encryption_at_rest_options")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[str]:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> Optional[Any]:
        return pulumi.get(self, "log_publishing_options")

    @property
    @pulumi.getter(name="nodeToNodeEncryptionOptions")
    def node_to_node_encryption_options(self) -> Optional['outputs.DomainNodeToNodeEncryptionOptions']:
        return pulumi.get(self, "node_to_node_encryption_options")

    @property
    @pulumi.getter(name="serviceSoftwareOptions")
    def service_software_options(self) -> Optional['outputs.DomainServiceSoftwareOptions']:
        return pulumi.get(self, "service_software_options")

    @property
    @pulumi.getter(name="snapshotOptions")
    def snapshot_options(self) -> Optional['outputs.DomainSnapshotOptions']:
        return pulumi.get(self, "snapshot_options")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DomainTag']]:
        """
        An arbitrary set of tags (key-value pairs) for this Domain.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vPCOptions")
    def v_pc_options(self) -> Optional['outputs.DomainVPCOptions']:
        return pulumi.get(self, "v_pc_options")


class AwaitableGetDomainResult(GetDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainResult(
            access_policies=self.access_policies,
            advanced_options=self.advanced_options,
            arn=self.arn,
            cluster_config=self.cluster_config,
            cognito_options=self.cognito_options,
            domain_arn=self.domain_arn,
            domain_endpoint=self.domain_endpoint,
            domain_endpoint_options=self.domain_endpoint_options,
            domain_endpoints=self.domain_endpoints,
            e_bs_options=self.e_bs_options,
            encryption_at_rest_options=self.encryption_at_rest_options,
            engine_version=self.engine_version,
            id=self.id,
            log_publishing_options=self.log_publishing_options,
            node_to_node_encryption_options=self.node_to_node_encryption_options,
            service_software_options=self.service_software_options,
            snapshot_options=self.snapshot_options,
            tags=self.tags,
            v_pc_options=self.v_pc_options)


def get_domain(domain_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainResult:
    """
    An example resource schema demonstrating some basic constructs and validation rules.
    """
    __args__ = dict()
    __args__['domainName'] = domain_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:opensearchservice:getDomain', __args__, opts=opts, typ=GetDomainResult).value

    return AwaitableGetDomainResult(
        access_policies=__ret__.access_policies,
        advanced_options=__ret__.advanced_options,
        arn=__ret__.arn,
        cluster_config=__ret__.cluster_config,
        cognito_options=__ret__.cognito_options,
        domain_arn=__ret__.domain_arn,
        domain_endpoint=__ret__.domain_endpoint,
        domain_endpoint_options=__ret__.domain_endpoint_options,
        domain_endpoints=__ret__.domain_endpoints,
        e_bs_options=__ret__.e_bs_options,
        encryption_at_rest_options=__ret__.encryption_at_rest_options,
        engine_version=__ret__.engine_version,
        id=__ret__.id,
        log_publishing_options=__ret__.log_publishing_options,
        node_to_node_encryption_options=__ret__.node_to_node_encryption_options,
        service_software_options=__ret__.service_software_options,
        snapshot_options=__ret__.snapshot_options,
        tags=__ret__.tags,
        v_pc_options=__ret__.v_pc_options)


@_utilities.lift_output_func(get_domain)
def get_domain_output(domain_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainResult]:
    """
    An example resource schema demonstrating some basic constructs and validation rules.
    """
    ...
