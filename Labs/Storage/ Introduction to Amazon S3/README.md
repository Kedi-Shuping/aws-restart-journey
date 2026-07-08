# S3 Static Website Hosting with AWS CLI

## Overview

This project demonstrates how to host a static website on Amazon S3 using the AWS CLI and IAM. The website files were extracted from a lab environment, uploaded to an S3 bucket, and configured for public access.

During the project, I created an IAM user with S3 full access, enabled static website hosting, and built a reusable deployment script using `aws s3 sync` to automate future updates.

**Note:** The original lab instructions used `aws s3 cp --recursive`. Since `aws s3 sync` only uploads changed files, I replaced it for faster, more efficient deployments.

---

## AWS Services Used

- Amazon S3
- AWS IAM
- AWS CLI
- AWS Systems Manager (SSM)

---

## Architecture

The solution follows this workflow:

1. **Developer** runs deployment script
2. **AWS CLI** syncs files to **S3 bucket**
3. **S3 bucket** hosts static website
4. **End users** access website via bucket endpoint

---

## Project Workflow

1. Created an S3 bucket with a unique name
2. Created an IAM user (`awsS3user`) with a login profile
3. Attached the `AmazonS3FullAccess` policy before signing out
4. Extracted static website files from the lab environment
5. Uploaded files to S3 with public-read access
6. Enabled static website hosting
7. Created a deployment script using `aws s3 sync`

---

## Deployment Script

```bash
#!/bin/bash
aws s3 sync /home/ec2-user/sysops-activity-files/static-website/ s3://kshuping004/ --acl public-read
