When design a solution in AWS, the first thing we need to think is how to manage the resources created in AWS. Different client will have different requirements, AWS provide a bunch of tools to help on the account management. Let's go through them.

## AWS Organisation hierarchy

First thing we need to understand the concepts in AWS Organisation:

- Organization: A set of AWS accounts grouped together under a single AWS Organizations entity
- Organisation Unit: Subgroups of AWS accounts within an organization. OUs help you organize accounts by function, team, or environment.
- Accounts: AWS accounts are the fundamental containers for resources and billing.
- Management Account: The root account of the organization that has full administrative control
- Member Accounts: AWS accounts that are part of an AWS Organization

With the above concepts. An organisation structure can be created based on the requirement. Management account can create new account or invite existing account to join the Organisation, and assign them to an OU.

For this part, the most important thing is understandng the things can only done by Management Account:

1. Create organisation/OU
2. Account Management
3. Add goverance control (SCP), and didn't impact by SCP
4. Consolidated Billing, reallocate discounts, such as Reserved Instance or Savings Plans discounts, that the account receives
5. Cross-Account Resource Sharing through AWS Resouce Manager
6. Delegated Administration.
7. Fully unrestricted access to all the resources.

Based above, Management account should not be used on daily jobs:

- Use the management account solely for managing the organization.
- Do not deploy workloads or applications in the management account.
- Set up strong security controls, such as enabling MFA and monitoring activity via AWS CloudTrail.

## Goverance & Compliance

Service Control Policy are policies that specify the maximum permissions for an AWS account or OU within an organization. It can be used for:

1. Limit the services or regions an account can use.
2. Enforce security and compliance requirements (e.g., prevent the use of insecure services or regions)
3. Implement organizational-wide restrictions

SCP applied to OU or Account, it limites all the accounts or Role under that umbrella.

AWS Config can be used to centrally track resource configurations and compliance across multiple accounts.
AWS License Manager can help you manage and track software licenses across multiple accounts.
AWS CloudTrail can be used to track activity and API calls across accounts. You can create a central trail that aggregates logs from multiple accounts for better visibility and auditing.
AWS Security Hub aggregates security findings across accounts within your organization, allowing you to centrally manage and respond to threats.

## Cross-Account Resource Sharing and Management

At AWS organisation leavel, you can use AWS RAM to sharing resources like VPCs, subnets, and Route 53 Resolver rules across accounts, reducing the need for resource duplication.

At account level, IAM roles can be used to allow accounts within the organization to access resources in other accounts without needing to manually configure permissions. create a role in target account with permission and allow source account to assume it, then the source account can assume the role to access target account allowed resource.

## Cost Management

1. Use AWS Organizations to manage billing for multiple accounts, enabling cost aggregation and volume discounts.
2. Allocate costs to business units, teams, or projects using tags and linked accounts.
3. Set up budgets and alerts to monitor and control spending per account.

## AWS Controle Tower

AWS Control Tower and its feature Account Factory offer significant benefits for managing and automating the setup of a multi-account AWS environment. These services are designed to simplify governance, security, and operations at scale, especially in large organizations with many AWS accounts. The Benefits of using AWS Control Tower and Account Factory:

- End-to-End Account Management: AWS Control Tower and Account Factory offer a fully automated solution for account setup, governance, security, and compliance.
- Consistency Across Accounts: Ensure that accounts are provisioned with consistent configurations and governance standards, reducing the risk of misconfiguration.
- Simplified Compliance and Security: By automatically enforcing security policies and compliance guardrails, you reduce the operational burden of managing governance at scale.
- Scalability: Scale automatically when need more accounts, making it ideal for growing organizations.
- Centralized Governance and Monitoring: centralizes logging and monitoring by automatically enabling AWS CloudTrail across all accounts in your environment.

## Conclusion:

Based all the info above, the steps to design a multi-account environment will be:

1. Have a clear idea about your organisation hierarchy，
2. Create management account, using this account to create the organisation and OU hierarchy base above design
3. Create new member account or invite existing account into corresponding OU.
4. Delegate organisation management responsbility to corresponding account. (Security, Billing, OU management etc)
5. Add SCP and apply it to corresponding OU/Account through delegated account
6. if needed, Integrate with Budget, AWS Config, License Manager, Cloudtrail, Security Hub etc for organisation level goverance, report, audit etc.
7. All of the above can be created in Controle Tower with Account Factory, to make a consistent and automatic pipeline of account provisioning.
