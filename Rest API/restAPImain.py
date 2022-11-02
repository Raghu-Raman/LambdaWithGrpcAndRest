from flask import Flask
from flask_restful import Resource, Api
import requests
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self,date,time,deltaTime,pattern):
        params = {'date': date, 'time': time, 'deltaTime': deltaTime, 'pattern': pattern}
        result = requests.get("https://49jyovhul2.execute-api.us-east-2.amazonaws.com/Prod/hello", params=params)
        # print(result.status_code)
        if 200 == result.status_code:
            return {'status_code':200,'body':str(result.content)}
        elif 404 == result.status_code:
            return{'status_code': 404,'body':"Invalid input parameters."}

api.add_resource(HelloWorld,"/helloWorld/<string:date>/<string:time>/<string:deltaTime>/<string:pattern>")

if(__name__=="__main__"):
    app.run(debug=True)

