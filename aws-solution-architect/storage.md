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
