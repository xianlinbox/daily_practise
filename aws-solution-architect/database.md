# DynamoDB

No SQL, max block size 400k, can migrate cassandra to it.

Keys: partition key/sort key/primary key
Indexs: LSI/GSI

TTL: time to live
Dynamo Stream: sending changes to stream trigger other services (lambda)
Global Tables: Cross Region replication. must with streams
DAX: DynamoDB accelator, cache layer

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

RDS proxy to avoid too many connections issue

## Backups

1. support multi region
2. Manual snapshots can share to up 20 aws accounts. automated snapshots can't share to other account.

## DMS(data migration service)

1. Can config data validation in the task to validate the job.
2. Has Table metrics to get stastics data.
3. premigration assessment: evaluates specified components of a database migration task to help identify any problems.

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

1. Cluster Endpoint: write
2. Reader Endpoint: LB for read
3. Custom Endpoint: to specific set of instance
4. Instance Encpoint: to specific db instance

## Logs

error log/query/general/audit, can integrate with Cloudwatch

Aurora Golobal Database: support write forwarding
Covert RDS to Aurora: snapshot/aurora-replica
