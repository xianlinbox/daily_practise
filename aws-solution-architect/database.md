# DynamoDB

No SQL, max block size 400k, can migrate cassandra to it.

Keys: partition key/sort key/primary key
Indexs: LSI/GSI

TTL: time to live
Dynamo Stream: sending changes to stream trigger other services (lambda)
Global Tables: Cross Region replication. must with streams
DAX: DynamoDB accelator, cache layer

## Provisioned with Auto Scaling

1.  increase read capacity or write capacity as often as necessary
2.  DynamoDB quotas remain in effect,
3.  doesn't prevent you from manually modifying provisioned throughput settings
4.  delete a table, scaling polices are not automatically deleted with it.

steps to enable:

1. choose table/global secondary index
2. choose capacity (read or write)
3. The upper and lower boundaries for the provisioned throughput settings
4. target utilization

## On-demand scaling

you don't need to think about provisioning throughput. Instead, your table will scale all behind the scenes automatically. Extreme spikes in load can occur and be handled seamlessly by AWS. This also brings a change in the cost structure for DynamoDB. With On-Demand Scaling, instead of paying for provisioned throughput, you pay per read or write request.

# Open Search

ELK on AWS

# RDS

AWS managed RDBMS
Lauched in VPC, storage in EBS.
snapshot
RDS events
Multi-AZ:

- created a standy instance, standby can't use for read/write until it became primary.
- The data will replicated to standby synchronously.
- upgrades happened at the same time

Read Replica:

- Read replicas can be within an Availability Zone, Cross-AZ, or Cross-Region. but cross Region make cause extra transfer fee.
- it uses the engines' native asynchronous replication to update the read replica
- upgrade the read replica ones before upgrade source db.

Cloudtrail can't track RDS queries

RDS for Oracle:
backups: RDS backups to RDS; Oracle RMAN to non RDS
RAC not support
DMS for on-prem migrate/replica to RDS for Oracle
Transparent transport Encryption supported

RDS for Lambda:

RDS proxy to avoid too many connections issue, RDS Proxy is fully compatible with the engine versions that it supports. You can enable RDS Proxy for most applications with no code changes.

## Backups

1. support multi region
2. Manual snapshots can share to up 20 aws accounts. automated snapshots can't share to other account.
3. The only way to unencrypt an encrypted database is to export the data and import the data into another DB instance.

## DMS(data migration service)

1. Can config data validation in the task to validate the job.
2. Has Table metrics to get stastics data.
3. pre-migration assessment: evaluates specified components of a database migration task to help identify any problems.
4. when create endpoints, in DMS console it will create IAM role automatically, CLI/API will not

### Redshift as the destination of DMS

The process is DMS move data to S3 first, then ingest S3 data into Redshift tables.

1. don't enable S3 version as a intermediate storage
2. Redshift and DMS must in the same region and same account
3. Redshift is locked down by default, need to grant user for accessing
4. can't change a schema started with \_
5. don't support varchar 60kb+
6. can't DELETE a multi column primary key
7. only support AWS DNS name
8. 4-hours timeout

# Aurora

only compatible to PG & Mysql
Load/offload data directly to S3
Very high availability
has a lab mode to enable Aurora features that are available in the current Aurora database version but are not enabled by default

Multi-AZ:

- update data to all read replicas synchronously.
- all instances are upgraded at the same time.

Read Replica:

## Endpoints

Host+port

1. Cluster Endpoint: write, one is down, a read replica will select as cluster endpoint
2. Reader Endpoint: LB for read
3. Custom Endpoint: to specific set of instance
4. Instance Encpoint: to specific db instance

## Logs

error log/query/general/audit, can integrate with Cloudwatch

Aurora Global Database: support write forwarding, it has multi regions for read but only one write.
Covert RDS to Aurora: snapshot/aurora-replica

## Aurora global database vs Cross-Region replica

1. need high availability of your Aurora cluster, use Aurora Replicas.
2. looking for cross-Region disaster recovery (DR), use Aurora global databases
3. cross-Region copy of your Aurora database, use Aurora Replicas
4. migrate RDS, use Aurora Replicas
