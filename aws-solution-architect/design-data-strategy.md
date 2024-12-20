In the last eposide, we have talked about how to migrated worloads to AWS, it have talked about the migration part of
data. In this eposide, we gonna talk more about data engineering in AWS.

# Data Ingestion

First part, how does user upload data into AWS. AWS offers various tools and services to ingest data into the cloud,
depending on the data's type, size, source, and frequency.

## Kinesis data streams

real-time data streaming platform for custom processing and analytics

- on-demand mode (auto managed)/provisioned mode (fine grain control on shard)
- Producer: any one can send data to streams with Https or SDK
- Shard/Partition Key: using shard to seaparate record into different stream, partion key used to decide which shard.
- Consumer: Customer data stream application, Lambda, Kinesis Data analytics
- Kinesis Client Library: thse SDK use to read/write data to steams
- Retention: data can retented in streams 1-7 days. default is 24 hours.
- Limitations: 2000 read/2 MB per second per shard, 1000 write/1MB per second per shard. This only apply to shard, we
  can provision more shard to get higher throughput.

## AWS IoT Core

## AWS

# Data Storage

## S3

no cross-Region snapshots, but have cross-Region replication

## Dynamo DB

## global table

## Scaling policy:

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

## Elastic Cache

# Data Analytics
