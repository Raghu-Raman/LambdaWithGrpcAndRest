import boto3

params={'date':"2022-10-24",'time':"20:40:00.000",'deltaTime':"10",'pattern':"INFO"}
response = requests.get("https://49jyovhul2.execute-api.us-east-2.amazonaws.com/Prod/hello",params)
print(response.content)