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
    'GetConversationModelResult',
    'AwaitableGetConversationModelResult',
    'get_conversation_model',
    'get_conversation_model_output',
]

@pulumi.output_type
class GetConversationModelResult:
    def __init__(__self__, article_suggestion_model_metadata=None, create_time=None, datasets=None, display_name=None, language_code=None, name=None, smart_reply_model_metadata=None, state=None):
        if article_suggestion_model_metadata and not isinstance(article_suggestion_model_metadata, dict):
            raise TypeError("Expected argument 'article_suggestion_model_metadata' to be a dict")
        pulumi.set(__self__, "article_suggestion_model_metadata", article_suggestion_model_metadata)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if datasets and not isinstance(datasets, list):
            raise TypeError("Expected argument 'datasets' to be a list")
        pulumi.set(__self__, "datasets", datasets)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if language_code and not isinstance(language_code, str):
            raise TypeError("Expected argument 'language_code' to be a str")
        pulumi.set(__self__, "language_code", language_code)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if smart_reply_model_metadata and not isinstance(smart_reply_model_metadata, dict):
            raise TypeError("Expected argument 'smart_reply_model_metadata' to be a dict")
        pulumi.set(__self__, "smart_reply_model_metadata", smart_reply_model_metadata)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="articleSuggestionModelMetadata")
    def article_suggestion_model_metadata(self) -> 'outputs.GoogleCloudDialogflowV2ArticleSuggestionModelMetadataResponse':
        """
        Metadata for article suggestion models.
        """
        return pulumi.get(self, "article_suggestion_model_metadata")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Creation time of this model.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def datasets(self) -> Sequence['outputs.GoogleCloudDialogflowV2InputDatasetResponse']:
        """
        Datasets used to create model.
        """
        return pulumi.get(self, "datasets")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the model. At most 64 bytes long.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> str:
        """
        Language code for the conversation model. If not specified, the language is en-US. Language at ConversationModel should be set for all non en-us languages. This should be a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US".
        """
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        ConversationModel resource name. Format: `projects//conversationModels/`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="smartReplyModelMetadata")
    def smart_reply_model_metadata(self) -> 'outputs.GoogleCloudDialogflowV2SmartReplyModelMetadataResponse':
        """
        Metadata for smart reply models.
        """
        return pulumi.get(self, "smart_reply_model_metadata")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of the model. A model can only serve prediction requests after it gets deployed.
        """
        return pulumi.get(self, "state")


class AwaitableGetConversationModelResult(GetConversationModelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConversationModelResult(
            article_suggestion_model_metadata=self.article_suggestion_model_metadata,
            create_time=self.create_time,
            datasets=self.datasets,
            display_name=self.display_name,
            language_code=self.language_code,
            name=self.name,
            smart_reply_model_metadata=self.smart_reply_model_metadata,
            state=self.state)


def get_conversation_model(conversation_model_id: Optional[str] = None,
                           location: Optional[str] = None,
                           project: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConversationModelResult:
    """
    Gets conversation model.
    """
    __args__ = dict()
    __args__['conversationModelId'] = conversation_model_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:dialogflow/v2:getConversationModel', __args__, opts=opts, typ=GetConversationModelResult).value

    return AwaitableGetConversationModelResult(
        article_suggestion_model_metadata=__ret__.article_suggestion_model_metadata,
        create_time=__ret__.create_time,
        datasets=__ret__.datasets,
        display_name=__ret__.display_name,
        language_code=__ret__.language_code,
        name=__ret__.name,
        smart_reply_model_metadata=__ret__.smart_reply_model_metadata,
        state=__ret__.state)


@_utilities.lift_output_func(get_conversation_model)
def get_conversation_model_output(conversation_model_id: Optional[pulumi.Input[str]] = None,
                                  location: Optional[pulumi.Input[str]] = None,
                                  project: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConversationModelResult]:
    """
    Gets conversation model.
    """
    ...
