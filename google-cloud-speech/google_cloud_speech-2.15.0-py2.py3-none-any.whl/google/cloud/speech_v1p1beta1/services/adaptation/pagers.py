# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Sequence,
    Tuple,
    Optional,
    Iterator,
)

from google.cloud.speech_v1p1beta1.types import cloud_speech_adaptation
from google.cloud.speech_v1p1beta1.types import resource


class ListPhraseSetPager:
    """A pager for iterating through ``list_phrase_set`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.speech_v1p1beta1.types.ListPhraseSetResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``phrase_sets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPhraseSet`` requests and continue to iterate
    through the ``phrase_sets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.speech_v1p1beta1.types.ListPhraseSetResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_speech_adaptation.ListPhraseSetResponse],
        request: cloud_speech_adaptation.ListPhraseSetRequest,
        response: cloud_speech_adaptation.ListPhraseSetResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.speech_v1p1beta1.types.ListPhraseSetRequest):
                The initial request object.
            response (google.cloud.speech_v1p1beta1.types.ListPhraseSetResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_speech_adaptation.ListPhraseSetRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_speech_adaptation.ListPhraseSetResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[resource.PhraseSet]:
        for page in self.pages:
            yield from page.phrase_sets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPhraseSetAsyncPager:
    """A pager for iterating through ``list_phrase_set`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.speech_v1p1beta1.types.ListPhraseSetResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``phrase_sets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPhraseSet`` requests and continue to iterate
    through the ``phrase_sets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.speech_v1p1beta1.types.ListPhraseSetResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_speech_adaptation.ListPhraseSetResponse]],
        request: cloud_speech_adaptation.ListPhraseSetRequest,
        response: cloud_speech_adaptation.ListPhraseSetResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.speech_v1p1beta1.types.ListPhraseSetRequest):
                The initial request object.
            response (google.cloud.speech_v1p1beta1.types.ListPhraseSetResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_speech_adaptation.ListPhraseSetRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[cloud_speech_adaptation.ListPhraseSetResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[resource.PhraseSet]:
        async def async_generator():
            async for page in self.pages:
                for response in page.phrase_sets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCustomClassesPager:
    """A pager for iterating through ``list_custom_classes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.speech_v1p1beta1.types.ListCustomClassesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``custom_classes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCustomClasses`` requests and continue to iterate
    through the ``custom_classes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.speech_v1p1beta1.types.ListCustomClassesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_speech_adaptation.ListCustomClassesResponse],
        request: cloud_speech_adaptation.ListCustomClassesRequest,
        response: cloud_speech_adaptation.ListCustomClassesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.speech_v1p1beta1.types.ListCustomClassesRequest):
                The initial request object.
            response (google.cloud.speech_v1p1beta1.types.ListCustomClassesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_speech_adaptation.ListCustomClassesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_speech_adaptation.ListCustomClassesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[resource.CustomClass]:
        for page in self.pages:
            yield from page.custom_classes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCustomClassesAsyncPager:
    """A pager for iterating through ``list_custom_classes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.speech_v1p1beta1.types.ListCustomClassesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``custom_classes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCustomClasses`` requests and continue to iterate
    through the ``custom_classes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.speech_v1p1beta1.types.ListCustomClassesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[cloud_speech_adaptation.ListCustomClassesResponse]
        ],
        request: cloud_speech_adaptation.ListCustomClassesRequest,
        response: cloud_speech_adaptation.ListCustomClassesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.speech_v1p1beta1.types.ListCustomClassesRequest):
                The initial request object.
            response (google.cloud.speech_v1p1beta1.types.ListCustomClassesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_speech_adaptation.ListCustomClassesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[cloud_speech_adaptation.ListCustomClassesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[resource.CustomClass]:
        async def async_generator():
            async for page in self.pages:
                for response in page.custom_classes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
