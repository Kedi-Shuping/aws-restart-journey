# AWS Lambda Sales Report Application

## Overview

This project demonstrates how to build and troubleshoot a serverless reporting solution using AWS Lambda.

The application extracts sales data from a MySQL database hosted on an Amazon EC2 LAMP server. It uses a Lambda Layer to package the external Python dependency, retrieves database connection information from AWS Systems Manager Parameter Store, and connects to the database through an Amazon VPC.

During the project, I configured IAM roles, created a Lambda Layer, deployed a Lambda function using the Python 3.10 runtime, configured VPC networking, analyzed CloudWatch logs, and resolved a database connectivity issue caused by Security Group rules.

> **Runtime note:** The original lab instructions specified **Python 3.9**. Since that runtime was no longer available in the AWS Management Console, I completed the project using **Python 3.10**.

## AWS Services and Components Used

- AWS Lambda
- AWS Lambda Layers
- Amazon EC2 (LAMP Server)
- AWS Identity and Access Management (IAM)
- AWS Systems Manager Parameter Store
- Amazon VPC
- Security Groups
- Amazon CloudWatch Logs
- MySQL
- Python 3.10

## Architecture

The solution follows this workflow:

```text
Customer
    │
    ▼
Cafe Website (Apache/PHP on Amazon EC2)
    │
    ▼
MySQL Database
    ▲
    │
AWS Lambda Data Extractor
    ▲
    │
AWS Systems Manager Parameter Store
```

The Lambda function retrieves database connection details from Parameter Store, connects to the MySQL database hosted on Amazon EC2 through the application's VPC, and extracts sales data for reporting.

## Project Workflow

1. Reviewed the IAM execution roles and permissions required for the Lambda function.
2. Created a Lambda Layer containing the PyMySQL library.
3. Created a Lambda function using the Python 3.10 runtime.
4. Configured the function to use the existing IAM execution role.
5. Attached the custom Lambda Layer to the function.
6. Imported the provided Python code for extracting sales data.
7. Configured the Lambda function to run inside the application's Amazon VPC.
8. Retrieved database connection details from AWS Systems Manager Parameter Store.
9. Created and executed a custom test event.
10. Used Amazon CloudWatch Logs to investigate a timeout error.
11. Identified and corrected the Security Group configuration to allow MySQL connectivity.
12. Successfully tested the Lambda function and verified the returned JSON response.

## Technical Context

The project combines serverless compute with a database hosted on EC2. Lambda provides the execution environment for the reporting logic, while the VPC configuration allows that function to reach the MySQL database. Parameter Store keeps connection information outside the function code, and the Lambda Layer supplies the PyMySQL dependency without packaging it directly into the function deployment.

The troubleshooting process was an important part of the project. A timeout does not necessarily mean that the Lambda function needs more execution time; it can also indicate that the function is waiting for a network connection that cannot be established.

## Troubleshooting

During testing, the Lambda function repeatedly timed out after three seconds. I temporarily increased the timeout to thirty seconds to test whether execution time was the limiting factor. CloudWatch logs then showed that the function was unable to establish the expected database connection.

I traced the connectivity path to the Security Group configuration and identified that MySQL traffic on port `3306` was not permitted. After correcting the inbound rule, the Lambda function connected successfully and returned the expected JSON response.

This demonstrated the importance of treating a timeout as a symptom rather than immediately assuming that the timeout setting itself is the root cause.

## Skills Demonstrated

- Built and configured AWS Lambda functions
- Created and attached Lambda Layers for external Python libraries
- Configured IAM execution roles and permissions
- Retrieved configuration values using AWS Systems Manager Parameter Store
- Connected AWS Lambda to resources inside an Amazon VPC
- Configured Security Groups for database connectivity
- Tested Lambda functions using custom JSON events
- Used Amazon CloudWatch Logs to troubleshoot execution failures
- Diagnosed and resolved network connectivity issues affecting Lambda execution
- Queried a MySQL database from AWS Lambda using Python

## Key Lessons Learned

The project reinforced that serverless does not mean network-independent. When Lambda is placed inside a VPC and needs to reach a database, the network path and security controls still determine whether the function can connect.

It also reinforced a useful troubleshooting principle: **a timeout describes what the application experienced, not necessarily why it happened**. Logs and network configuration provided the information needed to distinguish an execution-time problem from a connectivity problem.
