# Beanstalk

a developer centric view of app deployment, it deploys all the components aws managed. good for replatfotm your on-prem app to cloud

Managed service , control instance and os config by beanstalk,

Architecture model:

- Single instance
- ALB + ASG
- SQS + ASG only

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
Custom Resource
Stack Sets: deploy to multi accounts in OU
Drift: alert manual changes out of CF
Resource Input

# Service Catalog

Admin created the services can be used. each service is a cloud formation template. help new user to know what they can get or use
User use this service to get the AWS resources it needed.

# SAM

serless application model: use for deploy serverless application. it can help to shift the traffic between new version and old version.

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
