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
from ._inputs import *

__all__ = ['DeploymentArgs', 'Deployment']

@pulumi.input_type
class DeploymentArgs:
    def __init__(__self__, *,
                 create_policy: Optional[pulumi.Input[str]] = None,
                 credential: Optional[pulumi.Input['CredentialArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentLabelEntryArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preview: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input['TargetConfigurationArgs']] = None):
        """
        The set of arguments for constructing a Deployment resource.
        :param pulumi.Input[str] create_policy: Sets the policy to use for creating new resources.
        :param pulumi.Input['CredentialArgs'] credential: User provided default credential for the deployment.
        :param pulumi.Input[str] description: An optional user-provided description of the deployment.
        :param pulumi.Input[Sequence[pulumi.Input['DeploymentLabelEntryArgs']]] labels: Map of One Platform labels; provided by the client when the resource is created or updated. Specifically: Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?` Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] preview: If set to true, creates a deployment and creates "shell" resources but does not actually instantiate these resources. This allows you to preview what your deployment looks like. After previewing a deployment, you can deploy your resources by making a request with the `update()` method or you can use the `cancelPreview()` method to cancel the preview altogether. Note that the deployment will still exist after you cancel the preview and you must separately delete this deployment if you want to remove it.
        :param pulumi.Input['TargetConfigurationArgs'] target: [Input Only] The parameters that define your deployment, including the deployment configuration and relevant templates.
        """
        if create_policy is not None:
            pulumi.set(__self__, "create_policy", create_policy)
        if credential is not None:
            pulumi.set(__self__, "credential", credential)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if preview is not None:
            pulumi.set(__self__, "preview", preview)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if target is not None:
            pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter(name="createPolicy")
    def create_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Sets the policy to use for creating new resources.
        """
        return pulumi.get(self, "create_policy")

    @create_policy.setter
    def create_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_policy", value)

    @property
    @pulumi.getter
    def credential(self) -> Optional[pulumi.Input['CredentialArgs']]:
        """
        User provided default credential for the deployment.
        """
        return pulumi.get(self, "credential")

    @credential.setter
    def credential(self, value: Optional[pulumi.Input['CredentialArgs']]):
        pulumi.set(self, "credential", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional user-provided description of the deployment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentLabelEntryArgs']]]]:
        """
        Map of One Platform labels; provided by the client when the resource is created or updated. Specifically: Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?` Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentLabelEntryArgs']]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def preview(self) -> Optional[pulumi.Input[str]]:
        """
        If set to true, creates a deployment and creates "shell" resources but does not actually instantiate these resources. This allows you to preview what your deployment looks like. After previewing a deployment, you can deploy your resources by making a request with the `update()` method or you can use the `cancelPreview()` method to cancel the preview altogether. Note that the deployment will still exist after you cancel the preview and you must separately delete this deployment if you want to remove it.
        """
        return pulumi.get(self, "preview")

    @preview.setter
    def preview(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preview", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input['TargetConfigurationArgs']]:
        """
        [Input Only] The parameters that define your deployment, including the deployment configuration and relevant templates.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input['TargetConfigurationArgs']]):
        pulumi.set(self, "target", value)


class Deployment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_policy: Optional[pulumi.Input[str]] = None,
                 credential: Optional[pulumi.Input[pulumi.InputType['CredentialArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentLabelEntryArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preview: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[pulumi.InputType['TargetConfigurationArgs']]] = None,
                 __props__=None):
        """
        Creates a deployment and all of the resources described by the deployment manifest.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_policy: Sets the policy to use for creating new resources.
        :param pulumi.Input[pulumi.InputType['CredentialArgs']] credential: User provided default credential for the deployment.
        :param pulumi.Input[str] description: An optional user-provided description of the deployment.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentLabelEntryArgs']]]] labels: Map of One Platform labels; provided by the client when the resource is created or updated. Specifically: Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?` Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] preview: If set to true, creates a deployment and creates "shell" resources but does not actually instantiate these resources. This allows you to preview what your deployment looks like. After previewing a deployment, you can deploy your resources by making a request with the `update()` method or you can use the `cancelPreview()` method to cancel the preview altogether. Note that the deployment will still exist after you cancel the preview and you must separately delete this deployment if you want to remove it.
        :param pulumi.Input[pulumi.InputType['TargetConfigurationArgs']] target: [Input Only] The parameters that define your deployment, including the deployment configuration and relevant templates.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DeploymentArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a deployment and all of the resources described by the deployment manifest.

        :param str resource_name: The name of the resource.
        :param DeploymentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_policy: Optional[pulumi.Input[str]] = None,
                 credential: Optional[pulumi.Input[pulumi.InputType['CredentialArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentLabelEntryArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preview: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[pulumi.InputType['TargetConfigurationArgs']]] = None,
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
            __props__ = DeploymentArgs.__new__(DeploymentArgs)

            __props__.__dict__["create_policy"] = create_policy
            __props__.__dict__["credential"] = credential
            __props__.__dict__["description"] = description
            __props__.__dict__["id"] = id
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            __props__.__dict__["preview"] = preview
            __props__.__dict__["project"] = project
            __props__.__dict__["target"] = target
            __props__.__dict__["fingerprint"] = None
            __props__.__dict__["insert_time"] = None
            __props__.__dict__["manifest"] = None
            __props__.__dict__["operation"] = None
            __props__.__dict__["outputs"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["update"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Deployment, __self__).__init__(
            'google-native:deploymentmanager/alpha:Deployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Deployment':
        """
        Get an existing Deployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeploymentArgs.__new__(DeploymentArgs)

        __props__.__dict__["create_policy"] = None
        __props__.__dict__["credential"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["fingerprint"] = None
        __props__.__dict__["insert_time"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["manifest"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["operation"] = None
        __props__.__dict__["outputs"] = None
        __props__.__dict__["preview"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["target"] = None
        __props__.__dict__["update"] = None
        __props__.__dict__["update_time"] = None
        return Deployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createPolicy")
    def create_policy(self) -> pulumi.Output[Optional[str]]:
        """
        Sets the policy to use for creating new resources.
        """
        return pulumi.get(self, "create_policy")

    @property
    @pulumi.getter
    def credential(self) -> pulumi.Output['outputs.CredentialResponse']:
        """
        User provided default credential for the deployment.
        """
        return pulumi.get(self, "credential")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional user-provided description of the deployment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        Provides a fingerprint to use in requests to modify a deployment, such as `update()`, `stop()`, and `cancelPreview()` requests. A fingerprint is a randomly generated value that must be provided with `update()`, `stop()`, and `cancelPreview()` requests to perform optimistic locking. This ensures optimistic concurrency so that only one request happens at a time. The fingerprint is initially generated by Deployment Manager and changes after every request to modify data. To get the latest fingerprint value, perform a `get()` request to a deployment.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter(name="insertTime")
    def insert_time(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "insert_time")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Sequence['outputs.DeploymentLabelEntryResponse']]:
        """
        Map of One Platform labels; provided by the client when the resource is created or updated. Specifically: Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?` Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def manifest(self) -> pulumi.Output[str]:
        """
        URL of the manifest representing the last manifest that was successfully deployed. If no manifest has been successfully deployed, this field will be absent.
        """
        return pulumi.get(self, "manifest")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def operation(self) -> pulumi.Output['outputs.OperationResponse']:
        """
        The Operation that most recently ran, or is currently running, on this deployment.
        """
        return pulumi.get(self, "operation")

    @property
    @pulumi.getter
    def outputs(self) -> pulumi.Output[Sequence['outputs.DeploymentOutputEntryResponse']]:
        """
        List of outputs from the last manifest that deployed successfully.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter
    def preview(self) -> pulumi.Output[Optional[str]]:
        """
        If set to true, creates a deployment and creates "shell" resources but does not actually instantiate these resources. This allows you to preview what your deployment looks like. After previewing a deployment, you can deploy your resources by making a request with the `update()` method or you can use the `cancelPreview()` method to cancel the preview altogether. Note that the deployment will still exist after you cancel the preview and you must separately delete this deployment if you want to remove it.
        """
        return pulumi.get(self, "preview")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        Server defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output['outputs.TargetConfigurationResponse']:
        """
        [Input Only] The parameters that define your deployment, including the deployment configuration and relevant templates.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter
    def update(self) -> pulumi.Output['outputs.DeploymentUpdateResponse']:
        """
        If Deployment Manager is currently updating or previewing an update to this deployment, the updated configuration appears here.
        """
        return pulumi.get(self, "update")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Update timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "update_time")

