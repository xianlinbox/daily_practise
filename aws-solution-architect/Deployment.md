# Beanstalk

a developer centric view of app deployment, it deploys all the components aws managed. good for replatfotm your on-prem app to cloud
Just need to provide the code.

Managed service , control instance and os config by beanstalk,

Architecture model:

- Single instance
- ALB + ASG
- SQS + ASG only

Support Blue/Green deployment, but need to decouple production database first.

# Code Deploy

Instances are not managed by Beanstalk
Can deploy to EC2/ASG/ECS/Lambda
Appsec.yml + deployment strategy
Use hooks to verify deployment
Rollback with cloud watch Alarm
Deploy to ASG: In-place update/ green-blue deployment(must have ELB)

# Cloud Formation

IaC on AWS. backone for most of deploy service (Beanstalk, CodeDeploy)

Retain Policy
Custom Resource: enable you to write custom provisioning logic in templates that AWS CloudFormation runs anytime you create,
Stack Sets: deploy to multi accounts in OU
Drift: alert manual changes out of CF
Resource Input

## Term

1. template: blueprints in JSON/YAML format
2. Stack: a singe resource unit
3. Changeset: a summary of you proposed changes
4. stackset: A stack set lets you create stacks in AWS accounts across regions by using a single CloudFormation template. it is a regional resource
5. stack instance: a reference to an attempted or actual stack in a given account within a given Region.

# Service Catalog

Admin created the services can be used. each service is a cloud formation template. help new user to know what they can get or use
User use this service to get the AWS resources it needed.

# SAM

serless application model: use for deploy serverless application. it can help to shift the traffic between new version and old version.

1. Deploys new versions of your Lambda function
2. Gradually shifts customer traffic to the new version
3. Defines pre-traffic and post-traffic test functions to verify that the newly deployed code is configured correctly
4. Automatically rolls back the deployment if CloudWatch alarms are triggered

# Cloud Devlopment Kit

generate code to cloud formation template

# System Manager

need to install SSM agent, AWS AMI have it by default.
Run command on all the instances
no need SSH, it is an api call
Session manager provide a secure ssh between ec2 to local device
OpsCenter: create opsitem then SSM automation run command to fix it
Patch Manager:define patchbaseline, then run on all the services. Apply to both windows and linux: AWS-RunPatchBaseline

# Cloud Map

Resoucer discovery service

# Server Migration Service

automates the migration of your on-premises VMware vSphere, Microsoft Hyper-V/SCVMM, and Azure virtual machines to the AWS Cloud

# Blue/Green Deployment

Blue/Green deployment:uses two identical environments, one running the current version and the other running the new version. Traffic is switched between the environments, allowing for quick rollbacks if issues arise.

Canary Deployment: gradually rolls out updates to a small subset of users, allowing for early issue detection without affecting all users. Opswork doesn't support it.

Support service:

1. Route53: direct traffic by simply updating DNS records in the hosted zone
2. ELB: distributes incoming application traffic across designated EC2
3. EC2 ASG : attach different versions of launch configurations to an auto scaling group to enable blue/green deployment. auto scaling's termination policies and Standby state allow for blue/green deployment easier rollback.
4. OpsWorks: OpsWorks simplifies cloning entire stacks when you’re preparing blue/green environments.
5. CloudFormation: provides very powerful automation capabilities for provisioning blue/green environments and facilitating updates to switch traffic, whether through Route 53 DNS, ELB, or similar tools
6. CodeDeploy: Blue/Green deployment is a feature of CodeDeploy. CodeDeploy can also roll back deployment in case of failure. You can also use CloudWatch alarms to monitor the state of deployment and utilize CloudWatch Events to process the deployment or instance state change events.
7. Beanstalk: Beanstalk helps you run multiple versions of your application and provides capabilities to swap the environment URLs, facilitating blue/green deployment.
