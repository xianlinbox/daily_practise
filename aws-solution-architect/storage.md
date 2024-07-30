# EBS

Network Drive attach to 1 instance only, to special AZ. there is multi-attch for io type to attach to multi instance.

Volume Types (size/IO/thoughtput):

- gp2/gp3: general purpose SSD
- io: low latenct SSD
- st/sc : low cost HDD (can't used as the boot volume)

Snapshot: incremental,can copy for DR, saved in S3 and can pre-warm for fast loading.

Data Lifecycle Manager: help to manage snapshots
Aws backup: manage aws services backup including ebs

Encryption: not encryped by default, can enable at account level.

Local Instance Store: a phisical ephemeral device attach to EC2 instance, high io; can't resize, need manage lifecycle by user.

# EFS

Attach to multi EC2 (cross region even on-premise), expensive, cost per usage (no need planning usage).

- Encryption at rest with KMS
- Only attach to one VPC, create one ENI per AZ
- Compatible with linux based AMI
- Use Security Group to control access to EFS

Storage Tier for cost saving, using lifecycle policy to move data to different tier

VPC peering, On-prem Direct connect
Access point with pemission config on path
Cross Region Replication
