import pytest
import requests
import configparser

# passing the api endpoint of the lambda function
awsLink = "https://49jyovhul2.execute-api.us-east-2.amazonaws.com/Prod/hello"

configServer = configparser.ConfigParser()
configServer.read("configFileServer.ini")
configData = configServer['Server']

#testing if the input parameters are not none
def testNoneCheck():
    assert (configData['awsendpointapi'] is not None and configData['maxworkers'] is not None and configData['portnumber'] is not None)
# testing the input parameters to the configuration file parameters
def testConfig():
    assert (configData['awsendpointapi'] == awsLink and configData['maxworkers'] == "10" and configData['portnumber'] == "50051")

# sending an input that is not present in the s3 bucket.
def test1():
    date = "2022-11-23"
    time = "10:00:00.000"
    deltaTime = "10"
    pattern = "INFO"
    params = {'date': date, 'time': time, 'deltaTime': deltaTime, 'pattern': pattern}
    response = requests.get(awsLink, params=params)
    assert (response.text == "No file under the requested date")

# the input time is not within the given file
def test2():
    date = "2022-10-23"
    time = "10:00:00.000"
    deltaTime = "10"
    pattern = "INFO"
    params = {'date': date, 'time': time, 'deltaTime': deltaTime, 'pattern': pattern}
    response = requests.get(awsLink, params=params)
    assert (response.text == "Given input time is not present in the date you are looking for")

# The test is for sending an input which crosses the timelimit given in the file hence it returns only the hash value for the given time limit
def test3():
    date = "2022-10-23"
    time = "21:35:00.000"
    deltaTime = "20"
    pattern = "INFO"
    params = {'date': date, 'time': time, 'deltaTime': deltaTime, 'pattern': pattern}
    response = requests.get(awsLink, params=params)
    assert (response.text == "cbf06430815aed30112e67f5c90c35c6 is the md5 hash value generated for time interval 21:31:53.005000 to 21:41:21.669000")

# The test is to find the working of the algorithm when there is no pattern given
def test4():
    date = "2022-10-23"
    time = "21:35:00.000"
    deltaTime = "20"
    pattern = "INFOTAINMENT"
    params = {'date': date, 'time': time, 'deltaTime': deltaTime, 'pattern': pattern}
    response = requests.get(awsLink, params=params)
    assert (response.text == "No such pattern exists for the given time interval 21:31:53.005000 to 21:41:21.669000")

#This test performs with every right parameter given as input and expecting a proper response from the lambda fucntion
def test5():
    date = "2022-10-24"
    time = "20:40:00.000"
    deltaTime = "10"
    pattern = "INFO"
    params = {'date': date, 'time': time, 'deltaTime': deltaTime, 'pattern': pattern}
    response = requests.get(awsLink, params=params)
    assert (response.text == "23dd84f54f1764feee9e2ffa6ac2b950 is the md5 hash value generated for time interval 20:30:00.000000 to 20:50:00.000000")

#This test is similar to test 5 but the hash value has been changed to test out the hash value that is being generated.
def test6():
    date = "2022-10-24"
    time = "20:40:00.000"
    deltaTime = "10"
    pattern = "INFO"
    params = {'date': date, 'time': time, 'deltaTime': deltaTime, 'pattern': pattern}
    response = requests.get(awsLink, params=params)
    assert (response.text != "23dd84f54f17649e2ffa6ac2b950 is the md5 hash value generated for time interval 20:30:00.000000 to 20:50:00.000000")
