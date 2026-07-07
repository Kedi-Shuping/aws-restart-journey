# Amazon EBS (Elastic Block Store)

## Overview

This lab focused on creating and managing Amazon Elastic Block Store (EBS) volumes for Amazon EC2 instances. I learned how to create, attach, format, mount, and verify persistent block storage that remains available even when an EC2 instance is stopped.

## AWS Services Used

- Amazon EC2
- Amazon EBS

## Skills Demonstrated

- Creating an EBS volume
- Attaching an EBS volume to an EC2 instance
- Formatting and mounting a volume in Linux
- Verifying mounted storage
- Understanding persistent block storage

## Key Concepts Learned

- Difference between Amazon EBS and Instance Store
- Persistent storage for EC2 instances
- Block storage versus object storage
- Mounting storage using Linux commands
- Managing storage independently of the EC2 instance

## Linux Commands Used

```bash
sudo mkdir /mnt/data-store
sudo mount /dev/sdb /mnt/data-store
df -h
cat /etc/fstab
```

## Screenshots

### EBS Volume Attached to EC2

![EBS Attached](screenshots/Attach%20EBS%20to%20instance.png)

### Mounted EBS Volume in Linux

![Mounted EBS](screenshots/Mounted%20EBS%20from%20Linux.png)

## Outcome

Successfully created and attached an Amazon EBS volume to an EC2 instance, mounted it using Linux, verified that it was accessible, and gained hands-on experience with persistent storage in AWS.
