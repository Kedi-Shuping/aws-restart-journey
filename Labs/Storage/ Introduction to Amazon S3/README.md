# Hosting a Static Website on Amazon S3

## Overview

In this lab, I used the AWS CLI to upload a set of static website files to an S3 bucket and configure the bucket for static website hosting.

I also created an IAM user for the S3 work and wrote a small Bash script to make future uploads easier.

## What I Worked On

1. Created an S3 bucket named `kshuping004` in `us-west-2`.
2. Created an IAM user named `awsS3user`.
3. Attached the `AmazonS3FullAccess` policy to the user.
4. Extracted the website files from the lab environment.
5. Uploaded the files to the bucket using the AWS CLI with the `public-read` ACL.
6. Enabled static website hosting on the bucket.
7. Created a Bash script called `update-website.sh` to upload website changes with `aws s3 sync`.

## Deployment Script

I used `aws s3 sync` instead of the lab's original `aws s3 cp --recursive` command. Sync compares the source and destination and transfers files that need updating, which makes it useful when deploying later changes to the site.

```bash
#!/bin/bash

aws s3 sync /home/ec2-user/sysops-activity-files/static-website/ s3://kshuping004/ --acl public-read
```

## Website Endpoint

The S3 static website endpoint was:

http://kshuping004.s3-website-us-west-2.amazonaws.com

## How the Pieces Fit Together

```text
Website files
     |
     v
AWS CLI / update-website.sh
     |
     v
S3 bucket
     |
     v
Static website hosting
     |
     v
Website endpoint
```

The website files are stored as objects in the S3 bucket. The CLI uploads them, and S3 static website hosting serves the content through the website endpoint.

## What I Learned

This lab gave me practice using the AWS CLI to manage an S3 bucket instead of doing every step in the console. I also got to use IAM to create a separate user for the S3 tasks.

The deployment script was a useful addition. Rather than repeating the upload command manually every time the website changes, I could run the script and let `aws s3 sync` handle the transfer.

I also saw that hosting a static website on S3 involves more than uploading the files: the bucket needs static website hosting enabled, and the objects need permissions that allow the intended access.

## AWS Services and Tools

- **Amazon S3** — stores the website files and hosts the static website.
- **AWS IAM** — provides the user and permissions used for the S3 tasks.
- **AWS CLI** — creates the bucket and uploads the website files.
- **Bash** — runs the reusable deployment script.
