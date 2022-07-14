# @generated

# This file was generated by running `python -m dagster.grpc.compile`
# Do not edit this file directly, and do not attempt to recompile it using
# grpc_tools.protoc directly, as several changes must be made to the raw output

# pylint: disable=no-member, unused-argument

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import api_pb2 as api__pb2


class DagsterApiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
            "/api.DagsterApi/Ping",
            request_serializer=api__pb2.PingRequest.SerializeToString,
            response_deserializer=api__pb2.PingReply.FromString,
        )
        self.Heartbeat = channel.unary_unary(
            "/api.DagsterApi/Heartbeat",
            request_serializer=api__pb2.PingRequest.SerializeToString,
            response_deserializer=api__pb2.PingReply.FromString,
        )
        self.StreamingPing = channel.unary_stream(
            "/api.DagsterApi/StreamingPing",
            request_serializer=api__pb2.StreamingPingRequest.SerializeToString,
            response_deserializer=api__pb2.StreamingPingEvent.FromString,
        )
        self.GetServerId = channel.unary_unary(
            "/api.DagsterApi/GetServerId",
            request_serializer=api__pb2.Empty.SerializeToString,
            response_deserializer=api__pb2.GetServerIdReply.FromString,
        )
        self.ExecutionPlanSnapshot = channel.unary_unary(
            "/api.DagsterApi/ExecutionPlanSnapshot",
            request_serializer=api__pb2.ExecutionPlanSnapshotRequest.SerializeToString,
            response_deserializer=api__pb2.ExecutionPlanSnapshotReply.FromString,
        )
        self.ListRepositories = channel.unary_unary(
            "/api.DagsterApi/ListRepositories",
            request_serializer=api__pb2.ListRepositoriesRequest.SerializeToString,
            response_deserializer=api__pb2.ListRepositoriesReply.FromString,
        )
        self.ExternalPartitionNames = channel.unary_unary(
            "/api.DagsterApi/ExternalPartitionNames",
            request_serializer=api__pb2.ExternalPartitionNamesRequest.SerializeToString,
            response_deserializer=api__pb2.ExternalPartitionNamesReply.FromString,
        )
        self.ExternalNotebookData = channel.unary_unary(
            "/api.DagsterApi/ExternalNotebookData",
            request_serializer=api__pb2.ExternalNotebookDataRequest.SerializeToString,
            response_deserializer=api__pb2.ExternalNotebookDataReply.FromString,
        )
        self.ExternalPartitionConfig = channel.unary_unary(
            "/api.DagsterApi/ExternalPartitionConfig",
            request_serializer=api__pb2.ExternalPartitionConfigRequest.SerializeToString,
            response_deserializer=api__pb2.ExternalPartitionConfigReply.FromString,
        )
        self.ExternalPartitionTags = channel.unary_unary(
            "/api.DagsterApi/ExternalPartitionTags",
            request_serializer=api__pb2.ExternalPartitionTagsRequest.SerializeToString,
            response_deserializer=api__pb2.ExternalPartitionTagsReply.FromString,
        )
        self.ExternalPartitionSetExecutionParams = channel.unary_stream(
            "/api.DagsterApi/ExternalPartitionSetExecutionParams",
            request_serializer=api__pb2.ExternalPartitionSetExecutionParamsRequest.SerializeToString,
            response_deserializer=api__pb2.StreamingChunkEvent.FromString,
        )
        self.ExternalPipelineSubsetSnapshot = channel.unary_unary(
            "/api.DagsterApi/ExternalPipelineSubsetSnapshot",
            request_serializer=api__pb2.ExternalPipelineSubsetSnapshotRequest.SerializeToString,
            response_deserializer=api__pb2.ExternalPipelineSubsetSnapshotReply.FromString,
        )
        self.ExternalRepository = channel.unary_unary(
            "/api.DagsterApi/ExternalRepository",
            request_serializer=api__pb2.ExternalRepositoryRequest.SerializeToString,
            response_deserializer=api__pb2.ExternalRepositoryReply.FromString,
        )
        self.StreamingExternalRepository = channel.unary_stream(
            "/api.DagsterApi/StreamingExternalRepository",
            request_serializer=api__pb2.ExternalRepositoryRequest.SerializeToString,
            response_deserializer=api__pb2.StreamingExternalRepositoryEvent.FromString,
        )
        self.ExternalScheduleExecution = channel.unary_stream(
            "/api.DagsterApi/ExternalScheduleExecution",
            request_serializer=api__pb2.ExternalScheduleExecutionRequest.SerializeToString,
            response_deserializer=api__pb2.StreamingChunkEvent.FromString,
        )
        self.ExternalSensorExecution = channel.unary_stream(
            "/api.DagsterApi/ExternalSensorExecution",
            request_serializer=api__pb2.ExternalSensorExecutionRequest.SerializeToString,
            response_deserializer=api__pb2.StreamingChunkEvent.FromString,
        )
        self.ShutdownServer = channel.unary_unary(
            "/api.DagsterApi/ShutdownServer",
            request_serializer=api__pb2.Empty.SerializeToString,
            response_deserializer=api__pb2.ShutdownServerReply.FromString,
        )
        self.CancelExecution = channel.unary_unary(
            "/api.DagsterApi/CancelExecution",
            request_serializer=api__pb2.CancelExecutionRequest.SerializeToString,
            response_deserializer=api__pb2.CancelExecutionReply.FromString,
        )
        self.CanCancelExecution = channel.unary_unary(
            "/api.DagsterApi/CanCancelExecution",
            request_serializer=api__pb2.CanCancelExecutionRequest.SerializeToString,
            response_deserializer=api__pb2.CanCancelExecutionReply.FromString,
        )
        self.StartRun = channel.unary_unary(
            "/api.DagsterApi/StartRun",
            request_serializer=api__pb2.StartRunRequest.SerializeToString,
            response_deserializer=api__pb2.StartRunReply.FromString,
        )
        self.GetCurrentImage = channel.unary_unary(
            "/api.DagsterApi/GetCurrentImage",
            request_serializer=api__pb2.Empty.SerializeToString,
            response_deserializer=api__pb2.GetCurrentImageReply.FromString,
        )


class DagsterApiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Heartbeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StreamingPing(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetServerId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExecutionPlanSnapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListRepositories(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExternalPartitionNames(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExternalNotebookData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExternalPartitionConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExternalPartitionTags(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExternalPartitionSetExecutionParams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExternalPipelineSubsetSnapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExternalRepository(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StreamingExternalRepository(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExternalScheduleExecution(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExternalSensorExecution(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ShutdownServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CancelExecution(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CanCancelExecution(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StartRun(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetCurrentImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DagsterApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Ping": grpc.unary_unary_rpc_method_handler(
            servicer.Ping,
            request_deserializer=api__pb2.PingRequest.FromString,
            response_serializer=api__pb2.PingReply.SerializeToString,
        ),
        "Heartbeat": grpc.unary_unary_rpc_method_handler(
            servicer.Heartbeat,
            request_deserializer=api__pb2.PingRequest.FromString,
            response_serializer=api__pb2.PingReply.SerializeToString,
        ),
        "StreamingPing": grpc.unary_stream_rpc_method_handler(
            servicer.StreamingPing,
            request_deserializer=api__pb2.StreamingPingRequest.FromString,
            response_serializer=api__pb2.StreamingPingEvent.SerializeToString,
        ),
        "GetServerId": grpc.unary_unary_rpc_method_handler(
            servicer.GetServerId,
            request_deserializer=api__pb2.Empty.FromString,
            response_serializer=api__pb2.GetServerIdReply.SerializeToString,
        ),
        "ExecutionPlanSnapshot": grpc.unary_unary_rpc_method_handler(
            servicer.ExecutionPlanSnapshot,
            request_deserializer=api__pb2.ExecutionPlanSnapshotRequest.FromString,
            response_serializer=api__pb2.ExecutionPlanSnapshotReply.SerializeToString,
        ),
        "ListRepositories": grpc.unary_unary_rpc_method_handler(
            servicer.ListRepositories,
            request_deserializer=api__pb2.ListRepositoriesRequest.FromString,
            response_serializer=api__pb2.ListRepositoriesReply.SerializeToString,
        ),
        "ExternalPartitionNames": grpc.unary_unary_rpc_method_handler(
            servicer.ExternalPartitionNames,
            request_deserializer=api__pb2.ExternalPartitionNamesRequest.FromString,
            response_serializer=api__pb2.ExternalPartitionNamesReply.SerializeToString,
        ),
        "ExternalNotebookData": grpc.unary_unary_rpc_method_handler(
            servicer.ExternalNotebookData,
            request_deserializer=api__pb2.ExternalNotebookDataRequest.FromString,
            response_serializer=api__pb2.ExternalNotebookDataReply.SerializeToString,
        ),
        "ExternalPartitionConfig": grpc.unary_unary_rpc_method_handler(
            servicer.ExternalPartitionConfig,
            request_deserializer=api__pb2.ExternalPartitionConfigRequest.FromString,
            response_serializer=api__pb2.ExternalPartitionConfigReply.SerializeToString,
        ),
        "ExternalPartitionTags": grpc.unary_unary_rpc_method_handler(
            servicer.ExternalPartitionTags,
            request_deserializer=api__pb2.ExternalPartitionTagsRequest.FromString,
            response_serializer=api__pb2.ExternalPartitionTagsReply.SerializeToString,
        ),
        "ExternalPartitionSetExecutionParams": grpc.unary_stream_rpc_method_handler(
            servicer.ExternalPartitionSetExecutionParams,
            request_deserializer=api__pb2.ExternalPartitionSetExecutionParamsRequest.FromString,
            response_serializer=api__pb2.StreamingChunkEvent.SerializeToString,
        ),
        "ExternalPipelineSubsetSnapshot": grpc.unary_unary_rpc_method_handler(
            servicer.ExternalPipelineSubsetSnapshot,
            request_deserializer=api__pb2.ExternalPipelineSubsetSnapshotRequest.FromString,
            response_serializer=api__pb2.ExternalPipelineSubsetSnapshotReply.SerializeToString,
        ),
        "ExternalRepository": grpc.unary_unary_rpc_method_handler(
            servicer.ExternalRepository,
            request_deserializer=api__pb2.ExternalRepositoryRequest.FromString,
            response_serializer=api__pb2.ExternalRepositoryReply.SerializeToString,
        ),
        "StreamingExternalRepository": grpc.unary_stream_rpc_method_handler(
            servicer.StreamingExternalRepository,
            request_deserializer=api__pb2.ExternalRepositoryRequest.FromString,
            response_serializer=api__pb2.StreamingExternalRepositoryEvent.SerializeToString,
        ),
        "ExternalScheduleExecution": grpc.unary_stream_rpc_method_handler(
            servicer.ExternalScheduleExecution,
            request_deserializer=api__pb2.ExternalScheduleExecutionRequest.FromString,
            response_serializer=api__pb2.StreamingChunkEvent.SerializeToString,
        ),
        "ExternalSensorExecution": grpc.unary_stream_rpc_method_handler(
            servicer.ExternalSensorExecution,
            request_deserializer=api__pb2.ExternalSensorExecutionRequest.FromString,
            response_serializer=api__pb2.StreamingChunkEvent.SerializeToString,
        ),
        "ShutdownServer": grpc.unary_unary_rpc_method_handler(
            servicer.ShutdownServer,
            request_deserializer=api__pb2.Empty.FromString,
            response_serializer=api__pb2.ShutdownServerReply.SerializeToString,
        ),
        "CancelExecution": grpc.unary_unary_rpc_method_handler(
            servicer.CancelExecution,
            request_deserializer=api__pb2.CancelExecutionRequest.FromString,
            response_serializer=api__pb2.CancelExecutionReply.SerializeToString,
        ),
        "CanCancelExecution": grpc.unary_unary_rpc_method_handler(
            servicer.CanCancelExecution,
            request_deserializer=api__pb2.CanCancelExecutionRequest.FromString,
            response_serializer=api__pb2.CanCancelExecutionReply.SerializeToString,
        ),
        "StartRun": grpc.unary_unary_rpc_method_handler(
            servicer.StartRun,
            request_deserializer=api__pb2.StartRunRequest.FromString,
            response_serializer=api__pb2.StartRunReply.SerializeToString,
        ),
        "GetCurrentImage": grpc.unary_unary_rpc_method_handler(
            servicer.GetCurrentImage,
            request_deserializer=api__pb2.Empty.FromString,
            response_serializer=api__pb2.GetCurrentImageReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("api.DagsterApi", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class DagsterApi(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/Ping",
            api__pb2.PingRequest.SerializeToString,
            api__pb2.PingReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Heartbeat(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/Heartbeat",
            api__pb2.PingRequest.SerializeToString,
            api__pb2.PingReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def StreamingPing(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/api.DagsterApi/StreamingPing",
            api__pb2.StreamingPingRequest.SerializeToString,
            api__pb2.StreamingPingEvent.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetServerId(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/GetServerId",
            api__pb2.Empty.SerializeToString,
            api__pb2.GetServerIdReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ExecutionPlanSnapshot(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/ExecutionPlanSnapshot",
            api__pb2.ExecutionPlanSnapshotRequest.SerializeToString,
            api__pb2.ExecutionPlanSnapshotReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListRepositories(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/ListRepositories",
            api__pb2.ListRepositoriesRequest.SerializeToString,
            api__pb2.ListRepositoriesReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ExternalPartitionNames(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/ExternalPartitionNames",
            api__pb2.ExternalPartitionNamesRequest.SerializeToString,
            api__pb2.ExternalPartitionNamesReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ExternalNotebookData(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/ExternalNotebookData",
            api__pb2.ExternalNotebookDataRequest.SerializeToString,
            api__pb2.ExternalNotebookDataReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ExternalPartitionConfig(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/ExternalPartitionConfig",
            api__pb2.ExternalPartitionConfigRequest.SerializeToString,
            api__pb2.ExternalPartitionConfigReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ExternalPartitionTags(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/ExternalPartitionTags",
            api__pb2.ExternalPartitionTagsRequest.SerializeToString,
            api__pb2.ExternalPartitionTagsReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ExternalPartitionSetExecutionParams(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/api.DagsterApi/ExternalPartitionSetExecutionParams",
            api__pb2.ExternalPartitionSetExecutionParamsRequest.SerializeToString,
            api__pb2.StreamingChunkEvent.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ExternalPipelineSubsetSnapshot(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/ExternalPipelineSubsetSnapshot",
            api__pb2.ExternalPipelineSubsetSnapshotRequest.SerializeToString,
            api__pb2.ExternalPipelineSubsetSnapshotReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ExternalRepository(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/ExternalRepository",
            api__pb2.ExternalRepositoryRequest.SerializeToString,
            api__pb2.ExternalRepositoryReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def StreamingExternalRepository(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/api.DagsterApi/StreamingExternalRepository",
            api__pb2.ExternalRepositoryRequest.SerializeToString,
            api__pb2.StreamingExternalRepositoryEvent.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ExternalScheduleExecution(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/api.DagsterApi/ExternalScheduleExecution",
            api__pb2.ExternalScheduleExecutionRequest.SerializeToString,
            api__pb2.StreamingChunkEvent.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ExternalSensorExecution(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/api.DagsterApi/ExternalSensorExecution",
            api__pb2.ExternalSensorExecutionRequest.SerializeToString,
            api__pb2.StreamingChunkEvent.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ShutdownServer(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/ShutdownServer",
            api__pb2.Empty.SerializeToString,
            api__pb2.ShutdownServerReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CancelExecution(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/CancelExecution",
            api__pb2.CancelExecutionRequest.SerializeToString,
            api__pb2.CancelExecutionReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CanCancelExecution(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/CanCancelExecution",
            api__pb2.CanCancelExecutionRequest.SerializeToString,
            api__pb2.CanCancelExecutionReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def StartRun(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/StartRun",
            api__pb2.StartRunRequest.SerializeToString,
            api__pb2.StartRunReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetCurrentImage(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/api.DagsterApi/GetCurrentImage",
            api__pb2.Empty.SerializeToString,
            api__pb2.GetCurrentImageReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
