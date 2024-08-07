# Kinesis

A managed data stream services

- great for real time big data
- data is automatically replicated in 3 AZ

Family:

1. Streams: low latency data ingest at scale
2. Analytics: perform real-time analytics on streams using SQL
3. Firehose: load streams into S3/Elastic Search/Spunk/Redshift

## Streams:

- Load data in shards/partition, message are ordered per shard, shard can change over time
- data retention is 24 hours to 365 days
- can replay data
- data into kinesis, it's immutable, can't be deleted until data rentation gone
- data producers: sdk/kinesis agent/kinesis product lib
- 1mb/s, 1000 message/s write per shard, othereise ProvsionedThroughputExceptiob
- 2mb/s 5 api call/s read per shard, can use Consume enhance fan out to remove api calls limitation
- Capacity Model:
  - On-demand: no capacity planning, scale automatically
  * Provisioned: mange shards overtime

## Firehose

kind of ETL, read data, transform, load into another storage
Producer: Kinesis streams/ Iot/ CLouwatch
Transformer: lambda
Destination: S3/Elastic Search/Redshift/third parties/custom destination
records up to 1mb
failed data can sent to failover S3 bucket
we can set a buffer to make data load more efficiently, buffer can flush based on size/time, neal real-time
doesn't support re-play
kinesis agent can sent to firehose directly

## Analytics

Provide seach capability (SQL) on stream data.

# MSK

AWS managed kafka
Multi-AZ support up to 3 HA
Data is stored on EBS
Has a serverless version, MSK serverless.

1m size by default, can set to other values
can only add partion to a topic

consumer of MSK:

- Kinesis Data analytics with Spark
- Glue ETL with Spark Streaming
- Lambda
- Custom Application

# AWS Batch

Run Batch jobs as docker images

run options: Fargate/EC2 instance

Managed env/Unmanaged env

Multi-node mode

# AWS EMR

Elastic Map Reduce, build Hadoop cluster for big data processing
As it use a lot of EC2 instance, config instance type can save a lot of money.

# AWS Glue

AWS managed ETL tool.
Data Crawler -> Data Catalog -> Glue Jobs

# Redshift

AWS managed OLAP data warehouse
column storage of data
PB scale
Massively Parallel Query Execution
can integrated with Tableau or Quicksight
Snapshot
Cross region snapshot copy (enable snapshot copy grant)
Redshift spectrum: query data in S3 without load it
Has a workload manager
Concurrecy scaling: support high performance

# Document DB

AWS managed Mongo DB

# Timestream

AWS managed time series Database

# Athena

Serverless query service to analyze data stored in S3
Use standard SQL to query
Support csv, parquet, json different file format
Commonly with quicksight to create dashboard

Performance improvement:

1. use columnar data
2. compress data
3. partition dataset
4. use larger data file

Federated query: to query more data source

# Quicksight

bi with inteactive dashboard
