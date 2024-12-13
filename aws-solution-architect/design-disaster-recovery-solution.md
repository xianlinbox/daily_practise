Designing an effective Disaster Recovery (DR) strategy in AWS involves leveraging cloud-native services and best practices to ensure high availability, data durability, and quick recovery. AWS provides several approaches for disaster recovery, categorized by Recovery Time Objective (RTO) and Recovery Point Objective (RPO):

1. DR Models in AWS
   A. Backup and Restore
   Description: Data is backed up to AWS storage services (e.g., S3, Glacier) and restored during a disaster.
   RTO/RPO: High RTO (hours to days), flexible RPO (depends on backup frequency).
   Key Services:
   AWS Backup for automated backups.
   Amazon S3 and S3 Glacier for cost-effective storage.
   AWS Storage Gateway for hybrid environments.
   Use Case: Suitable for non-critical workloads or cost-sensitive environments.
   B. Pilot Light
   Description: A minimal, always-on environment is maintained in AWS with essential components. Full production is scaled up during a disaster.
   RTO/RPO: Moderate RTO (minutes to hours), low RPO (seconds to minutes).
   Key Services:
   Amazon EC2 instances with minimal capacity.
   Amazon RDS for database replication.
   Auto Scaling to quickly scale infrastructure.
   Use Case: Useful for workloads requiring quick recovery but not full-scale standby.
   C. Warm Standby
   Description: A scaled-down but functional version of the production environment runs in AWS and can be scaled up during a disaster.
   RTO/RPO: Low RTO (minutes), low RPO (seconds to minutes).
   Key Services:
   AWS Elastic Load Balancer (ELB) for traffic routing.
   Amazon Route 53 for DNS failover.
   AWS Systems Manager for automation.
   Use Case: Ideal for critical workloads where recovery time must be minimal.
   D. Multi-Site (Active-Active)
   Description: Fully redundant, active environments run in multiple AWS Regions, sharing the workload.
   RTO/RPO: Near-zero RTO and RPO.
   Key Services:
   AWS Global Accelerator for routing.
   Multi-Region Amazon RDS or DynamoDB Global Tables.
   Amazon S3 with cross-region replication.
   Use Case: Best for mission-critical workloads with no tolerance for downtime.
2. AWS DR Best Practices
   Data Replication:
   Use S3 Cross-Region Replication (CRR) for objects.
   Use RDS Multi-AZ or read replicas across regions.
   Use DynamoDB Global Tables for globally distributed databases.
   Networking:
   Configure Amazon Route 53 for DNS failover.
   Use Transit Gateway for network connectivity.
   Automation:
   Automate recovery processes with AWS Lambda and AWS Systems Manager.
   Use AWS CloudFormation for infrastructure as code to quickly rebuild environments.
   Monitoring and Testing:
   Use Amazon CloudWatch for monitoring.
   Regularly test DR plans with simulated outages using AWS Fault Injection Simulator.
   Understanding RTO & RPO

Balance cost with RTO/RPO

Strategy

- multi-site
- warm standby
- pilot light
- backup & restore

DR

- AWS elastic disaster recovery

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

ebs doesn't support cross-region snapshot, you need to create the snapshot in the same Region and then copy it across Regions
