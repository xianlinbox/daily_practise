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
- Typical case: website clickstream analysis,Fraud detection and log monitoring.

## Kinesis data firehose

Fully managed, serverless service for delivering real-time data to destinations.

- Source: AWS SDK/Kinesis data streams/kinesis agent or other opensource agent/AWS services(cloudwatch logs/vpc flow
  logs)
- Desntination: S3/Redshift/Splunk/OpenSearch
- support to call lambda for data transformation
- support buffer or batch to reduce processing overhead, but no retention
- uses at-least-once semantics, may cause duplicate records

## AWS IoT Core

full managed service, real-time data ingestion and management for IoT devices.

- Specifically tailored for IoT devices and protocols (MQTT, HTTPS, WebSocket).
- No explicit retention, processes in real time

## Others

There is a bunch of other services can helo user pass data into cloud like:

- S3 upload
- API call on custom service in EC2/ECS...
- The data migration part like Data sync/DMS etc

Most of them we have talked enough in data migration strategy, here just want to highlight some points of S3 upload:

### S3 upload

- support Transfer Accelerationc, which Speeds up transfers over long distances using AWS global edge locations.
- support multi-upload: which breaks large files into smaller parts, uploads them concurrently,

# Data Storage

After data ingested, we need a place to store these data. AWS provided a

## S3

an object storage service. the data stored organised with Buckets and Objects:

- Buckets: globally unique, containers to store object
- Objects: files uploaded, with optional metadata

Object can choose the Storage Class based on access pattern and cost needs:

- Standard
- Intelligent Tier
- Standard IA
- One-Zone IA
- Glacier
- Glacier Deep Archive

Security:

- data encryption: SSE-S3, SSE-KMS, or SSE-C or customer encryption before upload
- Access control: Bucket policies/IAM policies/Access Control Lists
- Block Public Access: IgnorePublicAcl/BlockPublicAcl/RestrictedPublicBucket/BlockPublicPolicy
- Object Lock: Prevents deletion or modification during a specified retention period.

Replication: no cross-Region snapshots, but have cross-Region replication or Same region replication

Lifecycle policies: Automatically transition objects to different storage classes or delete them.

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

## Kinesis Data Analytics

process and analyze streaming data in real-time using standard SQL queries, essentially enabling the creation of
applications that transform and provide insights from data as it arrives, without the need to manage complex
infrastructure or coding frameworks; it leverages the Apache Flink open-source engine for stream processing under the
hood.

- input: A Kinesis data stream/A Firehose delivery stream
- ouput: a Kinesis data stream/a Firehose delivery stream/a Lambda function

## S3 Select

## Athena

## AWS Glue

## EMR

## Redshift

- Spectrum

## Open Search
