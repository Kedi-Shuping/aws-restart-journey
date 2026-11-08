# Scaling and Load Balancing Your Architecture

## Overview

This lab brought together Amazon EC2, an Application Load Balancer, EC2 Auto Scaling, and CloudWatch. I started with an existing web server, created an AMI from it, and used that image as the basis for instances managed by an Auto Scaling group.

The finished setup distributed application traffic through a load balancer and ran instances across two Availability Zones. I then generated CPU load and watched the Auto Scaling group respond.

## What I Built

- Created an AMI from the original web server.
- Configured an Application Load Balancer and target group.
- Created a launch template using the web server AMI and its security group.
- Configured an Auto Scaling group across two Availability Zones.
- Set the group's minimum and desired capacity to 2, with a maximum of 4.
- Configured target tracking for average CPU utilization with a 50% target.
- Sent load to the application and observed the scaling response.

## How the Pieces Worked Together

The Application Load Balancer provided a single entry point and forwarded requests to healthy instances registered with its target group. The Auto Scaling group managed the number of EC2 instances available to handle that traffic.

When I generated CPU load, CloudWatch reported the high-CPU condition and the target-tracking policy responded by adding capacity. The activity history recorded the desired capacity increasing from 2 to 4.

This made the difference between the services clear: the load balancer distributes requests, while Auto Scaling adjusts the amount of compute capacity available to serve them.

## Architecture

```text
                         Users
                           |
                           v
                 Application Load Balancer
                           |
                           v
                      Target Group
                      /          \
                     v            v
               EC2 Instance  EC2 Instance
                     \            /
                      \          /
                    Auto Scaling Group
                           |
                           v
                 CloudWatch metrics
                  and scaling signals
```

The load balancer operated in public subnets, while the Auto Scaling instances were placed in private subnets across two Availability Zones.

## Verification

I verified that:

- The AMI was created successfully and used as the source image for the launch template.
- The load balancer's target group had two healthy application instances across two Availability Zones.
- The load-test page generated CPU load.
- The high-CPU CloudWatch alarm entered the **In alarm** state.
- Auto Scaling Activity History recorded the desired capacity changing from **2 to 4** and the launch of additional EC2 instances.

## Screenshots

The selected screenshots focus on the configuration and the result, rather than documenting every console step.

| Screenshot | What it shows |
|---|---|
| [Launch template](screenshots/01-ec2-launch-template.png) | The reusable EC2 instance configuration and AMI selection |
| [Healthy load-balancer targets](screenshots/02-load-balancer-healthy-targets.png) | Two healthy targets across Availability Zones |
| [High-CPU alarm](screenshots/03-cloudwatch-high-cpu-alarm.png) | CloudWatch detecting CPU utilization above the 50% threshold |
| [Auto Scaling scale-out](screenshots/04-auto-scaling-scale-out.png) | Activity History recording capacity increasing from 2 to 4 |

## Skills Demonstrated

- Amazon EC2 and Amazon Machine Images
- Application Load Balancer and target groups
- EC2 launch templates and Auto Scaling groups
- Multi-AZ deployment
- Public and private subnet placement
- CloudWatch alarms and target-tracking scaling
- Load testing and verification
- CLI-based AMI creation and troubleshooting

## Key Takeaway

The main lesson was seeing these services work together as one system. The load balancer routed requests to healthy instances, while Auto Scaling added compute capacity when demand increased. CloudWatch provided the monitoring signal that helped the architecture respond.
