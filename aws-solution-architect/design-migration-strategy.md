In last episode, we are more focus on how to deploy new things into AWS cloud. Actually in the real world, we did more
migration legacy workload rather than delivery new workloads. In this episode, let's talk about the migration strategy.

# 7Rs

7Rs are strategies organizations use to evaluate and plan the migration of applications to the cloud. These strategies
help in deciding the most appropriate approach for each workload based on its requirements, technical debt, and business
value.

## Retire

Identify applications or workloads that are no longer needed and can be decommissioned.

- Reduces costs and complexity.
- Frees up resources for more critical applications.

## Retain

Leave the application as-is, either because it's tightly integrated with other systems or due to business constraints.

- Avoid unnecessary effort on applications that aren’t a priority.
- Allows focusing resources on higher-impact migrations

## Relocate

Move to another cloud or hybrid environment.

- a hybrid cloud or specific hardware dependency is needed.
- Simplifies migration for workloads requiring a consistent infrastructure layer
- Provides continuity for legacy systems while using cloud infrastructure

## Re-Host

"Lift-and-shift" to the cloud.

- The application is compatible with the cloud environment without requiring major changes.
- Fast and simple migration
- Reduces on-premises infrastructure costs.

## Re-platform

Migrate the application to the cloud with some optimizations, such as switching to managed services or updating runtime
environments.

- Takes advantage of some cloud-native features without extensive re-architecture
- Balances effort and benefit.

## Re-Purchase

Replace the existing application with a commercial, off-the-shelf (COTS) solution, often SaaS.

- when application can be replaced by modern SaaS offerings.
- Avoids maintenance of custom applications.
- Leverages the benefits of modern, feature-rich SaaS platforms.

## Refactor

Modify the application to make it cloud-native, often by adopting microservices, serverless architectures, or
containerization.

- When the application is critical and can benefit significantly from cloud-native features like scalability,
  resilience, or cost efficiency.
- Fully leverages the cloud’s benefits (scalability, flexibility, cost optimization).
- Improves maintainability and modernizes the application architecture.

# Migration Assessment and Planning

Before start migration, we need to plan how to the migration, for each resources, which strategy we want to use, and the
priority. AWS provide several tools to help customer do this work:

## Application Discovery Service

help enterprises assess their on-premises environments in preparation for migration to AWS. It automatically collects
detailed information about an organization’s data center, including server configurations, resource utilization, running
applications, and their dependencies.

- Agent based discovery: install a agent on each server to collect details info.
- Agentless discovery: use Vmware Vcenter to gather info.
- Data collected is displayed in MigrationHub
- can export data into csv file or use third party tool to do deep analysis, like use AWS Migration Evaluator to
  estimate cost and provide suggestion.

## Migration Hub

Provides a central location to track the progress of application migrations across AWS and partner solutions.

- unified tracking dashboard
- integrated with other tools,like application discovery service/server migration service/application migration service.
- provide insights for migration priority

## Migration Evaluator

Provides insights into cost estimates and recommendations for migrating to AWS.

- Analyzes existing infrastructure.
- Provides a business case for migration with TCO (Total Cost of Ownership) analysis

# Application Migration

## AWS Elastic Beanstalk

Simplifies migration and deployment of web applications and services.

- Support for various platforms (Java, .NET, Python, Node.js)

## AWS App2Container

Migrates existing applications to containers running in Amazon ECS, EKS, or Fargate.

## AWS Mainframe Modernization

Migrates and modernizes mainframe applications to AWS.

- Provides re-platforming or refactoring options
- Includes tools to analyze and plan migrationss

## AWS Application Migration Service(MGN)

Simplifies lift-and-shift migrations of on-premises servers (physical or virtual) to AWS.

- Continuous replication of source servers to AWS.
- Automated testing and cutover.
- Supports various operating systems.

## AWS Server Migration Service (SMS)

Migrates on-premises VMware, Hyper-V, or Azure VMs to AWS as AMIs (Amazon Machine Images).

- Designed for VM-based migrations.

# Data Migration

Except the application, we also need to move the data to cloud.

## AWS Database Migration Service (DMS)

Migrates databases to AWS with minimal downtime.

- support both homogeneous(same db engine) and heterogeneous (cross db engine) migration
- Supports continuous data replication.

## AWS Schema Convert Tool

Assists in schema conversions for heterogeneous database migrations.

- Converts database schema and SQL code.
- Identifies conversion challenges and offers solutions.

## AWS Data sync

Automates and accelerates data movement between on-premises storage and AWS

- Supports NFS, SMB, and object storage.
- Ideal for recurring or incremental data transfer tasks.
- support transfer data between aws services, like S3 to EFS
- pay-as-you-go solution, automatically encryt and integrity validation

## AWS Storage Gateway

Bridges on-premises storage with AWS for hybrid environments.

- Types: File Gateway/Tape Gateway/Volume Gateway
- move/read data to cloud
- have local cache ensures low-latency access to frequently used data.

## AWS Snowball Family

Physical devices for transferring large-scale datasets to AWS.

- Snowball: Petabyte-scale data migration using portable devices
- Snowmobile: Exabyte-scale data migration using a secure shipping container
- support offline transfer due to limit connectivity
- lead time is approximately 1 week.
- support NFSv3, NFSv4, NFSv4.1 protocol, no USB support
- use Snowball Edge to support local data processing before upload to Cloud

## AWS Transfer Family

Migrates SFTP, FTPS, and FTP-based workflows to AWS.

- Fully managed file transfer service.
- Integrates with S3 and EFS.

## Amazon Data Lifecycle Manager(DLM)

automate the lifecycle management of your Amazon Elastic Block Store (EBS) snapshots and Amazon Elastic File System
(EFS) file systems.

- Automated Backups
- Retention policy
- Cross region copy
- Can config by event driven

### Resource Access Manager

securely share AWS resources with other AWS accounts, organizational units (OUs), or the entire AWS Organization

- support VPC Subnet/Transit Gateway/license manager/Route53 resolver rules/Ec2 reserve capacity/Aurora DB cluster
- no data movement, reduce duplication

# Conclusion

In AWS official site, it provide a diagram about the full migration process.
![Migration process](https://d2908q01vomqb2.cloudfront.net/cb7a1d775e800fd1ee4049f7dca9e041eb9ba083/2021/11/24/7-R-1024x516.png)

we just need to follow it and choose the right tools in each steps.
