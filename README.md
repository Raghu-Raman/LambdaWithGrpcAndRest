# Lambda with Grpc and Rest
**Name**: Raghuraman Venkatesh

**UIN**: 657500077

**E-mail**: rvenka26@uic.edu  
## Project Description
 The main objective of the project is to create lambda function in aws Lambda along with an exposed API endpoint, and connect it with server-client architectures connected by grpc and rest. The first part of the project is to create a client-server architecture connected by grpc 
 The second part of the project is to create a server program with a rest api attached with it.

## Project Overview
#### Grpc
  gRPC is a modern open source high performance Remote Procedure Call (RPC) framework that can run in any environment. It can efficiently connect services in and across data centers with pluggable support for load balancing, tracing, health checking and authentication.
#### Ec2 instance
  The first step is to create an EC2 instance and run the LogFileGenerator on the instance, and subsequently move the generated log files to the s3 bucket.
   #### Steps to create ec2 instance
   - Go to Aws and search for ec2 instance
   - Select the server you want to launch your ec2 instance onto.
   - Select the ```Machine Image``` that you want to choose. 
   - Select the ```General purpose``` under the ```Instance type```
   - Click on ``` Review and Launch``` and it will prompt to create a key value pair if it is not already there
   - After naming the key value pair, download the key pair onto your root directory and click ```Launch```
   - After Launching the instance, you can access with the information provided by aws to launch your own instance
   #### Setting up the program in the ec2 instance
   - To setup Java 11 on the ec2 instance , run the following command
   ```wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-securebackup-cookie" https://download.oracle.com/otn-pub/java/jdk/11.0.2+9/f51449fcd52f4d52b93a989c5c56ed3c/jdk-11.0.2_linux-x64_bin.rpm```
   - Update your Yum if you are running the Amazon Linux Build
   ```sudo yum update```
   - Install sbt on the ec2 instance using the following command
   ``` curl -L https://www.scala-sbt.org/sbt-rpm.repo > sbt-rpm.repo```
   ``` sudo mv sbt-rpm.repo /etc/yum.repos.d/ ```
   ``` sudo yum install sbt ```
   - To setup the LogFileGenerator in the ec2 instance, install git in the ec2 instance
   ``` sudo yum install git ```
   - Clone the CS441_Fall2022 repository 
   ```git clone https://github.com/0x1DOCD00D/CS441_Fall2022.git```
   - Edit the configurations under ``` application.conf``` file using 
   ```sudo nano application.conf```
   - Instead of using sudo for everying command you can instead become the superuser using the command ```sudo su```
   - Use the following bash script to generate the log file and move it to the s3 bucket.
   ```
   cd CS441_Fall2022/LogFileGenerator/;
   pwd;
   cd log;
   sudo rm -rf LogFileGenerator*;
   cd ..;
   sudo sbt clean compile run;
   cd ../..;
   aws s3  cp CS441_Fall2022/LogFileGenerator/log/LogFileGenerator*.log s3://tryingloghw2;
   ```
   - You can instead log it into crontab -e to set it up as a cronscript and set a time ```00 20 * * * /root/Script.sh```
   #### Lambda Function
   The lambda function is under the name ``` logEntries-HelloWorldFunction-2fcbFNhuHrsA```
   ###### Lambda is a compute service that lets you run code without provisioning or managing servers.
   - Lambda fuction can be created in AWS/Lambda
   - Click on 'Create Function' . Select ```Python``` and choose ```arm``` architechture
   - The algorithm to be performed is to perform O(Log n) search in the log message obtained from the s3 bucket.
   - Performing the binary search will provide with O(Log n)
   - The mid, left and right pointers will be moved accordingly to obtained the correct indices.
   - Once the indices are identified , we should go from left to right and obtain the patterns using regex matching
   - The patterns obtained are put in a string and obtain a md5 hash 
   - If there is no pattern or file there, return status code 400 else return code 200
  ###### Creating the AWS API endpoint
   - The ``` trigger ``` option has to be set for the lambda function with the following configurations API TYPE -```REST``` and SECURITY -```OPEN```
   - Thus the api trigger will be open to the world and can be accessed by making http requests to the api.
  ###### s3 - Lambda connection
   - Open the lambda function under ```Configuration``` , go to ```Permissions``` and click on ``` Execution Role```.
   - Create a role with policy access to s3 resources for writing , reading ,listing. 
   - Name the role along with the policy and attach it to the lambda function
   - The Lambda is now connected to s3 and can access all of its buckets.
   
 ## Grpc Server and Client
   The Grpc requires protobuf for transfering the data. Protobufs should be installed in the system locally.
   For Mac, Install brew package installer first from [here](https://brew.sh). Then after installing brew, install the 'protobuf' using the command
   ```brew install protobuf```.
   The server file is given under the name ```protoServer.py```. The server will be actively listening to the client side which is given under the name
   ```protoClient.py```.
   To execute the grpc server and client, follow the steps given below:
   - Clone the git onto Pycharm.
   - Make sure Python 3 is installed onto the system.
   - Move into the directory that contains the server , client and protobuf files.
   - Execute the following command ```python -m grpc_tools.protoc --proto_path=. ./request/logRequest.proto --python_out=. --grpc_python_out=.``` for compiling the ```logRequest.proto file```
   - Thus, two new files are created under the name ```logRequest_pb.py``` and ```logRequest_pb_grpc.py```
   - Now, run the server side of the program using the command ```python3 protoServer.py``` in one terminal.
   - Open new terminal and run the client program using the command ``` python3 protoClient.py```
   - The input paramters must be given in the command line along with client execution and must be in the order of date,time, deltaTime and pattern.
   - Output will be received in the client side.
   #### Configuration File
   The configuration file is ``` configFileServer.ini ```. This configuration file will contain all the parameters that will be used in the server file.
   #### Logging
   - Import Logging package in server file.
   - Set level for the logging parameter.
   - Set the file name where all the logging information is to be stored.
  ## Rest API Server and client.
   The rest local server is created using the flask package. The server will be listening in the port 5000. The Rest api can be tested using the ```test.py``` file.
   The input parameters can be changed in the ```test.py``` file.
   
  ## Testing
   - The testing file is under the name ```testingServer.py```
   - The input to this file is given from the config file.
   - Testing of configuration parameters and different outcomes is given here.
   - Use the command ```pytest testingServer.py```
  ## GET and POST Requests
   - The get and post requests to test the lambda function is posted in the document "GET&POST Requests".
   
  ## Output Files
  The output images are :
  1) Output with input time and delta time within the bounds of the file.
  2) Output with no file under the given date.
  3) Output with delta time beyond the limits of the file time.
  4) Output with no pattern in the given time.
  5) Output with given time not in the file.
  6) Testing outcomes.
