# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: onos/e2t/e2/v1beta1/e2.proto, onos/e2t/e2/v1beta1/control.proto, onos/e2t/e2/v1beta1/subscription.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import AsyncIterator, List, Optional

import betterproto
import grpclib


class Encoding(betterproto.Enum):
    PROTO = 0
    ASN1_PER = 1
    ASN1_XER = 2


class ErrorCauseMiscType(betterproto.Enum):
    UNSPECIFIED = 0
    CONTROL_PROCESSING_OVERLOAD = 1
    HARDWARE_FAILURE = 2
    OM_INTERVENTION = 3


class ErrorCauseProtocolType(betterproto.Enum):
    UNSPECIFIED = 0
    TRANSFER_SYNTAX_ERROR = 1
    ABSTRACT_SYNTAX_ERROR_REJECT = 2
    ABSTRACT_SYNTAX_ERROR_IGNORE_AND_NOTIFY = 3
    MESSAGE_NOT_COMPATIBLE_WITH_RECEIVER_STATE = 4
    SEMANTIC_ERROR = 5
    ABSTRACT_SYNTAX_ERROR_FALSELY_CONSTRUCTED_MESSAGE = 6


class ErrorCauseRicType(betterproto.Enum):
    UNSPECIFIED = 0
    RAN_FUNCTION_ID_INVALID = 1
    ACTION_NOT_SUPPORTED = 2
    EXCESSIVE_ACTIONS = 3
    DUPLICATE_ACTION = 4
    DUPLICATE_EVENT = 5
    FUNCTION_RESOURCE_LIMIT = 6
    REQUEST_ID_UNKNOWN = 7
    INCONSISTENT_ACTION_SUBSEQUENT_ACTION_SEQUENCE = 8
    CONTROL_MESSAGE_INVALID = 9
    CALL_PROCESS_ID_INVALID = 10
    CONTROL_TIMER_EXPIRED = 11
    CONTROL_FAILED_TO_EXECUTE = 12
    CONTROL_SYSTEM_NOT_READY = 13


class ErrorCauseRicServiceType(betterproto.Enum):
    UNSPECIFIED = 0
    FUNCTION_NOT_REQUIRED = 1
    EXCESSIVE_FUNCTIONS = 2
    RIC_RESOURCE_LIMIT = 3


class ErrorCauseTransportType(betterproto.Enum):
    UNSPECIFIED = 0
    TRANSPORT_RESOURCE_UNAVAILABLE = 1


class ActionType(betterproto.Enum):
    ACTION_TYPE_REPORT = 0
    ACTION_TYPE_INSERT = 1
    ACTION_TYPE_POLICY = 2


class SubsequentActionType(betterproto.Enum):
    SUBSEQUENT_ACTION_TYPE_CONTINUE = 0
    SUBSEQUENT_ACTION_TYPE_WAIT = 1


class TimeToWait(betterproto.Enum):
    TIME_TO_WAIT_ZERO = 0
    TIME_TO_WAIT_W1MS = 1
    TIME_TO_WAIT_W2MS = 2
    TIME_TO_WAIT_W5MS = 3
    TIME_TO_WAIT_W10MS = 4
    TIME_TO_WAIT_W20MS = 5
    TIME_TO_WAIT_W30MS = 6
    TIME_TO_WAIT_W40MS = 7
    TIME_TO_WAIT_W50MS = 8
    TIME_TO_WAIT_W100MS = 9
    TIME_TO_WAIT_W200MS = 10
    TIME_TO_WAIT_W500MS = 11
    TIME_TO_WAIT_W1S = 12
    TIME_TO_WAIT_W2S = 13
    TIME_TO_WAIT_W5S = 14
    TIME_TO_WAIT_W10S = 15
    TIME_TO_WAIT_W20S = 16
    TIME_TO_WAIT_W60S = 17


class ChannelEventType(betterproto.Enum):
    CHANNEL_EVENT_UNKNOWN = 0
    CHANNEL_CREATED = 1
    CHANNEL_UPDATED = 2
    CHANNEL_DELETED = 3
    CHANNEL_REPLAYED = 4


