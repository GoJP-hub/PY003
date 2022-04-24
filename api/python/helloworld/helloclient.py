
from unicodedata import name
from urllib import response
import grpc
import helloworld_pb2_grpc as hi_pb_grpc
import helloworld_pb2 as hi_pb

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hi_pb_grpc.GreeterStub(channel)
        response = stub.SayHello(hi_pb.HelloRequest(name="James"))
        print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()
