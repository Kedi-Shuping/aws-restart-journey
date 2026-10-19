# Project 2 — 3D E-Commerce Platform Architecture on AWS

## Project brief

Design an AWS cloud architecture for a global 3D e-commerce application where customers can interact with 3D product models before purchasing. The platform is expected to serve millions of users and must be fast, highly available, secure, scalable, and cost-efficient.

This is an **architecture design project**. The deliverables are an architecture diagram and a 1–2 page rationale; this README does not imply that the proposed system has been deployed.

## Requirements

The design must address all five requirements in the brief:

1. **High availability** — 24/7 availability, fault tolerance, and failover.
2. **Scalability** — accommodate unpredictable traffic spikes.
3. **Performance** — fast page loads, responsive 3D content, and smooth product rendering.
4. **Security** — follow AWS security best practices.
5. **Cost optimization** — avoid over-provisioning and use appropriate scaling, managed services, and monitoring.

## AWS services named in the brief

The architecture should consider:

- Amazon S3 — storage for 3D assets.
- Amazon CloudFront — content delivery.
- Amazon EC2 and/or AWS Lambda — backend compute.
- Amazon RDS and/or Amazon DynamoDB — product and customer data.
- Elastic Load Balancing — traffic distribution.
- Amazon Route 53 — DNS and domain management.
- Amazon CloudWatch and AWS Trusted Advisor — monitoring and optimization.

Service selection should be justified by the workload and requirements rather than including services without a clear purpose.

## Deliverables

- [ ] AWS architecture diagram.
- [ ] A 1–2 page explanation of the service choices.
- [ ] Explanation of how the design addresses all five requirements.
- [ ] Design trade-offs and challenges.

## Project files

Add the final architecture diagram and rationale document to this folder when they are ready. Keep supporting research and drafts clearly identified as working material.
