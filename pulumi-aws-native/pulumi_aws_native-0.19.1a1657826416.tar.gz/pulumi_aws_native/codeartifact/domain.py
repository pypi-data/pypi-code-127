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
                 domain_name: Optional[pulumi.Input[str]] = None,
                 encryption_key: Optional[pulumi.Input[str]] = None,
                 permissions_policy_document: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]]] = None):
        """
        The set of arguments for constructing a Domain resource.
        :param pulumi.Input[str] domain_name: The name of the domain.
        :param pulumi.Input[str] encryption_key: The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.
        :param Any permissions_policy_document: The access control resource policy on the provided domain.
        :param pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if encryption_key is not None:
            pulumi.set(__self__, "encryption_key", encryption_key)
        if permissions_policy_document is not None:
            pulumi.set(__self__, "permissions_policy_document", permissions_policy_document)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the domain.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.
        """
        return pulumi.get(self, "encryption_key")

    @encryption_key.setter
    def encryption_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_key", value)

    @property
    @pulumi.getter(name="permissionsPolicyDocument")
    def permissions_policy_document(self) -> Optional[Any]:
        """
        The access control resource policy on the provided domain.
        """
        return pulumi.get(self, "permissions_policy_document")

    @permissions_policy_document.setter
    def permissions_policy_document(self, value: Optional[Any]):
        pulumi.set(self, "permissions_policy_document", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 encryption_key: Optional[pulumi.Input[str]] = None,
                 permissions_policy_document: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTagArgs']]]]] = None,
                 __props__=None):
        """
        The resource schema to create a CodeArtifact domain.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: The name of the domain.
        :param pulumi.Input[str] encryption_key: The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.
        :param Any permissions_policy_document: The access control resource policy on the provided domain.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DomainArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The resource schema to create a CodeArtifact domain.

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
                 domain_name: Optional[pulumi.Input[str]] = None,
                 encryption_key: Optional[pulumi.Input[str]] = None,
                 permissions_policy_document: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTagArgs']]]]] = None,
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
            __props__ = DomainArgs.__new__(DomainArgs)

            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["encryption_key"] = encryption_key
            __props__.__dict__["permissions_policy_document"] = permissions_policy_document
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["owner"] = None
        super(Domain, __self__).__init__(
            'aws-native:codeartifact:Domain',
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

        __props__.__dict__["arn"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["encryption_key"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["owner"] = None
        __props__.__dict__["permissions_policy_document"] = None
        __props__.__dict__["tags"] = None
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the domain.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The name of the domain.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> pulumi.Output[str]:
        """
        The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.
        """
        return pulumi.get(self, "encryption_key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the domain. This field is used for GetAtt
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        The 12-digit account ID of the AWS account that owns the domain. This field is used for GetAtt
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="permissionsPolicyDocument")
    def permissions_policy_document(self) -> pulumi.Output[Optional[Any]]:
        """
        The access control resource policy on the provided domain.
        """
        return pulumi.get(self, "permissions_policy_document")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DomainTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

