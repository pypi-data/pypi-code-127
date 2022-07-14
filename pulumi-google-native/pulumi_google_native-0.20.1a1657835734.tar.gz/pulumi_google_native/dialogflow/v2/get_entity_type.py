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
    'GetEntityTypeResult',
    'AwaitableGetEntityTypeResult',
    'get_entity_type',
    'get_entity_type_output',
]

@pulumi.output_type
class GetEntityTypeResult:
    def __init__(__self__, auto_expansion_mode=None, display_name=None, enable_fuzzy_extraction=None, entities=None, kind=None, name=None):
        if auto_expansion_mode and not isinstance(auto_expansion_mode, str):
            raise TypeError("Expected argument 'auto_expansion_mode' to be a str")
        pulumi.set(__self__, "auto_expansion_mode", auto_expansion_mode)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if enable_fuzzy_extraction and not isinstance(enable_fuzzy_extraction, bool):
            raise TypeError("Expected argument 'enable_fuzzy_extraction' to be a bool")
        pulumi.set(__self__, "enable_fuzzy_extraction", enable_fuzzy_extraction)
        if entities and not isinstance(entities, list):
            raise TypeError("Expected argument 'entities' to be a list")
        pulumi.set(__self__, "entities", entities)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="autoExpansionMode")
    def auto_expansion_mode(self) -> str:
        """
        Optional. Indicates whether the entity type can be automatically expanded.
        """
        return pulumi.get(self, "auto_expansion_mode")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The name of the entity type.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enableFuzzyExtraction")
    def enable_fuzzy_extraction(self) -> bool:
        """
        Optional. Enables fuzzy entity extraction during classification.
        """
        return pulumi.get(self, "enable_fuzzy_extraction")

    @property
    @pulumi.getter
    def entities(self) -> Sequence['outputs.GoogleCloudDialogflowV2EntityTypeEntityResponse']:
        """
        Optional. The collection of entity entries associated with the entity type.
        """
        return pulumi.get(self, "entities")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Indicates the kind of entity type.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The unique identifier of the entity type. Required for EntityTypes.UpdateEntityType and EntityTypes.BatchUpdateEntityTypes methods. Format: `projects//agent/entityTypes/`.
        """
        return pulumi.get(self, "name")


class AwaitableGetEntityTypeResult(GetEntityTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEntityTypeResult(
            auto_expansion_mode=self.auto_expansion_mode,
            display_name=self.display_name,
            enable_fuzzy_extraction=self.enable_fuzzy_extraction,
            entities=self.entities,
            kind=self.kind,
            name=self.name)


def get_entity_type(entity_type_id: Optional[str] = None,
                    language_code: Optional[str] = None,
                    location: Optional[str] = None,
                    project: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEntityTypeResult:
    """
    Retrieves the specified entity type.
    """
    __args__ = dict()
    __args__['entityTypeId'] = entity_type_id
    __args__['languageCode'] = language_code
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:dialogflow/v2:getEntityType', __args__, opts=opts, typ=GetEntityTypeResult).value

    return AwaitableGetEntityTypeResult(
        auto_expansion_mode=__ret__.auto_expansion_mode,
        display_name=__ret__.display_name,
        enable_fuzzy_extraction=__ret__.enable_fuzzy_extraction,
        entities=__ret__.entities,
        kind=__ret__.kind,
        name=__ret__.name)


@_utilities.lift_output_func(get_entity_type)
def get_entity_type_output(entity_type_id: Optional[pulumi.Input[str]] = None,
                           language_code: Optional[pulumi.Input[Optional[str]]] = None,
                           location: Optional[pulumi.Input[str]] = None,
                           project: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEntityTypeResult]:
    """
    Retrieves the specified entity type.
    """
    ...
