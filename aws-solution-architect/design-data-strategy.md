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

S3 select: retrieve specific data from an S3 object using SQL queries, rather than downloading the entire object

## Dynamo DB

a fully managed NoSQL database. the core concepts:

- Table/Item/Attributes
- Primary Key/Composite Key/Secondary Indexes(global, local) for search performance

Capacity: Provision DynamoDB with RCU/WCU

Scaling policy:

- Auto-scaling: upper and low limits of the scaling/paying for provisioned throughput/best for predictable load
- On demanding: scale all behind the scenes automatically/ pay per read or write request/best for vary work load

Security: enrypt at rest by default, can config on Table-level and item-level access policies.

Special Features:

- DynamoDB Streams: Captures table modification events in real time (insert, update, delete). it can user for event
  driven following operations.
- DAX: In-memory caching for faster read operations.
- TTL: automatic delete item after a period
- Transaction: cross table ACID operation

Global Tables: a fully managed, multi-region, multi-active DynamoDB

- cross-region replication
- Multi-Active Writes with conflict resolution
- Low-Latency Access
- Disaster Recovery

## RDS

An AWS managed SQL database service.

Supported engine: Oracle/SQL server/MariaDB/MySQL/PostgreSQL

Storage Types:

- General Purpose SSD (gp2 or gp3): Cost-effective for most workloads.
- Provisioned IOPS SSD (io1 or io2): High-performance storage for I/O-intensive applications.

Features:

- Multi-AZ Deployments.
- Read Replicas: Improves read performance by replicating data to read-only instances, support cross-Region read
  replica.
- Automated backups to support point-in-time recovery
- Performance Insights helps identify slow queries and resource bottleneck.

## Aurora

a fully managed only MySQL and PostgreSQL compatible relational database. has a lot of advanced features, so has a
higher price compare to RDS.

Advanced features:

- faster: 5x for MySql, 3x for PostgreSql
- bigger: autoscale to 128 TB
- read replica cross 3 AZ
- Global Database: span aurora to multiple AWS regions.one primary AWS Region for write, and up to five read-only
  secondary AWS Regions.
- Continuous backup to S3; supports backtracking for time travel.
- support serveless version

Aurora Serverless:

- Automatically scales compute based on demand.
- Ideal for unpredictable or intermittent workloads.
- Pay for capacity in Aurora Capacity Units (ACUs).
- no cross-region replicas and not support Global database

## Elastic Cache

a fully managed in-memory data store and caching service

- support engine: redis/memcache
- Offers multi-AZ with automatic failover (Redis).

## EBS

block storage for use with Amazon EC2 instances.

- Volume types: general purpose/provisioned iops/throughput optimized/cold HDD
- Volumes can only attach to EC2 in same AZ
- Requires snapshot to move volume cross region

## EFS

a fully managed, scalable file storage service designed for use with AWS services and on-premises resources

- Mode: General purpose/Max I/O
- Storage Class: Standard/Infrequent access
- only support NFS protocol

## FSx

a fully managed service that provides specialized file systems optimized for different workloads

- support: windows file server/openZFS/Lustre(High-performanc, compute intensive)/NetAPP ONTAP

## Neptune

a fully managed graph database

- model: Property Graph/RDF Graph
- query: Gremlin, SPARQL, openCypher

# Data Analytics

## Kinesis Data Analytics

process and analyze streaming data in real-time using standard SQL queries, essentially enabling the creation of
applications that transform and provide insights from data as it arrives, without the need to manage complex
infrastructure or coding frameworks; it leverages the Apache Flink open-source engine for stream processing under the
hood.

- input: A Kinesis data stream/A Firehose delivery stream
- ouput: a Kinesis data stream/a Firehose delivery stream/a Lambda function

## Athena

a serverless, interactive query service that allows you to analyze data stored in Amazon S3 using SQL

- can work with different data format: csv, parquet, json, orc or avro
- good for ad-hoc queries, data exploration, and analytics without requiring a database setup or infrastructure
  management.

Working process:

1. data in S3
2. use AWS Glue Data catalog to define schema of the data
3. run SQL query on the s3 data directly
4. pay based the data voluem scaned

## AWS Glue

a fully managed extract, transform, and load (ETL) service

- support all data sources: structured, unstructured in DB, data in S3 or data in on-premise systems
- automate ETL workflows with triggers, job scheduling, and event-driven actions.
- support python/scala for scripting

Component:

- Glue Data catalog to create metadata through data discovering
- Glue ETL Jobs: the script to do the transform
- Glue Crawlers: scan data store to infer schema and inject to catalog
- Glue DataBrew: visual data cleaning and normalization
- Glue triggers: autimate the job by scheduling or event

Limitations:

- some job may need a latency for cold start
- not for real-time job

## Redshift

a fully managed, petabyte-scale cloud data warehouse service designed for fast and efficient analytics.

Features:

- Massive parallel processing through multiple nodes
- Columnar Storage: store data in column for high I/O
- Spectrum：Query data directly from S3 without loading it into the redshift, good for combine redshift data with S3
  data

Limitations:

- require ETL to prepare data
- need scaling for high user load
- not for transaction data

## EMR

a managed big data platform for processing and analyzing vast amounts of data using open-source tools like Apache Spark,
Hadoop, Hive, and Presto. It simplifies running and scaling these frameworks on AWS.

- Supports Apache Spark, Hadoop, Hive, HBase, Presto, Flink, and more
- can process data from S3, HDFS, DynamoDB, and relational databases
- use spot instances for non-critical workload to save cost

Limitations:

- requires some expertise in big data frameworks
- Cluster startup times can impact short, ad-hoc jobs.
- Running long-lived clusters may lead to higher costs compared to serverless solutions

## OpenSearch

# Conclusion
