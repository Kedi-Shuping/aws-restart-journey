# Challenge Lab: Amazon S3

## Overview

This challenge lab focused on creating an Amazon S3 bucket, uploading an object, making the **object** publicly accessible, accessing it through a web browser, and verifying the bucket contents with the AWS CLI.

The challenge intentionally required determining how to make an object public rather than providing the exact configuration steps.

## Objectives

- Create an Amazon S3 bucket.
- Upload an object into the bucket.
- Access the object using a web browser.
- Make the object, rather than the bucket, publicly accessible.
- List the contents of the S3 bucket using the AWS CLI.

## AWS Services and Tools

- Amazon S3
- AWS CLI
- Amazon EC2 / EC2 Instance Connect
- IAM and S3 access controls

## Architecture

```text
AWS CLI / Linux CLI Host
        |
        v
Amazon S3 Bucket
        |
        v
Object (hello.txt)
        |
        v
Public object access
        |
        v
Web Browser
```

## Project Workflow

1. Connected to the provisioned CLI Host through EC2 Instance Connect.
2. Configured the AWS CLI for the `us-west-2` region.
3. Created an S3 bucket.
4. Uploaded `hello.txt` to the bucket.
5. Attempted to access the object through a browser.
6. Troubleshot the permissions preventing public object access.
7. Disabled the relevant Block Public Access setting and changed Object Ownership to support the required ACL workflow.
8. Applied a `public-read` ACL to the object.
9. Verified that the object was accessible through its public URL.
10. Listed the bucket contents using the AWS CLI.

## Troubleshooting

The initial `put-object-acl` operation failed because S3 Block Public Access was preventing the public ACL from being applied.

The issue was resolved by changing the bucket's public-access and Object Ownership configuration so that the required object-level ACL could be used.

This demonstrated an important distinction:

```text
Block Public Access = OFF
            |
            v
Public access mechanisms are no longer automatically blocked
            |
            v
An explicit permission (such as a public-read ACL) is still required
```

Turning Block Public Access off did **not** by itself make the object public; the object still needed an appropriate permission.

## Skills Demonstrated

- S3 bucket creation and management
- AWS CLI fundamentals
- Object uploads
- S3 object permissions
- Block Public Access
- Object Ownership
- Access Control Lists (ACLs)
- Public object access
- Troubleshooting S3 permission errors
- Browser and CLI verification

## Key Commands

```bash
aws configure
aws s3 mb s3://<bucket-name> --region us-west-2
aws s3 cp hello.txt s3://<bucket-name>/
aws s3api put-object-acl --bucket <bucket-name> --key hello.txt --acl public-read
aws s3 ls s3://<bucket-name>/
```

## What I Learned

This challenge reinforced that S3 public access is controlled by multiple layers. Block Public Access can prevent public ACLs from being used, while Object Ownership determines whether ACL-based access control is available. The challenge also demonstrated how to troubleshoot an S3 permission failure instead of treating the error as a simple command problem.

## Evidence

Screenshots from the original lab are retained as portfolio evidence, including the bucket creation, ACL permission error, bucket verification, public URL verification, and updated permission configuration.
