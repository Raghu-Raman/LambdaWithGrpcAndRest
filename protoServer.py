from concurrent import futures
from configparser import ConfigParser
import requests
import grpc
import request.logRequest_pb2 as logRequest_pb2
import request.logRequest_pb2_grpc as logRequest_pb2_grpc
import logging

configServer = ConfigParser()
configServer.read("configFileServer.ini")
configData = configServer['Server']
logging.basicConfig(filename="logServer.log", level=logging.INFO)
logging.debug("Debug logging test...")


class logRequest(logRequest_pb2_grpc.logRequestServicer):
    def logMessageFind(self, request, context):
        #
        logging.info(
            "Passed in parameters. Input parameters are" + request.date + " " + request.time + " " + request.delta + " " + request.pattern)
        params = {'date': request.date, 'time': request.time, 'deltaTime': request.delta, 'pattern': request.pattern}
        logging.info("GET Request made from grpc client")
        result = requests.get(configData['awsendpointapi'], params=params)
        if result.status_code == 200:
            logging.info("Successful response for the given input parameters")
        elif result.status_code== 400:
            logging.error("Failure case due to invalid input")
        return logRequest_pb2.response(result=result.text)


def serve():
    logging.info("Starting the server")
    print("Stating the server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=int(configData["maxworkers"])))
    logRequest_pb2_grpc.add_logRequestServicer_to_server(logRequest(), server)
    print("Actively listening in port 50051")
    logging.info("Actively listening in port 50051")
    server.add_insecure_port('[::]:' + configData["portnumber"])
    server.start()
    server.wait_for_termination()
def testLogServer():
    with open('logServer.log','r') as f:
        content = f.readlines()
        assert(content is not None)
if __name__ == '__main__':
    serve()
