# AWS Lambda: Serverless Word Counter

## Overview

This project demonstrates a serverless, event-driven workflow using AWS Lambda, Amazon S3, and Amazon SNS.

When a text file is uploaded to an Amazon S3 bucket, an S3 event automatically invokes an AWS Lambda function. The function reads the uploaded file, counts its words, and publishes the result to an Amazon SNS topic, which delivers the notification by email.

The project demonstrates how multiple managed AWS services can be connected to automate a simple business process without maintaining a traditional application server.

## Architecture

```text
User
   │
   ▼
Amazon S3 Bucket
   │
(Object Created Event)
   │
   ▼
AWS Lambda
   │
(Counts Words)
   │
   ▼
Amazon SNS
   │
   ▼
Email Notification
```

## AWS Services and Components Used

- **Amazon S3** – Stores uploaded text files and generates the object-created event.
- **AWS Lambda** – Processes the uploaded file and counts the words.
- **Amazon SNS** – Publishes the result and delivers the notification to subscribed email recipients.
- **AWS IAM** – Provides the permissions required by the Lambda function.
- **Amazon CloudWatch Logs** – Captures Lambda execution information and supports troubleshooting.

## Project Workflow

1. Created an Amazon S3 bucket to store uploaded text files.
2. Created an Amazon SNS topic for email notifications.
3. Subscribed an email address to the SNS topic and confirmed the subscription.
4. Created an AWS Lambda function using the **Python 3.10** runtime.
5. Configured the Lambda execution role with the required IAM permissions.
6. Added the Python function that processes uploaded text files and counts their words.
7. Configured the S3 bucket to invoke Lambda when a new text file is uploaded.
8. Uploaded a sample text file to the S3 bucket.
9. Verified that the S3 event triggered the Lambda function and that the file was processed.
10. Confirmed that SNS delivered the resulting word count by email.

## Technical Context

The workflow is event-driven: the file upload is the event, Lambda is the processing layer, and SNS is the notification layer.

This removes the need for a continuously running server to watch the S3 bucket. Instead, S3 produces an event only when the relevant action occurs, and Lambda executes the processing logic in response.

IAM provides the permissions that allow the Lambda function to interact with the other AWS services, while CloudWatch Logs provides visibility into function execution when something does not behave as expected.

## Troubleshooting

During testing, the Lambda function initially returned a **500 Internal Server Error** instead of successfully processing the uploaded file.

### Investigation

I used the following checks to isolate the problem:

- Reviewed the Lambda execution logs in Amazon CloudWatch.
- Verified the IAM permissions assigned to the Lambda execution role.
- Confirmed that the Amazon SNS email subscription had been activated.
- Verified that the Amazon S3 trigger was correctly configured.

### Resolution

The problem was caused by an error in the Lambda function logic while processing the incoming event data. After correcting the function code and redeploying it, the Lambda function successfully processed uploaded files and SNS delivered the word count results by email.

## Screenshots

### Lambda Function Code

![Lambda Function Code](screenshots/02wordcount-lambda-function-code.png)

The Lambda function contains the Python code responsible for counting the words in an uploaded text file.

### Initial Function Test

![Function Test Failed](screenshots/03-wordcount-function-test-failed.png)

The initial test exposed the processing issue that was investigated using CloudWatch logs.

### Amazon S3 Trigger Configuration

![S3 Trigger](screenshots/05-wordcount-lambda-s3-trigger.png)

The Lambda function is configured with an S3 event notification that invokes it when a new text file is uploaded.

### Amazon SNS Email Notification

![SNS Email Notification](screenshots/06-wordcount-sns-email-notification.png)

After processing the uploaded file, Lambda publishes the word count to the SNS topic, which delivers the result by email.

## Skills Demonstrated

- Built and configured AWS Lambda functions
- Designed an event-driven serverless workflow
- Configured Amazon S3 event notifications
- Created and managed Amazon SNS topics and subscriptions
- Configured IAM execution roles and permissions
- Tested Lambda functions using S3 events
- Used Amazon CloudWatch Logs to troubleshoot execution issues
- Integrated multiple AWS services into a complete automated workflow

## Key Lessons Learned

The project demonstrated how event-driven architecture can connect storage, compute, and notification services into a single workflow.

It also reinforced the value of CloudWatch Logs during troubleshooting: when a Lambda invocation fails, execution logs can reveal whether the problem is related to application logic, permissions, configuration, or another part of the workflow.
