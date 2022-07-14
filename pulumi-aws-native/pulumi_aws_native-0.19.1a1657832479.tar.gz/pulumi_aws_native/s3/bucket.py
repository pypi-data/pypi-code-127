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

__all__ = ['BucketArgs', 'Bucket']

@pulumi.input_type
class BucketArgs:
    def __init__(__self__, *,
                 accelerate_configuration: Optional[pulumi.Input['BucketAccelerateConfigurationArgs']] = None,
                 access_control: Optional[pulumi.Input['BucketAccessControl']] = None,
                 analytics_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['BucketAnalyticsConfigurationArgs']]]] = None,
                 bucket_encryption: Optional[pulumi.Input['BucketEncryptionArgs']] = None,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 cors_configuration: Optional[pulumi.Input['BucketCorsConfigurationArgs']] = None,
                 intelligent_tiering_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['BucketIntelligentTieringConfigurationArgs']]]] = None,
                 inventory_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['BucketInventoryConfigurationArgs']]]] = None,
                 lifecycle_configuration: Optional[pulumi.Input['BucketLifecycleConfigurationArgs']] = None,
                 logging_configuration: Optional[pulumi.Input['BucketLoggingConfigurationArgs']] = None,
                 metrics_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['BucketMetricsConfigurationArgs']]]] = None,
                 notification_configuration: Optional[pulumi.Input['BucketNotificationConfigurationArgs']] = None,
                 object_lock_configuration: Optional[pulumi.Input['BucketObjectLockConfigurationArgs']] = None,
                 object_lock_enabled: Optional[pulumi.Input[bool]] = None,
                 ownership_controls: Optional[pulumi.Input['BucketOwnershipControlsArgs']] = None,
                 public_access_block_configuration: Optional[pulumi.Input['BucketPublicAccessBlockConfigurationArgs']] = None,
                 replication_configuration: Optional[pulumi.Input['BucketReplicationConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['BucketTagArgs']]]] = None,
                 versioning_configuration: Optional[pulumi.Input['BucketVersioningConfigurationArgs']] = None,
                 website_configuration: Optional[pulumi.Input['BucketWebsiteConfigurationArgs']] = None):
        """
        The set of arguments for constructing a Bucket resource.
        :param pulumi.Input['BucketAccelerateConfigurationArgs'] accelerate_configuration: Configuration for the transfer acceleration state.
        :param pulumi.Input['BucketAccessControl'] access_control: A canned access control list (ACL) that grants predefined permissions to the bucket.
        :param pulumi.Input[Sequence[pulumi.Input['BucketAnalyticsConfigurationArgs']]] analytics_configurations: The configuration and any analyses for the analytics filter of an Amazon S3 bucket.
        :param pulumi.Input[str] bucket_name: A name for the bucket. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the bucket name.
        :param pulumi.Input['BucketCorsConfigurationArgs'] cors_configuration: Rules that define cross-origin resource sharing of objects in this bucket.
        :param pulumi.Input[Sequence[pulumi.Input['BucketIntelligentTieringConfigurationArgs']]] intelligent_tiering_configurations: Specifies the S3 Intelligent-Tiering configuration for an Amazon S3 bucket.
        :param pulumi.Input[Sequence[pulumi.Input['BucketInventoryConfigurationArgs']]] inventory_configurations: The inventory configuration for an Amazon S3 bucket.
        :param pulumi.Input['BucketLifecycleConfigurationArgs'] lifecycle_configuration: Rules that define how Amazon S3 manages objects during their lifetime.
        :param pulumi.Input['BucketLoggingConfigurationArgs'] logging_configuration: Settings that define where logs are stored.
        :param pulumi.Input[Sequence[pulumi.Input['BucketMetricsConfigurationArgs']]] metrics_configurations: Settings that define a metrics configuration for the CloudWatch request metrics from the bucket.
        :param pulumi.Input['BucketNotificationConfigurationArgs'] notification_configuration: Configuration that defines how Amazon S3 handles bucket notifications.
        :param pulumi.Input['BucketObjectLockConfigurationArgs'] object_lock_configuration: Places an Object Lock configuration on the specified bucket.
        :param pulumi.Input[bool] object_lock_enabled: Indicates whether this bucket has an Object Lock configuration enabled.
        :param pulumi.Input['BucketOwnershipControlsArgs'] ownership_controls: Specifies the container element for object ownership rules.
        :param pulumi.Input['BucketReplicationConfigurationArgs'] replication_configuration: Configuration for replicating objects in an S3 bucket.
        :param pulumi.Input[Sequence[pulumi.Input['BucketTagArgs']]] tags: An arbitrary set of tags (key-value pairs) for this S3 bucket.
        """
        if accelerate_configuration is not None:
            pulumi.set(__self__, "accelerate_configuration", accelerate_configuration)
        if access_control is not None:
            pulumi.set(__self__, "access_control", access_control)
        if analytics_configurations is not None:
            pulumi.set(__self__, "analytics_configurations", analytics_configurations)
        if bucket_encryption is not None:
            pulumi.set(__self__, "bucket_encryption", bucket_encryption)
        if bucket_name is not None:
            pulumi.set(__self__, "bucket_name", bucket_name)
        if cors_configuration is not None:
            pulumi.set(__self__, "cors_configuration", cors_configuration)
        if intelligent_tiering_configurations is not None:
            pulumi.set(__self__, "intelligent_tiering_configurations", intelligent_tiering_configurations)
        if inventory_configurations is not None:
            pulumi.set(__self__, "inventory_configurations", inventory_configurations)
        if lifecycle_configuration is not None:
            pulumi.set(__self__, "lifecycle_configuration", lifecycle_configuration)
        if logging_configuration is not None:
            pulumi.set(__self__, "logging_configuration", logging_configuration)
        if metrics_configurations is not None:
            pulumi.set(__self__, "metrics_configurations", metrics_configurations)
        if notification_configuration is not None:
            pulumi.set(__self__, "notification_configuration", notification_configuration)
        if object_lock_configuration is not None:
            pulumi.set(__self__, "object_lock_configuration", object_lock_configuration)
        if object_lock_enabled is not None:
            pulumi.set(__self__, "object_lock_enabled", object_lock_enabled)
        if ownership_controls is not None:
            pulumi.set(__self__, "ownership_controls", ownership_controls)
        if public_access_block_configuration is not None:
            pulumi.set(__self__, "public_access_block_configuration", public_access_block_configuration)
        if replication_configuration is not None:
            pulumi.set(__self__, "replication_configuration", replication_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if versioning_configuration is not None:
            pulumi.set(__self__, "versioning_configuration", versioning_configuration)
        if website_configuration is not None:
            pulumi.set(__self__, "website_configuration", website_configuration)

    @property
    @pulumi.getter(name="accelerateConfiguration")
    def accelerate_configuration(self) -> Optional[pulumi.Input['BucketAccelerateConfigurationArgs']]:
        """
        Configuration for the transfer acceleration state.
        """
        return pulumi.get(self, "accelerate_configuration")

    @accelerate_configuration.setter
    def accelerate_configuration(self, value: Optional[pulumi.Input['BucketAccelerateConfigurationArgs']]):
        pulumi.set(self, "accelerate_configuration", value)

    @property
    @pulumi.getter(name="accessControl")
    def access_control(self) -> Optional[pulumi.Input['BucketAccessControl']]:
        """
        A canned access control list (ACL) that grants predefined permissions to the bucket.
        """
        return pulumi.get(self, "access_control")

    @access_control.setter
    def access_control(self, value: Optional[pulumi.Input['BucketAccessControl']]):
        pulumi.set(self, "access_control", value)

    @property
    @pulumi.getter(name="analyticsConfigurations")
    def analytics_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BucketAnalyticsConfigurationArgs']]]]:
        """
        The configuration and any analyses for the analytics filter of an Amazon S3 bucket.
        """
        return pulumi.get(self, "analytics_configurations")

    @analytics_configurations.setter
    def analytics_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BucketAnalyticsConfigurationArgs']]]]):
        pulumi.set(self, "analytics_configurations", value)

    @property
    @pulumi.getter(name="bucketEncryption")
    def bucket_encryption(self) -> Optional[pulumi.Input['BucketEncryptionArgs']]:
        return pulumi.get(self, "bucket_encryption")

    @bucket_encryption.setter
    def bucket_encryption(self, value: Optional[pulumi.Input['BucketEncryptionArgs']]):
        pulumi.set(self, "bucket_encryption", value)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the bucket. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the bucket name.
        """
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_name", value)

    @property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> Optional[pulumi.Input['BucketCorsConfigurationArgs']]:
        """
        Rules that define cross-origin resource sharing of objects in this bucket.
        """
        return pulumi.get(self, "cors_configuration")

    @cors_configuration.setter
    def cors_configuration(self, value: Optional[pulumi.Input['BucketCorsConfigurationArgs']]):
        pulumi.set(self, "cors_configuration", value)

    @property
    @pulumi.getter(name="intelligentTieringConfigurations")
    def intelligent_tiering_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BucketIntelligentTieringConfigurationArgs']]]]:
        """
        Specifies the S3 Intelligent-Tiering configuration for an Amazon S3 bucket.
        """
        return pulumi.get(self, "intelligent_tiering_configurations")

    @intelligent_tiering_configurations.setter
    def intelligent_tiering_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BucketIntelligentTieringConfigurationArgs']]]]):
        pulumi.set(self, "intelligent_tiering_configurations", value)

    @property
    @pulumi.getter(name="inventoryConfigurations")
    def inventory_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BucketInventoryConfigurationArgs']]]]:
        """
        The inventory configuration for an Amazon S3 bucket.
        """
        return pulumi.get(self, "inventory_configurations")

    @inventory_configurations.setter
    def inventory_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BucketInventoryConfigurationArgs']]]]):
        pulumi.set(self, "inventory_configurations", value)

    @property
    @pulumi.getter(name="lifecycleConfiguration")
    def lifecycle_configuration(self) -> Optional[pulumi.Input['BucketLifecycleConfigurationArgs']]:
        """
        Rules that define how Amazon S3 manages objects during their lifetime.
        """
        return pulumi.get(self, "lifecycle_configuration")

    @lifecycle_configuration.setter
    def lifecycle_configuration(self, value: Optional[pulumi.Input['BucketLifecycleConfigurationArgs']]):
        pulumi.set(self, "lifecycle_configuration", value)

    @property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(self) -> Optional[pulumi.Input['BucketLoggingConfigurationArgs']]:
        """
        Settings that define where logs are stored.
        """
        return pulumi.get(self, "logging_configuration")

    @logging_configuration.setter
    def logging_configuration(self, value: Optional[pulumi.Input['BucketLoggingConfigurationArgs']]):
        pulumi.set(self, "logging_configuration", value)

    @property
    @pulumi.getter(name="metricsConfigurations")
    def metrics_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BucketMetricsConfigurationArgs']]]]:
        """
        Settings that define a metrics configuration for the CloudWatch request metrics from the bucket.
        """
        return pulumi.get(self, "metrics_configurations")

    @metrics_configurations.setter
    def metrics_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BucketMetricsConfigurationArgs']]]]):
        pulumi.set(self, "metrics_configurations", value)

    @property
    @pulumi.getter(name="notificationConfiguration")
    def notification_configuration(self) -> Optional[pulumi.Input['BucketNotificationConfigurationArgs']]:
        """
        Configuration that defines how Amazon S3 handles bucket notifications.
        """
        return pulumi.get(self, "notification_configuration")

    @notification_configuration.setter
    def notification_configuration(self, value: Optional[pulumi.Input['BucketNotificationConfigurationArgs']]):
        pulumi.set(self, "notification_configuration", value)

    @property
    @pulumi.getter(name="objectLockConfiguration")
    def object_lock_configuration(self) -> Optional[pulumi.Input['BucketObjectLockConfigurationArgs']]:
        """
        Places an Object Lock configuration on the specified bucket.
        """
        return pulumi.get(self, "object_lock_configuration")

    @object_lock_configuration.setter
    def object_lock_configuration(self, value: Optional[pulumi.Input['BucketObjectLockConfigurationArgs']]):
        pulumi.set(self, "object_lock_configuration", value)

    @property
    @pulumi.getter(name="objectLockEnabled")
    def object_lock_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether this bucket has an Object Lock configuration enabled.
        """
        return pulumi.get(self, "object_lock_enabled")

    @object_lock_enabled.setter
    def object_lock_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "object_lock_enabled", value)

    @property
    @pulumi.getter(name="ownershipControls")
    def ownership_controls(self) -> Optional[pulumi.Input['BucketOwnershipControlsArgs']]:
        """
        Specifies the container element for object ownership rules.
        """
        return pulumi.get(self, "ownership_controls")

    @ownership_controls.setter
    def ownership_controls(self, value: Optional[pulumi.Input['BucketOwnershipControlsArgs']]):
        pulumi.set(self, "ownership_controls", value)

    @property
    @pulumi.getter(name="publicAccessBlockConfiguration")
    def public_access_block_configuration(self) -> Optional[pulumi.Input['BucketPublicAccessBlockConfigurationArgs']]:
        return pulumi.get(self, "public_access_block_configuration")

    @public_access_block_configuration.setter
    def public_access_block_configuration(self, value: Optional[pulumi.Input['BucketPublicAccessBlockConfigurationArgs']]):
        pulumi.set(self, "public_access_block_configuration", value)

    @property
    @pulumi.getter(name="replicationConfiguration")
    def replication_configuration(self) -> Optional[pulumi.Input['BucketReplicationConfigurationArgs']]:
        """
        Configuration for replicating objects in an S3 bucket.
        """
        return pulumi.get(self, "replication_configuration")

    @replication_configuration.setter
    def replication_configuration(self, value: Optional[pulumi.Input['BucketReplicationConfigurationArgs']]):
        pulumi.set(self, "replication_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BucketTagArgs']]]]:
        """
        An arbitrary set of tags (key-value pairs) for this S3 bucket.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BucketTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="versioningConfiguration")
    def versioning_configuration(self) -> Optional[pulumi.Input['BucketVersioningConfigurationArgs']]:
        return pulumi.get(self, "versioning_configuration")

    @versioning_configuration.setter
    def versioning_configuration(self, value: Optional[pulumi.Input['BucketVersioningConfigurationArgs']]):
        pulumi.set(self, "versioning_configuration", value)

    @property
    @pulumi.getter(name="websiteConfiguration")
    def website_configuration(self) -> Optional[pulumi.Input['BucketWebsiteConfigurationArgs']]:
        return pulumi.get(self, "website_configuration")

    @website_configuration.setter
    def website_configuration(self, value: Optional[pulumi.Input['BucketWebsiteConfigurationArgs']]):
        pulumi.set(self, "website_configuration", value)


class Bucket(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerate_configuration: Optional[pulumi.Input[pulumi.InputType['BucketAccelerateConfigurationArgs']]] = None,
                 access_control: Optional[pulumi.Input['BucketAccessControl']] = None,
                 analytics_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketAnalyticsConfigurationArgs']]]]] = None,
                 bucket_encryption: Optional[pulumi.Input[pulumi.InputType['BucketEncryptionArgs']]] = None,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 cors_configuration: Optional[pulumi.Input[pulumi.InputType['BucketCorsConfigurationArgs']]] = None,
                 intelligent_tiering_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketIntelligentTieringConfigurationArgs']]]]] = None,
                 inventory_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketInventoryConfigurationArgs']]]]] = None,
                 lifecycle_configuration: Optional[pulumi.Input[pulumi.InputType['BucketLifecycleConfigurationArgs']]] = None,
                 logging_configuration: Optional[pulumi.Input[pulumi.InputType['BucketLoggingConfigurationArgs']]] = None,
                 metrics_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketMetricsConfigurationArgs']]]]] = None,
                 notification_configuration: Optional[pulumi.Input[pulumi.InputType['BucketNotificationConfigurationArgs']]] = None,
                 object_lock_configuration: Optional[pulumi.Input[pulumi.InputType['BucketObjectLockConfigurationArgs']]] = None,
                 object_lock_enabled: Optional[pulumi.Input[bool]] = None,
                 ownership_controls: Optional[pulumi.Input[pulumi.InputType['BucketOwnershipControlsArgs']]] = None,
                 public_access_block_configuration: Optional[pulumi.Input[pulumi.InputType['BucketPublicAccessBlockConfigurationArgs']]] = None,
                 replication_configuration: Optional[pulumi.Input[pulumi.InputType['BucketReplicationConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketTagArgs']]]]] = None,
                 versioning_configuration: Optional[pulumi.Input[pulumi.InputType['BucketVersioningConfigurationArgs']]] = None,
                 website_configuration: Optional[pulumi.Input[pulumi.InputType['BucketWebsiteConfigurationArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::S3::Bucket

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['BucketAccelerateConfigurationArgs']] accelerate_configuration: Configuration for the transfer acceleration state.
        :param pulumi.Input['BucketAccessControl'] access_control: A canned access control list (ACL) that grants predefined permissions to the bucket.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketAnalyticsConfigurationArgs']]]] analytics_configurations: The configuration and any analyses for the analytics filter of an Amazon S3 bucket.
        :param pulumi.Input[str] bucket_name: A name for the bucket. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the bucket name.
        :param pulumi.Input[pulumi.InputType['BucketCorsConfigurationArgs']] cors_configuration: Rules that define cross-origin resource sharing of objects in this bucket.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketIntelligentTieringConfigurationArgs']]]] intelligent_tiering_configurations: Specifies the S3 Intelligent-Tiering configuration for an Amazon S3 bucket.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketInventoryConfigurationArgs']]]] inventory_configurations: The inventory configuration for an Amazon S3 bucket.
        :param pulumi.Input[pulumi.InputType['BucketLifecycleConfigurationArgs']] lifecycle_configuration: Rules that define how Amazon S3 manages objects during their lifetime.
        :param pulumi.Input[pulumi.InputType['BucketLoggingConfigurationArgs']] logging_configuration: Settings that define where logs are stored.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketMetricsConfigurationArgs']]]] metrics_configurations: Settings that define a metrics configuration for the CloudWatch request metrics from the bucket.
        :param pulumi.Input[pulumi.InputType['BucketNotificationConfigurationArgs']] notification_configuration: Configuration that defines how Amazon S3 handles bucket notifications.
        :param pulumi.Input[pulumi.InputType['BucketObjectLockConfigurationArgs']] object_lock_configuration: Places an Object Lock configuration on the specified bucket.
        :param pulumi.Input[bool] object_lock_enabled: Indicates whether this bucket has an Object Lock configuration enabled.
        :param pulumi.Input[pulumi.InputType['BucketOwnershipControlsArgs']] ownership_controls: Specifies the container element for object ownership rules.
        :param pulumi.Input[pulumi.InputType['BucketReplicationConfigurationArgs']] replication_configuration: Configuration for replicating objects in an S3 bucket.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketTagArgs']]]] tags: An arbitrary set of tags (key-value pairs) for this S3 bucket.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[BucketArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::S3::Bucket

        :param str resource_name: The name of the resource.
        :param BucketArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BucketArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerate_configuration: Optional[pulumi.Input[pulumi.InputType['BucketAccelerateConfigurationArgs']]] = None,
                 access_control: Optional[pulumi.Input['BucketAccessControl']] = None,
                 analytics_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketAnalyticsConfigurationArgs']]]]] = None,
                 bucket_encryption: Optional[pulumi.Input[pulumi.InputType['BucketEncryptionArgs']]] = None,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 cors_configuration: Optional[pulumi.Input[pulumi.InputType['BucketCorsConfigurationArgs']]] = None,
                 intelligent_tiering_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketIntelligentTieringConfigurationArgs']]]]] = None,
                 inventory_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketInventoryConfigurationArgs']]]]] = None,
                 lifecycle_configuration: Optional[pulumi.Input[pulumi.InputType['BucketLifecycleConfigurationArgs']]] = None,
                 logging_configuration: Optional[pulumi.Input[pulumi.InputType['BucketLoggingConfigurationArgs']]] = None,
                 metrics_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketMetricsConfigurationArgs']]]]] = None,
                 notification_configuration: Optional[pulumi.Input[pulumi.InputType['BucketNotificationConfigurationArgs']]] = None,
                 object_lock_configuration: Optional[pulumi.Input[pulumi.InputType['BucketObjectLockConfigurationArgs']]] = None,
                 object_lock_enabled: Optional[pulumi.Input[bool]] = None,
                 ownership_controls: Optional[pulumi.Input[pulumi.InputType['BucketOwnershipControlsArgs']]] = None,
                 public_access_block_configuration: Optional[pulumi.Input[pulumi.InputType['BucketPublicAccessBlockConfigurationArgs']]] = None,
                 replication_configuration: Optional[pulumi.Input[pulumi.InputType['BucketReplicationConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketTagArgs']]]]] = None,
                 versioning_configuration: Optional[pulumi.Input[pulumi.InputType['BucketVersioningConfigurationArgs']]] = None,
                 website_configuration: Optional[pulumi.Input[pulumi.InputType['BucketWebsiteConfigurationArgs']]] = None,
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
            __props__ = BucketArgs.__new__(BucketArgs)

            __props__.__dict__["accelerate_configuration"] = accelerate_configuration
            __props__.__dict__["access_control"] = access_control
            __props__.__dict__["analytics_configurations"] = analytics_configurations
            __props__.__dict__["bucket_encryption"] = bucket_encryption
            __props__.__dict__["bucket_name"] = bucket_name
            __props__.__dict__["cors_configuration"] = cors_configuration
            __props__.__dict__["intelligent_tiering_configurations"] = intelligent_tiering_configurations
            __props__.__dict__["inventory_configurations"] = inventory_configurations
            __props__.__dict__["lifecycle_configuration"] = lifecycle_configuration
            __props__.__dict__["logging_configuration"] = logging_configuration
            __props__.__dict__["metrics_configurations"] = metrics_configurations
            __props__.__dict__["notification_configuration"] = notification_configuration
            __props__.__dict__["object_lock_configuration"] = object_lock_configuration
            __props__.__dict__["object_lock_enabled"] = object_lock_enabled
            __props__.__dict__["ownership_controls"] = ownership_controls
            __props__.__dict__["public_access_block_configuration"] = public_access_block_configuration
            __props__.__dict__["replication_configuration"] = replication_configuration
            __props__.__dict__["tags"] = tags
            __props__.__dict__["versioning_configuration"] = versioning_configuration
            __props__.__dict__["website_configuration"] = website_configuration
            __props__.__dict__["arn"] = None
            __props__.__dict__["domain_name"] = None
            __props__.__dict__["dual_stack_domain_name"] = None
            __props__.__dict__["regional_domain_name"] = None
            __props__.__dict__["website_url"] = None
        super(Bucket, __self__).__init__(
            'aws-native:s3:Bucket',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Bucket':
        """
        Get an existing Bucket resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BucketArgs.__new__(BucketArgs)

        __props__.__dict__["accelerate_configuration"] = None
        __props__.__dict__["access_control"] = None
        __props__.__dict__["analytics_configurations"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["bucket_encryption"] = None
        __props__.__dict__["bucket_name"] = None
        __props__.__dict__["cors_configuration"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["dual_stack_domain_name"] = None
        __props__.__dict__["intelligent_tiering_configurations"] = None
        __props__.__dict__["inventory_configurations"] = None
        __props__.__dict__["lifecycle_configuration"] = None
        __props__.__dict__["logging_configuration"] = None
        __props__.__dict__["metrics_configurations"] = None
        __props__.__dict__["notification_configuration"] = None
        __props__.__dict__["object_lock_configuration"] = None
        __props__.__dict__["object_lock_enabled"] = None
        __props__.__dict__["ownership_controls"] = None
        __props__.__dict__["public_access_block_configuration"] = None
        __props__.__dict__["regional_domain_name"] = None
        __props__.__dict__["replication_configuration"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["versioning_configuration"] = None
        __props__.__dict__["website_configuration"] = None
        __props__.__dict__["website_url"] = None
        return Bucket(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accelerateConfiguration")
    def accelerate_configuration(self) -> pulumi.Output[Optional['outputs.BucketAccelerateConfiguration']]:
        """
        Configuration for the transfer acceleration state.
        """
        return pulumi.get(self, "accelerate_configuration")

    @property
    @pulumi.getter(name="accessControl")
    def access_control(self) -> pulumi.Output[Optional['BucketAccessControl']]:
        """
        A canned access control list (ACL) that grants predefined permissions to the bucket.
        """
        return pulumi.get(self, "access_control")

    @property
    @pulumi.getter(name="analyticsConfigurations")
    def analytics_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.BucketAnalyticsConfiguration']]]:
        """
        The configuration and any analyses for the analytics filter of an Amazon S3 bucket.
        """
        return pulumi.get(self, "analytics_configurations")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the specified bucket.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="bucketEncryption")
    def bucket_encryption(self) -> pulumi.Output[Optional['outputs.BucketEncryption']]:
        return pulumi.get(self, "bucket_encryption")

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Output[Optional[str]]:
        """
        A name for the bucket. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the bucket name.
        """
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> pulumi.Output[Optional['outputs.BucketCorsConfiguration']]:
        """
        Rules that define cross-origin resource sharing of objects in this bucket.
        """
        return pulumi.get(self, "cors_configuration")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The IPv4 DNS name of the specified bucket.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="dualStackDomainName")
    def dual_stack_domain_name(self) -> pulumi.Output[str]:
        """
        The IPv6 DNS name of the specified bucket. For more information about dual-stack endpoints, see [Using Amazon S3 Dual-Stack Endpoints](https://docs.aws.amazon.com/AmazonS3/latest/dev/dual-stack-endpoints.html).
        """
        return pulumi.get(self, "dual_stack_domain_name")

    @property
    @pulumi.getter(name="intelligentTieringConfigurations")
    def intelligent_tiering_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.BucketIntelligentTieringConfiguration']]]:
        """
        Specifies the S3 Intelligent-Tiering configuration for an Amazon S3 bucket.
        """
        return pulumi.get(self, "intelligent_tiering_configurations")

    @property
    @pulumi.getter(name="inventoryConfigurations")
    def inventory_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.BucketInventoryConfiguration']]]:
        """
        The inventory configuration for an Amazon S3 bucket.
        """
        return pulumi.get(self, "inventory_configurations")

    @property
    @pulumi.getter(name="lifecycleConfiguration")
    def lifecycle_configuration(self) -> pulumi.Output[Optional['outputs.BucketLifecycleConfiguration']]:
        """
        Rules that define how Amazon S3 manages objects during their lifetime.
        """
        return pulumi.get(self, "lifecycle_configuration")

    @property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(self) -> pulumi.Output[Optional['outputs.BucketLoggingConfiguration']]:
        """
        Settings that define where logs are stored.
        """
        return pulumi.get(self, "logging_configuration")

    @property
    @pulumi.getter(name="metricsConfigurations")
    def metrics_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.BucketMetricsConfiguration']]]:
        """
        Settings that define a metrics configuration for the CloudWatch request metrics from the bucket.
        """
        return pulumi.get(self, "metrics_configurations")

    @property
    @pulumi.getter(name="notificationConfiguration")
    def notification_configuration(self) -> pulumi.Output[Optional['outputs.BucketNotificationConfiguration']]:
        """
        Configuration that defines how Amazon S3 handles bucket notifications.
        """
        return pulumi.get(self, "notification_configuration")

    @property
    @pulumi.getter(name="objectLockConfiguration")
    def object_lock_configuration(self) -> pulumi.Output[Optional['outputs.BucketObjectLockConfiguration']]:
        """
        Places an Object Lock configuration on the specified bucket.
        """
        return pulumi.get(self, "object_lock_configuration")

    @property
    @pulumi.getter(name="objectLockEnabled")
    def object_lock_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether this bucket has an Object Lock configuration enabled.
        """
        return pulumi.get(self, "object_lock_enabled")

    @property
    @pulumi.getter(name="ownershipControls")
    def ownership_controls(self) -> pulumi.Output[Optional['outputs.BucketOwnershipControls']]:
        """
        Specifies the container element for object ownership rules.
        """
        return pulumi.get(self, "ownership_controls")

    @property
    @pulumi.getter(name="publicAccessBlockConfiguration")
    def public_access_block_configuration(self) -> pulumi.Output[Optional['outputs.BucketPublicAccessBlockConfiguration']]:
        return pulumi.get(self, "public_access_block_configuration")

    @property
    @pulumi.getter(name="regionalDomainName")
    def regional_domain_name(self) -> pulumi.Output[str]:
        """
        Returns the regional domain name of the specified bucket.
        """
        return pulumi.get(self, "regional_domain_name")

    @property
    @pulumi.getter(name="replicationConfiguration")
    def replication_configuration(self) -> pulumi.Output[Optional['outputs.BucketReplicationConfiguration']]:
        """
        Configuration for replicating objects in an S3 bucket.
        """
        return pulumi.get(self, "replication_configuration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.BucketTag']]]:
        """
        An arbitrary set of tags (key-value pairs) for this S3 bucket.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="versioningConfiguration")
    def versioning_configuration(self) -> pulumi.Output[Optional['outputs.BucketVersioningConfiguration']]:
        return pulumi.get(self, "versioning_configuration")

    @property
    @pulumi.getter(name="websiteConfiguration")
    def website_configuration(self) -> pulumi.Output[Optional['outputs.BucketWebsiteConfiguration']]:
        return pulumi.get(self, "website_configuration")

    @property
    @pulumi.getter(name="websiteURL")
    def website_url(self) -> pulumi.Output[str]:
        """
        The Amazon S3 website endpoint for the specified bucket.
        """
        return pulumi.get(self, "website_url")

