# EBS

Network Drive attach to 1 instance only, to special AZ. there is multi-attch for io type to attach to multi instance.

Volume Types (size/IO/thoughtput):

- gp2/gp3: general purpose SSD
- io: low latenct SSD
- st/sc : low cost HDD (can't used as the boot volume), maxium 500 IOPS

With gp2 you get a baseline of 100 IOPS and then 3 IOPS per GiB after the first 33.33GiB, with a max of 16,000 IOPS. Pricing is based on volume size.

Snapshot: incremental,can copy for DR, saved in S3 and can pre-warm for fast loading.

Data Lifecycle Manager: help to manage snapshots
Aws backup: manage aws services backup including ebs

Encryption: not encryped by default, can enable at account level.

Local Instance Store: a phisical ephemeral device attach to EC2 instance, high io; can't resize, need manage lifecycle by user.we should use EBS mostly. only extremely high IOPS may consider local instance store. EBS is maximum 256K for provisioned IOPS SSD

we can config RAID 0 for I/O perforamance, RAID 1 for redundency.

# EFS

Attach to multi EC2 (cross region even on-premise), expensive, cost per usage (no need planning usage).

- Encryption at rest with KMS
- Only attach to one VPC, create one ENI per AZ
- Compatible with linux based AMI
- Use Security Group to control access to EFS

Storage Tier for cost saving, using lifecycle policy to move data to different tier

VPC peering, On-prem Direct connect
Access point with pemission config on path
Cross Region Replication

EFS can attach to both on-prem server and EC2 instance.

EFS doesn't support cross region replication

# S3

Save for objects.

Anti Pattern:

1. lots of small files
2. Use as a file syste,
3. Search/Indexing

Replication:Cross Region Replication/SRR (same region replication)
Combine with lifecycle rules and Replciation time control for in time replication

MUlti-upload/Byte fetch range
S3 Select: filter on the server.
S3 analytics: provide recommandation for how to store your data in S3

S3 transfer accelerator: use edge location for faster upload
S3 access point: simplify data access for any AWS service or customer application that stores data in S3. With S3 Access Points, customers can create unique access control policies for each access point to easily control access to shared datasets. mostly for the shared data.

Storage Lens:

A dashboard:

- summary metrics
- Cost Optimization Metrics
- Data Protection Metrics
- Access Management Metrics
- Event Metrics
- Performance Metrics
- Activity Metrics
  Free and Paid advanced metrics

  By default, you can create up to 100 buckets in each of your AWS accounts
  NL

## settings

For the majority of modern use cases in S3, we recommend that you keep ACLs disabled by applying the Bucket owner enforced setting and using your bucket policy to share data with users outside of your account as needed. This approach simplifies permissions management.
ACL disabled:

- bucket owner enforced (default): access policy decided permission.

ACLs enabled:

- Bucket owner preferred – The bucket owner owns and has full control over new objects that other accounts write to the bucket with the bucket-owner-full-control canned ACL.\
- Object writer – The AWS account that uploads an object owns the object, has full control over it, and can grant other users access to it through ACLs.

Public Access:

- IgnorePublicAcls option to TRUE: ignore all public ACLs on a bucket and any objects that it contains
- BlockPublicAcls: PUT bucket ACL and PUT objects requests are blocked if granting public access.
- BlockPublicPolicy: reject put request if public access policy attached
- RestrictPublicBuckets: Restricts access to principles in the bucket owners’ AWS account

## S3 Achitecture

S3 can as the host of static content, combine with EC2 or Cloud front to provide the content, we also can provide pre-signed URL to client to direct talk to S3.

## event notification

S3 Event Notifications feature to receive notifications when certain events happen in your S3 bucket, the destination can be: SNS/SQS/EventBridge/Lambda, can check the API called but can't check api inside permission,

we can enable object-level logging and add cloudtrail to capture this log for analysis.

## Pricing

S3 don't need to pay for the following scenario:

1. data transfer in from internet
2. data transfer out to cloudfront
3. data transfer out to EC2 in the same region

## deny uncrypted object upload

1. For object encryption at rest, you can set the default encryption behavior on an Amazon S3
2. To deny unencrypted objects, "s3:x-amz-server-side-encryption" can be added which allows only encrypted object upload and can restrict to a specific KMS key as well.
3. Amazon CloudFront can use 301 response code to redirect HTTP requests to HTTPS and allows only secured traffic.

# FSx

lauch 3rd party service (windows file server/Lusture) as a full managed service in AWS
FSx Deployment options: Scratch FS/Persistent FS

FSx architecture Solution:

1. MIgration from one AZ to multi AZ: DataSync/Backup.
2. Decrease FSx Size: it can only increase, decrease need to create a new one and data sync
3. Data lazy loading: only load data is needed before processing. not all at once.

we can monitor storage capacity and file system activity using Amazon CloudWatch; monitor FSx API calls using AWS CloudTrail, monitor end-user actions with file access auditing using Amazon CloudWatch Logs and Amazon Kinesis Data Firehose

# DataSync

Move large amount of data from and to
it need DataSync agent to do the work.
A single Datasync task can 10GB/s

# Data Exchange

Buy and load third party data (mckinsey, reteuers ect) through AWS

# Transfer Family

FTP protocal data transfer in/out S3 & EFS

Tips:

1. Database cloning is only available for Aurora and not for RDS.

# Storage Gateway

Hybrid cloud storage service that gives you on-premises access to virtually unlimited cloud storage. make cloud acess by on-prem, FSx make on-prem access by Cloud

## 3 Types:

Tape gateway: presents virtual tapes to leading to backup applications
Volume gateway: presents iSCSI block storage volumes to your on-premises applications. cached (frequent access data)/stored (full data then backup)
S3 File Gateway: presents Server Message Block (SMB) or Network File System (NFS) based access to data in S3
FSx File Gateway: accelerate your file-based storage migration to the cloud to enable faster performance, improved data protection, and reduced cost.
