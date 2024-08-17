# Step functions

visualize serveless workflow for orchestrate lambdas; it can parrel, sequence, timeout, condition, error handling

- it can integrated with almost all other AWS services, eg: SQS/SNS/Batch/EC2/DynamoDB
- it can be triggered by Console/CLI/API/Api gateway/lambda/event bridge, not an S3 event directly.
- Task type: lambda/activity/service/wait
- Workflow types: Express (at least once, 5 minutes)/Standard( Exact once, 1 year)

# SQS

- max size for a message is 256k, the large file can use S3 link instead
- has a FIFO model. but 300 message/s without batching, batching is 3000 message/s, which means batch size is maxium 10.

- Dead letter Queue.after a threshold times of processing, the message can send to DLQ, it must same type of the original queue. good for debug failure message. it can has a retention day. we can redrive message in DLQ back to normal queue.

short polling: query subset of servers then return, may not return all the messages in first response.
long polling: query all the servers then return, only timeout will return empty message.
visibility timout:a period of time during which Amazon SQS prevents all consumers from receiving and processing the message
SQS doesn't allow a message be consumed by multi consumer at the sam time.
Message timers let you specify an initial invisibility period for a message added to a queue.

# Amazon MQ

A manged message broker service of AWS for RabbitMQ and ActiveMQ, you can just replatform you MQ rather than refactor to use SQS.

# AWS SNS

1. up to 12.5m subscriper for each topic;each account can have 100k topics be default
2. there is a message filter feature to let subscripter only take special message in that topic
3. SNS ensured FIFO per topic
4. compare eventbridge, eb has more targets and more focus on event driven architecture, SNS is more focus on pub/sub
5. SNS+SQS: fistributed one requets to multi SQS, support cross region communication
