In last episode, we have created accounts to hold the aws resources. In this episode we gonna talk about the network connectivity. network connectivity is essential for designing secure, efficient, and cost-effective cloud environments.

# AWS global infrastructure

Before dive into network connectivity, we should have a big picture about AWS cloud infra. The Global infra is built around AWS Regions and Availability Zones:

- **Region**: a physical location in the world where have multiple Availability Zones
- **Availabity Zone**: Availability Zones consist of one or more discrete data centers

Based on the gobal infra, AWS provided a bunch of services to reduce network latency:

- Local Zone: Run applications on AWS infrastructure closer to your end users and workloads
- Wavelength Zone: Embed AWS compute and storage services within communications service providers’ (CSP) 5G networks
- Edge Network services: Global Accelerator, CloudFront, Route 53, lambda@Edge etc
- DX locations: Create a dedicated network connection to AWS

# The core concept: VPC

**VPC**: A logically isolated network within AWS, allowing you to define IP ranges, subnets, routing tables, and security settings.The key features in VPC are:

- **Subnets**:
  - Public subnets for resources with internet access.
  - Private subnets for internal resources without direct internet access.
- **Route Tables**: Control how traffic is routed within the VPC and to external networks.
- **Elastic IP Addresses**: Static IP addresses for resources requiring constant public IPs

BTW: VPC can only be created in one region, but it can cross multi AZ. subnet can only land in one AZ.

Several AWS services need to host within a VPC for functionality, security, or compliance. These services typically interact with your resources privately.:

1. Compute Services: EC2/ECS/EKS
2. Storage Services: RDS/Aurora/ElastiCache/FSx
3. Networking Services: VPC Endpoints/PrivateLink/ELB/NAT Gateway/Instance
4. Analytics and Search Services: EMR/OpenSearch/Redshift
5. Security and Identity Services: Directory Service/WorkSpaces
6. Integration and Message Queueing: MQ

# The types of connectivity

As described above, VPC hold a lot of resouces and controlled the network connection between these resources. For a complicated system There are a bunch of role involed:

1. End user (In Office/home)
2. AWS managed services(S3/API Gateway/CloudFront etc)
3. Resources in VPC
4. Resources in another VPC (another region/another account)
5. Resource in on-prem data center

Let's check how does they connect with each other:

- End user
  - AWS Managed service: As AWS managed service are open to public, end user can connect to it directly
  - Resources in VPC/Resources in another VPC(they are same to end user):
    - Option 1: ClientVPN/site-to-site VPN build connection between end user location with VPC.
    - option 2: VPC provide public access through an internet gateway
    - option 3: End user connect through AWS manged service like API gateway
  - Resource in on-prem data center: ClientVPN build connection between end user location with data center.

# Monitoring

AWS provided serveral services to monitor the network traffic, As a solution architect you need to know how to choose the right tool based on business requirement.

## VPC Flow Logs:

- Purpose: Capture information about the IP traffic flowing to and from network interfaces in your VPC.
- Key Data Points:
  - Source and destination IP addresses.
  - Protocols and port numbers.
  - Traffic acceptance or rejection status.
- Use case:
  - Troubleshooting connectivity issues
  - Monitoring for unusual traffic patterns
  - Compiance an auditing
- Data store: S3/Cloudwatch log

## VPC Flow Logs:

- Purpose: Capture information about the IP traffic flowing to and from network interfaces in your VPC.
- Key Data Points:
  - Source and destination IP addresses.
  - Protocols and port numbers.
  - Traffic acceptance or rejection status.
- Use case:
  - Troubleshooting connectivity issues
  - Monitoring for unusual traffic patterns
  - Compiance an auditing
- Data store: S3/Cloudwatch log

## Traffic Mirroring

- Purpose: Capture and inspect live network traffic from EC2 instances for analysis.
- Key Data Points: the data packet which include message content.
- Use case:
  - Content inspection
  - Threat monitoring
  - Troubleshooting

## CloudTrail logs

- Purpose: Monitor network-related API calls and changes to network configurations.
- Use Cases:
  - Auditing changes to VPCs, security groups, and routing tables.
  - Tracking unauthorized or unusual changes to network configurations.

## Amazon CloudWatch

- Purpose: Monitor network-related metrics, such as data transfer rates, errors, and latency.
- Use Cases:
  - Monitoring performance of Load Balancers, NAT Gateways, and Transit Gateways.
  - Setting up alarms for unusual traffic volumes.

## Amazon CloudWatch Internet Monitor

- Purpose: visibility into how internet issues impact the performance and availability between your applications hosted on AWS and your end users.

## Amazon VPC IP Address Manager (IPAM)

- Purpose: plan, track, and monitor IP addresses for your workloads. For more information, see IP Address Manager.

## Reachability Analyzer

- Purpose: analyze and debug network reachability between two resources in your VPC.

## Network Access Analyzer

- Purpose: understand network access to your resources, identify improvements to your network security posture and demonstrate that your network meets specific compliance requirements.

## AWS Network Manager

- Purpose: Provides a centralized view of your global network.
- Use Cases:
  - Monitor network connections between AWS environments and on-premises networks.
  - Visualize network health and traffic flows.
- Key Features:
  - Real-time network topology visualization.
  - Centralized performance monitoring for Site-to-Site VPN and Direct Connect.

# Conclusion

keep one genenral principle in mind: **Try to use prvate network as much as possible**
