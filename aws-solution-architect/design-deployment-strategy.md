After setup the environment, Next step we need to take is deploy the resources we needed to AWS cloud. AWS also provide a bunch of services to support apply industry best practices into deployment strategy. But to be honest, in this field, there is already a very mature ecosystem/community exists, like terraform, Github actions etc. They already build some kind of industry standard, most user will intgerate AWS cloud deployment with them, rather than choose AWS provided services.

So in this episode, let's just quickly go throug what kinds of services AWS provide, and what kind of deployment strategy it support.

## Infra

Deploying Infra

- Cloud Formation

Updating Infra

- AWS System Manager

## Application

Deploying App

- CI/CD pipeline in AWS
  - CodeCommit
  - CodeBuild
  - CodeDeploy
- ML in CI/CD
  - SageMaker

Updating App

## Deployment Strategy

- In place
- Linear
- Blue/Green
- Canary
- All at once

Conclusion
