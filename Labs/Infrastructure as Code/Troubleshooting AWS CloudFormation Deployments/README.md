# Troubleshooting AWS CloudFormation Deployments

## Overview

This lab focused on troubleshooting AWS CloudFormation deployments from the command line. I worked through a failed stack creation, traced the failure from a CloudFormation WaitCondition to an EC2 bootstrap script, corrected the underlying template, and redeployed the stack successfully.

The lab then introduced configuration drift by changing a security group outside CloudFormation. I used CloudFormation drift detection to identify the modified resource and the specific SSH ingress change. Finally, I worked through a failed stack deletion caused by an S3 bucket containing an object and used resource retention to remove the stack while preserving the bucket for controlled cleanup.

## Technical Context

CloudFormation manages infrastructure from a declared template, but a stack failure does not always expose the underlying cause. In this exercise, the initial failure appeared as a WaitCondition timeout. Investigating the EC2 instance and its cloud-init output showed that the bootstrap script had stopped before it could send the expected CloudFormation signal.

The lab also demonstrated that infrastructure managed by CloudFormation can drift from its declared configuration when resources are changed manually. CloudFormation drift detection can identify the affected resource and provide details about the differences.

## Troubleshooting the Failed Deployment

The initial CloudFormation deployment reached a rollback state after the WaitCondition timed out. The stack event showed that the WaitCondition had received zero signals when one was expected.

Rather than allowing the failed resources to disappear, I recreated the stack with `DO_NOTHING` so the EC2 instance could be investigated directly.

![CloudFormation stack failure with resources retained](screenshots/01-CloudFormation-stack-failure-with-resources-retained.png)

### Investigating the EC2 bootstrap process

The EC2 instance was accessed through SSH and the cloud-init output was inspected with elevated permissions:

```bash
sudo tail -50 /var/log/cloud-init-output.log
```

The log showed:

```text
+ yum install -y http
No package http available.
Error: Nothing to do
Failed running /var/lib/cloud/instance/scripts/part-001 [1]
```

I then inspected the bootstrap script itself:

```bash
sudo cat /var/lib/cloud/instance/scripts/part-001
```

The script attempted to install `http`, while the later commands configured and started `httpd` and sent the CloudFormation signal.

The script began with:

```bash
#!/bin/bash -ex
```

Because the package installation failed, the script stopped before reaching the `cfn-signal` command. The resulting chain was:

```text
Invalid package name: http
        ↓
yum installation failed
        ↓
Bootstrap script stopped
        ↓
cfn-signal was never sent
        ↓
WaitCondition timed out
        ↓
CloudFormation deployment failed
```

![EC2 cloud-init log reveals invalid http package](screenshots/02-EC2-cloud-init-log-reveals-invalid-http-package.png)

### Correcting the template

I corrected the package installation command in the CloudFormation template:

```bash
yum install -y httpd
```

The correction was verified with:

```bash
cat template1.yaml | grep httpd
```

The corrected template was redeployed and the resources reached `CREATE_COMPLETE`.

![CloudFormation corrected stack resources created successfully](screenshots/03-CloudFormation-corrected-stack-resources-created-successfully.png)

The CloudFormation outputs provided the S3 bucket name and EC2 public IP. I opened the deployed web server and verified that it returned:

```text
Hello from your web server!
```

This confirmed that the template correction resolved the deployment failure.

## CloudFormation Drift

After the successful deployment, I manually changed the WebServerSG inbound SSH rule from:

```text
0.0.0.0/0
```

to the user's IP address.

I then created an object in the CloudFormation-managed S3 bucket and used the AWS CLI to inspect the stack and its resources.

![CloudFormation drift detected in security group](screenshots/04-CloudFormation-drift-detected-in-security-group.png)

### Detecting drift

Drift detection was initiated with:

```bash
aws cloudformation detect-stack-drift --stack-name myStack
```

The completed detection reported:

```text
StackDriftStatus: DRIFTED
DetectionStatus: DETECTION_COMPLETE
DriftedStackResourceCount: 1
```

I queried the stack resources and found that the security group was `MODIFIED` while the S3 bucket remained `IN_SYNC`.

### Identifying the change

Resource-level drift information showed that the SSH ingress source had changed from the template's `0.0.0.0/0` value to the user's IP address in the live security group.

This provided a clear comparison between the declared CloudFormation configuration and the actual AWS resource.

I also attempted to update the stack using the unchanged template. CloudFormation returned:

```text
No updates are to be performed
```

This demonstrated that detecting drift does not by itself create a template update for CloudFormation to apply; the declared template had not changed.

## Troubleshooting Stack Deletion

A normal stack deletion failed because the S3 bucket still contained the object `myfile`.

I first identified the S3 bucket's CloudFormation logical ID:

```bash
aws cloudformation describe-stack-resources \
  --stack-name myStack \
  --query "StackResources[?ResourceType == 'AWS::S3::Bucket'].LogicalResourceId" \
  --output text
```

The logical ID was:

```text
MyBucket
```

I then deleted the stack while retaining that resource:

```bash
aws cloudformation delete-stack \
  --stack-name myStack \
  --retain-resources MyBucket
```

The stack was removed while the bucket and its object remained available for cleanup.

![CloudFormation stack deleted while S3 bucket retained](screenshots/05-CloudFormation-stack-deleted-while-S3-bucket-retained.png)

I subsequently removed the retained S3 bucket and its contents manually:

```bash
aws s3 rb s3://mystack-mybucket-msdsdlihmsvf/ --force
```

Final checks confirmed that the CloudFormation stack and S3 bucket had been removed.

## Key Technical Takeaways

- A CloudFormation failure can require investigation beyond the stack-level error message.
- Preserving failed resources can make it possible to inspect the underlying cause.
- EC2 cloud-init logs can reveal failures in CloudFormation-managed bootstrap scripts.
- A failed command in a script using `bash -e` can prevent later commands, including CloudFormation signaling, from running.
- CloudFormation drift detection identifies differences between declared and live resource configuration.
- Resource-level drift information can expose the specific property that changed.
- A stack update using an unchanged template does not automatically reconcile a manually modified resource.
- S3 objects can prevent CloudFormation from deleting a bucket during stack deletion.
- `--retain-resources` can be used to remove a stack while preserving a specified resource for separate cleanup.

## Skills Demonstrated

- AWS CloudFormation
- AWS CLI
- JMESPath queries
- CloudFormation stack event analysis
- EC2 cloud-init troubleshooting
- Linux command-line investigation
- CloudFormation drift detection
- Resource-level configuration analysis
- CloudFormation stack lifecycle management
- Root-cause analysis and iterative troubleshooting
