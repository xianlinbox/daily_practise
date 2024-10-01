# EC2

## Types

R for Ram/C for cpu/I for io/M for medium/G for gpu

## Placement Groups

cluster/spread/partition
we can move instance between groups

An Elastic Fabric Adapter (EFA) is a network device that you can attach to your Amazon EC2 instance to accelerate High Performance Computing (HPC) and machine learning applications. EFA enables you to achieve the application performance of an on-premises HPC cluster, with the scalability, flexibility, and elasticity provided by the AWS Cloud.

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

Fargate: running containers in serverless way, the underline is EKS/ECS.

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
ALB node which is a dynamically defined high number port between 1024 and 65535.

least outstanding requests when the requests for your application vary in complexity or your targets vary in processing capability. Round robin is a good choice when the requests and targets are similar, or if you need to distribute requests equally among targets.

ALB vs NLB

| item              | ALB                           | NLB                        |
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

Global Accelerator can do similar thing as NLB. But more expensive.

Connection Draining: To ensure that an ELB stops sending requests to instances that are de-registering or unhealthy while keeping the existing connections open, use connection draining. This enables the load balancer to complete in-flight requests made to instances that are de-registering or unhealthy.

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

## REST API vs HTTP API

1. both RESTful API products. REST APIs support more features than HTTP APIs,
2. HTTP API is cheaper. REST API can provide a direct AWS Service integration, like Dynamo Tables

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

- Pulic Hosted Zones: contain records that specify how you want to route traffic on the internet
- Private Hosted Zones: contain records that specify how you want to route traffic in an Amazon VPC

DNSSEC: securing DNS traffic

## cross account Route53 config

An app in account A can't resolve CNAME records created in private zones of Route53 in account B. To make it possible, we need to:

1. From an instance in Account B, authorize the association between the private hosted zone in Account B and the virtual private cloud in Account A.
2. From an instance in Account A, create the association between the private hosted zone in Account A and the virtual private cloud in Account B.
3. Delete the association authorization after the association is created.

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
- If a record in a group of records that have the same name and type doesn't have an associated health check, treat it as healthy
- If none of the records in a group of records are healthy, choose one based on the routing policy
- All the records with non-zero weights must be unhealthy before Route 53 starts to respond to DNS queries using records that have weights of zero.
- active-active failover,Route 53 can respond to a DNS query using any healthy record; active-passive failover,Route 53 includes only the healthy primary resource, when all primary unhealth, include healthy secondary resources.

Hybrid DNS:
Resolver Rules:

- Inbound Resolver Endpoint
- Outbound Resolver Endpoint

# Global Accelerator & Cloud Front

They both use edge location and support shield

Accelator is more for redirect, can also work for TCP/UDP, MQTT, ip -> endpoints, can used for distribute traff
Global Accelerator can only to: ELB/ALB/EC2/Elastic IP.

GA provided custom routing accelerator, which allows use your own app logic to routing, this one only support VPC subnet endpoints, each containing one or more EC2 instances that are running your application

CloudFront is more for CDN, DNS -> IP, if DNS cached, CloudFront can't help on anything.

## GA vs Route53

1. Both can help routing traffic to specific resources
2. GA support static ip address to hide the backend complexity. Route 53 not support

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

# AWS Compute Optimizer

Using machine learning to analyze historical utilization metrics. Compute Optimizer provides a set of APIs and a console experience to help you reduce costs and increase workload performance by recommending the optimal AWS resources for your AWS workloads.
