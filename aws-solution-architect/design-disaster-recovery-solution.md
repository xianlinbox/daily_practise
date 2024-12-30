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

### ECS/EKS

- Multi-AZ Deployment: In case of a failure in one AZ, ECS automatically launches new tasks in healthy AZs to maintain
  the desired task count. EKS will attempt to reschedule any failed pods to healthy nodes in the same region.
  Cross-Region

### FSx

provides automated backups that are enabled by default when you create a new FSx file system. These backups are taken
daily and stored in Amazon S3.

- takes incremental snapshots
- retained for 7 days by default but can be extended up to 90 days
- performed during a configurable maintenance window.
- restore from automated backups to recover from accidental deletion or corruption.
- Backups are within the same region as the FSx file system. cross-region and cross-account backup strategies need AWS
  Backup or AWS DataSync.

### S3

- Replication: enables you to automatically replicate objects between buckets, it natively support Cross-Region
  Replication/Same-Region Replication RDS Aurora DynamoDB/ Cross-Account Replication
- lifecycle policies can be used to manage backups and data retention

### RDS

To support Disaster Recovery, RDS provide the following features:

- Automated Backups: Daily backups with point-in-time recovery (PITR) within a retention window.
- Multi-AZ Deployments: Synchronous replication to a standby instance in another AZ. failover to standby insatnce
  automatically, extra cost on the standby instance.
- Read Replicas: Asynchronous replication, manually promoted to primary in case of failure. This support cross-region
  replica.

### Aurora

Aurora has Global Databases to provide low-latency global replication across multiple AWS regions.

- In case of a failure in the primary region, you can promote a replica in another region to become the new primary.
- Allows for cross-region disaster recovery with minimal downtime.

### DynamoDB

Global Tables: replicate data across multiple AWS regions, providing automatic disaster recovery at the regional level.

- Writes to DynamoDB tables are automatically propagated to all other regions that are part of the Global Table.
- If one region becomes unavailable, fail over to a different region with minimal downtime, ensuring business
  continuity.

Point-in-Time Recovery (PITR): restore your DynamoDB table to any point in time within the last 35 days,

- helping recover from data corruption, accidental deletions, or unwanted changes.
- only available for Standard DynamoDB tables and cannot be used for On-Demand tables.
- Does not provide cross-region disaster recovery by itself

Backups: built-in backup and restore capabilities, which allow you to take on-demand backups of your DynamoDB tables.

- Backups are region-specific and do not natively support cross-region disaster recovery
- Restoring a table from backup might take some time, depending on the size of the table.

## Monitoring, Routing, Scaling

The above services will restore the application and storage. As described above, the restored application or storage may
have a different endpoint. So AWS provided service discovery and loadbalancer to make system automatically found the

- CloudWatch Alarms: notify you of any performance issues or failures in critical systems that could trigger your
  disaster recovery plan.
- Route53 Health Checks & DNS Failover
- Global Accelerator fails over traffic to healthy endpoints.
- Cloud Map for ECS/EKS internal service discovery
- Elastic Load Balancing (ELB) to distribute traffic across containers, even in multiple AZs or regions.

# Conclusion

From the info above, when design a disaster recovery strategy, we need to:

1. Defines the objective (RTO&RPO)
2. The Application and Data storage in the system
3. Based on the RTO/RPO to choose the DR Approach.
4. Use AWS services to simplify the DR implementation and Document the DR plan
5. Review and update the DR plan as applications and infrastructure evolve
