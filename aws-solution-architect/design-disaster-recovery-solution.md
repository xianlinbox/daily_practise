In the last episodes, we have talked:

- Config your cloud environment
- Move your application and data into cloud

When your system had migrated to AWS, we can use the the cloud capability to improve system reliability, which involves
a Disaster Recovery strategy. In this episode, let's discuss how to design an effective Disaster Recovery (DR) strategy
in AWS.

# The Objective of A Disaster Recovery Strategy

There are two objectives for a rescovery:

1. Recovery Time Objective (RTO): How long can the service be offline
2. Recovery Point Objective (RPO): How many data can the service lose

AWS provides several approaches to achieve different objectives.

# The Approaches of Disaster Recovery in AWS

## Backup and Restore

- Description: Data is backed up to AWS storage services (e.g., S3, Glacier) and restored during a disaster.
- RTO/RPO: High, RTO (hours to days), flexible RPO (depends on backup frequency).
- Use Case: Suitable for non-critical workloads or cost-sensitive environments.

## Pilot Light

- Description: A minimal, always-on environment is maintained in AWS with essential components. Full production is
  scaled up during a disaster.
- RTO/RPO: Moderate RTO (minutes to hours), low RPO (seconds to minutes).
- Use Case: Useful for workloads requiring quick recovery but not full-scale standby.

## Warm Standby

- Description: A scaled-down but functional version of the production environment runs in AWS and can be scaled up
  during a disaster.
- RTO/RPO: Low RTO (minutes), low RPO (seconds to minutes).
- Use Case: Ideal for critical workloads where recovery time must be minimal.

## Multi-Site (Active-Active)

- Description: Fully redundant, active environments run in multiple AWS Regions, sharing the workload.
- RTO/RPO: Near-zero RTO and RPO.
- Use Case: Best for mission-critical workloads with no tolerance for downtime.

# The DR support in AWS services

To implemented the above approaches, AWS provided servcies to help us do it easily.

## AWS Backup

a fully managed service designed to centralize and automate data protection across AWS services.

Features:

- Single interface to manage and monitor all backup activities.
- Define schedule, retention and lifecycle rules for backup
- support Cross-account, cross-region backup
- recover data to specific point of time
- Audit Manager provide audit and track backup activities
- AWS Backup Vault can provide an isolation storage for the backup

Support Services:

- Compute: EC2(instance and volume)
- Storage: S3,EFS, EBS, EFS, FSx, RDS, Aurora, DynamoDB
- Others: EKS persistent Volume, Storage Gateway(volume)

Storage Tier: Warm Storage (expensive but fast)/ Cold Storage (cheap and slow, hours)

## Amazon Data Lifecycle Manager(DLM)

automate the lifecycle management of your Amazon Elastic Block Store (EBS) snapshots and Amazon Elastic File System
(EFS) file systems backups.

- Automated Backups
- Retention policy
- Cross region copy
- Cross-Account Sharing
- Can config by event driven

## service-specific backups

### EC2

For EC2 instance DR, There are 2 services can help on it:

Snapshot:

- a point-in-time copy of EBS volume, save it to S3, only for EBS volume, no configuration, OS, and data
- To restore a snapshot, you create a new EBS volume from the snapshot and attach it to an EC2 instance.
- for cross-account, cross-region copy, need to do it manually
- the destination account must have permission to launch EC2 instances using the snapshot.

Create AMI from instance:

- backup of the entire EC2 instance, including the operating system, configurations, and all attached EBS volumes.
- To restore an EC2 instance, you launch a new instance from the AMI
- Also support Cross-Region and Cross-Account copy
- Need to modify permissions to allow other accounts to access the AMI.

### FSx

provides automated backups that are enabled by default when you create a new FSx file system. These backups are taken
daily and stored in Amazon S3.

- takes incremental snapshots
- retained for 7 days by default but can be extended up to 90 days
- performed during a configurable maintenance window.
- restore from automated backups to recover from accidental deletion or corruption.
- Backups are within the same region as the FSx file system. cross-region and cross-account backup strategies need AWS
  Backup or AWS DataSync.

S3 RDS Aurora DynamoDB

## Routing, Scaling for the routing

AWS Elastic Load Balancer (ELB) for traffic routing.

## Monitor, Triggering for failover

- AWS elastic disaster recovery
- cloudwatch alarm
- Route53 health check

Amazon EC2 instances with minimal capacity. Amazon RDS for database replication. Auto Scaling to quickly scale
infrastructure.

AWS Elastic Load Balancer (ELB) for traffic routing. Amazon Route 53 for DNS failover. AWS Systems Manager for
automation.

AWS Backup for automated backups. Amazon S3 and S3 Glacier for cost-effective storage. AWS Storage Gateway for hybrid
environments.

AWS Global Accelerator for routing. Multi-Region Amazon RDS or DynamoDB Global Tables. Amazon S3 with cross-region
replication. Use S3 Cross-Region Replication (CRR) for objects. Use RDS Multi-AZ or read replicas across regions. Use
DynamoDB Global Tables for globally distributed databases. Networking: Configure Amazon Route 53 for DNS failover. Use
Transit Gateway for network connectivity. Automation: Automate recovery processes with AWS Lambda and AWS Systems
Manager. Use AWS CloudFormation for infrastructure as code to quickly rebuild environments. Monitoring and Testing: Use
Amazon CloudWatch for monitoring. Regularly test DR plans with simulated outages using AWS Fault Injection Simulator.

AWS elastic disaster recovery

Understanding AWS component replication capability

DB

- Database management service vs DataSync

EC2

- quotas

correct routing after DR

- health checks
- routing algorithm
- TTL for DNS records for

Monitoring to triger failover

- cloudwatch alarm
- Route53 health check

Improve the Reliability

- Multi region/ Multi AZ
- Decoupling
- Scale group
- AWS services support scaling actions

ebs doesn't support cross-region snapshot, you need to create the snapshot in the same Region and then copy it across
Regions
