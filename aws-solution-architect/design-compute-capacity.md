In the last episoed, we talked about how to move data to cloud, how to manage data and how to do the data analytics.
this episode, we gonna focus on the compute part, where and how is our code runinng in AWS cloud.

# Serverless Part

## Lambda

a serverless compute service that runs code in response to events and automatically manages the underlying compute
resources.

- for short live task, max execution time: 900 seconds
- use IAM for access control, can enable with VPC to access private resources
- config with memory, cpu goes with memory, up to 10GB
- deploy artifact: zip/image, size: 50mb to 250mb
- concurrency: default 1000 per account , can increase. there are 2 concurrency mode:Reserved/Provisioned

Lambda@Edge

Specific lambda which runs serverless code closer to users at AWS edge locations. it is tightly integrated with
CloudFront.

- size up to 10MB
- Customize and manipulate HTTP requests/responses with Amazon CloudFront
- Perform user authentication and authorization at the edge
- Modify headers or cache keys for CDN optimization.
- Serve different content dynamically based on geographic location or user attributes

## AppRunner

A service that allows you to deploy web applications and APIs from source code repositories or container images.

- Automatic Scaling
- built in load balancer
- source integartion: code repo/image registry
- customize through environment variable

## Batch

a fully managed service that enables you to run batch computing workloads at any scale

Components:

- Job definition
- Job Queue: manage the jobs to be processed, can create multiple queues with different priorities
- Compute environment: AWS infrastructure resources used to run your jobs, automatically scale to meet the job
  requirement.

# EC2 based part

## EC2

scalable virtual servers (instances) to host applications

Instance Types: GP/Compute/Memory/Storage/Accelerate for different purpose

Price model:

- On-demand: Pay per second, no commitment
- Reserved: Up to 75% discount for 1- or 3-year commitments
- Spot Instance (Draining): Up to 90% savings; ideal for fault-tolerant workloads.
- Saving plan: Flexible savings with commitment to compute usage.
- Delicated Host/Instance: Dedicated hardware for regulatory needs.

Placement Group:

- Cluster: low latency
- Spread: Fault tolerant
- Partion: Fault isolation

Advanced Features:

- Enhanced Networking (ENA, EFA): Improved bandwidth and lower latency for HPC.
- Burst Performance: temporarily provide higher CPU performance than their baseline.

## Beanstalk

a fully managed Platform-as-a-Service (PaaS) that simplifies the deployment, scaling, and management of applications
Compare to ECS, Beanstalk is easier to use but may result in higher costs due to resource overprovisioning.

- support: Node.js, Python, Java, .NET, PHP, Ruby, Go, and Docker

Process:

1. Code Deployment: upload code or image, then beanstalk will config all the infra needed, lik EC2, Load balancer
2. Configuration: config environment variables, instance types, scaling parameters etc through beanstalk management
   console
3. Manage environments: sets up the operating system, middleware, and runtime for your application.

Features:

- Environment Management: provide staging, and production env, and allow one click to deloy to different env. support
  blue/green deployment.
- Auto scaling and integrated with ELB
- health monitoring
- Automatic Patching

## Lightsail

a simplified platform for deploying and managing virtual private servers (VPS) and applications

- Pre-configured Instances
- simplified ec2 with less config and predictable cost
- less scability, small application

## Outposts

A fully managed service that extends AWS infrastructure, services, APIs, and tools to on-premises environments, allowing
you to run applications with low latency or data residency requirements seamlessly.

Components:

- Outpost Racks: hardware rack with compute and storage resources.
- Local Gateway: Provides local network connectivity to on-premises infrastructure.
- AWS Region Connectivity: Requires a connection to an AWS Region for control plane operations, updates, and management.

# orchestration

## AWS StepFunction

a fully managed serverless orchestration service that lets you coordinate and manage distributed applications or
workflows using visual workflows.

Components:

- State Machine: A JSON-based definition of the workflow.
- State: Task/Choice/Parallel/Map/Pass,Fail,Wait
- Input/Output: Passes JSON data between states.

Type:

- Standard: for long-run work, running time up to 1 year.
- Express: for short-live work, running time up to 5 minutes

The workflow can be synchronous (wait for result) or asynchronous(don't wait for result)

## ECS

a fully managed container orchestration service that enables you to run and scale containerized applications on AWS.ECS
can be cheaper than Beanstalk, particularly for containerized applications or workloads with dynamic scaling needs.

Launch Type:

- EC2: Managed EC2 Instances/Full control, you chose the EC2 instance to run the application
- Fargate: serverless,only specify the CPU and memory requirements for your containers. Fargate handles the
  provisioning, scaling, and running of containers.

Components:

- Task: a running instance of a containerized application.
- Service: allows you to run and maintain a specified number of instances of a task definition simultaneously
- Scheduler:

Networking:

- Bridge: shared host's network stack, good for containter to container communication
- Host: shared the ec2 instance network space. good for performance sensitive
- AwsVpc: containers get their own ENI. good for isolation workload

IAM roles can be assigned to tasks, allowing them to interact with AWS services

## EKS

a fully managed service that makes it easy to run Kubernetes on AWS without needing to install and operate your own
Kubernetes control plane.

- Supports Hybrid/Multi-Region Deployments:
- Fully Compatible with Kubernetes

Worker Node Options:

- AWS managed
- self managed
- Fargate

Networking Modes:

- VPC ENI pugin
- Third party like calico

## Fargate

a serverless compute engine for containers that allows you to run and manage containers without managing the underlying
infrastructure.

- intgrated with ECS/EKS seamlessly
- Task-Level Isolation, each task runs in its own environment.
- Integrated with IAM for access control, the role can assign at task level
- pay by seconds based on vCPU and memory resources allocated to the containers.

Limitations:

- more expensive for consistent, high workloads
- less config compare manage EC2 directly
- No GPU support

# Conclusion

Based on the information above, when we choose the compute components, you need to:

1. Figure out your task characteristic:

- Just a simple api, or need to load a lot of data.
- How long it will run?
- It meed more CPU, I/O or memory
- Any limitations? like must run in local

2. Figure out your team's capability

- Does your team have infra capbilities to manage instance by yourself
- Does You team have knowledge about docker, K8s.
- ...

The first one will narrow down the compute node and its type we can choose, the second one will decide how we manage the
compute notes.
