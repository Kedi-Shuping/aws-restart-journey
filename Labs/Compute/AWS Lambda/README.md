# AWS Lambda Sales Report Application

## Overview

This project demonstrates how to build and troubleshoot a serverless reporting solution using AWS Lambda.

The application extracts sales data from a MySQL database hosted on an Amazon EC2 LAMP server. It uses a Lambda Layer to package external Python dependencies, retrieves database connection information securely from AWS Systems Manager Parameter Store, and connects to the database through an Amazon VPC.

During the project, I configured IAM roles, created a Lambda Layer, deployed a Lambda function using the Python 3.10 runtime, configured VPC networking, analyzed CloudWatch logs, and resolved a database connectivity issue caused by Security Group rules.

> **Note:** The original lab instructions specified **Python 3.9**. Since that runtime was no longer available in the AWS Management Console, I completed the lab using **Python 3.10**.
## AWS Services Used

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

The Lambda function retrieves database credentials securely from Parameter Store, connects to the MySQL database hosted on Amazon EC2 through an Amazon VPC, and extracts sales data for reporting.

## Project Workflow

1. Reviewed the IAM execution roles and permissions required for the Lambda functions.
2. Created a Lambda Layer containing the PyMySQL library.
3. Created a Lambda function using the Python 3.10 runtime.
4. Configured the function to use an existing IAM execution role.
5. Attached the custom Lambda Layer to the function.
6. Imported the provided Python code for extracting sales data.
7. Configured the Lambda function to run inside the application's Amazon VPC.
8. Retrieved database connection details from AWS Systems Manager Parameter Store.
9. Created and executed a custom test event.
10. Used Amazon CloudWatch Logs to investigate a timeout error.
11. Identified and corrected the Security Group configuration to allow MySQL connectivity.
12. Successfully tested the Lambda function and verified the returned JSON response.
    

## Skills Demonstrated

- Built and configured AWS Lambda functions
- Created and attached Lambda Layers for external Python libraries
- Configured IAM execution roles and permissions
- Retrieved sensitive configuration values using AWS Systems Manager Parameter Store
- Connected AWS Lambda to resources inside an Amazon VPC
- Configured Security Groups for database connectivity
- Tested Lambda functions using custom JSON events
- Used Amazon CloudWatch Logs to troubleshoot execution failures
- Resolved network connectivity issues affecting Lambda execution
- Queried a MySQL database from AWS Lambda using Python

  ## Challenges Encountered

During testing, my Lambda function kept timing out after three seconds. I first increased the timeout to thirty seconds to verify whether execution time was the problem. After reviewing the CloudWatch logs, I discovered the real issue wasn't the timeout, it was a Security Group blocking MySQL traffic on port 3306. Once I fixed the inbound rule, the function connected successfully.
