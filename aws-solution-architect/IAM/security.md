# Goverance

## Cloud Trail

Enable by default, record all the events happened in your accout, good for goverance, compliance,audit

Event Bridge
CloudWatch metrics
S3 analysis

## KMS

AWS provided software encryption key management system.
Key Type: Symmetric and Asymmetric
Keys:

- Customer managed keys: all management controled by customer.
- AWS managed keys: auto rotate each 1 year
- AWS owned keys:

Key Materials Origin:

1. AWS
2. External
3. Custom Key store (eg: CloudHSM)

KMS support multi region keys. it's a primary-replica logic not a global one.

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

## AWS Shield, WAF, AWS Firewall Manager

## AWS Inspector

## AWS GuardDuty

## IAM Condition key
