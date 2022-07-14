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

__all__ = [
    'GetConsentArtifactResult',
    'AwaitableGetConsentArtifactResult',
    'get_consent_artifact',
    'get_consent_artifact_output',
]

@pulumi.output_type
class GetConsentArtifactResult:
    def __init__(__self__, consent_content_screenshots=None, consent_content_version=None, guardian_signature=None, metadata=None, name=None, user_id=None, user_signature=None, witness_signature=None):
        if consent_content_screenshots and not isinstance(consent_content_screenshots, list):
            raise TypeError("Expected argument 'consent_content_screenshots' to be a list")
        pulumi.set(__self__, "consent_content_screenshots", consent_content_screenshots)
        if consent_content_version and not isinstance(consent_content_version, str):
            raise TypeError("Expected argument 'consent_content_version' to be a str")
        pulumi.set(__self__, "consent_content_version", consent_content_version)
        if guardian_signature and not isinstance(guardian_signature, dict):
            raise TypeError("Expected argument 'guardian_signature' to be a dict")
        pulumi.set(__self__, "guardian_signature", guardian_signature)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)
        if user_signature and not isinstance(user_signature, dict):
            raise TypeError("Expected argument 'user_signature' to be a dict")
        pulumi.set(__self__, "user_signature", user_signature)
        if witness_signature and not isinstance(witness_signature, dict):
            raise TypeError("Expected argument 'witness_signature' to be a dict")
        pulumi.set(__self__, "witness_signature", witness_signature)

    @property
    @pulumi.getter(name="consentContentScreenshots")
    def consent_content_screenshots(self) -> Sequence['outputs.ImageResponse']:
        """
        Optional. Screenshots, PDFs, or other binary information documenting the user's consent.
        """
        return pulumi.get(self, "consent_content_screenshots")

    @property
    @pulumi.getter(name="consentContentVersion")
    def consent_content_version(self) -> str:
        """
        Optional. An string indicating the version of the consent information shown to the user.
        """
        return pulumi.get(self, "consent_content_version")

    @property
    @pulumi.getter(name="guardianSignature")
    def guardian_signature(self) -> 'outputs.SignatureResponse':
        """
        Optional. A signature from a guardian.
        """
        return pulumi.get(self, "guardian_signature")

    @property
    @pulumi.getter
    def metadata(self) -> Mapping[str, str]:
        """
        Optional. Metadata associated with the Consent artifact. For example, the consent locale or user agent version.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name of the Consent artifact, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consentArtifacts/{consent_artifact_id}`. Cannot be changed after creation.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        """
        User's UUID provided by the client.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter(name="userSignature")
    def user_signature(self) -> 'outputs.SignatureResponse':
        """
        Optional. User's signature.
        """
        return pulumi.get(self, "user_signature")

    @property
    @pulumi.getter(name="witnessSignature")
    def witness_signature(self) -> 'outputs.SignatureResponse':
        """
        Optional. A signature from a witness.
        """
        return pulumi.get(self, "witness_signature")


class AwaitableGetConsentArtifactResult(GetConsentArtifactResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConsentArtifactResult(
            consent_content_screenshots=self.consent_content_screenshots,
            consent_content_version=self.consent_content_version,
            guardian_signature=self.guardian_signature,
            metadata=self.metadata,
            name=self.name,
            user_id=self.user_id,
            user_signature=self.user_signature,
            witness_signature=self.witness_signature)


def get_consent_artifact(consent_artifact_id: Optional[str] = None,
                         consent_store_id: Optional[str] = None,
                         dataset_id: Optional[str] = None,
                         location: Optional[str] = None,
                         project: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConsentArtifactResult:
    """
    Gets the specified Consent artifact.
    """
    __args__ = dict()
    __args__['consentArtifactId'] = consent_artifact_id
    __args__['consentStoreId'] = consent_store_id
    __args__['datasetId'] = dataset_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:healthcare/v1:getConsentArtifact', __args__, opts=opts, typ=GetConsentArtifactResult).value

    return AwaitableGetConsentArtifactResult(
        consent_content_screenshots=__ret__.consent_content_screenshots,
        consent_content_version=__ret__.consent_content_version,
        guardian_signature=__ret__.guardian_signature,
        metadata=__ret__.metadata,
        name=__ret__.name,
        user_id=__ret__.user_id,
        user_signature=__ret__.user_signature,
        witness_signature=__ret__.witness_signature)


@_utilities.lift_output_func(get_consent_artifact)
def get_consent_artifact_output(consent_artifact_id: Optional[pulumi.Input[str]] = None,
                                consent_store_id: Optional[pulumi.Input[str]] = None,
                                dataset_id: Optional[pulumi.Input[str]] = None,
                                location: Optional[pulumi.Input[str]] = None,
                                project: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConsentArtifactResult]:
    """
    Gets the specified Consent artifact.
    """
    ...
