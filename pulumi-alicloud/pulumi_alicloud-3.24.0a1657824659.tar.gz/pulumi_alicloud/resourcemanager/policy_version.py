# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PolicyVersionArgs', 'PolicyVersion']

@pulumi.input_type
class PolicyVersionArgs:
    def __init__(__self__, *,
                 policy_document: pulumi.Input[str],
                 policy_name: pulumi.Input[str],
                 is_default_version: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a PolicyVersion resource.
        :param pulumi.Input[str] policy_document: The content of the policy. The content must be 1 to 2,048 characters in length.
        :param pulumi.Input[str] policy_name: The name of the policy. Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        :param pulumi.Input[bool] is_default_version: Specifies whether to set the policy version as the default version. Default to `false`.
        """
        pulumi.set(__self__, "policy_document", policy_document)
        pulumi.set(__self__, "policy_name", policy_name)
        if is_default_version is not None:
            warnings.warn("""Field 'is_default_version' has been deprecated from provider version 1.90.0""", DeprecationWarning)
            pulumi.log.warn("""is_default_version is deprecated: Field 'is_default_version' has been deprecated from provider version 1.90.0""")
        if is_default_version is not None:
            pulumi.set(__self__, "is_default_version", is_default_version)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Input[str]:
        """
        The content of the policy. The content must be 1 to 2,048 characters in length.
        """
        return pulumi.get(self, "policy_document")

    @policy_document.setter
    def policy_document(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_document", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Input[str]:
        """
        The name of the policy. Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="isDefaultVersion")
    def is_default_version(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to set the policy version as the default version. Default to `false`.
        """
        return pulumi.get(self, "is_default_version")

    @is_default_version.setter
    def is_default_version(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_default_version", value)


@pulumi.input_type
class _PolicyVersionState:
    def __init__(__self__, *,
                 is_default_version: Optional[pulumi.Input[bool]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PolicyVersion resources.
        :param pulumi.Input[bool] is_default_version: Specifies whether to set the policy version as the default version. Default to `false`.
        :param pulumi.Input[str] policy_document: The content of the policy. The content must be 1 to 2,048 characters in length.
        :param pulumi.Input[str] policy_name: The name of the policy. Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        """
        if is_default_version is not None:
            warnings.warn("""Field 'is_default_version' has been deprecated from provider version 1.90.0""", DeprecationWarning)
            pulumi.log.warn("""is_default_version is deprecated: Field 'is_default_version' has been deprecated from provider version 1.90.0""")
        if is_default_version is not None:
            pulumi.set(__self__, "is_default_version", is_default_version)
        if policy_document is not None:
            pulumi.set(__self__, "policy_document", policy_document)
        if policy_name is not None:
            pulumi.set(__self__, "policy_name", policy_name)

    @property
    @pulumi.getter(name="isDefaultVersion")
    def is_default_version(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to set the policy version as the default version. Default to `false`.
        """
        return pulumi.get(self, "is_default_version")

    @is_default_version.setter
    def is_default_version(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_default_version", value)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[str]]:
        """
        The content of the policy. The content must be 1 to 2,048 characters in length.
        """
        return pulumi.get(self, "policy_document")

    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_document", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy. Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_name", value)


class PolicyVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 is_default_version: Optional[pulumi.Input[bool]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example_policy = alicloud.resourcemanager.Policy("examplePolicy",
            policy_name="tftest",
            policy_document=\"\"\"		{
        			"Statement": [{
        				"Action": ["oss:*"],
        				"Effect": "Allow",
        				"Resource": ["acs:oss:*:*:*"]
        			}],
        			"Version": "1"
        		}
        \"\"\")
        example_policy_version = alicloud.resourcemanager.PolicyVersion("examplePolicyVersion",
            policy_name=example_policy.policy_name,
            policy_document=\"\"\"		{
        			"Statement": [{
        				"Action": ["oss:*"],
        				"Effect": "Allow",
        				"Resource": ["acs:oss:*:*:myphotos"]
        			}],
        			"Version": "1"
        		}
        \"\"\")
        ```

        ## Import

        Resource Manager Policy Version can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:resourcemanager/policyVersion:PolicyVersion example tftest:v2
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] is_default_version: Specifies whether to set the policy version as the default version. Default to `false`.
        :param pulumi.Input[str] policy_document: The content of the policy. The content must be 1 to 2,048 characters in length.
        :param pulumi.Input[str] policy_name: The name of the policy. Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example_policy = alicloud.resourcemanager.Policy("examplePolicy",
            policy_name="tftest",
            policy_document=\"\"\"		{
        			"Statement": [{
        				"Action": ["oss:*"],
        				"Effect": "Allow",
        				"Resource": ["acs:oss:*:*:*"]
        			}],
        			"Version": "1"
        		}
        \"\"\")
        example_policy_version = alicloud.resourcemanager.PolicyVersion("examplePolicyVersion",
            policy_name=example_policy.policy_name,
            policy_document=\"\"\"		{
        			"Statement": [{
        				"Action": ["oss:*"],
        				"Effect": "Allow",
        				"Resource": ["acs:oss:*:*:myphotos"]
        			}],
        			"Version": "1"
        		}
        \"\"\")
        ```

        ## Import

        Resource Manager Policy Version can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:resourcemanager/policyVersion:PolicyVersion example tftest:v2
        ```

        :param str resource_name: The name of the resource.
        :param PolicyVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 is_default_version: Optional[pulumi.Input[bool]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyVersionArgs.__new__(PolicyVersionArgs)

            if is_default_version is not None and not opts.urn:
                warnings.warn("""Field 'is_default_version' has been deprecated from provider version 1.90.0""", DeprecationWarning)
                pulumi.log.warn("""is_default_version is deprecated: Field 'is_default_version' has been deprecated from provider version 1.90.0""")
            __props__.__dict__["is_default_version"] = is_default_version
            if policy_document is None and not opts.urn:
                raise TypeError("Missing required property 'policy_document'")
            __props__.__dict__["policy_document"] = policy_document
            if policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'policy_name'")
            __props__.__dict__["policy_name"] = policy_name
        super(PolicyVersion, __self__).__init__(
            'alicloud:resourcemanager/policyVersion:PolicyVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            is_default_version: Optional[pulumi.Input[bool]] = None,
            policy_document: Optional[pulumi.Input[str]] = None,
            policy_name: Optional[pulumi.Input[str]] = None) -> 'PolicyVersion':
        """
        Get an existing PolicyVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] is_default_version: Specifies whether to set the policy version as the default version. Default to `false`.
        :param pulumi.Input[str] policy_document: The content of the policy. The content must be 1 to 2,048 characters in length.
        :param pulumi.Input[str] policy_name: The name of the policy. Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PolicyVersionState.__new__(_PolicyVersionState)

        __props__.__dict__["is_default_version"] = is_default_version
        __props__.__dict__["policy_document"] = policy_document
        __props__.__dict__["policy_name"] = policy_name
        return PolicyVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="isDefaultVersion")
    def is_default_version(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether to set the policy version as the default version. Default to `false`.
        """
        return pulumi.get(self, "is_default_version")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[str]:
        """
        The content of the policy. The content must be 1 to 2,048 characters in length.
        """
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[str]:
        """
        The name of the policy. Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        """
        return pulumi.get(self, "policy_name")

