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

### secuity features in VPC

- Security Group: allow specific inbound and outbound traffic at the resource level (such as an EC2 instance).
- Network ACL: allow or deny specific inbound and outbound traffic at the subnet level
- BPA(Block Public Access): centralized security feature that enables you to authoritatively prevent public internet access to VPC resources

### security features in S3

- BPA(Block Public Access):controls across an entire AWS Account or at the individual S3 bucket level to ensure that objects never have public access, now and in the future.

  - BlockPublicAcls: any put with public acl are blocked
  - IgnorePublicAcls: ignore all public ACLs on a bucket and any objects that it contains
  - BlockPublicPolicy: reject calls to PUT Bucket policy if the specified bucket policy allows public access
  - RestrictPublicBuckets: allow public policy to only AWS service principals and authorized users within the bucket owner's account and access point owner's account.

- Object Lock: blocks permanent object deletion during a customer-defined retention period.

## Data Security

With the above access control, we can make sure the resources are accessed by the correct principal. Another part for security is keep data safe. For Data security, there are 2 parts need to consider:

### encrypt Data at rest

For data encyption at rest, we have 2 options: server-side encryption and client-side encryption:

- server-side encryption.

  - encrypted data in cloud
  - easier to ensure encryption implemented correctly and applied consistently

- client-side encryption.
  - encrypted data in client application
  - ensure a consistent security posture as data traverses within our service architecture, whether in AWS, on-premises, or in a hybrid model.

Both of them can use AWS KMS to mange the encrytion key, and through the access policy in KMS to control who can decrypt the data. AWS KMS has 3 kinds of keys:

- Customer managed keys: The KMS keys that you create.
- AWS managed keys: KMS keys that AWS services create in your AWS account, can't modify. auto rotate each 1 year
- AWS owned keys: KMS keys that AWS services create in a service account

KMS doesn't support annonymous requests, so public access S3 object can't use it for encryption.
KMS support multi region keys. it's a primary-replica logic not a global one. process for encrypt and decrypt:

- encrypt: GenerateDataKey from KMS-> use data key to encrypt data -> Store the encrypted data key alongside the encrypted data
- decrypt: request KMS to decrypt the encrypted data key -> Use the decrypted data key to decrypt the data

#### CloudHSM

- A decdicated AWS provisioned encryption hardware
- Client manage their keys entirely
- Must use with HSM client software.

### encrypt Data in tansit

To protect data in transit, AWS encourages customers to leverage a multi-level approach. All network traffic between AWS data centers is transparently encrypted at the physical layer. All traffic within a VPC and between peered VPCs across regions is transparently encrypted at the network layer when using supported Amazon EC2 instance types. At the application layer, customers have a choice about whether and how to use encryption using a protocol like Transport Layer Security (TLS). All AWS service endpoints support TLS to create a secure HTTPS connection to make API requests.

- encypt at transit
  - vpn
  - inter-network
  - https and certificate

## Infra Security

Most the infra part are maintained by AWS. except

Infra

- patch

## Tools

- Amazon Macie
- An Amazon Cognito
- IAM access Analyzer
- IAM credential report
- AWS Security Hub
- AWS Network Firewall
- AWS Shield

# Conclusion
