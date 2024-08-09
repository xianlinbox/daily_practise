# CloudWatch

Metrics:have default one and can create custom ones.
Alarms: can trigger actions or send to eventbridge.
Dashboards: show metrics of multi regions

Synthetics Canary: configurable script to monito app api,url; can integrate with Alarms. it provide blueprints for common tasks.

Track IP address need access log or cloud trail data event.
Cloud watch agent can't publish data to firehose stream.

## Event Bridge

Defaut event bus/Partner Event Bus/ Custom Event Bus

Partners: Datadog/Zendesk to partner eventbus

Archive events and replay archive events

event schema registry and versioned to understand the schema of events

Resource based policy to allow diff accounts publish to event bus

# X-Ray:

Visual analysis of our application
Tracing request in distributed systems

# Personal Health Dashboard

1. global sevice
2. show how aws outage impacts you
