In last episode, we have make all the components in the system connected with each other, the next step we need to make sure the resources are accessed securely. In this episode, we gonna talk about the security strategy.

when talking about security in AWS, The shared responsibility model are always mentioned:
![Shared Resposibility Model](https://d1.awsstatic.com/security-center/Shared_Responsibility_Model_V2.59d1eccec334b366627e9295b304202faf7b899b.jpg)

As a solution archiect, your job will be using security mechanism in AWS to cover the customer parts.

# The Security Mechanism in AWS

AWS provides a comprehensive suite of security mechanisms designed to protect infrastructure, data, and applications. we need to understand them and know how to apply them based on business requirement.

## Identity Access control

### Identity

Permission Boundary is applied to IAM entities (users or roles), using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity

- IAM access Analyzer
- IAM credential report

## Resoucre access control

## Data

## others

## Tools

# Incident Response

Infra

- patch

Data

- encrypt at rest
  - which kms use
  - conig rule
  - cloud trail for auditing
- encypt at transit
  - vpn
  - inter-network
  - https and certificate

Incident response
