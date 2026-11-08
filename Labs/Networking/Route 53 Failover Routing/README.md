# Route 53 Failover Routing

## Overview

This lab demonstrated DNS failover for a café website hosted on two EC2 web servers in separate Availability Zones within the same AWS Region.

The primary website was hosted at `44.238.1.18` in `us-west-2a`. When its Route 53 health check changed from **Healthy** to **Unhealthy**, the café website was subsequently accessible from the secondary server at `52.41.137.204` in `us-west-2b`.

The exercise demonstrated how Route 53 failover routing can direct DNS responses away from an unhealthy primary endpoint and toward a secondary endpoint.

## Architecture and Service Roles

- **Amazon Route 53 hosted zone:** stored the DNS records used to route requests to the café website.
- **Failover routing records:** identified the primary and secondary endpoints for the same DNS name.
- **Route 53 health check:** monitored the primary website endpoint and reported its health status.
- **Amazon SNS:** provided the notification topic associated with the primary website health monitoring.
- **Amazon CloudWatch:** supports alarm and notification workflows for monitored health-check status.

The two web servers were deployed in separate Availability Zones, `us-west-2a` and `us-west-2b`, within **US West (Oregon), `us-west-2`**. This was an Availability Zone failover exercise, not a multi-Region deployment.

## Configuration Context

The lab instructions called for:

- A primary café website endpoint at `44.238.1.18` in `us-west-2a`.
- A secondary café website endpoint at `52.41.137.204` in `us-west-2b`.
- Route 53 failover records using PRIMARY and SECONDARY roles.
- A health check named `Primary-Website-Health` for the primary website.
- A health-check request path of `/cafe`.
- An SNS topic named `Primary-Website-Health` for health-related notifications.

The captured health-check creation form does not visibly establish the saved request path. The captured secondary-record form also appears to show the primary health-check ID selected, whereas the lab instructions say to leave the secondary record's health-check association blank. The final saved record configuration was not captured, so these two settings are not presented here as verified final-state facts.

## Failover Demonstration

The screenshots captured the important stages of the exercise:

1. The café website was accessible from the primary endpoint, `44.238.1.18`, in `us-west-2a`.
2. The primary health check changed from **Healthy** to **Unhealthy**.
3. The café website was subsequently accessible from the secondary endpoint, `52.41.137.204`, in `us-west-2b`.

This sequence demonstrates the observed failover behaviour between the two Availability Zones.

## Notifications

The SNS subscription confirmation email for the `Primary-Website-Health` topic was received on **19 August 2026 at 4:38 PM**. I confirmed the subscription using the email link.

The lab instructions also expected an alarm notification email with a subject beginning `ALARM: Primary-Website-Health-awsroute53-`. That specific notification email was not recovered, so successful delivery of the alarm email is not claimed as screenshot-verified evidence.

## Evidence and Verification

The portfolio evidence focuses on the key outcomes rather than documenting every console action:

- Primary café website responding from the first Availability Zone.
- Route 53 health-check status changing from **Healthy** to **Unhealthy**.
- Café website responding from the secondary Availability Zone.
- Relevant Route 53 and health-check configuration screens, where the captured details are legible.

The observed website failover is supported by the captured sequence. The exact saved health-check path and final secondary-record health-check association remain unverified.

## Skills Demonstrated

- Configuring DNS failover routing with Amazon Route 53
- Understanding PRIMARY and SECONDARY failover record roles
- Using health checks to evaluate endpoint availability
- Deploying and comparing web endpoints across Availability Zones
- Observing DNS failover behaviour when a primary endpoint becomes unhealthy
- Integrating Amazon SNS into a monitoring and notification workflow
- Distinguishing Availability Zone resilience from multi-Region architecture

## Key Takeaway

This lab demonstrated how Route 53 failover routing can improve application availability by directing DNS queries to a secondary endpoint when the primary endpoint is unhealthy.

The practical result was a café website that became accessible from the secondary Availability Zone after the primary health check reported an unhealthy endpoint. The exercise connected DNS routing, endpoint health monitoring, and notification services in a working failover scenario.
