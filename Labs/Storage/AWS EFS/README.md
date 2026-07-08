# Amazon EFS Shared File Storage

## Overview

This project demonstrates how to create and configure Amazon Elastic File System (EFS) and mount it to multiple Amazon EC2 instances.

The shared file system allows multiple EC2 instances to access the same files simultaneously over the network using the NFS protocol. During the project, I created an EFS file system, configured mount targets in multiple Availability Zones, mounted the file system on two EC2 instances, and verified that changes made on one instance were immediately visible on the other.

## AWS Services Used

- Amazon EFS
- Amazon EC2
- Amazon VPC
- Security Groups
- Mount Targets
- Amazon Linux
- NFS (Network File System)

## Project Workflow

1. Launched two Amazon EC2 instances.
2. Created an Amazon EFS file system.
3. Created mount targets in multiple Availability Zones.
4. Configured Security Groups to allow NFS traffic (TCP Port 2049).
5. Connected to both EC2 instances using EC2 Instance Connect.
6. Installed the Amazon EFS utilities.
7. Mounted the EFS file system on both EC2 instances.
8. Verified that the Amazon EFS file system was successfully mounted on both EC2 instances.
9. Created files on the first EC2 instance.
10. Confirmed that files created on one EC2 instance were immediately visible on the second instance.
11. Verified that both EC2 instances were reading and writing to the same shared storage.

## Skills Demonstrated

- Configured shared network storage using Amazon EFS
- Created EFS mount targets
- Configured Security Groups for NFS communication
- Mounted network file systems on Linux
- Connected multiple EC2 instances to shared storage
- Verified persistent shared storage across servers
- Used Linux commands to validate mounted file systems