<img width="1453" alt="Screen Shot 2022-11-01 at 5 23 23 PM" src="https://user-images.githubusercontent.com/78893470/199366606-d85a6801-9512-41bf-8967-fe57e9099706.png">
<img width="903" alt="Screen Shot 2022-11-01 at 5 24 01 PM" src="https://user-images.githubusercontent.com/78893470/199366607-06931af7-b962-41b0-8c31-a1ef0f43cc70.png">
<img width="1453" alt="Screen Shot 2022-11-01 at 5 24 32 PM" src="https://user-images.githubusercontent.com/78893470/199366608-f7d3d2c5-b046-4247-b091-7ffece263006.png">
<img width="988" alt="Screen Shot 2022-11-01 at 7 27 43 PM" src="https://user-images.githubusercontent.com/78893470/199366722-02ce2e12-598e-41cd-98fc-56e6d82aa7f7.png">
<img width="890" alt="Screen Shot 2022-11-01 at 5 25 42 PM" src="https://user-images.githubusercontent.com/78893470/199366611-81d882a0-f3ca-48b9-bb61-e7bd21fe4178.png">
<img width="762" alt="Screen Shot 2022-11-01 at 5 13 01 PM" src="https://user-images.githubusercontent.com/78893470/199366604-2bc2c147-7e9d-49ce-96f1-b09c6b94678a.png">

## Youtube Link
The youtube video for the given project along with explanation is given [here](https://youtu.be/dYWVTq57cu4)
