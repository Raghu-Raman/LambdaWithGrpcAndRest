# LambdaWithGrpcAndRest
**Name**: Raghuraman Venkatesh
**E-mail**: rvenka26@uic.edu  
##Project Description
 The main objective of the project is to create lambda function in aws Lambda along with an exposed API endpoint, and connect it with server-client architectures connected by grpc and rest. The first part of the project is to create a client-server architecture connected by grpc 
 The second part of the project is to create a server program with a rest api attached with it.

##Project Overview
####Grpc
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
 ####Lambda Function
   Lambda is a compute service that lets you run code without provisioning or managing servers.
   - Lambda fuction can be created in AWS/Lambda
   - Click on 'Create Function' . Select ```Python``` and choose ```arm``` architechture
   - The algorithm to be performed is to perform O(Log n) search in the log message obtained from the s3 bucket.
   - Performing the binary search will provide with O(Log n)
   - The mid, left and right pointers will be moved accordingly to obtained the correct indices.
   - Once the indices are identified , we should go from left to right and obtain the patterns using regex matching
   - The patterns obtained are put in a string and obtain a md5 hash 
   - If there is no pattern or file there, return status code 400 else return code 200



