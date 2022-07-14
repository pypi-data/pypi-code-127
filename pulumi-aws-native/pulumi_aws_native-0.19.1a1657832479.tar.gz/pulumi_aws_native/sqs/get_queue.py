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
    'GetQueueResult',
    'AwaitableGetQueueResult',
    'get_queue',
    'get_queue_output',
]

@pulumi.output_type
class GetQueueResult:
    def __init__(__self__, arn=None, content_based_deduplication=None, deduplication_scope=None, delay_seconds=None, fifo_throughput_limit=None, kms_data_key_reuse_period_seconds=None, kms_master_key_id=None, maximum_message_size=None, message_retention_period=None, queue_url=None, receive_message_wait_time_seconds=None, redrive_allow_policy=None, redrive_policy=None, sqs_managed_sse_enabled=None, tags=None, visibility_timeout=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if content_based_deduplication and not isinstance(content_based_deduplication, bool):
            raise TypeError("Expected argument 'content_based_deduplication' to be a bool")
        pulumi.set(__self__, "content_based_deduplication", content_based_deduplication)
        if deduplication_scope and not isinstance(deduplication_scope, str):
            raise TypeError("Expected argument 'deduplication_scope' to be a str")
        pulumi.set(__self__, "deduplication_scope", deduplication_scope)
        if delay_seconds and not isinstance(delay_seconds, int):
            raise TypeError("Expected argument 'delay_seconds' to be a int")
        pulumi.set(__self__, "delay_seconds", delay_seconds)
        if fifo_throughput_limit and not isinstance(fifo_throughput_limit, str):
            raise TypeError("Expected argument 'fifo_throughput_limit' to be a str")
        pulumi.set(__self__, "fifo_throughput_limit", fifo_throughput_limit)
        if kms_data_key_reuse_period_seconds and not isinstance(kms_data_key_reuse_period_seconds, int):
            raise TypeError("Expected argument 'kms_data_key_reuse_period_seconds' to be a int")
        pulumi.set(__self__, "kms_data_key_reuse_period_seconds", kms_data_key_reuse_period_seconds)
        if kms_master_key_id and not isinstance(kms_master_key_id, str):
            raise TypeError("Expected argument 'kms_master_key_id' to be a str")
        pulumi.set(__self__, "kms_master_key_id", kms_master_key_id)
        if maximum_message_size and not isinstance(maximum_message_size, int):
            raise TypeError("Expected argument 'maximum_message_size' to be a int")
        pulumi.set(__self__, "maximum_message_size", maximum_message_size)
        if message_retention_period and not isinstance(message_retention_period, int):
            raise TypeError("Expected argument 'message_retention_period' to be a int")
        pulumi.set(__self__, "message_retention_period", message_retention_period)
        if queue_url and not isinstance(queue_url, str):
            raise TypeError("Expected argument 'queue_url' to be a str")
        pulumi.set(__self__, "queue_url", queue_url)
        if receive_message_wait_time_seconds and not isinstance(receive_message_wait_time_seconds, int):
            raise TypeError("Expected argument 'receive_message_wait_time_seconds' to be a int")
        pulumi.set(__self__, "receive_message_wait_time_seconds", receive_message_wait_time_seconds)
        if redrive_allow_policy and not isinstance(redrive_allow_policy, dict):
            raise TypeError("Expected argument 'redrive_allow_policy' to be a dict")
        pulumi.set(__self__, "redrive_allow_policy", redrive_allow_policy)
        if redrive_policy and not isinstance(redrive_policy, dict):
            raise TypeError("Expected argument 'redrive_policy' to be a dict")
        pulumi.set(__self__, "redrive_policy", redrive_policy)
        if sqs_managed_sse_enabled and not isinstance(sqs_managed_sse_enabled, bool):
            raise TypeError("Expected argument 'sqs_managed_sse_enabled' to be a bool")
        pulumi.set(__self__, "sqs_managed_sse_enabled", sqs_managed_sse_enabled)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if visibility_timeout and not isinstance(visibility_timeout, int):
            raise TypeError("Expected argument 'visibility_timeout' to be a int")
        pulumi.set(__self__, "visibility_timeout", visibility_timeout)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of the queue.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="contentBasedDeduplication")
    def content_based_deduplication(self) -> Optional[bool]:
        """
        For first-in-first-out (FIFO) queues, specifies whether to enable content-based deduplication. During the deduplication interval, Amazon SQS treats messages that are sent with identical content as duplicates and delivers only one copy of the message.
        """
        return pulumi.get(self, "content_based_deduplication")

    @property
    @pulumi.getter(name="deduplicationScope")
    def deduplication_scope(self) -> Optional[str]:
        """
        Specifies whether message deduplication occurs at the message group or queue level. Valid values are messageGroup and queue.
        """
        return pulumi.get(self, "deduplication_scope")

    @property
    @pulumi.getter(name="delaySeconds")
    def delay_seconds(self) -> Optional[int]:
        """
        The time in seconds for which the delivery of all messages in the queue is delayed. You can specify an integer value of 0 to 900 (15 minutes). The default value is 0.
        """
        return pulumi.get(self, "delay_seconds")

    @property
    @pulumi.getter(name="fifoThroughputLimit")
    def fifo_throughput_limit(self) -> Optional[str]:
        """
        Specifies whether the FIFO queue throughput quota applies to the entire queue or per message group. Valid values are perQueue and perMessageGroupId. The perMessageGroupId value is allowed only when the value for DeduplicationScope is messageGroup.
        """
        return pulumi.get(self, "fifo_throughput_limit")

    @property
    @pulumi.getter(name="kmsDataKeyReusePeriodSeconds")
    def kms_data_key_reuse_period_seconds(self) -> Optional[int]:
        """
        The length of time in seconds for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. The value must be an integer between 60 (1 minute) and 86,400 (24 hours). The default is 300 (5 minutes).
        """
        return pulumi.get(self, "kms_data_key_reuse_period_seconds")

    @property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> Optional[str]:
        """
        The ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK. To use the AWS managed CMK for Amazon SQS, specify the (default) alias alias/aws/sqs.
        """
        return pulumi.get(self, "kms_master_key_id")

    @property
    @pulumi.getter(name="maximumMessageSize")
    def maximum_message_size(self) -> Optional[int]:
        """
        The limit of how many bytes that a message can contain before Amazon SQS rejects it. You can specify an integer value from 1,024 bytes (1 KiB) to 262,144 bytes (256 KiB). The default value is 262,144 (256 KiB).
        """
        return pulumi.get(self, "maximum_message_size")

    @property
    @pulumi.getter(name="messageRetentionPeriod")
    def message_retention_period(self) -> Optional[int]:
        """
        The number of seconds that Amazon SQS retains a message. You can specify an integer value from 60 seconds (1 minute) to 1,209,600 seconds (14 days). The default value is 345,600 seconds (4 days).
        """
        return pulumi.get(self, "message_retention_period")

    @property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> Optional[str]:
        """
        URL of the source queue.
        """
        return pulumi.get(self, "queue_url")

    @property
    @pulumi.getter(name="receiveMessageWaitTimeSeconds")
    def receive_message_wait_time_seconds(self) -> Optional[int]:
        """
        Specifies the duration, in seconds, that the ReceiveMessage action call waits until a message is in the queue in order to include it in the response, rather than returning an empty response if a message isn't yet available. You can specify an integer from 1 to 20. Short polling is used as the default or when you specify 0 for this property.
        """
        return pulumi.get(self, "receive_message_wait_time_seconds")

    @property
    @pulumi.getter(name="redriveAllowPolicy")
    def redrive_allow_policy(self) -> Optional[Any]:
        """
        The string that includes the parameters for the permissions for the dead-letter queue redrive permission and which source queues can specify dead-letter queues as a JSON object.
        """
        return pulumi.get(self, "redrive_allow_policy")

    @property
    @pulumi.getter(name="redrivePolicy")
    def redrive_policy(self) -> Optional[Any]:
        """
        A string that includes the parameters for the dead-letter queue functionality (redrive policy) of the source queue.
        """
        return pulumi.get(self, "redrive_policy")

    @property
    @pulumi.getter(name="sqsManagedSseEnabled")
    def sqs_managed_sse_enabled(self) -> Optional[bool]:
        """
        Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (e.g. SSE-KMS or SSE-SQS ).
        """
        return pulumi.get(self, "sqs_managed_sse_enabled")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.QueueTag']]:
        """
        The tags that you attach to this queue.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="visibilityTimeout")
    def visibility_timeout(self) -> Optional[int]:
        """
        The length of time during which a message will be unavailable after a message is delivered from the queue. This blocks other components from receiving the same message and gives the initial component time to process and delete the message from the queue. Values must be from 0 to 43,200 seconds (12 hours). If you don't specify a value, AWS CloudFormation uses the default value of 30 seconds.
        """
        return pulumi.get(self, "visibility_timeout")


class AwaitableGetQueueResult(GetQueueResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetQueueResult(
            arn=self.arn,
            content_based_deduplication=self.content_based_deduplication,
            deduplication_scope=self.deduplication_scope,
            delay_seconds=self.delay_seconds,
            fifo_throughput_limit=self.fifo_throughput_limit,
            kms_data_key_reuse_period_seconds=self.kms_data_key_reuse_period_seconds,
            kms_master_key_id=self.kms_master_key_id,
            maximum_message_size=self.maximum_message_size,
            message_retention_period=self.message_retention_period,
            queue_url=self.queue_url,
            receive_message_wait_time_seconds=self.receive_message_wait_time_seconds,
            redrive_allow_policy=self.redrive_allow_policy,
            redrive_policy=self.redrive_policy,
            sqs_managed_sse_enabled=self.sqs_managed_sse_enabled,
            tags=self.tags,
            visibility_timeout=self.visibility_timeout)


def get_queue(queue_url: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetQueueResult:
    """
    Resource Type definition for AWS::SQS::Queue


    :param str queue_url: URL of the source queue.
    """
    __args__ = dict()
    __args__['queueUrl'] = queue_url
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:sqs:getQueue', __args__, opts=opts, typ=GetQueueResult).value

    return AwaitableGetQueueResult(
        arn=__ret__.arn,
        content_based_deduplication=__ret__.content_based_deduplication,
        deduplication_scope=__ret__.deduplication_scope,
        delay_seconds=__ret__.delay_seconds,
        fifo_throughput_limit=__ret__.fifo_throughput_limit,
        kms_data_key_reuse_period_seconds=__ret__.kms_data_key_reuse_period_seconds,
        kms_master_key_id=__ret__.kms_master_key_id,
        maximum_message_size=__ret__.maximum_message_size,
        message_retention_period=__ret__.message_retention_period,
        queue_url=__ret__.queue_url,
        receive_message_wait_time_seconds=__ret__.receive_message_wait_time_seconds,
        redrive_allow_policy=__ret__.redrive_allow_policy,
        redrive_policy=__ret__.redrive_policy,
        sqs_managed_sse_enabled=__ret__.sqs_managed_sse_enabled,
        tags=__ret__.tags,
        visibility_timeout=__ret__.visibility_timeout)


@_utilities.lift_output_func(get_queue)
def get_queue_output(queue_url: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetQueueResult]:
    """
    Resource Type definition for AWS::SQS::Queue


    :param str queue_url: URL of the source queue.
    """
    ...
