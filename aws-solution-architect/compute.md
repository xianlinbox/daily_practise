# EC2

## Types

R for Ram/C for cpu/I for io/M for medium/G for gpu

## Placement Groups

cluster/spread/partition
we can move instance between groups

## Launch Types

On-Demand: short, predicatable pricing,reliable
Spot: short, cheap, not reliable
Reserved: (long workload, min 1 year)
Dedicated instance: no share hardware
Dedicated host: own physical server, good for license at core/cpu level
Graviton 2/3: best pricing, only support linux. use for caching,HPC

## Metrics

RAM is not included in the metrics

## Recovery

we can use cloud alarm to recovery failed instance with same config

# High Performance Computing

Services to help HPC:

1. Data Management & Transfer

- Direct Connect
- Snowball & SnowMobile
- AWS DataSync

2. Computing Network

3. Storage

4. Automation and orchestration

# Auto Scaling Group

1. Instance Refresh
2. Update Strategy
   can't be triggered by S3 event directly

# ECS/ECR/EKS/Fargate

ECS components:

- ECS Cluster
- ECS Service
- Task Definition
- Tasks: an instance of task
- ECS IAM role

Integated with ALB, Parameter Store, Secrets Manager

Networking:

- None
- Bridge
- Host
- awsvpc

Fargate:

ECR: support cross-region/cross-account replication

EKS:

App Runner: similar as Heroku,easy way to deploy web appliction/API in AWS, it's a regional service, can only use in one region

ECS/EKS Anywhere: run containser service in on-prem infra

# Lambda

limits: memory/storage/CPU/Runtime/language/concurrent/size

CPU is not configurable, it go with RAM, more RAM means more CPU

# # Load Balancer:

CLB -> ALB (Http/webcocket)/NLB (TLS/TCP; high performance, low latency)/GWLB (ip level)
Cross Zone Load balancing (diff LB has different setting and charges)
Sticky Session
Routing algorithm:(LOR,Round Robin, Flow Hash)

# API Gateway:

compare ALB, it provides limit/authentication/cache and more functionalities
Limits: 29s timeout/10M payload
Endpoint Types:

1. Edge Optimized
2. Regional
3. Private

Cache: 0.5G-237G, per request URL, can manually refresh

Usage Plans & API keys: we can config the limits for each client. client are identified by API key.

Web Socket API:stateful/bi-direction, use case:chat
Private API gateway: only accessiable from VPC interface endpoint

# App Sync

AWS version GraphQL, can integrated with AWS cognito

# Route 53

Map hostname to IP

CNAME: map a host name to another one
Alias: Map a hostname to an aws resource (can't do it for an EC2 DNS name)
Records TTL: save traffic to ROute 53
Routing policy for multi records: return all client chose/ weighted/ latency based/ failover/ geo-location/ip-based routing
Traffic Flow: setting management for complex routing

Hosted Zones: A container of records defines how to route traffic

- Pulic Hosted Zones:
- Private Hosted Zones:

DNSSEC: securing DNS traffic
Health Check
Hybrid DNS:
Resolver Rules:

- Inbound Resolver Endpoint
- Outbound Resolver Endpoint

# Global Accelerator & Cloud Front

They both use edge location and support shield
Accelator is more for redirect, can also work for TCP/UDP, MQTT
Cloud Front is more for for CDN

# Architecture Style

1. EC2 with elastic ip
2. Ec2 instances with route 53
3. ALB with Auto Scaling Group
4. ALB +ECS (backed by ASG or Fargate)
5. ALB + Lambda
6. API Gateway + Lambda
7. API gateway + AWS services
8. API Gateway + HTTP server backend

# AWS outpost

Build AWS service on company's data center, it can extended to cloud if needed.

# AWS wave length/Local Zones

Wave Length: Deloy service in the edge device and get extremely low latency service.
Local Zones: Amazon provided more detail local zone

# Edge Optimized

use an ACM certificate with an API Gateway edge-optimized custom domain name, you must request or import the certificate in the us-east-1 Region.
