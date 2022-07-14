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

__all__ = [
    'GetBotAliasResult',
    'AwaitableGetBotAliasResult',
    'get_bot_alias',
    'get_bot_alias_output',
]

@pulumi.output_type
class GetBotAliasResult:
    def __init__(__self__, arn=None, bot_alias_id=None, bot_alias_locale_settings=None, bot_alias_name=None, bot_alias_status=None, bot_version=None, conversation_log_settings=None, description=None, sentiment_analysis_settings=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if bot_alias_id and not isinstance(bot_alias_id, str):
            raise TypeError("Expected argument 'bot_alias_id' to be a str")
        pulumi.set(__self__, "bot_alias_id", bot_alias_id)
        if bot_alias_locale_settings and not isinstance(bot_alias_locale_settings, list):
            raise TypeError("Expected argument 'bot_alias_locale_settings' to be a list")
        pulumi.set(__self__, "bot_alias_locale_settings", bot_alias_locale_settings)
        if bot_alias_name and not isinstance(bot_alias_name, str):
            raise TypeError("Expected argument 'bot_alias_name' to be a str")
        pulumi.set(__self__, "bot_alias_name", bot_alias_name)
        if bot_alias_status and not isinstance(bot_alias_status, str):
            raise TypeError("Expected argument 'bot_alias_status' to be a str")
        pulumi.set(__self__, "bot_alias_status", bot_alias_status)
        if bot_version and not isinstance(bot_version, str):
            raise TypeError("Expected argument 'bot_version' to be a str")
        pulumi.set(__self__, "bot_version", bot_version)
        if conversation_log_settings and not isinstance(conversation_log_settings, dict):
            raise TypeError("Expected argument 'conversation_log_settings' to be a dict")
        pulumi.set(__self__, "conversation_log_settings", conversation_log_settings)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if sentiment_analysis_settings and not isinstance(sentiment_analysis_settings, dict):
            raise TypeError("Expected argument 'sentiment_analysis_settings' to be a dict")
        pulumi.set(__self__, "sentiment_analysis_settings", sentiment_analysis_settings)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="botAliasId")
    def bot_alias_id(self) -> Optional[str]:
        return pulumi.get(self, "bot_alias_id")

    @property
    @pulumi.getter(name="botAliasLocaleSettings")
    def bot_alias_locale_settings(self) -> Optional[Sequence['outputs.BotAliasLocaleSettingsItem']]:
        return pulumi.get(self, "bot_alias_locale_settings")

    @property
    @pulumi.getter(name="botAliasName")
    def bot_alias_name(self) -> Optional[str]:
        return pulumi.get(self, "bot_alias_name")

    @property
    @pulumi.getter(name="botAliasStatus")
    def bot_alias_status(self) -> Optional['BotAliasStatus']:
        return pulumi.get(self, "bot_alias_status")

    @property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> Optional[str]:
        return pulumi.get(self, "bot_version")

    @property
    @pulumi.getter(name="conversationLogSettings")
    def conversation_log_settings(self) -> Optional['outputs.BotAliasConversationLogSettings']:
        return pulumi.get(self, "conversation_log_settings")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="sentimentAnalysisSettings")
    def sentiment_analysis_settings(self) -> Optional['outputs.SentimentAnalysisSettingsProperties']:
        """
        Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.
        """
        return pulumi.get(self, "sentiment_analysis_settings")


class AwaitableGetBotAliasResult(GetBotAliasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBotAliasResult(
            arn=self.arn,
            bot_alias_id=self.bot_alias_id,
            bot_alias_locale_settings=self.bot_alias_locale_settings,
            bot_alias_name=self.bot_alias_name,
            bot_alias_status=self.bot_alias_status,
            bot_version=self.bot_version,
            conversation_log_settings=self.conversation_log_settings,
            description=self.description,
            sentiment_analysis_settings=self.sentiment_analysis_settings)


def get_bot_alias(bot_alias_id: Optional[str] = None,
                  bot_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBotAliasResult:
    """
    A Bot Alias enables you to change the version of a bot without updating applications that use the bot
    """
    __args__ = dict()
    __args__['botAliasId'] = bot_alias_id
    __args__['botId'] = bot_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:lex:getBotAlias', __args__, opts=opts, typ=GetBotAliasResult).value

    return AwaitableGetBotAliasResult(
        arn=__ret__.arn,
        bot_alias_id=__ret__.bot_alias_id,
        bot_alias_locale_settings=__ret__.bot_alias_locale_settings,
        bot_alias_name=__ret__.bot_alias_name,
        bot_alias_status=__ret__.bot_alias_status,
        bot_version=__ret__.bot_version,
        conversation_log_settings=__ret__.conversation_log_settings,
        description=__ret__.description,
        sentiment_analysis_settings=__ret__.sentiment_analysis_settings)


@_utilities.lift_output_func(get_bot_alias)
def get_bot_alias_output(bot_alias_id: Optional[pulumi.Input[str]] = None,
                         bot_id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBotAliasResult]:
    """
    A Bot Alias enables you to change the version of a bot without updating applications that use the bot
    """
    ...
