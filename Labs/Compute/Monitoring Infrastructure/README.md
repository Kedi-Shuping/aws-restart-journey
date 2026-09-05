# Monitoring Infrastructure

## Overview

In this lab, I configured monitoring for an Apache web server running on an Amazon EC2 instance. The work covered system monitoring, application log collection, custom metrics, alarms and notifications, instance state-change notifications, and AWS Config rules.

I worked through the monitoring setup by connecting the different AWS services and then testing the notifications and metrics to confirm that they were working as expected.

## AWS Services and Tools Used

- Amazon EC2
- AWS Systems Manager
- AWS Systems Manager Parameter Store
- Amazon CloudWatch
- Amazon SNS
- Amazon EventBridge
- AWS Config
- Apache HTTP Server

## Project Workflow

1. Installed the Amazon CloudWatch Agent on the EC2 web server using Systems Manager Run Command.
2. Stored the CloudWatch Agent configuration in Systems Manager Parameter Store and configured the agent to collect Apache logs and system metrics.
3. Generated a 404 response from the web server and used CloudWatch Logs to confirm that the request was recorded.
4. Created a CloudWatch metric filter and alarm to count 404 errors and send an SNS notification when the threshold was reached.
5. Inspected CloudWatch Agent metrics for disk usage and memory usage to see information from inside the EC2 operating system.
6. Created an EventBridge rule to detect EC2 instances entering the `stopped` or `terminated` state and send an SNS notification.
7. Configured AWS Config rules to check EC2-related resources for required tags and volume usage.

## Technical Context

The main monitoring points were:

- **CloudWatch Agent:** The agent collected Apache access and error logs as well as CPU, disk, memory, and swap metrics from inside the EC2 instance.
- **CloudWatch Logs and Metrics:** Logs were used to investigate web requests, while a metric filter converted matching 404 log entries into a numeric metric that could be monitored by an alarm.
- **SNS:** SNS delivered email notifications when the 404 alarm threshold was reached and when the EventBridge rule detected an EC2 state change.
- **EventBridge:** The rule matched EC2 state-change events for both `stopped` and `terminated` states.
- **AWS Config:** Config rules evaluated resources for the required `project` tag and checked whether EBS volumes were in use.

## Troubleshooting

### CloudWatch Alarm Statistic

The 404 alarm initially remained in the OK state even after generating multiple 404 responses. I found that the alarm was using the Average statistic instead of Sum. Since the metric filter added a value of `1` for each matching 404 event, changing the statistic to Sum allowed the alarm to count the errors correctly. The alarm then entered the ALARM state and sent the SNS notification.

### EventBridge Rule Creation

EventBridge initially failed when I tried to create the rule. The console showed that AWS was attempting to create an IAM role, but the lab environment did not allow that action. Changing the configuration to use the SNS topic without an execution role allowed the rule to be created successfully.

After the EC2 instance was stopped, EventBridge detected the state change and SNS sent the notification as expected. The instance was later terminated during the lab teardown, which triggered a second notification. This confirmed that the rule was matching both `stopped` and `terminated` states.

## Verification

The monitoring configuration was tested at several levels:

- CloudWatch Logs recorded the generated 404 request.
- The 404 metric filter produced a metric that could be used by a CloudWatch alarm.
- The alarm reached the ALARM state after the configured threshold was exceeded and an SNS email was received.
- CloudWatch Agent metrics showed disk and memory information from inside the EC2 instance.
- EventBridge successfully triggered SNS notifications for both stopped and terminated EC2 states.
- AWS Config evaluated the configured rules and showed compliant and noncompliant resources.

## Screenshots

### CloudWatch Agent Configuration

![CloudWatch Agent configuration completed successfully](screenshots/01-cloudwatch-agent-configuration.png)

The CloudWatch Agent was configured through Systems Manager using the configuration stored in Parameter Store.

### CloudWatch Alarm and SNS Notification

![CloudWatch alarm notification for 404 errors](screenshots/02-cloudwatch-alarm-sns-notification.png)

The 404 alarm entered the ALARM state after the threshold was exceeded and SNS delivered the notification by email.

### CloudWatch Agent Disk Metrics

![CloudWatch Agent disk metrics](screenshots/03-cwagent-disk-metrics.png)

The CWAgent metrics showed filesystem information collected from inside the EC2 operating system.

### CloudWatch Agent Memory Metrics

![CloudWatch Agent memory metrics](screenshots/04-cwagent-memory-metrics.png)

The memory metric showed the percentage of memory being used by the EC2 host over time.

### EventBridge EC2 State Change Notifications

![EventBridge EC2 state change notification](screenshots/05-eventbridge-state-change-notifications.png)

The EventBridge rule matched EC2 state changes and SNS delivered notifications for both stopped and terminated states.

### AWS Config Rules

![AWS Config rules overview](screenshots/06-aws-config-rules.png)

The AWS Config rules evaluated resources for the required `project` tag and EBS volume usage.

### AWS Config Compliant Resource

![AWS Config required-tags compliant Web Server](screenshots/07-aws-config-compliant-web-server.png)

The Web Server instance was shown as compliant with the required `project` tag.

## Skills Demonstrated

- Configuring the CloudWatch Agent on an EC2 instance using Systems Manager
- Using Parameter Store to manage monitoring configuration
- Collecting and investigating Apache web server logs
- Creating CloudWatch metric filters and alarms
- Understanding CloudWatch metric statistics when counting log events
- Configuring SNS notifications
- Creating and troubleshooting EventBridge event patterns and targets
- Monitoring EC2 state changes
- Using AWS Config rules to evaluate resource configuration
- Troubleshooting AWS service configuration and permission issues
- Connecting logs, metrics, events, and notifications into a monitoring workflow
