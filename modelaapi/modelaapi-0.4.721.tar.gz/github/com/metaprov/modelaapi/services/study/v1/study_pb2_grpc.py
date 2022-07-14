# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from github.com.metaprov.modelaapi.services.study.v1 import study_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2


class StudyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListStudies = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.study.v1.StudyService/ListStudies',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.ListStudyRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.ListStudyResponse.FromString,
                )
        self.CreateStudy = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.study.v1.StudyService/CreateStudy',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CreateStudyRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CreateStudyResponse.FromString,
                )
        self.GetStudy = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.study.v1.StudyService/GetStudy',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.GetStudyRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.GetStudyResponse.FromString,
                )
        self.UpdateStudy = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.study.v1.StudyService/UpdateStudy',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.UpdateStudyRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.UpdateStudyResponse.FromString,
                )
        self.DeleteStudy = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.study.v1.StudyService/DeleteStudy',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.DeleteStudyRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.DeleteStudyResponse.FromString,
                )
        self.CreateStudyProfile = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.study.v1.StudyService/CreateStudyProfile',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CreateStudyProfileRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CreateStudyProfileResponse.FromString,
                )
        self.GetStudyProfile = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.study.v1.StudyService/GetStudyProfile',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.GetStudyProfileRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.GetStudyProfileResponse.FromString,
                )
        self.AbortStudy = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.study.v1.StudyService/AbortStudy',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.AbortStudyRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.AbortStudyResponse.FromString,
                )
        self.PauseStudy = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.study.v1.StudyService/PauseStudy',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.PauseStudyRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.PauseStudyResponse.FromString,
                )
        self.ResumeStudy = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.study.v1.StudyService/ResumeStudy',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.ResumeStudyRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.ResumeStudyResponse.FromString,
                )
        self.CompleteSearch = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.study.v1.StudyService/CompleteSearch',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CompleteSearchRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CompleteSearchResponse.FromString,
                )


class StudyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListStudies(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateStudy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStudy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateStudy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteStudy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateStudyProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStudyProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AbortStudy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PauseStudy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResumeStudy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteSearch(self, request, context):
        """Force completion of the search.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StudyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListStudies': grpc.unary_unary_rpc_method_handler(
                    servicer.ListStudies,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.ListStudyRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.ListStudyResponse.SerializeToString,
            ),
            'CreateStudy': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateStudy,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CreateStudyRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CreateStudyResponse.SerializeToString,
            ),
            'GetStudy': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStudy,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.GetStudyRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.GetStudyResponse.SerializeToString,
            ),
            'UpdateStudy': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateStudy,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.UpdateStudyRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.UpdateStudyResponse.SerializeToString,
            ),
            'DeleteStudy': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteStudy,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.DeleteStudyRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.DeleteStudyResponse.SerializeToString,
            ),
            'CreateStudyProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateStudyProfile,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CreateStudyProfileRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CreateStudyProfileResponse.SerializeToString,
            ),
            'GetStudyProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStudyProfile,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.GetStudyProfileRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.GetStudyProfileResponse.SerializeToString,
            ),
            'AbortStudy': grpc.unary_unary_rpc_method_handler(
                    servicer.AbortStudy,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.AbortStudyRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.AbortStudyResponse.SerializeToString,
            ),
            'PauseStudy': grpc.unary_unary_rpc_method_handler(
                    servicer.PauseStudy,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.PauseStudyRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.PauseStudyResponse.SerializeToString,
            ),
            'ResumeStudy': grpc.unary_unary_rpc_method_handler(
                    servicer.ResumeStudy,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.ResumeStudyRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.ResumeStudyResponse.SerializeToString,
            ),
            'CompleteSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.CompleteSearch,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CompleteSearchRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CompleteSearchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'github.com.metaprov.modelaapi.services.study.v1.StudyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StudyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListStudies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.study.v1.StudyService/ListStudies',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.ListStudyRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.ListStudyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateStudy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.study.v1.StudyService/CreateStudy',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CreateStudyRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CreateStudyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStudy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.study.v1.StudyService/GetStudy',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.GetStudyRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.GetStudyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateStudy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.study.v1.StudyService/UpdateStudy',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.UpdateStudyRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.UpdateStudyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteStudy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.study.v1.StudyService/DeleteStudy',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.DeleteStudyRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.DeleteStudyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateStudyProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.study.v1.StudyService/CreateStudyProfile',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CreateStudyProfileRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CreateStudyProfileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStudyProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.study.v1.StudyService/GetStudyProfile',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.GetStudyProfileRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.GetStudyProfileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AbortStudy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.study.v1.StudyService/AbortStudy',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.AbortStudyRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.AbortStudyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PauseStudy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.study.v1.StudyService/PauseStudy',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.PauseStudyRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.PauseStudyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResumeStudy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.study.v1.StudyService/ResumeStudy',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.ResumeStudyRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.ResumeStudyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CompleteSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.study.v1.StudyService/CompleteSearch',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CompleteSearchRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_study_dot_v1_dot_study__pb2.CompleteSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
