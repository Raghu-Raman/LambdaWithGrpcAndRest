import requests

BASE ="http://127.0.0.1:5000/"

response = requests.get(BASE+"helloWorld/2022-10-24/20:40:00.000/10/INFO")

print(response.json())

