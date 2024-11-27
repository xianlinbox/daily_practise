# Step functions

visualize serveless workflow for orchestrate lambdas; it can parrel, sequence, timeout, condition, error handling

- it can integrated with almost all other AWS services, eg: SQS/SNS/Batch/EC2/DynamoDB
- it can be triggered by Console/CLI/API/Api gateway/lambda/event bridge, not an S3 event directly.
- Task type: lambda/activity/service/wait
- Workflow types: Express (at least once, 5 minutes)/Standard( Exact once, 1 year)

## Execution Guarantee

1. Standard Workflows:

- ideal for long-running (up to one year), durable, and auditable workflows,
- exact-once running.
- suited to orchestrating non-idempotent actions

2. Express Workflows

- ideal for high-volume, event-processing workloads such as IoT data ingestion, streaming data processing and transformation, and mobile application backends.
- Can run multiple in parallel
- run for up to five minutes,
- at-least-once runnong
- orchestrating idempotent actions
- Synchronous (wait for result) vs Asynchronous(don't wait for result)

##

# SQS

- max size for a message is 256k, the large file can use S3 link instead
- has a FIFO model. but 300 message/s without batching, batching is 3000 message/s, which means batch size is maxium 10.

- Dead letter Queue.after a threshold times of processing, the message can send to DLQ, it must same type of the original queue. good for debug failure message. it can has a retention day. we can redrive message in DLQ back to normal queue.
- Delay queues: let you postpone the delivery of all new messages to a queue for several seconds,maxium 15minutes

short polling: query subset of servers then return, may not return all the messages in first response.
long polling: query all the servers then return, only timeout will return empty message.
visibility timout:a period of time during which Amazon SQS prevents other consumers from receiving and processing the message
SQS doesn't allow a message be consumed by multi consumer at the sam time.
Message timers let you specify an initial invisibility period for a message added to a queue.
SQS queue depth metrics for

## Encrypted SQS queue

support Server-side encryption (SSE). Server-side encryption (SSE) lets you store the data in encrypted format in the SQS queues. By default, SQS encrypts all the messages in queues using SQS-managed encryption keys (SSE-SQS).

Another option is to use the SSE-KMS, encryption with the AWS Key Management Service Key. You may choose a default key provided by AWS or your own Customer Manager Key (CMK). The KMS key that you assign to your queue must have a key policy that includes permissions for all principals that are authorized to use the queue.

# Amazon MQ

A manged message broker service of AWS for RabbitMQ and ActiveMQ, you can just replatform you MQ rather than refactor to use SQS.

# AWS SNS

1. up to 12.5m subscriper for each topic;each account can have 100k topics be default
2. there is a message filter feature to let subscripter only take special message in that topic
3. SNS ensured FIFO per topic
4. compare eventbridge, eb has more targets and more focus on event driven architecture, SNS is more focus on pub/sub
5. SNS+SQS: fistributed one requets to multi SQS, support cross region communication
