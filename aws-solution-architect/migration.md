# the 7Rs

Retire: give up
Retain: left as it is
Relocate: just move to another place. no additional operation needed
Rehost: no cloud optimization done.
Replatform: no change on core architecture,but use some cloud optimization
Repurchase: Moving to a different product on cloud.
Refactor/Rearchitecture: change code or architecture needed.

# Hybrid Cloud

Use Storage gateway to bridge on-prem and cloud data. we have diff gatway for diff storage
Gateway support refresh cache

SnowCone and Snowball Edge: hardware device for move large data. there is S3 adapter can improve the file write speeds.

SnowMobile: for data 10PB+, Snowball for data <10PB

# Database Migration Service

Migrated DB to another one; must create an EC2 instance to perform replication task

- Provided Schema Conversion Tool to covert schema
- Not work for OpenSearch Data
- Working with Snowball for fast large amount DB migration

# Cloud Adoption Readiness Tool

Answer a bunch of questions to get an custom report to guide your migrations

# Disaster Recovery

Objectives: RPO(data loss)/RTO(downtime)
Staretgies: warm stanby (minmum)/backup-restore (rebuild)/hot-site, multi-sites (full)/pilot light (stand up critical core system)
Tips: backup/HA/Replication/Automation/Chaos testing

# Fault injection Simulator

Chaos testing managed by AWS
works on ECS/EKS/EC2/RDS ..
create a experiment template then run on the instances then stop experient, then view the result

# Application Discover Service

Migration Datahub
Application Migration Service

Elastic Disaster Recovery
Migration Evaluator
