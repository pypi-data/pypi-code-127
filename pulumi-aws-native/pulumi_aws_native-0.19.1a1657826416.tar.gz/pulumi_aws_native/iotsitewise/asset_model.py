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
from ._enums import *
from ._inputs import *

__all__ = ['AssetModelArgs', 'AssetModel']

@pulumi.input_type
class AssetModelArgs:
    def __init__(__self__, *,
                 asset_model_composite_models: Optional[pulumi.Input[Sequence[pulumi.Input['AssetModelCompositeModelArgs']]]] = None,
                 asset_model_description: Optional[pulumi.Input[str]] = None,
                 asset_model_hierarchies: Optional[pulumi.Input[Sequence[pulumi.Input['AssetModelHierarchyArgs']]]] = None,
                 asset_model_name: Optional[pulumi.Input[str]] = None,
                 asset_model_properties: Optional[pulumi.Input[Sequence[pulumi.Input['AssetModelPropertyArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['AssetModelTagArgs']]]] = None):
        """
        The set of arguments for constructing a AssetModel resource.
        :param pulumi.Input[Sequence[pulumi.Input['AssetModelCompositeModelArgs']]] asset_model_composite_models: The composite asset models that are part of this asset model. Composite asset models are asset models that contain specific properties.
        :param pulumi.Input[str] asset_model_description: A description for the asset model.
        :param pulumi.Input[Sequence[pulumi.Input['AssetModelHierarchyArgs']]] asset_model_hierarchies: The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. You can specify up to 10 hierarchies per asset model.
        :param pulumi.Input[str] asset_model_name: A unique, friendly name for the asset model.
        :param pulumi.Input[Sequence[pulumi.Input['AssetModelPropertyArgs']]] asset_model_properties: The property definitions of the asset model. You can specify up to 200 properties per asset model.
        :param pulumi.Input[Sequence[pulumi.Input['AssetModelTagArgs']]] tags: A list of key-value pairs that contain metadata for the asset model.
        """
        if asset_model_composite_models is not None:
            pulumi.set(__self__, "asset_model_composite_models", asset_model_composite_models)
        if asset_model_description is not None:
            pulumi.set(__self__, "asset_model_description", asset_model_description)
        if asset_model_hierarchies is not None:
            pulumi.set(__self__, "asset_model_hierarchies", asset_model_hierarchies)
        if asset_model_name is not None:
            pulumi.set(__self__, "asset_model_name", asset_model_name)
        if asset_model_properties is not None:
            pulumi.set(__self__, "asset_model_properties", asset_model_properties)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="assetModelCompositeModels")
    def asset_model_composite_models(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssetModelCompositeModelArgs']]]]:
        """
        The composite asset models that are part of this asset model. Composite asset models are asset models that contain specific properties.
        """
        return pulumi.get(self, "asset_model_composite_models")

    @asset_model_composite_models.setter
    def asset_model_composite_models(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssetModelCompositeModelArgs']]]]):
        pulumi.set(self, "asset_model_composite_models", value)

    @property
    @pulumi.getter(name="assetModelDescription")
    def asset_model_description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the asset model.
        """
        return pulumi.get(self, "asset_model_description")

    @asset_model_description.setter
    def asset_model_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "asset_model_description", value)

    @property
    @pulumi.getter(name="assetModelHierarchies")
    def asset_model_hierarchies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssetModelHierarchyArgs']]]]:
        """
        The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. You can specify up to 10 hierarchies per asset model.
        """
        return pulumi.get(self, "asset_model_hierarchies")

    @asset_model_hierarchies.setter
    def asset_model_hierarchies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssetModelHierarchyArgs']]]]):
        pulumi.set(self, "asset_model_hierarchies", value)

    @property
    @pulumi.getter(name="assetModelName")
    def asset_model_name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique, friendly name for the asset model.
        """
        return pulumi.get(self, "asset_model_name")

    @asset_model_name.setter
    def asset_model_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "asset_model_name", value)

    @property
    @pulumi.getter(name="assetModelProperties")
    def asset_model_properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssetModelPropertyArgs']]]]:
        """
        The property definitions of the asset model. You can specify up to 200 properties per asset model.
        """
        return pulumi.get(self, "asset_model_properties")

    @asset_model_properties.setter
    def asset_model_properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssetModelPropertyArgs']]]]):
        pulumi.set(self, "asset_model_properties", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssetModelTagArgs']]]]:
        """
        A list of key-value pairs that contain metadata for the asset model.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssetModelTagArgs']]]]):
        pulumi.set(self, "tags", value)


class AssetModel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asset_model_composite_models: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetModelCompositeModelArgs']]]]] = None,
                 asset_model_description: Optional[pulumi.Input[str]] = None,
                 asset_model_hierarchies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetModelHierarchyArgs']]]]] = None,
                 asset_model_name: Optional[pulumi.Input[str]] = None,
                 asset_model_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetModelPropertyArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetModelTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::IoTSiteWise::AssetModel

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetModelCompositeModelArgs']]]] asset_model_composite_models: The composite asset models that are part of this asset model. Composite asset models are asset models that contain specific properties.
        :param pulumi.Input[str] asset_model_description: A description for the asset model.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetModelHierarchyArgs']]]] asset_model_hierarchies: The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. You can specify up to 10 hierarchies per asset model.
        :param pulumi.Input[str] asset_model_name: A unique, friendly name for the asset model.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetModelPropertyArgs']]]] asset_model_properties: The property definitions of the asset model. You can specify up to 200 properties per asset model.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetModelTagArgs']]]] tags: A list of key-value pairs that contain metadata for the asset model.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AssetModelArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::IoTSiteWise::AssetModel

        :param str resource_name: The name of the resource.
        :param AssetModelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssetModelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asset_model_composite_models: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetModelCompositeModelArgs']]]]] = None,
                 asset_model_description: Optional[pulumi.Input[str]] = None,
                 asset_model_hierarchies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetModelHierarchyArgs']]]]] = None,
                 asset_model_name: Optional[pulumi.Input[str]] = None,
                 asset_model_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetModelPropertyArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetModelTagArgs']]]]] = None,
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
            __props__ = AssetModelArgs.__new__(AssetModelArgs)

            __props__.__dict__["asset_model_composite_models"] = asset_model_composite_models
            __props__.__dict__["asset_model_description"] = asset_model_description
            __props__.__dict__["asset_model_hierarchies"] = asset_model_hierarchies
            __props__.__dict__["asset_model_name"] = asset_model_name
            __props__.__dict__["asset_model_properties"] = asset_model_properties
            __props__.__dict__["tags"] = tags
            __props__.__dict__["asset_model_arn"] = None
            __props__.__dict__["asset_model_id"] = None
        super(AssetModel, __self__).__init__(
            'aws-native:iotsitewise:AssetModel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AssetModel':
        """
        Get an existing AssetModel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AssetModelArgs.__new__(AssetModelArgs)

        __props__.__dict__["asset_model_arn"] = None
        __props__.__dict__["asset_model_composite_models"] = None
        __props__.__dict__["asset_model_description"] = None
        __props__.__dict__["asset_model_hierarchies"] = None
        __props__.__dict__["asset_model_id"] = None
        __props__.__dict__["asset_model_name"] = None
        __props__.__dict__["asset_model_properties"] = None
        __props__.__dict__["tags"] = None
        return AssetModel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assetModelArn")
    def asset_model_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the asset model, which has the following format.
        """
        return pulumi.get(self, "asset_model_arn")

    @property
    @pulumi.getter(name="assetModelCompositeModels")
    def asset_model_composite_models(self) -> pulumi.Output[Optional[Sequence['outputs.AssetModelCompositeModel']]]:
        """
        The composite asset models that are part of this asset model. Composite asset models are asset models that contain specific properties.
        """
        return pulumi.get(self, "asset_model_composite_models")

    @property
    @pulumi.getter(name="assetModelDescription")
    def asset_model_description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the asset model.
        """
        return pulumi.get(self, "asset_model_description")

    @property
    @pulumi.getter(name="assetModelHierarchies")
    def asset_model_hierarchies(self) -> pulumi.Output[Optional[Sequence['outputs.AssetModelHierarchy']]]:
        """
        The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. You can specify up to 10 hierarchies per asset model.
        """
        return pulumi.get(self, "asset_model_hierarchies")

    @property
    @pulumi.getter(name="assetModelId")
    def asset_model_id(self) -> pulumi.Output[str]:
        """
        The ID of the asset model.
        """
        return pulumi.get(self, "asset_model_id")

    @property
    @pulumi.getter(name="assetModelName")
    def asset_model_name(self) -> pulumi.Output[str]:
        """
        A unique, friendly name for the asset model.
        """
        return pulumi.get(self, "asset_model_name")

    @property
    @pulumi.getter(name="assetModelProperties")
    def asset_model_properties(self) -> pulumi.Output[Optional[Sequence['outputs.AssetModelProperty']]]:
        """
        The property definitions of the asset model. You can specify up to 200 properties per asset model.
        """
        return pulumi.get(self, "asset_model_properties")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.AssetModelTag']]]:
        """
        A list of key-value pairs that contain metadata for the asset model.
        """
        return pulumi.get(self, "tags")

