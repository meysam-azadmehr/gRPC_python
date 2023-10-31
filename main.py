import grpc
from concurrent import futures
import your_proto_pb2
import your_proto_pb2_grpc

class YourServicer(your_proto_pb2_grpc.YourServiceServicer):
    def GetData(self, request, context):
        data = "Hello, World!"
        return your_proto_pb2.DataResponse(data=data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    your_proto_pb2_grpc.add_YourServiceServicer_to_server(YourServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()