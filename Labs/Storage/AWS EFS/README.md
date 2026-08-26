# Amazon EFS Shared File Storage

## Overview

This project demonstrates how to create and configure Amazon Elastic File System (EFS) and mount it to multiple Amazon EC2 instances.

Amazon EFS provides shared file storage that can be accessed by multiple EC2 instances over the network using NFS. During the exercise, I created an EFS file system, configured mount targets across multiple sites, installed the Amazon EFS utilities on Linux, mounted the file system, and verified access from multiple instances.

## Training Evidence

**AWS SimuLearn:** File Systems in the Cloud  
**Completed:** July 7, 2026

[View AWS Completion Certificate](../../../Certifications/aws-simulearn-file-systems-in-the-cloud-certificate.pdf)

## AWS Services and Components Used

- Amazon EFS
- Amazon EC2
- Amazon VPC
- Security Groups
- EFS Mount Targets
- Amazon Linux
- NFS

## Project Workflow

1. Created an Amazon EFS file system.
2. Configured mount targets in multiple Availability Zones/sites.
3. Configured network access for NFS traffic (TCP port 2049).
4. Connected to EC2 instances using EC2 Instance Connect.
5. Installed the Amazon EFS utilities on Linux.
6. Mounted the EFS file system to a local directory.
7. Verified that the EFS file system was successfully mounted.
8. Verified that the shared file system was accessible across multiple sites/instances.

## Technical Context

Amazon EFS is network file storage rather than block storage attached to a single EC2 instance. EC2 clients access the same EFS file system over the VPC using NFS. EFS mount targets provide network access to the file system within the Availability Zones where clients connect.

The practical exercise demonstrated the Linux side of this relationship: installing the EFS utilities, mounting the file system, and validating the resulting mount from EC2 instances.

## Evidence

The screenshots below highlight the key configuration and validation steps from the completed SimuLearn exercise.

### 1. Amazon EFS File System Created

This screenshot shows the successful creation of the Amazon Elastic File System (EFS), including the `PetModels-EFS-1` file system.

![Amazon EFS File System Created](screenshots/efs-file-system-created.png)

---

### 2. EFS Mount Targets Created

This screenshot shows the configuration of EFS mount targets, providing network access to the shared file system from the VPC.

![EFS Mount Targets Created](screenshots/efs-mount-targets-created.png)

---

### 3. EFS Mounted on an EC2 Instance

This screenshot shows the Amazon EFS utilities being installed and the EFS file system being mounted on a Linux EC2 instance.

![EFS Mounted on EC2 Instance](screenshots/efs-mounted-on-ec2-instance.png)

---

### 4. EFS Mounted Across Multiple Sites

This screenshot verifies that the same EFS file system was mounted and accessible across multiple sites, with the terminal evidence showing mounts for sites A, B, and C.

![EFS Mounted on All Sites](screenshots/efs-mounted-on-all-sites.png)

## Skills Demonstrated

- Configured shared network storage using Amazon EFS
- Created and configured EFS mount targets
- Configured Security Groups for NFS communication
- Installed EFS utilities on Linux
- Mounted network file systems on Linux
- Connected multiple EC2 instances/sites to shared storage
- Used Linux commands to validate mounted file systems
- Interpreted how EFS provides shared storage to networked compute resources
