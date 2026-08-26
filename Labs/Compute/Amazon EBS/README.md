# Amazon EBS (Elastic Block Store)

## Overview

This lab demonstrated how Amazon Elastic Block Store (EBS) provides persistent block storage for Amazon EC2. I created an EBS volume, attached it to an EC2 instance, formatted and mounted it in Linux, wrote data to the volume, and then used an EBS snapshot to restore that data to a new volume.

## Training Evidence

**AWS Re/Start lab:** Working with Amazon EBS

## AWS Services and Components Used

- Amazon EBS
- Amazon EC2
- Amazon EBS Snapshots
- Amazon Linux
- Linux filesystem and mount utilities

## Project Workflow

1. Created a 1 GiB `gp2` EBS volume in the same Availability Zone as the EC2 instance.
2. Attached the volume to the EC2 instance as `/dev/sdb`.
3. Created an `ext3` filesystem and mounted the volume at `/mnt/data-store`.
4. Added the volume to `/etc/fstab` and verified the mounted storage with `df -h`.
5. Created `file.txt` on the EBS volume and verified that the data was accessible.
6. Created an EBS snapshot of the volume.
7. Deleted the original `file.txt` and verified that it was no longer present.
8. Created a new EBS volume from the snapshot and attached it to the EC2 instance as `/dev/sdc`.
9. Mounted the restored volume at `/mnt/data-store2` and verified that the original `file.txt` had been recovered.

## Technical Context

Amazon EBS provides block storage designed for use with EC2. Unlike ephemeral instance storage, EBS volumes are persistent independently of the lifecycle of the EC2 instance.

The exercise also demonstrated the relationship between an EBS volume and its snapshot. A snapshot provides a point-in-time backup from which a new EBS volume can be created. In this lab, that recovery path was tested by deleting a file from the original volume and then confirming that the file was available after restoring the snapshot to a new volume.

On the Linux side, the exercise required creating a filesystem, mounting the block device, configuring `/etc/fstab`, and using standard Linux commands to verify storage and data.

## Evidence

The screenshots below highlight the key configuration and validation steps from the completed lab.

### 1. EBS Volume Attached to EC2

Created the EBS volume and attached `My Volume` to the Lab EC2 instance.

![EBS Volume Attached](screenshots/Attach%20EBS%20to%20instance.png)

---

### 2. Snapshot-Based Data Recovery

Created a snapshot of the EBS volume, deleted the original `file.txt`, and restored the snapshot to a new volume. The restored volume was mounted separately and verified to contain the original file.

![EBS Mounted and Recovery Verified](screenshots/Mounted%20EBS%20from%20Linux.png)

## Skills Demonstrated

- Created and managed Amazon EBS volumes
- Attached block storage to an EC2 instance
- Formatted and mounted a Linux block device
- Configured persistent mounts using `/etc/fstab`
- Used Linux commands to inspect and verify storage
- Created and used EBS snapshots for data recovery
- Restored an EBS snapshot to a new volume
- Verified data recovery after restoring from a snapshot

## What I Learned

This lab reinforced the difference between block storage and the compute instance using it. I also gained practical experience with the full EBS storage lifecycle: provisioning a volume, attaching and mounting it, writing data, creating a snapshot, and restoring that snapshot to recover the data.

The recovery exercise showed how an EBS snapshot can provide a recoverable point-in-time copy of a volume, allowing the data to be restored to a new EBS volume when needed.
