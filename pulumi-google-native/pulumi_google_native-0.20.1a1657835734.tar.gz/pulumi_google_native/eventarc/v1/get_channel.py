# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetChannelResult',
    'AwaitableGetChannelResult',
    'get_channel',
    'get_channel_output',
]

@pulumi.output_type
class GetChannelResult:
    def __init__(__self__, activation_token=None, create_time=None, crypto_key_name=None, name=None, provider=None, pubsub_topic=None, state=None, uid=None, update_time=None):
        if activation_token and not isinstance(activation_token, str):
            raise TypeError("Expected argument 'activation_token' to be a str")
        pulumi.set(__self__, "activation_token", activation_token)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if crypto_key_name and not isinstance(crypto_key_name, str):
            raise TypeError("Expected argument 'crypto_key_name' to be a str")
        pulumi.set(__self__, "crypto_key_name", crypto_key_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provider and not isinstance(provider, str):
            raise TypeError("Expected argument 'provider' to be a str")
        pulumi.set(__self__, "provider", provider)
        if pubsub_topic and not isinstance(pubsub_topic, str):
            raise TypeError("Expected argument 'pubsub_topic' to be a str")
        pulumi.set(__self__, "pubsub_topic", pubsub_topic)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="activationToken")
    def activation_token(self) -> str:
        """
        The activation token for the channel. The token must be used by the provider to register the channel for publishing.
        """
        return pulumi.get(self, "activation_token")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The creation time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> str:
        """
        Optional. Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt their event data. It must match the pattern `projects/*/locations/*/keyRings/*/cryptoKeys/*`.
        """
        return pulumi.get(self, "crypto_key_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the channel. Must be unique within the location on the project and must be in `projects/{project}/locations/{location}/channels/{channel_id}` format.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def provider(self) -> str:
        """
        The name of the event provider (e.g. Eventarc SaaS partner) associated with the channel. This provider will be granted permissions to publish events to the channel. Format: `projects/{project}/locations/{location}/providers/{provider_id}`.
        """
        return pulumi.get(self, "provider")

    @property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> str:
        """
        The name of the Pub/Sub topic created and managed by Eventarc system as a transport for the event delivery. Format: `projects/{project}/topics/{topic_id}`.
        """
        return pulumi.get(self, "pubsub_topic")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of a Channel.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def uid(self) -> str:
        """
        Server assigned unique identifier for the channel. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The last-modified time.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetChannelResult(GetChannelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetChannelResult(
            activation_token=self.activation_token,
            create_time=self.create_time,
            crypto_key_name=self.crypto_key_name,
            name=self.name,
            provider=self.provider,
            pubsub_topic=self.pubsub_topic,
            state=self.state,
            uid=self.uid,
            update_time=self.update_time)


def get_channel(channel_id: Optional[str] = None,
                location: Optional[str] = None,
                project: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetChannelResult:
    """
    Get a single Channel.
    """
    __args__ = dict()
    __args__['channelId'] = channel_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:eventarc/v1:getChannel', __args__, opts=opts, typ=GetChannelResult).value

    return AwaitableGetChannelResult(
        activation_token=__ret__.activation_token,
        create_time=__ret__.create_time,
        crypto_key_name=__ret__.crypto_key_name,
        name=__ret__.name,
        provider=__ret__.provider,
        pubsub_topic=__ret__.pubsub_topic,
        state=__ret__.state,
        uid=__ret__.uid,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_channel)
def get_channel_output(channel_id: Optional[pulumi.Input[str]] = None,
                       location: Optional[pulumi.Input[str]] = None,
                       project: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetChannelResult]:
    """
    Get a single Channel.
    """
    ...
