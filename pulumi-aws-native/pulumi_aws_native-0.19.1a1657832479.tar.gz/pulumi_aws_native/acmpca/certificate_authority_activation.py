# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CertificateAuthorityActivationArgs', 'CertificateAuthorityActivation']

@pulumi.input_type
class CertificateAuthorityActivationArgs:
    def __init__(__self__, *,
                 certificate: pulumi.Input[str],
                 certificate_authority_arn: pulumi.Input[str],
                 certificate_chain: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CertificateAuthorityActivation resource.
        :param pulumi.Input[str] certificate: Certificate Authority certificate that will be installed in the Certificate Authority.
        :param pulumi.Input[str] certificate_authority_arn: Arn of the Certificate Authority.
        :param pulumi.Input[str] certificate_chain: Certificate chain for the Certificate Authority certificate.
        :param pulumi.Input[str] status: The status of the Certificate Authority.
        """
        pulumi.set(__self__, "certificate", certificate)
        pulumi.set(__self__, "certificate_authority_arn", certificate_authority_arn)
        if certificate_chain is not None:
            pulumi.set(__self__, "certificate_chain", certificate_chain)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Input[str]:
        """
        Certificate Authority certificate that will be installed in the Certificate Authority.
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> pulumi.Input[str]:
        """
        Arn of the Certificate Authority.
        """
        return pulumi.get(self, "certificate_authority_arn")

    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate_authority_arn", value)

    @property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> Optional[pulumi.Input[str]]:
        """
        Certificate chain for the Certificate Authority certificate.
        """
        return pulumi.get(self, "certificate_chain")

    @certificate_chain.setter
    def certificate_chain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_chain", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the Certificate Authority.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class CertificateAuthorityActivation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 certificate_authority_arn: Optional[pulumi.Input[str]] = None,
                 certificate_chain: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Used to install the certificate authority certificate and update the certificate authority status.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate: Certificate Authority certificate that will be installed in the Certificate Authority.
        :param pulumi.Input[str] certificate_authority_arn: Arn of the Certificate Authority.
        :param pulumi.Input[str] certificate_chain: Certificate chain for the Certificate Authority certificate.
        :param pulumi.Input[str] status: The status of the Certificate Authority.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CertificateAuthorityActivationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Used to install the certificate authority certificate and update the certificate authority status.

        :param str resource_name: The name of the resource.
        :param CertificateAuthorityActivationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CertificateAuthorityActivationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 certificate_authority_arn: Optional[pulumi.Input[str]] = None,
                 certificate_chain: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
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
            __props__ = CertificateAuthorityActivationArgs.__new__(CertificateAuthorityActivationArgs)

            if certificate is None and not opts.urn:
                raise TypeError("Missing required property 'certificate'")
            __props__.__dict__["certificate"] = certificate
            if certificate_authority_arn is None and not opts.urn:
                raise TypeError("Missing required property 'certificate_authority_arn'")
            __props__.__dict__["certificate_authority_arn"] = certificate_authority_arn
            __props__.__dict__["certificate_chain"] = certificate_chain
            __props__.__dict__["status"] = status
            __props__.__dict__["complete_certificate_chain"] = None
        super(CertificateAuthorityActivation, __self__).__init__(
            'aws-native:acmpca:CertificateAuthorityActivation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CertificateAuthorityActivation':
        """
        Get an existing CertificateAuthorityActivation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CertificateAuthorityActivationArgs.__new__(CertificateAuthorityActivationArgs)

        __props__.__dict__["certificate"] = None
        __props__.__dict__["certificate_authority_arn"] = None
        __props__.__dict__["certificate_chain"] = None
        __props__.__dict__["complete_certificate_chain"] = None
        __props__.__dict__["status"] = None
        return CertificateAuthorityActivation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[str]:
        """
        Certificate Authority certificate that will be installed in the Certificate Authority.
        """
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> pulumi.Output[str]:
        """
        Arn of the Certificate Authority.
        """
        return pulumi.get(self, "certificate_authority_arn")

    @property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Output[Optional[str]]:
        """
        Certificate chain for the Certificate Authority certificate.
        """
        return pulumi.get(self, "certificate_chain")

    @property
    @pulumi.getter(name="completeCertificateChain")
    def complete_certificate_chain(self) -> pulumi.Output[str]:
        """
        The complete certificate chain, including the Certificate Authority certificate.
        """
        return pulumi.get(self, "complete_certificate_chain")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the Certificate Authority.
        """
        return pulumi.get(self, "status")

