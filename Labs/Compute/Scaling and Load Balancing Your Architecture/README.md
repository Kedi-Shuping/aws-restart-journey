# Scaling and Load Balancing Your Architecture

## Overview

This lab brought together Amazon EC2, Elastic Load Balancing, EC2 Auto Scaling, and CloudWatch to build an architecture that can distribute traffic and respond to changing demand.

The starting point was a single web server. I created an AMI from that instance, built an Application Load Balancer and target group, then used a launch template and Auto Scaling group to run identical web servers across two Availability Zones.

## What I Built

- Created a reusable AMI from the existing web server.
- Created an Application Load Balancer across two public subnets.
- Created a target group for the application instances.
- Created a launch template using the web server AMI and Web Security Group.
- Created an Auto Scaling group spanning two private subnets.
- Set desired and minimum capacity to 2, with a maximum of 4 instances.
- Configured target tracking using average CPU utilization with a 50% target.
- Used CloudWatch alarms to observe the scaling behaviour.
- Generated application load and verified that Auto Scaling launched additional instances.

## How It Worked

The load balancer became the entry point for the application. Requests were forwarded to healthy instances registered in the target group rather than being sent directly to a particular EC2 instance.

The Auto Scaling group maintained the required capacity across the private subnets. When the application load increased, the CloudWatch alarm and target-tracking policy caused the group to add capacity. When demand was low, the same policy could scale the group back toward the desired capacity.

This was a useful example of how load balancing and scaling solve different problems: the load balancer distributes traffic, while Auto Scaling changes how much compute capacity is available.

## Architecture

```text
                         Users
                           |
                           v
                 Application Load Balancer
                    /                  \
                   v                    v
             Target Group         Target Group
                   |                    |
             EC2 Instance        EC2 Instance
                   \                    /
                    \                  /
                     Auto Scaling Group
                           |
                     CloudWatch
                 (CPU / scaling signals)
```

The lab's final architecture places the Auto Scaling instances in private subnets across two Availability Zones while the load balancer operates in the public subnets.

## Verification

I verified that:

- The AMI was created successfully.
- The Application Load Balancer was created and received traffic through its DNS name.
- Two Auto Scaling instances registered with the target group and became healthy.
- The Load Test application was reachable through the load balancer.
- Increased application load caused the high-CPU alarm to enter the **In alarm** state.
- Auto Scaling responded by launching additional instances.
- The original Web Server 1 instance could then be terminated because it was no longer needed by the running architecture.

## Screenshots

Portfolio screenshots will be added here as they are captured and uploaded.

## Skills Demonstrated

- Amazon EC2
- Amazon Machine Images (AMI)
- Elastic Load Balancing / Application Load Balancer
- EC2 target groups
- EC2 launch templates
- EC2 Auto Scaling
- Multi-AZ architecture
- Private and public subnets
- Amazon CloudWatch alarms
- Target tracking scaling policies
- Architecture verification and troubleshooting

## Key Lessons Learned

The main takeaway from this lab was seeing the services work together as one system rather than as isolated AWS features. The load balancer provides the traffic distribution layer, the target group tracks which instances can receive traffic, Auto Scaling manages the amount of compute capacity, and CloudWatch provides the monitoring and scaling signals that allow the architecture to react to demand.
