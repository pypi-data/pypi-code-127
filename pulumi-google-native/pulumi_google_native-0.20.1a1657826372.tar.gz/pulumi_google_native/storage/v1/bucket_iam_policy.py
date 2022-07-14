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

__all__ = ['BucketIamPolicyArgs', 'BucketIamPolicy']

@pulumi.input_type
class BucketIamPolicyArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 bindings: Optional[pulumi.Input[Sequence[pulumi.Input['BucketIamPolicyBindingsItemArgs']]]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 user_project: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a BucketIamPolicy resource.
        :param pulumi.Input[Sequence[pulumi.Input['BucketIamPolicyBindingsItemArgs']]] bindings: An association between a role, which comes with a set of permissions, and members who may assume that role.
        :param pulumi.Input[str] etag: HTTP 1.1  Entity tag for the policy.
        :param pulumi.Input[str] kind: The kind of item this is. For policies, this is always storage#policy. This field is ignored on input.
        :param pulumi.Input[str] resource_id: The ID of the resource to which this policy belongs. Will be of the form projects/_/buckets/bucket for buckets, and projects/_/buckets/bucket/objects/object for objects. A specific generation may be specified by appending #generationNumber to the end of the object name, e.g. projects/_/buckets/my-bucket/objects/data.txt#17. The current generation can be denoted with #0. This field is ignored on input.
        :param pulumi.Input[str] user_project: The project to be billed for this request. Required for Requester Pays buckets.
        :param pulumi.Input[int] version: The IAM policy format version.
        """
        pulumi.set(__self__, "bucket", bucket)
        if bindings is not None:
            pulumi.set(__self__, "bindings", bindings)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if user_project is not None:
            pulumi.set(__self__, "user_project", user_project)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def bindings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BucketIamPolicyBindingsItemArgs']]]]:
        """
        An association between a role, which comes with a set of permissions, and members who may assume that role.
        """
        return pulumi.get(self, "bindings")

    @bindings.setter
    def bindings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BucketIamPolicyBindingsItemArgs']]]]):
        pulumi.set(self, "bindings", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        HTTP 1.1  Entity tag for the policy.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        The kind of item this is. For policies, this is always storage#policy. This field is ignored on input.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the resource to which this policy belongs. Will be of the form projects/_/buckets/bucket for buckets, and projects/_/buckets/bucket/objects/object for objects. A specific generation may be specified by appending #generationNumber to the end of the object name, e.g. projects/_/buckets/my-bucket/objects/data.txt#17. The current generation can be denoted with #0. This field is ignored on input.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="userProject")
    def user_project(self) -> Optional[pulumi.Input[str]]:
        """
        The project to be billed for this request. Required for Requester Pays buckets.
        """
        return pulumi.get(self, "user_project")

    @user_project.setter
    def user_project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_project", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        """
        The IAM policy format version.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class BucketIamPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bindings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketIamPolicyBindingsItemArgs']]]]] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 user_project: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Updates an IAM policy for the specified bucket.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketIamPolicyBindingsItemArgs']]]] bindings: An association between a role, which comes with a set of permissions, and members who may assume that role.
        :param pulumi.Input[str] etag: HTTP 1.1  Entity tag for the policy.
        :param pulumi.Input[str] kind: The kind of item this is. For policies, this is always storage#policy. This field is ignored on input.
        :param pulumi.Input[str] resource_id: The ID of the resource to which this policy belongs. Will be of the form projects/_/buckets/bucket for buckets, and projects/_/buckets/bucket/objects/object for objects. A specific generation may be specified by appending #generationNumber to the end of the object name, e.g. projects/_/buckets/my-bucket/objects/data.txt#17. The current generation can be denoted with #0. This field is ignored on input.
        :param pulumi.Input[str] user_project: The project to be billed for this request. Required for Requester Pays buckets.
        :param pulumi.Input[int] version: The IAM policy format version.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BucketIamPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Updates an IAM policy for the specified bucket.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param BucketIamPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BucketIamPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bindings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketIamPolicyBindingsItemArgs']]]]] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 user_project: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None,
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
            __props__ = BucketIamPolicyArgs.__new__(BucketIamPolicyArgs)

            __props__.__dict__["bindings"] = bindings
            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["etag"] = etag
            __props__.__dict__["kind"] = kind
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["user_project"] = user_project
            __props__.__dict__["version"] = version
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["bucket"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(BucketIamPolicy, __self__).__init__(
            'google-native:storage/v1:BucketIamPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BucketIamPolicy':
        """
        Get an existing BucketIamPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BucketIamPolicyArgs.__new__(BucketIamPolicyArgs)

        __props__.__dict__["bindings"] = None
        __props__.__dict__["bucket"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["user_project"] = None
        __props__.__dict__["version"] = None
        return BucketIamPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bindings(self) -> pulumi.Output[Sequence['outputs.BucketIamPolicyBindingsItemResponse']]:
        """
        An association between a role, which comes with a set of permissions, and members who may assume that role.
        """
        return pulumi.get(self, "bindings")

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        HTTP 1.1  Entity tag for the policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of item this is. For policies, this is always storage#policy. This field is ignored on input.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        The ID of the resource to which this policy belongs. Will be of the form projects/_/buckets/bucket for buckets, and projects/_/buckets/bucket/objects/object for objects. A specific generation may be specified by appending #generationNumber to the end of the object name, e.g. projects/_/buckets/my-bucket/objects/data.txt#17. The current generation can be denoted with #0. This field is ignored on input.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="userProject")
    def user_project(self) -> pulumi.Output[Optional[str]]:
        """
        The project to be billed for this request. Required for Requester Pays buckets.
        """
        return pulumi.get(self, "user_project")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        The IAM policy format version.
        """
        return pulumi.get(self, "version")

