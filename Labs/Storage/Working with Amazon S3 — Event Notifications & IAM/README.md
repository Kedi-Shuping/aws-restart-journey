# Working with Amazon S3 — Event Notifications & IAM

## Overview

This AWS re/Start lab focused on using Amazon S3 through the AWS CLI, controlling access to objects with IAM, and building an event-driven notification workflow with Amazon SNS.

The lab used an S3 bucket as an image-sharing location for a restricted IAM user (`mediacouser`). S3 was configured to publish object creation and removal events to an SNS topic, which delivered notifications by email.

## Objectives

- Create and configure an Amazon S3 bucket using the AWS CLI.
- Upload and verify objects in Amazon S3.
- Inspect and test IAM permissions for a restricted user.
- Configure Amazon S3 event notifications.
- Publish S3 events to an Amazon SNS topic.
- Verify event delivery through email.
- Test both permitted and denied object operations.

## AWS Services and Tools

- Amazon S3
- AWS IAM
- Amazon SNS
- AWS CLI
- Amazon EC2 / EC2 Instance Connect

## Architecture

```text
                         Object events
                              |
                              v
                    +-------------------+
                    |   Amazon S3        |
                    | cafe-kedi-20260903 |
                    +---------+---------+
                              |
                 ObjectCreated / ObjectRemoved
                              |
                              v
                    +-------------------+
                    |   Amazon SNS       |
                    | s3NotificationTopic|
                    +---------+---------+
                              |
                     Confirmed subscription
                              |
                              v
                         Email inbox
```

## Access Model

The lab used two identities for different purposes.

### Lab / administrative identity

The initial CLI identity was used to create and configure the S3 bucket and notification infrastructure.

### `mediacouser`

A restricted IAM user was used to test application-style object access. The policy allowed object operations such as `PutObject`, `GetObject`, and `DeleteObject` under the required S3 path, while bucket administration permissions were not granted.

The restriction was verified in the S3 console when `mediacouser` was unable to retrieve bucket-level configuration such as the bucket policy and Object Ownership settings.

## Project Workflow

1. Connected to the CLI Host using EC2 Instance Connect.
2. Configured the AWS CLI for `us-west-2`.
3. Created the S3 bucket `cafe-kedi-20260903`.
4. Uploaded the initial image set under the `images/` prefix.
5. Inspected the IAM group and policy associated with `mediacouser`.
6. Created access keys for `mediacouser` and securely retained the credentials.
7. Verified `mediacouser` could view, upload, and delete permitted objects but could not administer the bucket.
8. Created the SNS topic `s3NotificationTopic`.
9. Added an SNS topic resource policy allowing Amazon S3 to publish notifications from the lab bucket.
10. Created and confirmed an email subscription to the SNS topic.
11. Created an S3 notification configuration for `images/` that listens for object creation and removal events.
12. Applied the notification configuration to the S3 bucket using `put-bucket-notification-configuration`.
13. Verified the complete S3 → SNS → email event path with real object operations.
14. Tested an unauthorized public ACL operation and received `AccessDenied`.
15. Ended the temporary lab environment after the evidence was captured.

## Event Notification Configuration

The S3 notification configuration was designed to publish these event families for objects under `images/`:

```text
s3:ObjectCreated:*
s3:ObjectRemoved:*
```

The CLI configuration was applied with:

```bash
aws s3api put-bucket-notification-configuration \
  --bucket cafe-kedi-20260903 \
  --notification-configuration file://s3EventNotification.json
```

## CLI Verification Tests

The lab deliberately tested three different object operations to prove that event filtering was working as intended.

| Operation | Result | Notification |
|---|---|---|
| PUT `images/Caramel-Delight.jpg` | Allowed | `ObjectCreated:Put` email received |
| GET `images/Donuts.jpg` | Allowed | No notification |
| DELETE `images/Strawberry-Tarts.jpg` | Allowed | `ObjectRemoved:Delete` email received |
| `PutObjectAcl --acl public-read` | Denied | `AccessDenied` |

### Object creation

```bash
aws s3api put-object \
  --bucket cafe-kedi-20260903 \
  --key images/Caramel-Delight.jpg \
  --body ~/new-images/Caramel-Delight.jpg
```

S3 accepted the upload and an SNS email notification showed `ObjectCreated:Put` for `images/Caramel-Delight.jpg`.

### Object retrieval

```bash
aws s3api get-object \
  --bucket cafe-kedi-20260903 \
  --key images/Donuts.jpg \
  Donuts.jpg
```

The object was retrieved successfully. No notification was generated because GET was not included in the S3 event configuration.

### Object deletion

```bash
aws s3api delete-object \
  --bucket cafe-kedi-20260903 \
  --key images/Strawberry-Tarts.jpg
```

The object was deleted successfully and an SNS email notification showed `ObjectRemoved:Delete` for `images/Strawberry-Tarts.jpg`.

### Unauthorized public ACL attempt

```bash
aws s3api put-object-acl \
  --bucket cafe-kedi-20260903 \
  --key images/Donuts.jpg \
  --acl public-read
```

The operation failed with `AccessDenied`. The AWS response identified the missing `s3:PutObjectAcl` authorization and also reported that public ACLs were prevented by the S3 Block Public Access `BlockPublicAcls` setting.

This demonstrated that a successful object workflow does not imply permission to change the object's public-access configuration.

## Troubleshooting

During notification setup, the S3 event notification JSON was initially placed in the SNS topic access-policy editor. These are two different policy/configuration mechanisms.

The configuration was corrected by restoring the SNS resource policy so that S3 was explicitly allowed to publish to the topic, then applying the event notification JSON separately to the S3 bucket with `put-bucket-notification-configuration`.

The successful test notification confirmed that the corrected configuration was functioning.

## Security Observations

The lab demonstrated several layers of access control:

```text
IAM permissions
      |
      v
What mediacouser is allowed to request
      |
      v
S3 bucket/object controls
      |
      v
Block Public Access
      |
      v
Whether a public ACL can actually be applied
```

The `mediacouser` account could work with permitted objects without receiving bucket administration privileges. The attempted `public-read` ACL was rejected rather than allowing the user to expose the object publicly.

## Portfolio Evidence

Six portfolio screenshots were captured during the lab:

1. `01-s3-bucket-creation-upload-verification.png` — bucket creation, image upload, and CLI verification.
2. `02-s3-iam-permission-boundary.png` — restricted user's bucket-level permission boundary.
3. `03-s3-sns-event-notification-configured.png` — successful application of the S3 notification configuration.
4. `04-s3-event-notification-object-created.png` — delivered `ObjectCreated:Put` notification.
5. `05-s3-event-notification-object-removed.png` — delivered `ObjectRemoved:Delete` notification.
6. `06-s3-public-acl-access-denied.png` — denied `PutObjectAcl` request and S3 Block Public Access response.

A separate teardown screenshot was retained as operational evidence showing that the temporary lab resources were terminating.

## Key Lessons

- S3 event notifications are configured on the bucket and can route matching object events to services such as SNS.
- SNS resource policies control whether a service such as S3 is allowed to publish to a topic.
- IAM permissions determine what an identity such as `mediacouser` can request.
- Event filtering matters: PUT and DELETE generated notifications while GET did not.
- Successful object access does not imply bucket administration privileges.
- S3 Block Public Access can prevent public ACLs even when an API request attempts to apply one.
- Testing both successful and intentionally denied operations provides stronger evidence of a security design than testing only the happy path.

## Outcome

The lab successfully demonstrated an event-driven S3 workflow with IAM-controlled object access and SNS email notifications, including positive and negative authorization tests.
