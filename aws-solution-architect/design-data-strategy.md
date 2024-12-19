In the last eposide, we have talked about how to migrated worloads to AWS, it have talked about the migration part of data. In this eposide, we gonna talk more about data engineering in AWS.

# Data Ingestion

First part, how does user upload data into AWS. Except the migration part we already discussed in the migration strategy eposide. There are a few others channels user can use.

## Kinesis data stream

## AWS Iot

## AWS

# Data Storage

## S3

no cross-Region snapshots, but have cross-Region replication

## Dynamo DB

Scaling policy:
Auto-scaling

- upper and low limits of the scaling
- paying for provisioned throughput
- best for predictable load

On demanding

- scale all behind the scenes automatically.
- pay per read or write request.
- best for vary work load

## RDS

- cross-Region read replica

## Aurora

# Data Analytics
