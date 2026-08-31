# Managing Services and Monitoring an EC2 Instance

## Lab Overview

This lab focused on managing a Linux service with `systemctl`, inspecting running processes with `top`, generating a temporary CPU workload, and observing the resulting resource usage through Amazon CloudWatch.

The work was performed on an Amazon Linux 2 EC2 instance running in AWS.

---

## Skills Demonstrated

- Inspecting Linux services with `systemctl`
- Starting and stopping the Apache HTTP Server (`httpd`)
- Interpreting service states such as `loaded`, `inactive (dead)`, and `active (running)`
- Verifying a web service from a browser using an EC2 public IP address
- Monitoring Linux processes with `top`
- Identifying CPU-intensive processes
- Generating a controlled CPU workload with a Bash script
- Monitoring EC2 metrics with Amazon CloudWatch
- Correlating an operating-system workload with CloudWatch CPU utilization
- Using terminal output and monitoring data as troubleshooting evidence

---

## Linux Service Management

The first part of the lab used `systemctl` to inspect and manage the Apache HTTP Server.

### Check service status

```bash
sudo systemctl status httpd.service
```

The service was installed and loaded but initially showed:

```text
Active: inactive (dead)
```

This demonstrates an important distinction: a service can be **installed and available** without currently being **running**.

### Start Apache

```bash
sudo systemctl start httpd.service
```

The service was then checked again:

```bash
sudo systemctl status httpd.service
```

The resulting state was:

```text
Active: active (running)
```

The status output also showed the Apache process and its worker processes running under the `httpd.service` control group.

### Verify the web server

The EC2 instance's public IP address was opened in a browser using HTTP. The Apache HTTP Server 2.4 test page was returned successfully, confirming that the service was reachable and functioning.

### Stop Apache

After verification, the service was stopped as part of the lab cleanup:

```bash
sudo systemctl stop httpd.service
```

The lab therefore demonstrated the complete service-management cycle:

**inspect → start → verify → stop**

---

## Process Monitoring with `top`

The next part of the lab introduced the Linux `top` utility.

```bash
top
```

`top` provides a live view of processes and system resource usage, including CPU and memory utilization.

The initial observation showed the instance largely idle, with CPU utilization at approximately 0%.

The workload script was then started with:

```bash
./stress.sh & top
```

This launched the workload in the background while opening `top` for live monitoring.

During the workload, multiple `stress` processes appeared near the top of the process list. The observed CPU utilization rose substantially, with the EC2 instance showing approximately 62% CPU utilization at the time of the captured observation.

The process table made the cause visible: the `stress` processes were consuming the CPU rather than the increase being an unexplained system metric.

The script was designed to run temporarily and subsequently completed, allowing the instance to return to its normal workload level.

---

## Monitoring with Amazon CloudWatch

The lab then moved from host-level monitoring to AWS-level monitoring using Amazon CloudWatch.

The CloudWatch EC2 automatic dashboard displayed metrics including:

- CPU Utilization
- DiskReadBytes
- DiskReadOps
- DiskWriteBytes
- DiskWriteOps
- NetworkIn

The CPU Utilization graph showed a clear spike corresponding to the period when the `stress.sh` workload was running. After the workload ended, CPU utilization dropped back toward the instance's normal baseline.

This provided a useful connection between two monitoring layers:

```text
Linux process
     ↓
CPU workload
     ↓
EC2 instance resource consumption
     ↓
CloudWatch CPU Utilization metric
```

The lab therefore demonstrated that CloudWatch can provide an AWS-level view of activity occurring inside an EC2 instance, while Linux tools such as `top` provide more detailed process-level evidence.

---

## Key Lessons Learned

### 1. Installed does not mean running

`systemctl status` distinguishes between a service being loaded and a service actually running. In this lab, Apache was installed and ready but initially inactive.

### 2. `start` and `enable` are different operations

Starting `httpd` made the service run immediately. The lab did not require enabling it to start automatically at boot. These are separate service-management concepts.

### 3. `top` answers "what is using the machine?"

CloudWatch can show that CPU utilization increased, but `top` can reveal the individual processes responsible. Using both provides stronger troubleshooting evidence than relying on a single monitoring layer.

### 4. Monitoring becomes more useful when correlated

The most valuable observation in this lab was not simply that CPU utilization increased. The increase could be correlated with the `stress` processes visible in `top`, and the same workload was reflected as a spike in the CloudWatch CPU Utilization metric.

### 5. Evidence does not always need to be a screenshot

For this lab, the repository documents the commands, observed states, and results directly rather than accumulating screenshots that are difficult to manage later. The emphasis is on preserving reproducible technical evidence and explaining what the evidence demonstrates.

---

## Outcome

Successfully managed the Apache HTTP Server on an EC2 instance, verified the service through HTTP, monitored Linux processes during a controlled CPU workload, and correlated host-level observations with Amazon CloudWatch metrics.

This lab strengthened the connection between **Linux administration, process troubleshooting, EC2 monitoring, and AWS observability**.
