
from concurrent import futures
import grpc


import helloworld_pb2_grpc as hi_pb_grpc
import helloworld_pb2 as hi_pb

class Helloworld(hi_pb_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hi_pb.HelloResponse(message='Hi %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hi_pb_grpc.add_GreeterServicer_to_server(Helloworld(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()