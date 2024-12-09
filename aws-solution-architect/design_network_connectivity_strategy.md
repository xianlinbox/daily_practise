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

Several AWS services need to host within a VPC for functionality, security, or compliance. These services typically interact with your resources privately:

1. Compute Services: EC2/ECS/EKS
2. Storage Services: RDS/Aurora/ElastiCache/FSx
3. Networking Services: VPC Endpoints/PrivateLink/ELB/NAT Gateway/Instance
4. Analytics and Search Services: EMR/OpenSearch/Redshift
5. Security and Identity Services: Directory Service/WorkSpaces
6. Integration and Message Queueing: MQ

# The AWS resources that supports network connection

## Direct Connection

Establish a dedicated connection from an on-premises network to one or more VPCs.

- uses industry-standard 802.1Q VLANs to connect to Amazon VPC using private IP addresses. configure three different types of VIFs:Public/Transit/Private.
- The installation of a Direct Connect Dedicated Connection can take from several weeks to a few months.
- Direct Connect Gateway can be used for multi-VPC connectivity, connect to mulri vpc's virtuak private gateway

## Site-to-Site VPN

AWS managed VPN endpoint, creating an IPsec VPN connection between your remote networks and Amazon VPC over the internet.

- it connected to virtual private gateway in VPC. virtual private gateway support multiple user gateway connections.which means we can implement redundancy and failover
- support using AWS Global Accelerator accelerated VPN connection
- public accessable service.

## Client VPN

an AWS managed high availability and scalability service enabling secure software remote access

## Software VPN

creating a VPN connection between your remote network and a software VPN appliance running in your Amazon VPC network

- customer connect vpn software running in ec2 instance through Internet Gateway.
- recommended if you must manage both ends of the VPN connection

## Transit Gateway

an AWS managed high availability and scalability regional network transit hub used to interconnect VPCs and customer networks.

- can work together with VPN, Direct connect to connect multi VPCs with local network.
- supports and encourages multiple user gateway connections so that you can implement redundancy and failover

## VPN CloudHub

uses an Amazon VPC virtual private gateway with multiple customer gateways, each using unique BGP autonomous system numbers (ASNs). The remote sites must not have overlapping IP ranges.

- operates on a simple hub-and-spoke model that you can use with or without a VPC.

## VPC peering

a networking connection between two VPCs that enables routing using each VPC’s private IP addresses

- Support cross-account, cross-region peering
- Do not support transitive peering
- Both IPv4 and IPv6 traffic is supported

## Internet Gateway

## Egress-only Gateway

NAT Gateway/Instance

Interface/Gateway Endpoint

Private Link

# The types of connectivity

As described above, VPC hold a lot of resouces and controlled the network connection between these resources. For a complicated system There are a bunch of role involed:

1. End user (In Office/home)
2. AWS managed services(S3/API Gateway/CloudFront etc)
3. Resources in VPC
4. Resources in another VPC (another region/another account)
5. Resource in on-prem data center
6. Resource in the public network

Let's check how does they connect with each other:

## For the end users/Resource in the public network (init request from internet)

- **AWS Managed service/Resource in the public network**: As these services are open to public, end user with network can access them directly
- **Resources in VPC/Resources in another VPC**: There are 2 kinds of resources in VPC

  - Public resources, resources are located in public subnets(Web Apps, APIs, Load Balancer etc.): user can access them through IGW(Internet Gateway) with correct IP/DNS/Security setting.
  - Private resources, resources are located in private subnets RDS databases, internal APIs etc: user need to setup VPN(Client VPN/site to site VPN/ Direct Connect) with correct route table/security setting

  AWS Transit Gateway can be used to interconnect VPCs and customer networks.

- **Resource in on-prem data center**: user can user vpn to connect to data center.

## For AWS managed service

- **Resources in VPC/Resources in another VPC**:
  - Public resources: AWS managed service has capability to access public resources directly same as end user.
  - Private resources: This one can be access through VPC Endpoint (Gateway Endpoint for S3/DynamoDB, Interface Endpoint for other AWS services).
- **Resource in on-prem data center**: Use VPN/Direct Connect build connection between on-prem and AWS cloud.
- **Resource in the public network**: AWS managed service has capability to fetch data from internet.

## For Resource in VPC

- **Resource in the public network**: VPC can connect internet through NAT Gateway, or Egress-Internet-Gateway
- **AWS Managed Service**: VPC Gateway/Interface Endpoint can use to connect to aws managed services.
- **Resources in another VPC**: VPC peering/ Transit Gateway/PrivateLink/VPN between instances through IGW/VPN between intsance and virtual private gateway.
- **Resource in on-prem data center**:

## For resource in on-prem data center

- **Resource in the public network**
- **AWS Managed Service**
- **Resources in VPCs**: Direct Connect Gateway can be used for multi-VPC connectivity. Transit Gateway can be used to interconnect VPCs and customer networks.

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
