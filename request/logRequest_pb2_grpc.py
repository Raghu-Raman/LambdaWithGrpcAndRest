# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from request import logRequest_pb2 as request_dot_logRequest__pb2


class logRequestStub(object):
    """Define the service that the server provides to the client
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.logMessageFind = channel.unary_unary(
                '/request.logRequest/logMessageFind',
                request_serializer=request_dot_logRequest__pb2.requestCall.SerializeToString,
                response_deserializer=request_dot_logRequest__pb2.response.FromString,
                )


class logRequestServicer(object):
    """Define the service that the server provides to the client
    """

    def logMessageFind(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_logRequestServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'logMessageFind': grpc.unary_unary_rpc_method_handler(
                    servicer.logMessageFind,
                    request_deserializer=request_dot_logRequest__pb2.requestCall.FromString,
                    response_serializer=request_dot_logRequest__pb2.response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'request.logRequest', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class logRequest(object):
    """Define the service that the server provides to the client
    """

    @staticmethod
    def logMessageFind(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/request.logRequest/logMessageFind',
            request_dot_logRequest__pb2.requestCall.SerializeToString,
            request_dot_logRequest__pb2.response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
