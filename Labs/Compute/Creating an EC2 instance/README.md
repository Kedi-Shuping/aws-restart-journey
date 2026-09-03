# Deploying and Managing an Amazon EC2 Web Server

## Overview

This project demonstrates the deployment and lifecycle management of an Amazon EC2 web server running Amazon Linux 2023.

I configured Apache using EC2 User Data, allowed HTTP access through a Security Group, monitored the instance, resized both compute and storage resources, and tested termination protection.

## AWS Services and Components Used

- Amazon EC2
- Amazon EBS
- Amazon VPC
- Security Groups
- Amazon Machine Image (AMI)
- Amazon CloudWatch

## Project Workflow

1. Launched an EC2 instance using an Amazon Linux 2023 AMI.
2. Configured the instance's Security Group to allow HTTP traffic.
3. Used EC2 User Data with Bash to deploy Apache during instance initialization.
4. Monitored the instance's health and status.
5. Used Amazon CloudWatch to observe the instance from the AWS monitoring layer.
6. Expanded the attached EBS volume.
7. Changed the EC2 instance type to demonstrate compute resizing.
8. Enabled termination protection and tested its effect on the instance lifecycle.
9. Disabled termination protection and terminated the instance as part of cleanup.

## Technical Context

This project demonstrates how several AWS components work together to deliver and manage a basic web server:

```text
Amazon VPC
    │
    ▼
EC2 Instance ─── Security Group ─── HTTP access
    │
    ├── Amazon EBS ─── persistent block storage
    │
    └── User Data ─── Apache installation/configuration
            │
            ▼
      Web Server

EC2 ─── CloudWatch ─── instance monitoring
```

EC2 provides the compute capacity, while EBS supplies persistent block storage attached to the instance. The Security Group controls network access to the instance, and User Data provides automated initialization when the instance launches.

The exercise also demonstrated that EC2 resources can be modified after deployment. Compute capacity can be changed by selecting another instance type, while attached EBS storage can be expanded independently. Termination protection provides an additional safeguard against accidental instance deletion.

## Screenshots

### EC2 Instance Launched
![EC2 Instance Launched](screenshots/ec2-instance-launched.png)

### Security Group Updated
![Security Group Updated](screenshots/security-group-updated.png)

### EC2 Monitoring
![EC2 Monitoring](screenshots/ec2-monitoring.png)

### CloudWatch Monitoring
![CloudWatch Instance Screenshot](screenshots/ec2-cloudwatch-instance-screenshot.png)

### EBS Volume Resized
![EBS Volume Resized](screenshots/ebs-volume-resized.png)

### EC2 Instance Type Changed
![EC2 Instance Type Changed](screenshots/ec2-instance-type-changed.png)

### Termination Protection Enabled
![Termination Protection Enabled](screenshots/termination-protection-enabled.png)

### EC2 Instance Terminated
![EC2 Instance Terminated](screenshots/ec2-instance-terminated.png)

## Skills Demonstrated

- Launched and configured an EC2 instance
- Selected an appropriate Amazon Machine Image (AMI)
- Configured Security Groups for HTTP access
- Used EC2 User Data for automated server initialization
- Deployed Apache on Amazon Linux
- Monitored EC2 health and resource activity
- Used Amazon CloudWatch for instance monitoring
- Resized EC2 compute resources
- Expanded Amazon EBS storage
- Enabled and tested EC2 termination protection
- Managed the EC2 instance lifecycle from deployment through termination

## Key Lessons Learned

EC2 is not an isolated compute resource. A functioning web server depends on the relationship between the instance, its network access controls, attached storage, initialization process, and monitoring tools.

The project also reinforced the value of automation during deployment. Using User Data allowed the web server configuration to begin automatically as part of instance initialization rather than requiring every setup command to be performed manually.
