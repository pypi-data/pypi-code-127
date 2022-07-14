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
    'GetNoteResult',
    'AwaitableGetNoteResult',
    'get_note',
    'get_note_output',
]

@pulumi.output_type
class GetNoteResult:
    def __init__(__self__, attestation_authority=None, base_image=None, build=None, create_time=None, deployable=None, discovery=None, expiration_time=None, intoto=None, kind=None, long_description=None, name=None, package=None, related_note_names=None, related_url=None, sbom=None, short_description=None, spdx_file=None, spdx_package=None, spdx_relationship=None, update_time=None, vulnerability=None):
        if attestation_authority and not isinstance(attestation_authority, dict):
            raise TypeError("Expected argument 'attestation_authority' to be a dict")
        pulumi.set(__self__, "attestation_authority", attestation_authority)
        if base_image and not isinstance(base_image, dict):
            raise TypeError("Expected argument 'base_image' to be a dict")
        pulumi.set(__self__, "base_image", base_image)
        if build and not isinstance(build, dict):
            raise TypeError("Expected argument 'build' to be a dict")
        pulumi.set(__self__, "build", build)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if deployable and not isinstance(deployable, dict):
            raise TypeError("Expected argument 'deployable' to be a dict")
        pulumi.set(__self__, "deployable", deployable)
        if discovery and not isinstance(discovery, dict):
            raise TypeError("Expected argument 'discovery' to be a dict")
        pulumi.set(__self__, "discovery", discovery)
        if expiration_time and not isinstance(expiration_time, str):
            raise TypeError("Expected argument 'expiration_time' to be a str")
        pulumi.set(__self__, "expiration_time", expiration_time)
        if intoto and not isinstance(intoto, dict):
            raise TypeError("Expected argument 'intoto' to be a dict")
        pulumi.set(__self__, "intoto", intoto)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if long_description and not isinstance(long_description, str):
            raise TypeError("Expected argument 'long_description' to be a str")
        pulumi.set(__self__, "long_description", long_description)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if package and not isinstance(package, dict):
            raise TypeError("Expected argument 'package' to be a dict")
        pulumi.set(__self__, "package", package)
        if related_note_names and not isinstance(related_note_names, list):
            raise TypeError("Expected argument 'related_note_names' to be a list")
        pulumi.set(__self__, "related_note_names", related_note_names)
        if related_url and not isinstance(related_url, list):
            raise TypeError("Expected argument 'related_url' to be a list")
        pulumi.set(__self__, "related_url", related_url)
        if sbom and not isinstance(sbom, dict):
            raise TypeError("Expected argument 'sbom' to be a dict")
        pulumi.set(__self__, "sbom", sbom)
        if short_description and not isinstance(short_description, str):
            raise TypeError("Expected argument 'short_description' to be a str")
        pulumi.set(__self__, "short_description", short_description)
        if spdx_file and not isinstance(spdx_file, dict):
            raise TypeError("Expected argument 'spdx_file' to be a dict")
        pulumi.set(__self__, "spdx_file", spdx_file)
        if spdx_package and not isinstance(spdx_package, dict):
            raise TypeError("Expected argument 'spdx_package' to be a dict")
        pulumi.set(__self__, "spdx_package", spdx_package)
        if spdx_relationship and not isinstance(spdx_relationship, dict):
            raise TypeError("Expected argument 'spdx_relationship' to be a dict")
        pulumi.set(__self__, "spdx_relationship", spdx_relationship)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)
        if vulnerability and not isinstance(vulnerability, dict):
            raise TypeError("Expected argument 'vulnerability' to be a dict")
        pulumi.set(__self__, "vulnerability", vulnerability)

    @property
    @pulumi.getter(name="attestationAuthority")
    def attestation_authority(self) -> 'outputs.AuthorityResponse':
        """
        A note describing an attestation role.
        """
        return pulumi.get(self, "attestation_authority")

    @property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> 'outputs.BasisResponse':
        """
        A note describing a base image.
        """
        return pulumi.get(self, "base_image")

    @property
    @pulumi.getter
    def build(self) -> 'outputs.BuildResponse':
        """
        A note describing build provenance for a verifiable build.
        """
        return pulumi.get(self, "build")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time this note was created. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def deployable(self) -> 'outputs.DeployableResponse':
        """
        A note describing something that can be deployed.
        """
        return pulumi.get(self, "deployable")

    @property
    @pulumi.getter
    def discovery(self) -> 'outputs.DiscoveryResponse':
        """
        A note describing the initial analysis of a resource.
        """
        return pulumi.get(self, "discovery")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> str:
        """
        Time of expiration for this note. Empty if note does not expire.
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter
    def intoto(self) -> 'outputs.InTotoResponse':
        """
        A note describing an in-toto link.
        """
        return pulumi.get(self, "intoto")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The type of analysis. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> str:
        """
        A detailed description of this note.
        """
        return pulumi.get(self, "long_description")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def package(self) -> 'outputs.PackageResponse':
        """
        A note describing a package hosted by various package managers.
        """
        return pulumi.get(self, "package")

    @property
    @pulumi.getter(name="relatedNoteNames")
    def related_note_names(self) -> Sequence[str]:
        """
        Other notes related to this note.
        """
        return pulumi.get(self, "related_note_names")

    @property
    @pulumi.getter(name="relatedUrl")
    def related_url(self) -> Sequence['outputs.RelatedUrlResponse']:
        """
        URLs associated with this note.
        """
        return pulumi.get(self, "related_url")

    @property
    @pulumi.getter
    def sbom(self) -> 'outputs.DocumentNoteResponse':
        """
        A note describing a software bill of materials.
        """
        return pulumi.get(self, "sbom")

    @property
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> str:
        """
        A one sentence description of this note.
        """
        return pulumi.get(self, "short_description")

    @property
    @pulumi.getter(name="spdxFile")
    def spdx_file(self) -> 'outputs.FileNoteResponse':
        """
        A note describing an SPDX File.
        """
        return pulumi.get(self, "spdx_file")

    @property
    @pulumi.getter(name="spdxPackage")
    def spdx_package(self) -> 'outputs.PackageInfoNoteResponse':
        """
        A note describing an SPDX Package.
        """
        return pulumi.get(self, "spdx_package")

    @property
    @pulumi.getter(name="spdxRelationship")
    def spdx_relationship(self) -> 'outputs.RelationshipNoteResponse':
        """
        A note describing an SPDX File.
        """
        return pulumi.get(self, "spdx_relationship")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time this note was last updated. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def vulnerability(self) -> 'outputs.VulnerabilityResponse':
        """
        A note describing a package vulnerability.
        """
        return pulumi.get(self, "vulnerability")


class AwaitableGetNoteResult(GetNoteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNoteResult(
            attestation_authority=self.attestation_authority,
            base_image=self.base_image,
            build=self.build,
            create_time=self.create_time,
            deployable=self.deployable,
            discovery=self.discovery,
            expiration_time=self.expiration_time,
            intoto=self.intoto,
            kind=self.kind,
            long_description=self.long_description,
            name=self.name,
            package=self.package,
            related_note_names=self.related_note_names,
            related_url=self.related_url,
            sbom=self.sbom,
            short_description=self.short_description,
            spdx_file=self.spdx_file,
            spdx_package=self.spdx_package,
            spdx_relationship=self.spdx_relationship,
            update_time=self.update_time,
            vulnerability=self.vulnerability)


def get_note(note_id: Optional[str] = None,
             project: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNoteResult:
    """
    Gets the specified note.
    """
    __args__ = dict()
    __args__['noteId'] = note_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:containeranalysis/v1beta1:getNote', __args__, opts=opts, typ=GetNoteResult).value

    return AwaitableGetNoteResult(
        attestation_authority=__ret__.attestation_authority,
        base_image=__ret__.base_image,
        build=__ret__.build,
        create_time=__ret__.create_time,
        deployable=__ret__.deployable,
        discovery=__ret__.discovery,
        expiration_time=__ret__.expiration_time,
        intoto=__ret__.intoto,
        kind=__ret__.kind,
        long_description=__ret__.long_description,
        name=__ret__.name,
        package=__ret__.package,
        related_note_names=__ret__.related_note_names,
        related_url=__ret__.related_url,
        sbom=__ret__.sbom,
        short_description=__ret__.short_description,
        spdx_file=__ret__.spdx_file,
        spdx_package=__ret__.spdx_package,
        spdx_relationship=__ret__.spdx_relationship,
        update_time=__ret__.update_time,
        vulnerability=__ret__.vulnerability)


@_utilities.lift_output_func(get_note)
def get_note_output(note_id: Optional[pulumi.Input[str]] = None,
                    project: Optional[pulumi.Input[Optional[str]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNoteResult]:
    """
    Gets the specified note.
    """
    ...
