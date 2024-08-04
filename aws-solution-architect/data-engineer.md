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

## Firehose

kind of ETL, read data, transform, load into another storage
Producer: Kinesis streams/ Iot/ CLouwatch
Transformer: lambda
Destination: S3/Elastic Search/Redshift/third parties/custom destination
records up to 1mb
failed data can sent to failover S3 bucket
we can set a buffer to make data load more efficiently, buffer can flush based on size/time, neal real-time
doesn't support re-play

## Analytics

Provide seach capability (SQL) on stream data.
