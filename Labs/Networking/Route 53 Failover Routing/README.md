# Route 53 Failover Routing

## Overview

In this lab, I configured Amazon Route 53 failover routing for a café website hosted on two EC2 instances in separate Availability Zones.

The primary website was hosted at `44.238.1.18` in `us-west-2a`, with a secondary website at `52.41.137.204` in `us-west-2b`. I used a Route 53 health check to monitor the primary endpoint and observed what happened when its status changed from **Healthy** to **Unhealthy**.

The café website subsequently loaded from the secondary endpoint. This gave me a practical look at how Route 53 can use health checks and failover records to direct DNS responses away from an unhealthy primary endpoint.

## AWS Services and Components Used

- Amazon Route 53
- Amazon EC2
- Amazon SNS
- Amazon CloudWatch
- Route 53 Health Checks
- Failover Routing Records
- Availability Zones

## Architecture

Both web servers were deployed in **US West (Oregon), `us-west-2`**, but in different Availability Zones.

```text
                 Café website DNS name
                          |
                          v
                    Amazon Route 53
                          |
                 Failover routing records
                    /             \
                   /               \
             PRIMARY             SECONDARY
                |                    |
                v                    v
          Primary EC2           Secondary EC2
          us-west-2a            us-west-2b
          44.238.1.18           52.41.137.204
                |
                v
        Route 53 health check
                |
        Healthy / Unhealthy
```

The health check monitored the primary website endpoint. When the primary became unhealthy, the failover configuration allowed Route 53 to use the secondary endpoint.

This was **Availability Zone failover within one Region**, not a deployment across two AWS Regions.

## Project Workflow

1. Worked with the café website hosted on the primary EC2 instance in `us-west-2a`.
2. Identified the secondary café website hosted in `us-west-2b`.
3. Created a Route 53 hosted zone and configured failover routing records for the café website.
4. Created the `Primary-Website-Health` health check for the primary endpoint.
5. Configured the SNS topic used for health-related notifications.
6. Confirmed the SNS email subscription through the confirmation link sent by AWS Notifications.
7. Tested the primary endpoint and observed its health-check status.
8. Observed the health check change from **Healthy** to **Unhealthy**.
9. Refreshed the café website and observed it loading from the secondary endpoint in the other Availability Zone.

## Failover Demonstration

The primary café website was initially served from `44.238.1.18` in `us-west-2a`. When the primary health check changed to **Unhealthy**, Route 53 failed over to the secondary website at `52.41.137.204` in `us-west-2b`.

I was able to access the café website through the secondary instance after the primary health check failed. This was the result I was looking for: traffic was directed away from the unhealthy primary endpoint and the secondary endpoint took over.

## Health Checks and Notifications

The health check was named `Primary-Website-Health`. The lab instructions specified the `/cafe` request path for the health check, but the captured creation form does not show the path value. I therefore cannot verify the final saved path from the available screenshot.

The captured secondary-record form also appears to show the primary health-check ID selected. The lab instructions say to leave the secondary record's health-check association blank. There is no screenshot of the final saved record, so I have not treated that setting as confirmed.

The SNS email subscription confirmation for `Primary-Website-Health` was received on **19 August 2026 at 4:38 PM**, and I confirmed the subscription using the link in the email. The separate alarm notification expected by the lab was not recovered from the inbox, so I have not used it as evidence of successful alarm-email delivery.

## Screenshots

### Primary Café Website

The café page was accessible from the primary endpoint, `44.238.1.18`, in `us-west-2a`.

![Primary café website](screenshots/01-primary-cafe-website.png)

### Primary Health Check

The health-check evidence shows the primary endpoint changing from **Healthy** to **Unhealthy**.

![Primary health check status](screenshots/02-primary-health-check-unhealthy.png)

### Secondary Café Website

After the primary endpoint became unhealthy, the café page loaded from the secondary endpoint, `52.41.137.204`, in `us-west-2b`.

![Secondary café website](screenshots/03-secondary-cafe-website.png)

## Skills Demonstrated

- Configured DNS failover routing with Amazon Route 53
- Worked with PRIMARY and SECONDARY failover records
- Created and monitored a Route 53 health check
- Used health status to understand endpoint availability
- Tested website availability across two Availability Zones
- Integrated Amazon SNS into a notification workflow
- Distinguished Availability Zone failover from multi-Region deployment
- Verified failover through the application endpoint, not just the console configuration

## Key Lessons Learned

This lab helped connect DNS routing with application availability. A secondary server is useful only when the routing configuration can direct users to it when the primary endpoint is unhealthy.

It was also useful to see the difference between deploying resources in separate Availability Zones and deploying across separate AWS Regions. Both can support resilience, but this exercise used two Availability Zones within `us-west-2`.

The clearest evidence was the change from the primary café website to the secondary one after the health check reported an unhealthy endpoint.
