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
Multi-AZ / Read Replica
Cloudtrail can't track RDS queries

RDS for Oracle:
backups: RDS backups to RDS; Oracle RMAN to non RDS
RAC not support
DMS for on-prem migrate/replica to RDS for Oracle
Transparent transport Encryption supported

RDS for Lambda:

RDS proxy to avoid too many connections issue

# Aurora

only compatible to PG & Mysql
Load/offload data directly to S3
Very high availability

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
