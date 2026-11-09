# Automating Deployments with AWS CloudFormation

## Overview

In this lab, I used AWS CloudFormation to create and manage AWS infrastructure from a YAML template. Instead of creating each resource manually in the console, I described the resources in a template and deployed them as a stack.

The exercise built the stack in stages: I started with the network and security resources, updated the template to add storage, and then updated it again to add an EC2 instance.

## Resources defined in the template

The final `template.yaml` includes:

- **VPC** with DNS support and DNS hostnames enabled
- **Internet Gateway** attached to the VPC
- **Public subnet** with automatic public IPv4 address assignment
- **Route table** with a default route to the Internet Gateway
- **Security group** allowing inbound HTTP traffic on TCP port 80
- **S3 bucket**
- **EC2 instance** using the Amazon Linux 2 AMI resolved through the public Systems Manager parameter
- **CloudFormation output** for the VPC's default security group ID

The EC2 instance type is `t3.micro`. The template defines the network and HTTP access, but it does not install or configure a web application.

## What I did

1. Created a CloudFormation template in YAML.
2. Deployed the initial stack with the VPC and security resources.
3. Updated the stack to include an S3 bucket.
4. Updated the template again to add the EC2 application server.
5. Used the latest Amazon Linux 2 AMI value from an AWS Systems Manager public parameter rather than hard-coding an AMI ID.
6. Checked the stack and its resources after the updates.
7. Deleted the stack after completing the exercise.

The lab history records the EC2 resource reaching `CREATE_COMPLETE`, the stack reaching `UPDATE_COMPLETE`, and the stack later reaching `DELETE_COMPLETE`.

## What I learned

This exercise helped me understand the CloudFormation stack lifecycle: create a stack, update it by changing the template, inspect the resources CloudFormation manages, and delete the stack when it is no longer needed.

I also learned how parameters and intrinsic functions make templates more reusable. For example, the AMI parameter uses the SSM public parameter path, while functions such as `!Ref`, `!GetAtt`, and `!GetAZs` connect resources and retrieve values inside the template.

## Project files

- `template.yaml` — the CloudFormation template used for the exercise.

## Evidence

The YAML template is included in this folder as the retained technical artefact for the lab. No screenshots were retained for this exercise.
