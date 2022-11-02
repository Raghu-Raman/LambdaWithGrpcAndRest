from __future__ import print_function

import grpc
import request.logRequest_pb2 as logRequest_pb2
import request.logRequest_pb2_grpc as logRequest_pb2_grpc
import logging
import sys
import pytest

logging.basicConfig(filename="logClient.log", level=logging.INFO)
logging.debug("Debug logging test...")

#getting input parameters
logging.info("Getting the input parameters")
dateInput = sys.argv[1]
timeInput = sys.argv[2]
deltaInput = sys.argv[3]
patternInput = sys.argv[4]
print("The input parameters are "+dateInput+" "+timeInput+" "+deltaInput+" "+patternInput)
logging.info("The input parameters are "+dateInput+" "+timeInput+" "+deltaInput+" "+patternInput)

def runClient():
    #creating an insecure channel
    with grpc.insecure_channel('0.0.0.0:50051')as channel:
        stub = logRequest_pb2_grpc.logRequestStub(channel) #creating a stub call the function
        response = stub.logMessageFind(logRequest_pb2.requestCall(date = dateInput,time = timeInput,delta=deltaInput,pattern=patternInput))
        logging.info(response.result)
        print(response.result) #printing response
if __name__ == '__main__':
    runClient() #running client function.
