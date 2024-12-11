In last episode, we have make all the components in the system connected with each other, the next step we need to make sure the resources are accessed securely. In this episode, we gonna talk about the security strategy.

when talking about security in AWS, The shared responsibility model are always mentioned:
![Shared Resposibility Model](https://d1.awsstatic.com/security-center/Shared_Responsibility_Model_V2.59d1eccec334b366627e9295b304202faf7b899b.jpg)

As a solution archiect, your job will be using security mechanism in AWS to cover the customer parts.

# The Security Mechanism in AWS

AWS provides a comprehensive suite of security mechanisms designed to protect infrastructure, data, and applications. we need to understand them and know how to apply them based on business requirement.

## Identity

In the multi-account strategy episode, we have talked about the organisation, OU and account. also about apply SCP at the OU/Account level to limit permission. Inside each account, AWS provide IAM to group and manage identity. An IAM identity represents a human user or programmatic workload that can be authenticated and then authorized to perform actions in AWS accounts.

### account root user

When you first create an Amazon Web Services (AWS) account, the email address and password you provide are the credentials for your root user, which

- has access to all AWS services and resources in the account.
- suggest to working with organisation for better management
- play tasks that require root user credentials

### users

An IAM user is an entity that you create in your AWS account. The IAM user represents the human user or workload who uses the IAM user to interact with AWS resources. An IAM user consists of a name and credentials.

- an user with admin priviledge is not same as root user
- defined within AWS account, only associated with one AWS account
- when IAM user are present as a service account, use its credentials to make AWS requests. remembee to store access key in a safe place(eg: secret manageer).

### user group

a collection of IAM users.

- user group can contain many users, and a user can belong to multiple user groups
- can't be nested
- no default user group include all users

### role

an IAM identity that you can create in your account that has specific permissions

- intended to be assumable by anyone who needs it.
- no standard long-term credentials,just a temporary security credentials for your role session
- use to delegate access to users, applications, or services with assume role.

### identity providers and federation

manage your user identities outside of AWS and give these external user identities permissions to use AWS resources in your account. eg: Microsoft AD etc

- support OIDC and SAML protocol, OIDC is commonly used when an application that does not run on AWS needs access to AWS resources.

### Temporary Security Credentials

use AWS Security Token Service (AWS STS) to create and provide trusted users with temporary security credentials that can control access to your AWS resources

- short-term, not stored, retrieve dynamically when need one.
- STS is global service, but support regional endpoint.
- implement with AssumeRole/AssumeRoleWithSAML/AssumeRoleWithWebIdentity/GetSessionToken/GetFederationToken

Common scenarios:

- Identity federation
  - OpenID Connect (OIDC) federation supports Login with Amazon, Facebook, Google, and any OpenID Connect (OIDC)-compatible identity provider.
  - SAML federation, support SSO with Microsoft AD
- Access delegation: using AssumeRole and trust policy to grant principal in another account to access your account's resources.
  - when delegate access cross account ,use trust policy with external ID to avoid confused deputy problem
  - when delegate access cross service ,use trust policy with aws:SourceArn, aws:SourceAccount, aws:SourceOrgID. or aws:SourceOrgPaths global condition context keys to avoid confused deputy problem
- Use GetSessionToken to do MFA validation
- Use GetFederationToken to build a proxy-authorizaion

## Access Management

Identity just give you an unique principal let system know who you are, what you can do (permissions) are defined in the attached policy.

### Policy

A policy is an object in AWS(mostly a json document), associated with an identity or resource, defines their permissions. AWS evaluates these policies when an IAM principal (user or role) makes a request. Permissions in the policies determine whether the request is allowed or denied. There are different kinds of policies AWS support:

#### Organizations SCPs

define the maximum permissions for IAM users and IAM roles within accounts in your organization or organizational unit (OU)

- apply at Organisation/OU/Account level
- only limit permissions, does not grant permission

#### Organizations RCPs

define the maximum permissions for resources within accounts in your organization or organizational unit (OU)

- apply at Organisation/OU/Account level
- same as SCPs, only limit permissions, does not grant permission

#### Permission Boundary

Using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity

- apply to IAM entity (user, user group, role)
- only limit permissions, does not grant permission
- only limit identity-based policy, not impact resource-based policy.

#### Identity-based Policies

grant permissions to an identity (user group, user or role)

#### Resource-based Policies

Attach inline policies to resources,grant permissions to the principal that is specified in the policy

- principal can cross-account
- support resources: S3/KMS/SQS/SNS/Lambda/EventBridge/IoT/SecretsManager
- eg:S3 bucket policies and IAM role trust policies

#### Access control lists

control which principals in other accounts can access the resource to which the ACL is attached. similiar to resource based policy

- only policy type that does not use the JSON policy document structure
- cannot grant permissions to entities within the same account
- support service: S3/VPC/EFS/SQS/Directory Service/CloudFront

#### Policy Evaluation

1. By default, all requests are implicitly denied
2. An explicit allow in an identity-based or resource-based policy overrides this default.
3. If a permissions boundary, Organizations SCP or session policy is present, it might override the allow with an implicit deny.
4. An explicit deny in any policy overrides any allows.

## Data Security

Data

- encrypt at rest
  - which kms use
  - conig rule
  - cloud trail for auditing
- encypt at transit
  - vpn
  - inter-network
  - https and certificate

## Infra Security

Infra

- patch

## Tools

- An Amazon Cognito
- IAM access Analyzer
- IAM credential report

# Incident Response

# Conclusion
