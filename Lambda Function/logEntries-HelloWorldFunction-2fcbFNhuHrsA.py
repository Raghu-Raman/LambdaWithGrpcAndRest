import json
import re
import uuid
import datetime
import boto3
import hashlib
import pytest

# import requests

#perform binary search for the log messages
def binarySearch(contents,startTime,endTime):
    timePattern = "[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}" #time pattern to find the time in a given string
    left = 0 # intialize lower bound (left) to 0
    right = len(contents)-1 # intialize higher bound(right) to length of the string
    #perform binary search
    while(left<=right):
        mid = (left + right) // 2
        midTimePattern = re.match(timePattern,contents[mid])
        if(midTimePattern is not None):
            midTimetemp = midTimePattern.group()
            midTimeDT = datetime.datetime.strptime(midTimetemp,"%H:%M:%S.%f")
            midTime = midTimeDT.time()
        # print(midTime)
        if(startTime > midTime):
            left = mid+1
        elif(endTime < midTime):
            right = mid - 1
        else:
            #return the left right and mid value.
            return(left,mid,right)
    return(None,None,None)

def lambda_handler(event, context):
    #define the input parameters for post function
    if(event['httpMethod']=='POST'): # get params
        eventBody = json.loads(event['body'])
        dateParam = eventBody['date']
        timeParam = eventBody['time']
        deltaTimeParam = eventBody['deltaTime']
        patternParam = eventBody['pattern']
        time = datetime.datetime.strptime(timeParam,"%H:%M:%S.%f")
        deltaTime = datetime.datetime.strptime(deltaTimeParam,"%M")
        logFileKey = 'LogFileGenerator.'+dateParam+'.log'
    #define the input parameters for the get function
    elif(event['httpMethod']=='GET'):
        dateParam = event['queryStringParameters']['date']
        timeParam = event['queryStringParameters']['time']
        deltaTimeParam = event['queryStringParameters']['deltaTime']
        patternParam = event['queryStringParameters']['pattern']
        time = datetime.datetime.strptime(timeParam,"%H:%M:%S.%f")
        deltaTime = datetime.datetime.strptime(deltaTimeParam,"%M")
        logFileKey = 'LogFileGenerator.'+dateParam+'.log'
    s3 = boto3.client('s3') # create a s3 client for the s3 resource
    try:
        data = s3.get_object(Bucket='tryingloghw2', Key=logFileKey)
    except:# if there is no file under the given date,following will be returned
        return  {
        "statusCode": 404,
        "body": "False. No file under the requested date"
    }
    timePattern = "[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}"
    contents = data['Body'].read().decode('utf-8').split('\n')
    deltaTimeInt = int(deltaTime.strftime("%M"))
    #The next 6 lines of code checks if the input time is lesser than the starting time of the file similarly if the input end time is greater than the end time of the file
    fileStartTimePattern = re.match(timePattern,contents[1])
    fileStartTimeGroup = fileStartTimePattern.group()
    fileStartTime = datetime.datetime.strptime(fileStartTimeGroup,"%H:%M:%S.%f")
    fileEndTimePattern = re.match(timePattern,contents[len(contents)-3])
    fileEndTimeGroup = fileEndTimePattern.group()
    fileEndTime = datetime.datetime.strptime(fileEndTimeGroup,"%H:%M:%S.%f")
    startTime = time - datetime.timedelta(minutes=deltaTimeInt)
    endTime = time + datetime.timedelta(minutes=deltaTimeInt)
    if(time<fileStartTime or time>fileEndTime):
        if(startTime<fileStartTime or endTime>fileEndTime):
            return{ "statusCode":404,
            "body": "False. Given input time is not present in the log file for the  date you provided"
            }
    l,m,r = binarySearch(contents, startTime.time(), endTime.time()) # call the binary search on the given content
    returnString = str(l)+" "+str(m)+" "+str(r)
    startTimeString = str(startTime.strftime("%H:%M:%S.%f"))
    endTimeString = str(endTime.strftime("%H:%M:%S.%f"))
    resultString = ""
    for i in range(l,r):
        tempTimePattern = re.match(timePattern,contents[i])
        tempTimeGroup = tempTimePattern.group()
        tempTime = datetime.datetime.strptime(tempTimeGroup,"%H:%M:%S.%f")
        if(tempTime.time()>startTime.time() and tempTime.time()<endTime.time()):
            pattern = re.search(patternParam,contents[i])
            if(pattern is not None):
                result = hashlib.md5(contents[i].encode('utf-8')).hexdigest()
                resultString += str(result) + ", "
    if(startTime<fileStartTime):
        startTime = fileStartTime
    if(endTime>fileEndTime):
        endTime = fileEndTime
    startTimeString = str(startTime.strftime("%H:%M:%S.%f"))
    endTimeString = str(endTime.strftime("%H:%M:%S.%f"))
    if not len(resultString):
        return{
            "statusCode":404,
            "body":"False. No such pattern exists for the given time interval "+startTimeString+" to "+endTimeString
        }
    returnValue = resultString+" are the md5 hash values generated for time interval "+startTimeString+" to "+endTimeString
    # return the response to the call
    return {
        "statusCode": 200,
        "body": returnValue
    }
# @pytest.fixture
def test_1():
    logFileKey = 'LogFileGenerator.2022-10-23.log'
    s3 = boto3.client('s3')  # create a s3 client for the s3 resource
    data = s3.get_object(Bucket='tryingloghw2', Key=logFileKey)
    timeParam = "21:33:00.000"
    deltaTimeParam = "1"
    time = datetime.datetime.strptime(timeParam, "%H:%M:%S.%f")
    deltaTime = datetime.datetime.strptime(deltaTimeParam, "%M")
    deltaTimeInt = int(deltaTime.strftime("%M"))
    contents = data['Body'].read().decode('utf-8').split('\n')
    startTime = time - datetime.timedelta(minutes=deltaTimeInt)
    endTime = time + datetime.timedelta(minutes=deltaTimeInt)
    l,m,r = binarySearch(contents, startTime.time(), endTime.time()) # call the binary search on the given content
    assert(l==0 and m == 12 and r == 24)
