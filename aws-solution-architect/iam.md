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
- Access Analyzer: Policy Validation/Policy Generation

## Tips:

1. Not Action vs Deny: Not Action which allow you to add Action in another policy.
2. AWS CloudTrail — Provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services.
