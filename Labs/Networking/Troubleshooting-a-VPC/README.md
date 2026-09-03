# Troubleshooting a VPC

## Overview

AWS re/Start hands-on lab focused on diagnosing and repairing VPC connectivity problems using layered network reasoning and VPC Flow Logs.

The lab involved two separate connectivity failures affecting the same EC2 web server. Rather than treating the symptoms as isolated problems, the investigation followed the packet through the VPC networking layers and used evidence to identify the failing control.

## Objectives

- Create and verify VPC Flow Logs.
- Troubleshoot VPC and network configuration.
- Analyze VPC Flow Logs to identify rejected traffic.
- Correlate observed traffic with AWS networking configuration.

## AWS Services / Components

- Amazon VPC
- Amazon EC2
- VPC Flow Logs
- Amazon S3
- Internet Gateway
- Route Tables
- Network ACLs
- Security Groups
- AWS CLI

## Incident 1 — Web Server HTTP Access Failed

### Problem

The web server's public IP did not load in a browser. Initial network testing showed the host was not responding normally, while `nmap -Pn` showed the host was reachable but the scanned ports were filtered.

### Initial hypothesis

Security Group rules were considered first because TCP/80 access was failing.

### Investigation / evidence

The web server Security Group already allowed inbound TCP/80 and TCP/22 from `0.0.0.0/0`, so the Security Group did not explain the HTTP failure.

The associated public subnet route table contained only the VPC local route and was missing the default route to the Internet Gateway.

### Root cause

The subnet had no `0.0.0.0/0` route pointing to the Internet Gateway. The instance therefore had no routing path for Internet-bound traffic.

### Fix

Added the default route to the Internet Gateway:

```bash
aws ec2 create-route \
  --route-table-id rtb-0bc3c3b4dbd119f8e \
  --destination-cidr-block 0.0.0.0/0 \
  --gateway-id igw-041b735629c399b76
```

### Verification

The web server subsequently loaded successfully and returned:

> Hello From Your Web Server!

## Incident 2 — SSH Access Failed

### Problem

HTTP access was restored, but EC2 Instance Connect / SSH access to the web server still failed.

### Investigation / evidence

The subnet's Network ACL contained an explicit inbound rule denying TCP/22 from `0.0.0.0/0`.

Network ACL rules are evaluated in ascending rule-number order, with the first matching rule taking effect. The explicit deny therefore matched SSH traffic before the later broad allow rule could apply.

### Root cause

Inbound Network ACL rule 40 denied TCP port 22.

### Fix

Removed the offending rule:

```bash
aws ec2 delete-network-acl-entry \
  --network-acl-id acl-07db8c039c58ab5c3 \
  --rule-number 40 \
  --ingress
```

### Verification

EC2 Instance Connect / SSH succeeded, and the remote host confirmed its identity:

```text
[ec2-user@web-server ~]$ hostname
web-server
```

## Flow Log Forensics

After enabling VPC Flow Logs and confirming delivery to S3, the log files were retrieved from the bucket and inspected from the CLI Host.

A broad text search initially produced false positives because the string `22` can occur inside unrelated port numbers or other fields. The investigation was refined to an exact destination-port and action filter:

```bash
awk '$7 == 22 && $13 == "REJECT" {print}' *.log
```

This exposed the relevant rejected SSH records:

```text
2 388245325342 eni-04de19ecd5eb08234 35.161.200.46 10.0.1.21 44376 22 6 1 60 1788426218 1788426248 REJECT OK
2 388245325342 eni-04de19ecd5eb08234 35.161.200.46 10.0.1.21 44382 22 6 1 60 1788426218 1788426248 REJECT OK
```

The records showed:

- Source: `35.161.200.46` (CLI Host)
- Destination: `10.0.1.21` (Web Server private IP)
- Destination port: `22`
- Protocol: TCP (`6`)
- Action: `REJECT`
- ENI: `eni-04de19ecd5eb08234`
- Time window: `09:03:38–09:04:08 UTC`

The ENI was then correlated to the web server using AWS CLI, confirming that it belonged to the EC2 instance with private IP `10.0.1.21`.

### Important forensic distinction

VPC Flow Logs report observed network traffic and whether it was accepted or rejected; they do not directly state that a particular Network ACL rule caused the rejection. Root cause was established by correlating the rejected TCP/22 records with the NACL configuration, removing the matching deny rule, and successfully repeating the SSH connection.

## Packet Path

```text
CLI Host
  │
  │ TCP/22
  ▼
Web Server ENI
  │
  ├── Network ACL → explicit TCP/22 DENY (Rule 40)
  │
  └── Flow Log → REJECT

After removing Rule 40:

CLI Host
  │
  │ TCP/22
  ▼
Web Server ENI
  │
  └── Network ACL → traffic permitted
                    ↓
                 SSH succeeds
```

## What This Lab Demonstrated

- A route table determines where traffic is routed; it does not authorize traffic.
- A Network ACL is a subnet-level, stateless traffic filter.
- A Security Group is an instance-level, stateful traffic filter.
- Route tables, NACLs, and Security Groups solve different parts of the packet's journey.
- VPC Flow Logs are metadata about observed network flows, not packet captures.
- Broad searches can create misleading forensic results; filtering on exact fields produces stronger evidence.
- Network troubleshooting is more reliable when the packet path is followed layer by layer.

## Key Lesson

The most important skill demonstrated was not memorizing AWS console steps. It was using observable evidence to move from symptom → hypothesis → diagnostic test → root cause → targeted fix → verification.

## Portfolio Evidence

Screenshots documenting the investigation and verification are included with this lab where available.

1. Initial `nmap` host discovery and filtered-port evidence
2. Route table showing the missing Internet Gateway route
3. Web server restored after the route fix
4. NACL showing the explicit SSH deny rule
5. Successful SSH verification (`hostname` → `web-server`)
6. VPC Flow Log evidence showing rejected TCP/22 traffic from the CLI Host to the Web Server
