# Troubleshooting an EC2 Web Application

## Overview

In this lab, I troubleshot an AWS Café web application running on an Amazon EC2 instance. The investigation involved an EC2 launch failure, instance and security group validation, HTTP connectivity, and application-level verification.

Rather than treating the web application as a single problem, I traced the failure across the AWS configuration, network access, operating system, and application layers.

## AWS Services and Tools Used

- Amazon EC2
- Amazon VPC
- Security Groups
- Amazon Machine Image (AMI)
- Apache HTTP Server
- AWS CLI
- Nmap

## Project Workflow

1. Investigated an EC2 launch failure caused by an AMI that was not valid in the selected AWS Region.
2. Corrected the launch configuration and successfully launched the web server.
3. Tested application access from a browser and identified that the lab application was being accessed over HTTP rather than HTTPS.
4. Validated the security group associated with the current EC2 instance instead of relying on a stale security group ID from an earlier run.
5. Inspected network access and HTTP connectivity using AWS CLI output and network testing.
6. Verified the Apache/web application stack on the EC2 host.
7. Confirmed the Café application was functioning by loading the Order History page and retrieving stored order data.

## Technical Context

The troubleshooting required keeping several layers separate:

- **EC2:** The instance had to launch with an AMI available in the selected Region.
- **Networking:** The active instance security group and HTTP access had to be validated against the current instance rather than an earlier resource.
- **Web server:** Apache had to be available on the EC2 host.
- **Application:** The Café application had to respond successfully and return its stored order information.

This made the lab useful for practicing fault isolation rather than simply following a provisioning sequence.

## Verification

The final application test successfully loaded the Café application's Order History page and displayed stored order information, confirming that the web application was reachable and functioning at the application level.

## Skills Demonstrated

- Troubleshooting EC2 launch failures
- Understanding AMI and AWS Region relationships
- Validating the resources actually attached to an EC2 instance
- Inspecting Security Group configuration
- Troubleshooting HTTP connectivity
- Using AWS CLI for resource investigation
- Using Nmap for network-level validation
- Checking a Linux web server and application stack
- Verifying an application through an end-to-end browser test
- Separating infrastructure, networking, operating system, and application-layer failures
