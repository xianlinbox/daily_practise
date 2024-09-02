## The Terminology of AWS IAM

### Control Tower

- Set up and govern a secure, well-architected multi-account AWS environment (aka Landing Zone)

* Guardrails are used for goverance and compliance:

  - Preventive: disallow actions

  - Detective: monitor/report/scan

* Steps to setup Control Tower:
  1. Choose Region and define region accessibility
  2. Create OU(Organisation Unit), Security OU by defaut, we can create more OU.
  3. Create Accounts
* In Control Tower, we can move existing OU and enroll existing account under control.

### Organisation

An account management service that enables you to consolidate multiple AWS accounts into an organization

- Focus on account management and consolidated billing capabilities

OrganizationAccountAccessRole/ManagementAccount:

- admin permission for account management

* Accounts create with Organisation got it automatically

Multi-Account Strategy inside Orgnisation:

1. Create Account per Department, each department manage account can create account for each env (dev/qa/prod)
2. Use Tag standards for billing purpose
3. Cloud Trail/Cloud watch logs for Goverance
4. Create an account for security

Benefits inside one Organistion:

1. Pricing benefits/ Savings plan discount
2. Sharing or not reserved instances betweens accounts in this OU

Moving Accounts

1. Remove from Old OU
2. Sent invitation from new OU

Available Feature sets:

- All features: default one which can use all features
- Consolidate billing feature: basic management,can't set SCP for all accounts

## SCP (sevice control policy)

- SCPs affect all users and roles in attached accounts, including the root user. The only exceptions are those described in Tasks and entities not restricted by SCPs. It has no effect on service-link Role
- The following elements aren't supported in SCPs: Principal/NotPrincipal/NotResource

### AWS Config

Manage config rules cross all the accounts in the organisation,ue to assess, audit, and evaluate the configurations of your AWS resources.

- it allows to remediate the resources are not compliance with config rules; use SSM or APIs

### User

For long term credential

### Role

Short term credential, use STS

- Instance Role
- Service Role
- Cross Account Role

Assume a role will get new role priviledge but lost the old ones. we can use resource based policy to give both user priviledge.

### Group

grouped policy to easier assign multi policy to multi users/roles

A security group controls the traffic that is allowed to reach and leave the resources that it is associated with

when we create a security group, it has no inbound rule and an outbound rule to all traffic out.
the traffic is stateful, request is in and repsonse can out no matter what the outbound rule is.

security group is not a valid condition/principal in Policy or a

### Policy

Define what a User/Role can/Can't do

- AWS Managed Policy
- Custom Policy
- Inline Policy
- Resource-based policy

Anatomy: json document with effect, action, resource, condition, policy variables
Deny has precedence over Allow
Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization.

Organisation level/Acoount -> SCP; User/Role -> Permission boundary;

### STS: Security Token Service

Assume user a role, Provide access to resources temporarily
Ability to revoke active sessions and credentials for a role.

### AWS Resource Access Manager

Share resources you own to other account within your org.
Avoid resource duplication

The Resouce can be shared:

1. VPC Subnet, Prefix List
2. Route53 Resolver rules
3. ...

## Federation & Cognito

- Give user out of AWS access to AWS resources.
- Support any SAML2.0 and Microsoft AD identity providers, implemented by AssumeRoleWithSAML.
- AWS SSO is new federation way replace old SAML2.0
- For not support SAML Identity provider, we need to custom identity broker to do the AssumeRole work by ourselves.

WebIdentity without Cognito (Not recommend)

1. Get webidentity from Google/Aamzon ...
2. AssumeRoleWithWebIdentity
3. Use this new role to access AWS resources

WebIdentity with Cognito (recommend)

1. Get web identity from Google/Aamzon ...
2. Exchange web identity with coginito for a cognito token
3. Use cognito token to AssumeRole
4. Access resource with short term credential

Add IAM policy by condition to limit web identity access priviledge

## Best Practices

1. Use least priviledge

## Tools

- Access Advisor:
- Access Analyzer: Policy Validation/Policy Generation, cannot be used for near real-time detection

## Tips:

1. Not Action vs Deny: Not Action which allow you to add Action in another policy.
2. AWS CloudTrail — Provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services.
3. we can't have user defined in both SSO and AD at the same time.
4. Group & users are link to single account, can't assign a user to another account's group

## IAM Role

It has 3 permission policies:

1. Permission policies: after assume this role. what you can do.
2. Permissions boundary: set the maximum permissions that an identity-based policy can grant to an IAM entity.
3. Trust relationship: define which principal can assume this role.

### process for assume role cross AWS accounts

1. In destination account, create a IAM role and attach the permission for the work and trust policy for who can assume this role.
2. In source account, add IAM policy to allow your worker resource to assume the IAM role and do the work.

Lambda don't have service-linked roles.

### Confused Deputy Problem

we trusted a company, it can use AssumeRole to get the pemission to access AWS resource, another client of this company may also get the permission. this is called deputy problem.

1. Including the external ID condition in the role’s trust policy.
2. Company in charge of generate unique external ID to different client
3. config external ID in the trust policy.
