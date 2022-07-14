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
    'GetComponentResult',
    'AwaitableGetComponentResult',
    'get_component',
    'get_component_output',
]

@pulumi.output_type
class GetComponentResult:
    def __init__(__self__, app_id=None, binding_properties=None, children=None, collection_properties=None, component_type=None, environment_name=None, events=None, id=None, name=None, overrides=None, properties=None, schema_version=None, source_id=None, variants=None):
        if app_id and not isinstance(app_id, str):
            raise TypeError("Expected argument 'app_id' to be a str")
        pulumi.set(__self__, "app_id", app_id)
        if binding_properties and not isinstance(binding_properties, dict):
            raise TypeError("Expected argument 'binding_properties' to be a dict")
        pulumi.set(__self__, "binding_properties", binding_properties)
        if children and not isinstance(children, list):
            raise TypeError("Expected argument 'children' to be a list")
        pulumi.set(__self__, "children", children)
        if collection_properties and not isinstance(collection_properties, dict):
            raise TypeError("Expected argument 'collection_properties' to be a dict")
        pulumi.set(__self__, "collection_properties", collection_properties)
        if component_type and not isinstance(component_type, str):
            raise TypeError("Expected argument 'component_type' to be a str")
        pulumi.set(__self__, "component_type", component_type)
        if environment_name and not isinstance(environment_name, str):
            raise TypeError("Expected argument 'environment_name' to be a str")
        pulumi.set(__self__, "environment_name", environment_name)
        if events and not isinstance(events, dict):
            raise TypeError("Expected argument 'events' to be a dict")
        pulumi.set(__self__, "events", events)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if overrides and not isinstance(overrides, dict):
            raise TypeError("Expected argument 'overrides' to be a dict")
        pulumi.set(__self__, "overrides", overrides)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if schema_version and not isinstance(schema_version, str):
            raise TypeError("Expected argument 'schema_version' to be a str")
        pulumi.set(__self__, "schema_version", schema_version)
        if source_id and not isinstance(source_id, str):
            raise TypeError("Expected argument 'source_id' to be a str")
        pulumi.set(__self__, "source_id", source_id)
        if variants and not isinstance(variants, list):
            raise TypeError("Expected argument 'variants' to be a list")
        pulumi.set(__self__, "variants", variants)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[str]:
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="bindingProperties")
    def binding_properties(self) -> Optional['outputs.ComponentBindingProperties']:
        return pulumi.get(self, "binding_properties")

    @property
    @pulumi.getter
    def children(self) -> Optional[Sequence['outputs.ComponentChild']]:
        return pulumi.get(self, "children")

    @property
    @pulumi.getter(name="collectionProperties")
    def collection_properties(self) -> Optional['outputs.ComponentCollectionProperties']:
        return pulumi.get(self, "collection_properties")

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> Optional[str]:
        return pulumi.get(self, "component_type")

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[str]:
        return pulumi.get(self, "environment_name")

    @property
    @pulumi.getter
    def events(self) -> Optional['outputs.ComponentEvents']:
        return pulumi.get(self, "events")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def overrides(self) -> Optional['outputs.ComponentOverrides']:
        return pulumi.get(self, "overrides")

    @property
    @pulumi.getter
    def properties(self) -> Optional['outputs.ComponentProperties']:
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> Optional[str]:
        return pulumi.get(self, "schema_version")

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[str]:
        return pulumi.get(self, "source_id")

    @property
    @pulumi.getter
    def variants(self) -> Optional[Sequence['outputs.ComponentVariant']]:
        return pulumi.get(self, "variants")


class AwaitableGetComponentResult(GetComponentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetComponentResult(
            app_id=self.app_id,
            binding_properties=self.binding_properties,
            children=self.children,
            collection_properties=self.collection_properties,
            component_type=self.component_type,
            environment_name=self.environment_name,
            events=self.events,
            id=self.id,
            name=self.name,
            overrides=self.overrides,
            properties=self.properties,
            schema_version=self.schema_version,
            source_id=self.source_id,
            variants=self.variants)


def get_component(app_id: Optional[str] = None,
                  environment_name: Optional[str] = None,
                  id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetComponentResult:
    """
    Definition of AWS::AmplifyUIBuilder::Component Resource Type
    """
    __args__ = dict()
    __args__['appId'] = app_id
    __args__['environmentName'] = environment_name
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:amplifyuibuilder:getComponent', __args__, opts=opts, typ=GetComponentResult).value

    return AwaitableGetComponentResult(
        app_id=__ret__.app_id,
        binding_properties=__ret__.binding_properties,
        children=__ret__.children,
        collection_properties=__ret__.collection_properties,
        component_type=__ret__.component_type,
        environment_name=__ret__.environment_name,
        events=__ret__.events,
        id=__ret__.id,
        name=__ret__.name,
        overrides=__ret__.overrides,
        properties=__ret__.properties,
        schema_version=__ret__.schema_version,
        source_id=__ret__.source_id,
        variants=__ret__.variants)


@_utilities.lift_output_func(get_component)
def get_component_output(app_id: Optional[pulumi.Input[str]] = None,
                         environment_name: Optional[pulumi.Input[str]] = None,
                         id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetComponentResult]:
    """
    Definition of AWS::AmplifyUIBuilder::Component Resource Type
    """
    ...