class SubscriptionEventType(betterproto.Enum):
    SUBSCRIPTION_EVENT_UNKNOWN = 0
    SUBSCRIPTION_CREATED = 1
    SUBSCRIPTION_UPDATED = 2
    SUBSCRIPTION_DELETED = 3
    SUBSCRIPTION_REPLAYED = 4


class ChannelPhase(betterproto.Enum):
    CHANNEL_CLOSED = 0
    CHANNEL_OPEN = 1


class ChannelState(betterproto.Enum):
    CHANNEL_PENDING = 0
    CHANNEL_COMPLETE = 1
    CHANNEL_FAILED = 2


class SubscriptionPhase(betterproto.Enum):
    SUBSCRIPTION_CLOSED = 0
    SUBSCRIPTION_OPEN = 1


class SubscriptionState(betterproto.Enum):
    SUBSCRIPTION_PENDING = 0
    SUBSCRIPTION_COMPLETE = 1
    SUBSCRIPTION_FAILED = 2


@dataclass(eq=False, repr=False)
class RequestHeaders(betterproto.Message):
    app_id: str = betterproto.string_field(1)
    app_instance_id: str = betterproto.string_field(2)
    e2_node_id: str = betterproto.string_field(3)
    service_model: "ServiceModel" = betterproto.message_field(4)
    encoding: "Encoding" = betterproto.enum_field(5)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ResponseHeaders(betterproto.Message):
    encoding: "Encoding" = betterproto.enum_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ServiceModel(betterproto.Message):
    name: str = betterproto.string_field(1)
    version: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Error(betterproto.Message):
    """Error is an E2AP protocol error"""

    cause: "ErrorCause" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ErrorCause(betterproto.Message):
    unknown: "ErrorCauseUnknown" = betterproto.message_field(1, group="cause")
    protocol: "ErrorCauseProtocol" = betterproto.message_field(2, group="cause")
    ric: "ErrorCauseRic" = betterproto.message_field(3, group="cause")
    ric_service: "ErrorCauseRicService" = betterproto.message_field(4, group="cause")
    transport: "ErrorCauseTransport" = betterproto.message_field(5, group="cause")
    misc: "ErrorCauseMisc" = betterproto.message_field(6, group="cause")

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ErrorCauseUnknown(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ErrorCauseMisc(betterproto.Message):
    type: "ErrorCauseMiscType" = betterproto.enum_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ErrorCauseProtocol(betterproto.Message):
    type: "ErrorCauseProtocolType" = betterproto.enum_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ErrorCauseRic(betterproto.Message):
    type: "ErrorCauseRicType" = betterproto.enum_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ErrorCauseRicService(betterproto.Message):
    type: "ErrorCauseRicServiceType" = betterproto.enum_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ErrorCauseTransport(betterproto.Message):
    type: "ErrorCauseTransportType" = betterproto.enum_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ControlRequest(betterproto.Message):
    headers: "RequestHeaders" = betterproto.message_field(1)
    message: "ControlMessage" = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ControlMessage(betterproto.Message):
    header: bytes = betterproto.bytes_field(1)
    payload: bytes = betterproto.bytes_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ControlResponse(betterproto.Message):
    headers: "ResponseHeaders" = betterproto.message_field(1)
    outcome: "ControlOutcome" = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ControlOutcome(betterproto.Message):
    """Error is an E2AP protocol error"""

    payload: bytes = betterproto.bytes_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SubscribeRequest(betterproto.Message):
    headers: "RequestHeaders" = betterproto.message_field(1)
    transaction_id: str = betterproto.string_field(2)
    subscription: "SubscriptionSpec" = betterproto.message_field(3)
    transaction_timeout: timedelta = betterproto.message_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SubscribeResponse(betterproto.Message):
    headers: "ResponseHeaders" = betterproto.message_field(1)
    ack: "Acknowledgement" = betterproto.message_field(2, group="message")
    indication: "Indication" = betterproto.message_field(3, group="message")

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class UnsubscribeRequest(betterproto.Message):
    headers: "RequestHeaders" = betterproto.message_field(1)
    transaction_id: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class UnsubscribeResponse(betterproto.Message):
    """Error is an E2AP protocol error"""

    headers: "ResponseHeaders" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SubscriptionSpec(betterproto.Message):
    event_trigger: "EventTrigger" = betterproto.message_field(1)
    actions: List["Action"] = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class EventTrigger(betterproto.Message):
    payload: bytes = betterproto.bytes_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Action(betterproto.Message):
    id: int = betterproto.int32_field(1)
    type: "ActionType" = betterproto.enum_field(2)
    payload: bytes = betterproto.bytes_field(3)
    subsequent_action: "SubsequentAction" = betterproto.message_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SubsequentAction(betterproto.Message):
    type: "SubsequentActionType" = betterproto.enum_field(1)
    time_to_wait: "TimeToWait" = betterproto.enum_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Acknowledgement(betterproto.Message):
    channel_id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Indication(betterproto.Message):
    header: bytes = betterproto.bytes_field(1)
    payload: bytes = betterproto.bytes_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetChannelRequest(betterproto.Message):
    channel_id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetChannelResponse(betterproto.Message):
    channel: "Channel" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListChannelsRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListChannelsResponse(betterproto.Message):
    channels: List["Channel"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class WatchChannelsRequest(betterproto.Message):
    no_replay: bool = betterproto.bool_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class WatchChannelsResponse(betterproto.Message):
    event: "ChannelEvent" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ChannelEvent(betterproto.Message):
    type: "ChannelEventType" = betterproto.enum_field(1)
    channel: "Channel" = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetSubscriptionRequest(betterproto.Message):
    subscription_id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetSubscriptionResponse(betterproto.Message):
    subscription: "Subscription" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListSubscriptionsRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListSubscriptionsResponse(betterproto.Message):
    subscriptions: List["Subscription"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class WatchSubscriptionsRequest(betterproto.Message):
    no_replay: bool = betterproto.bool_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class WatchSubscriptionsResponse(betterproto.Message):
    event: "SubscriptionEvent" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SubscriptionEvent(betterproto.Message):
    type: "SubscriptionEventType" = betterproto.enum_field(1)
    subscription: "Subscription" = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ChannelMeta(betterproto.Message):
    app_id: str = betterproto.string_field(1)
    app_instance_id: str = betterproto.string_field(2)
    e2_node_id: str = betterproto.string_field(3)
    transaction_id: str = betterproto.string_field(4)
    subscription_id: str = betterproto.string_field(5)
    service_model: "ServiceModel" = betterproto.message_field(6)
    encoding: "Encoding" = betterproto.enum_field(7)
    revision: int = betterproto.uint64_field(8)
    finalizers: List[str] = betterproto.string_field(9)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Channel(betterproto.Message):
    id: str = betterproto.string_field(1)
    meta: "ChannelMeta" = betterproto.message_field(2)
    spec: "ChannelSpec" = betterproto.message_field(3)
    status: "ChannelStatus" = betterproto.message_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ChannelSpec(betterproto.Message):
    subscription: "SubscriptionSpec" = betterproto.message_field(1)
    transaction_timeout: timedelta = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ChannelStatus(betterproto.Message):
    phase: "ChannelPhase" = betterproto.enum_field(1)
    state: "ChannelState" = betterproto.enum_field(2)
    error: "Error" = betterproto.message_field(3)
    timestamp: datetime = betterproto.message_field(4)
    term: int = betterproto.uint64_field(5)
    master: str = betterproto.string_field(6)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SubscriptionMeta(betterproto.Message):
    e2_node_id: str = betterproto.string_field(1)
    service_model: "ServiceModel" = betterproto.message_field(2)
    encoding: "Encoding" = betterproto.enum_field(3)
    revision: int = betterproto.uint64_field(4)
    finalizers: List[str] = betterproto.string_field(5)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Subscription(betterproto.Message):
    id: str = betterproto.string_field(1)
    meta: "SubscriptionMeta" = betterproto.message_field(2)
    spec: "SubscriptionSpec" = betterproto.message_field(3)
    status: "SubscriptionStatus" = betterproto.message_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SubscriptionStatus(betterproto.Message):
    phase: "SubscriptionPhase" = betterproto.enum_field(1)
    state: "SubscriptionState" = betterproto.enum_field(2)
    error: "Error" = betterproto.message_field(3)
    channels: List[str] = betterproto.string_field(4)
    term: int = betterproto.uint64_field(5)
    master: str = betterproto.string_field(6)

    def __post_init__(self) -> None:
        super().__post_init__()


class ControlServiceStub(betterproto.ServiceStub):
    async def control(
        self, *, headers: "RequestHeaders" = None, message: "ControlMessage" = None
    ) -> "ControlResponse":

        request = ControlRequest()
        if headers is not None:
            request.headers = headers
        if message is not None:
            request.message = message

        return await self._unary_unary(
            "/onos.e2t.e2.v1beta1.ControlService/Control", request, ControlResponse
        )


class SubscriptionServiceStub(betterproto.ServiceStub):
    async def subscribe(
        self,
        *,
        headers: "RequestHeaders" = None,
        transaction_id: str = "",
        subscription: "SubscriptionSpec" = None,
        transaction_timeout: timedelta = None,
    ) -> AsyncIterator["SubscribeResponse"]:

        request = SubscribeRequest()
        if headers is not None:
            request.headers = headers
        request.transaction_id = transaction_id
        if subscription is not None:
            request.subscription = subscription
        if transaction_timeout is not None:
            request.transaction_timeout = transaction_timeout

        async for response in self._unary_stream(
            "/onos.e2t.e2.v1beta1.SubscriptionService/Subscribe",
            request,
            SubscribeResponse,
        ):
            yield response

    async def unsubscribe(
        self, *, headers: "RequestHeaders" = None, transaction_id: str = ""
    ) -> "UnsubscribeResponse":

        request = UnsubscribeRequest()
        if headers is not None:
            request.headers = headers
        request.transaction_id = transaction_id

        return await self._unary_unary(
            "/onos.e2t.e2.v1beta1.SubscriptionService/Unsubscribe",
            request,
            UnsubscribeResponse,
        )


class SubscriptionAdminServiceStub(betterproto.ServiceStub):
    async def get_channel(self, *, channel_id: str = "") -> "GetChannelResponse":

        request = GetChannelRequest()
        request.channel_id = channel_id

        return await self._unary_unary(
            "/onos.e2t.e2.v1beta1.SubscriptionAdminService/GetChannel",
            request,
            GetChannelResponse,
        )

    async def list_channels(self) -> "ListChannelsResponse":

        request = ListChannelsRequest()

        return await self._unary_unary(
            "/onos.e2t.e2.v1beta1.SubscriptionAdminService/ListChannels",
            request,
            ListChannelsResponse,
        )

    async def watch_channels(
        self, *, no_replay: bool = False
    ) -> AsyncIterator["WatchChannelsResponse"]:

        request = WatchChannelsRequest()
        request.no_replay = no_replay

        async for response in self._unary_stream(
            "/onos.e2t.e2.v1beta1.SubscriptionAdminService/WatchChannels",
            request,
            WatchChannelsResponse,
        ):
            yield response

    async def get_subscription(
        self, *, subscription_id: str = ""
    ) -> "GetSubscriptionResponse":

        request = GetSubscriptionRequest()
        request.subscription_id = subscription_id

        return await self._unary_unary(
            "/onos.e2t.e2.v1beta1.SubscriptionAdminService/GetSubscription",
            request,
            GetSubscriptionResponse,
        )

    async def list_subscriptions(self) -> "ListSubscriptionsResponse":

        request = ListSubscriptionsRequest()

        return await self._unary_unary(
            "/onos.e2t.e2.v1beta1.SubscriptionAdminService/ListSubscriptions",
            request,
            ListSubscriptionsResponse,
        )

    async def watch_subscriptions(
        self, *, no_replay: bool = False
    ) -> AsyncIterator["WatchSubscriptionsResponse"]:

        request = WatchSubscriptionsRequest()
        request.no_replay = no_replay

        async for response in self._unary_stream(
            "/onos.e2t.e2.v1beta1.SubscriptionAdminService/WatchSubscriptions",
            request,
            WatchSubscriptionsResponse,
        ):
            yield response
