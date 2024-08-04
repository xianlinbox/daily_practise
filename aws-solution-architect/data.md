# Kinesis Data Stream

Limits:

- Number of data streams: no upper stream,
- Number of shards: no upper limit. 200 shards per AWS account, in some region is 500
- Data stream throughput: no upper limit, support up to 1 MB/sec or 1,000 records/sec write throughput;2 MB/sec or 2,000 records/sec read throughput
- Data payload size: The maximum size of the data payload of a record before base64-encoding is up to 1 MB.
