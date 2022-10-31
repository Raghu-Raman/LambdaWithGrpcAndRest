import configparser

config = configparser.ConfigParser()

config["Server"]={
    "awsEndpointApi" : "https://49jyovhul2.execute-api.us-east-2.amazonaws.com/Prod/hello",
    "maxWorkers" : 10,
    "portNumber" : "50051"
}

with open("configFileServer.ini","w") as f:
    config.write(f)
