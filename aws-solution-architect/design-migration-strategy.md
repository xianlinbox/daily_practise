In last episode, we are more focus on how to deploy new things into AWS cloud. Actually in the real world, we did more migration legacy workload rather than delivery new workloads. In this episode, let's talk about the migration strategy.

# 7Rs

7Rs are strategies organizations use to evaluate and plan the migration of applications to the cloud. These strategies help in deciding the most appropriate approach for each workload based on its requirements, technical debt, and business value.

## Retire

Identify applications or workloads that are no longer needed and can be decommissioned.

- Reduces costs and complexity.
- Frees up resources for more critical applications.

## Retain

Leave the application as-is, either because it's tightly integrated with other systems or due to business constraints.

- Avoid unnecessary effort on applications that aren’t a priority.
- Allows focusing resources on higher-impact migrations

## Relocate

Move to another cloud or hybrid environment.

- a hybrid cloud or specific hardware dependency is needed.
- Simplifies migration for workloads requiring a consistent infrastructure layer
- Provides continuity for legacy systems while using cloud infrastructure

## Re-Host

"Lift-and-shift" to the cloud.

- The application is compatible with the cloud environment without requiring major changes.
- Fast and simple migration
- Reduces on-premises infrastructure costs.

## Re-platform

Migrate the application to the cloud with some optimizations, such as switching to managed services or updating runtime environments.

- Takes advantage of some cloud-native features without extensive re-architecture
- Balances effort and benefit.

## Re-Purchase

Replace the existing application with a commercial, off-the-shelf (COTS) solution, often SaaS.

- when application can be replaced by modern SaaS offerings.
- Avoids maintenance of custom applications.
- Leverages the benefits of modern, feature-rich SaaS platforms.

## Refactor

Modify the application to make it cloud-native, often by adopting microservices, serverless architectures, or containerization.

- When the application is critical and can benefit significantly from cloud-native features like scalability, resilience, or cost efficiency.
- Fully leverages the cloud’s benefits (scalability, flexibility, cost optimization).
- Improves maintainability and modernizes the application architecture.

# Application Migration

# Data Migration

# Conclusion

![Migration process](https://d2908q01vomqb2.cloudfront.net/cb7a1d775e800fd1ee4049f7dca9e041eb9ba083/2021/11/24/7-R-1024x516.png)

1.

Migration Hub

Application Discovery Service
Application Migration Service
Server Migration Service

Application Migration

1. understand different compute options

- serverless lambda

Data Migration:

- Data sync
- Transfer family
- Database migration service
- Storage Gateway
