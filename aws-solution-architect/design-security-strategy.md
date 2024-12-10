In last episode, we have make all the components in the system connected with each other, the next step we need to make sure the resources are accessed securely. In this episode, we gonna talk about the security strategy.

# The security mechanism in AWS

IAM

Permission Boundary is applied to IAM entities (users or roles), using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity

- IAM access Analyzer
- IAM credential report

Guard Duty
Inspector

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
