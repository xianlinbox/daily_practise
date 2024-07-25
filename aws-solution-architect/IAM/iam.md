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

### Group

### Role

### Policy

- AWS Managed Policy
- Custom Policy
- Inline Policy

### Permission Boundaries

### Organisation SCP

#### Policy Schema

### STS: Security Token Service

## Best Practices

1. Use least priviledge

## Tools

- Access Advisor:
- Access Analyzer:

## Tips:

1. Not Action vs Deny: Not Action which allow you to add Action in another policy.
2. AWS CloudTrail — Provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services.
