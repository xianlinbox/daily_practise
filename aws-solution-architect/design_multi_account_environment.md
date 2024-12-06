When design a solution in AWS, the first thing we need to think is how to manage the resources created in AWS. Different client will have different requirements, AWS provide a bunch of tools to help on the account management. Let's go through them.

## AWS Organisation hierarchy

First thing we need to understand the concepts in AWS Organisation:

- Organization: A set of AWS accounts grouped together under a single AWS Organizations entity
- Organisation Unit: Subgroups of AWS accounts within an organization. OUs help you organize accounts by function, team, or environment.
- Accounts: AWS accounts are the fundamental containers for resources and billing.
- Management Account: The root account of the organization that has full administrative control
- Member Accounts: AWS accounts that are part of an AWS Organization

With the above concepts. An organisation structure can be created based on the requirement. Management account can create new account or invite existing account to join the Organisation, and assign them to an OU.

The accounts are grouped in hierarchy

security
governance
oeprtational
compliance

AWS orgniations

Access Manager

AWS controle tower

- Landing Zone
- Account Factory
- Guardrail
-
