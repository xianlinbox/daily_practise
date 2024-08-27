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

## Termination protection

prevent your instance from being accidentally terminated, you can enable termination protection for the instance. The DisableApiTermination attribute controls whether the instance can be terminated using the AWS Management Console, AWS Command Line Interface (AWS CLI), or API. It didn't protect ASG scaling.

## Lauch Configuration

A launch configuration is an instance configuration template that an Auto Scaling group uses to launch EC2 instances.
When you create a launch configuration, the default value for the instance placement tenancy is null and the instance tenancy is controlled by the tenancy attribute of the VPC.

LC(null/default) + VPC(dedicated) => dedicated
LC(dedicated) + VPC(default/dedicated) => dedicated
LC(default/null) + VPC(default) => shared

## Change Subnet

It's not possible to move an existing instance to another subnet, Availability Zone, or VPC. Instead, you can create a new Amazon Machine Image (AMI) from the source instance to manually migrate the instance.

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
3. Rebalancing AZ: start new one then terminate old one.
4. ASG Scaling sequence: terminate unhealthy one, start the new one

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

By default, it runs in AWS owned VPC, has public access, if VPC-enabled, it will only access your VPC network.

layers: help lambda to reuse code

# # Load Balancer:

CLB -> ALB/ELB (Http/webcocket)/NLB (TLS/TCP; high performance, low latency)/GWLB (ip level)
Cross Zone Load balancing (diff LB has different setting and charges)
Sticky Session
Routing algorithm:(LOR,Round Robin, Flow Hash)
Don't support cross region load balancing

ALB can't assign IP, if you need an IP, you need to put a NLB before it and assign IP to the NLB.

Target types: instance ID/IP/ALB

ALB vs ELB

| item              | ALB                           | ELB                        |
| ----------------- | ----------------------------- | -------------------------- |
| protocols         | HTTP/HTTPS/grpc               | TCP/UDP                    |
| traffic spikes    | need to report to AWS support | handle by itself           |
| static ip         | not suppport                  | support                    |
| TLS termination   | yes                           | yes                        |
| Targets           | instance id, ip, lambda       | instance id/ip/ALB         |
| routing algorithm | LOR,RR,                       | flow hash, random          |
| maximum targets   | 1000-5000                     | 500-1000                   |
| security group    | target reachable to ALB only  | target reachable to client |
| WAF               | yes                           | no                         |
| Authentication    | yes                           | no                         |
| Sticky Session    | yes                           | no                         |

Global Accelerator can do similar thing as NLB. But more expensive

# API Gateway:

compare ALB, it provides limit/authentication/cache and more functionalities
Limits: 29s timeout/10M payload
Endpoint Types:

1. Edge Optimized: For geographically distributed clients, default one. it route api call to the nearest CloudFront location then internal to api gateway.
2. Regional: for clients in the same region
3. Private: can only be accessed from your Amazon Virtual Private Cloud (VPC) using an interface VPC endpoint

Cache: 0.5G-237G, per request URL, can manually refresh

Usage Plans & API keys: we can config the limits for each client. client are identified by API key.

Web Socket API:stateful/bi-direction, use case:chat
Private API gateway: only accessiable from VPC interface endpoint
For an API Gateway, a "504 Gateway Timeout" error implies an "Endpoint Request Timed-out Exception".

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

## Health Checker

Monitor the health and performance of your web applications, web servers, and other resources.

The type for health check:

1. Endpoint (in or out AWS)
2. Compute metrics from other health checks
3. Cloudwatch metrics alarms (not the metrics)

- we can use Application Recovery Controller to set up routing control health checks with DNS failover records to manage traffic failover for your application.
- if monitor endpoint with domain name , it will only use IP v4 to monitor. as the health check is outside the VPC. so the endpoint must have a public IP.
- build connection within 4s, then return http code in 2s.
- Https health checks don't validate SSL/TLS certificates, so checks don't fail if a certificate is invalid or expired. But the endpoint must support TLS 1.0+
- additional charge apply to no AWS endpoint. even the health check is disabled.
- 18% report healthy is healthy for ROute 53
- Support TCP, need to build connection in 10s

Hybrid DNS:
Resolver Rules:

- Inbound Resolver Endpoint
- Outbound Resolver Endpoint

# Global Accelerator & Cloud Front

They both use edge location and support shield

Accelator is more for redirect, can also work for TCP/UDP, MQTT, ip -> endpoints, can used for distribute traff
Global Accelerator can only to: ELB/ALB/EC2/Elastic IP.

CloudFront is more for CDN, DNS -> IP, if DNS cached, CloudFront can't help on anything.

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

# System Manager

an AWS service that you can use to view and control your infrastructure on AWS.AWS Systems Manager Agent (SSM Agent) is Amazon software that can be installed and configured on an EC2 instance, an on-premises server, or a virtual machine (VM). SSM Agent makes it possible for Systems Manager to update, manage, and configure these resources.

System Manager supports an SSM document for Patch Manager. AWS-RunPatchBaseline, which performs patching operations on instances for both security-related and other types of updates. AWS-ApplyPatchBaseline SSM document supports patching on Windows instances only
