# Goverance

## Cloud Trail

Enable by default, record all the events happened in your accout, good for goverance, compliance,audit

Event Bridge
CloudWatch metrics
S3 analysis

CLoud trail can't analysis VPC flow logs

Log file integrity: To determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it,

## KMS

AWS provided software encryption key management system.
Key Type: Symmetric and Asymmetric
Keys:

- Customer managed keys: The KMS keys that you create.
- AWS managed keys: KMS keys that AWS services create in your AWS account, can't modify. auto rotate each 1 year
- AWS owned keys: KMS keys that AWS services create in a service account

Key Materials Origin:

1. AWS
2. External
3. Custom Key store (eg: CloudHSM)

KMS support multi region keys. it's a primary-replica logic not a global one.
kms:GenerateDataKey (can use for client encryption)/kms:GetPublicKey/kms:GetKeyPolicy

KMS doesn't support annonymous requests, so public access S3 object can't use it for encryption. (and bucket owner also must be the object owner. can't use object writer setting )

### CloudHSM

AWS provisioned encryption hardware
Dedicated Hardware
Client manage their keys entirely
Must use with HSM client software.

pros:

- Multi-AZ

## Parameter Store

## Database Security

## SSl, SNI, MITM

## ACM

ACM is a regional service.

## S3

- Access Point

Encryption Type:

- SSE-S3: Key managed and handled by AWS
- SSE-KMS: use KMS for the encrytion key
- SSE-C: manage your own encrytion keys
- Client Side Encryption: encrypt data out of AWS
- Glacier: all data is encrypted under AWS control.

Glacier select: allows you to to perform filtering directly against a Glacier object using standard SQL statements. but it only apply to text data, not compressed data

## AWS Shield, WAF, AWS Firewall Manager

WAF for granular config for one application.
Network firewall: a managed service that makes it easy to deploy essential network protections for all of your Amazon Virtual Private Clouds (VPCs).
Firewall Manager: Manage rules for all the accounts in the organisation, define the common sets for all the accounts
Shield for additional feature on top of

WAF can protect the following resources: ALB/CloudFront/API Gateway/AppSync/Cognito User pool

WAF can configure geo match/ipset to allow/block
WAF ACL log can sent to cloudwatch, S3, Firehose.

A web access control list (web ACL) gives you fine-grained control over all of the HTTP(S) web requests that your protected resource responds to. You can protect Amazon CloudFront, Amazon API Gateway, Application Load Balancer, and AWS AppSync resources.

## AWS Inspector

an automated vulnerability management service that continually scans Amazon Elastic Compute Cloud (EC2) and container workloads for software vulnerabilities and unintended network exposure.

## AWS GuardDuty

Intelligent Thread discovery service
using data:

1. Cloudtrail logs
2. DNS logs
3. VPC FLow logs
4. S3 logs/eks/volumes logs etc.

Integrate with EventBridge for notify findings.
GuardDutyDelegateAdminAccount.

Amazon GuardDuty can manage multiple AWS accounts from a single administrator account through AWS Organizations integration

## IAM Condition key

# Security Group vs Network ACL

1. Layer of defense : Instance vs subnet
2. Scope of application: single instance vs all instances in the subnet
3. Default rule: allow all traffic vs deny all traffic
4. Order of rules: no order vs in order
5. Stateful?: Stateful, if inbound allowed then outbound also allowed, vs stateless, need to config both inbound and outbound.
