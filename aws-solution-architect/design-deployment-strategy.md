After setup the environment, Next step we need to take is deploy the resources we needed to AWS cloud. AWS also provide a bunch of services to support apply industry best practices into deployment strategy. But to be honest, in this field, there is already a very mature ecosystem/community exists, like terraform, Github actions etc. They already build some kind of industry standard, most user will intgerate AWS cloud deployment with them, rather than choose AWS provided services.

So in this episode, let's just quickly go throug what kind of deployment services AWS provided, and what kind of deployment strategy it support.

## Infra(Cloud Formation)

For deployment resources into AWS, AWS provide CloudFormation, a powerful tool for infrastructure as code (IaC), allowing you to define and manage AWS resources in a declarative way. It lets you model, provision, and manage AWS infrastructure using templates. These templates describe the desired state of your infrastructure and CloudFormation ensures resources match that state.

### Components:

- template in json/yaml: Define AWS resources and their configurations
- stacks: A collection of resources defined by a template and managed together
- stacksets: Create and manage stacks across multiple AWS accounts and regions. StackSets work best with AWS Organizations for automatic account management, managed in managed account.

### Best practices:

- Use drift detection to identify manual changes and keep consistency
- Use Changsets to preview changes before applying them to a stack.
- Changes to a stack can impact running resources. Test updates in a non-production environment first.
- Reuse templates by referencing them within other templates.
- Use StackSets to provision resources in multiple accounts and regions.

## Serverless Application

AWS provide SAM (Serverless Application Model) for building serverless applications. It extends AWS CloudFormation to simplify the deployment and management of serverless resources such as AWS Lambda, API Gateway, DynamoDB, and more. it supports:

- Encourages the use of environment variables, monitoring, and tracing via AWS X-Ray.
- Local Development and Testing.
- Package and deploy applications to AWS with a single command.
- Cross-Service Integration: Seamlessly connects Lambda with other AWS services like S3, DynamoDB, SNS, SQS, etc.

The process to use SAM:

1. Define your application in a SAM template (template.yaml).
2. Use the `sam build` command to compile dependencies and prepare your application.
3. Use `sam local invoke` or `sam local start-api` to test Lambda functions or APIs.
4. Package and deploy with `sam deploy`.

## Standard Application

AWS provided a bunch of tools to support industry CI/CD pipeline to build/deploy your application:

### AWS CodeCommit:

- Managed Git-based repository for storing source code.
- Supports version control and integration with other AWS services.

### AWS CodeBuild:

- Fully managed build service to compile code, run tests, and produce build artifacts.

### AWS CodeArtifact:

- Manages software packages and dependencies for builds. can use ECR/S3 to save artifact

### AWS CodeDeploy:

- Automates deployments to services like EC2, Lambda, or on-prem servers.

### AWS CodePipeline:

- Orchestrates the CI/CD process, integrating all stages like source, build, and deploy.

### SageMaker

- CI/CD pipelines to streamline the process of building, training, and deploying machine learning (ML) models.

## Deployment Strategy

AWS provides several strategies to ensure that deployments are efficient, reliable, and scalable, we nee to choose the correct one based on our business requirements, service architecture, and risk tolerance:

### In place

the previous version of the application on each compute resource is stopped, the latest application is installed, and the new version of the application is started and validated.

- deploy application without creating new infrastructure
- the availability of application can be affected during deployments
- can be all-at-once or done as a rolling update.

### Linear

Linear deployment means traffic is shifted in equal increments with an equal number of minutes between each increment. You can choose from predefined linear options that specify the percentage of traffic shifted in each increment and the number of minutes between each increment.

- Suitable for applications that can tolerate some downtime during updates.
- Reduces risk by limiting the number of instances affected at any given time
- support: Elastic Beanstalk, AWS CodeDeploy with EC2, Lambda, ECS, and on-premises servers.

### Blue/Green

releasing applications by shifting traffic between two identical environments running differing versions of the application

- minimize downtime during application updates
- Reducing risk by validating the new version before making it live.
- supports: Elastic Beanstalk, AWS CodeDeploy with EC2 instances, Lambda, and ECS.

### Canary

incrementally deploy the new version, making it visible to new users in a slow fashion. As you gain confidence in the deployment, you will deploy it to replace the current version in its entirety.

- Testing new features on a small percentage of users.
- Minimizing risk in production environments.
- Support: AWS CodeDeploy with EC2, Lambda, and ECS. No Beanstalk

### All at once

all traffic is shifted from the original environment to the replacement environment all at once.

## Conclusion

Based all the info above, the steps to build your deployment pipeline will be:

1. Collecting all the respurces need to deploy
2. Have a clear idea about location
