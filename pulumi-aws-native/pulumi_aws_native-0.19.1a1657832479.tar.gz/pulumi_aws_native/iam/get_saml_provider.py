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
    'GetSAMLProviderResult',
    'AwaitableGetSAMLProviderResult',
    'get_saml_provider',
    'get_saml_provider_output',
]

@pulumi.output_type
class GetSAMLProviderResult:
    def __init__(__self__, arn=None, saml_metadata_document=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if saml_metadata_document and not isinstance(saml_metadata_document, str):
            raise TypeError("Expected argument 'saml_metadata_document' to be a str")
        pulumi.set(__self__, "saml_metadata_document", saml_metadata_document)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of the SAML provider
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="samlMetadataDocument")
    def saml_metadata_document(self) -> Optional[str]:
        return pulumi.get(self, "saml_metadata_document")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.SAMLProviderTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetSAMLProviderResult(GetSAMLProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSAMLProviderResult(
            arn=self.arn,
            saml_metadata_document=self.saml_metadata_document,
            tags=self.tags)


def get_saml_provider(arn: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSAMLProviderResult:
    """
    Resource Type definition for AWS::IAM::SAMLProvider


    :param str arn: Amazon Resource Name (ARN) of the SAML provider
    """
    __args__ = dict()
    __args__['arn'] = arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:iam:getSAMLProvider', __args__, opts=opts, typ=GetSAMLProviderResult).value

    return AwaitableGetSAMLProviderResult(
        arn=__ret__.arn,
        saml_metadata_document=__ret__.saml_metadata_document,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_saml_provider)
def get_saml_provider_output(arn: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSAMLProviderResult]:
    """
    Resource Type definition for AWS::IAM::SAMLProvider


    :param str arn: Amazon Resource Name (ARN) of the SAML provider
    """
    ...
