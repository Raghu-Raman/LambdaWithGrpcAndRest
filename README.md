# Lambda with Grpc and Rest
**Name**: Raghuraman Venkatesh
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
   #### Lambda Function
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
   
  ## Output Files
   <img width="1333" alt="Screen Shot 2022-10-31 at 10 48 04 PM" src="https://user-images.githubusercontent.com/78893470/199274891-7d56c258-8ca9-466e-83bf-405ea7a7f4d1.png">
<img width="982" alt="Screen Shot 2022-10-31 at 10 48 29 PM" src="https://user-images.githubusercontent.com/78893470/199274892-833cf65d-ae39-45b7-bf53-c5487b78b80b.png">
<img width="959" alt="Screen Shot 2022-10-31 at 10 48 43 PM" src="https://user-images.githubusercontent.com/78893470/199274894-ac84a776-4dc5-45e8-947e-e7e08fea8117.png">
<img width="1214" alt="Screen Shot 2022-10-31 at 10 49 08 PM" src="https://user-images.githubusercontent.com/78893470/199274895-c6490821-43b3-4e86-9bb9-2a7837140ec9.png">
<img width="1120" alt="Screen Shot 2022-10-31 at 10 49 31 PM" src="https://user-images.githubusercontent.com/78893470/199274896-725615d1-1a50-4368-a4b3-7d44876fce41.png">
<img width="910" alt="Screen Shot 2022-10-31 at 10 54 18 PM" src="https://user-images.githubusercontent.com/78893470/199274897-9e23b160-96bb-4cc3-849d-9ef1b6e2d6a0.png">
<img width="1069" alt="Screen Shot 2022-10-31 at 10 57 38 PM" src="https://user-images.githubusercontent.com/78893470/199274898-9889a650-a33f-4a01-8018-6f9dea446ba9.png">
<img width="1004" alt="Screen Shot 2022-10-31 at 10 59 15 PM" src="https://user-images.githubusercontent.com/78893470/199274899-c50d7bb3-435f-414c-be75-8f4874ae1300.png">

