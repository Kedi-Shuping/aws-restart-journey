# CloudFormation Challenge

## Overview

In this challenge, I built and deployed an AWS environment using a CloudFormation YAML template. The task was to describe the network, security group, and EC2 instance as infrastructure as code, then deploy the template as a stack.

I created the template from scratch rather than relying on a pre-built stack.

## Resources defined in the template

The `template.yaml` defines:

- **VPC** with CIDR block `10.0.0.0/20`
- **Internet Gateway** attached to the VPC
- **Subnet** with CIDR block `10.0.0.0/24`, named `MyPrivateSubnet`
- **Route table** associated with the subnet
- **Security group** allowing inbound SSH traffic on TCP port 22 from `0.0.0.0/0`
- **EC2 instance** using instance type `t3.micro`
- **Amazon Linux 2 AMI parameter** resolved from the public Systems Manager parameter path

## What I did

1. Wrote the CloudFormation template in YAML.
2. Defined the VPC and attached an Internet Gateway to it.
3. Created the subnet and its route table association.
4. Added a security group with the SSH ingress rule required by the exercise.
5. Defined the EC2 instance and referenced the Amazon Linux 2 AMI through Systems Manager.
6. Deployed the template as a CloudFormation stack and reviewed the resources created by the stack.

## Network configuration notes

The subnet is named `MyPrivateSubnet` in the template. It is associated with a route table, but the template does not add a default route to the Internet Gateway. It also does not enable automatic public IPv4 address assignment for the subnet or instance.

Attaching an Internet Gateway to a VPC does not, by itself, make a subnet public. A route from the subnet's route table to the Internet Gateway, along with the required public addressing, would also be needed for direct internet connectivity.

The security group allows SSH from `0.0.0.0/0`, meaning the rule permits connection attempts from any IPv4 address. This reflects the exercise configuration; it should be restricted to trusted source IP ranges in a real environment.

## What I learned

This challenge gave me practice translating infrastructure requirements into CloudFormation resources and connecting those resources through references and dependencies.

It also reinforced that resource names and labels do not determine network behaviour. The route table and addressing configuration determine whether a subnet has a route to the internet; an Internet Gateway attachment alone is not enough.

## Project files

- `template.yaml` — the CloudFormation template created for the challenge.

## Evidence

The YAML template is included in this folder as the retained technical artefact for the challenge. No screenshots were retained for this exercise.
