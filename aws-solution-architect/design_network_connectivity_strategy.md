In last episode, we have created accounts to hold the aws resources. In this episode we gonna talk about the network
connectivity. network connectivity is essential for designing secure, efficient, and cost-effective cloud environments.

# AWS global infrastructure

Before dive into network connectivity, we should have a big picture about AWS cloud infra. The Global infra is built
around AWS Regions and Availability Zones:

- **Region**: a physical location in the world where have multiple Availability Zones
- **Availabity Zone**: Availability Zones consist of one or more discrete data centers

Based on the gobal infra, AWS provided a bunch of services to reduce network latency:

- Local Zone: Run applications on AWS infrastructure closer to your end users and workloads
- Wavelength Zone: Embed AWS compute and storage services within communications service providers’ (CSP) 5G networks
- Edge Network services: Global Accelerator, CloudFront, Route 53, lambda@Edge etc
- DX locations: Create a dedicated network connection to AWS

## Global Accelerator

network service that improves the availability and performance of your applications by routing traffic through the AWS
global network. It provides static IP addresses for your applications and routes traffic to optimal endpoints based on
latency, health, and policies.

- static ip
- regional failover
- performance optimization
- support ALB/NLB/EC2/IP
- flexiable traffic control.
- Accelerator/Listener/Endpoint/Endpoint Group/health check

# The core concept: VPC

**VPC**: A logically isolated network within AWS, allowing you to define IP ranges, subnets, routing tables, and
security settings.The key features in VPC are:

- **Subnets**:
  - Public subnets for resources with internet access.
  - Private subnets for internal resources without direct internet access.
- **Route Tables**: Control how traffic is routed within the VPC and to external networks.
- **Elastic IP Addresses**: Static IP addresses for resources requiring constant public IPs

BTW: VPC can only be created in one region, but it can cross multi AZ. subnet can only land in one AZ.

Several AWS services need to host within a VPC for functionality, security, or compliance. These services typically
interact with your resources privately:

1. Compute Services: EC2/ECS/EKS
2. Storage Services: RDS/Aurora/ElastiCache/FSx
3. Networking Services: VPC Endpoints/PrivateLink/ELB/NAT Gateway/Instance
4. Analytics and Search Services: EMR/OpenSearch/Redshift
5. Security and Identity Services: Directory Service/WorkSpaces
6. Integration and Message Queueing: MQ

# The AWS resources that supports network connection

## Route 53

scalable and highly available Domain Name System (DNS) web service. It mainly support 3 features:

### Domain registration

Acts as a domain registrer, enabling you to register and manage domain names.

- Register new domains directly through Route 53.
- Manage domain transfers and renewals.
- Automates DNS configuration for newly registered domains.

### DNS Services

Routes traffic for your domains to AWS resources or other web applications using DNS records.

Support Record Type:

- A (Address): Maps a domain to an IPv4 address.
- AAAA (IPv6 Address): Maps a domain to an IPv6 address.
- CNAME (Canonical Name): Maps an alias domain to another domain.
- MX (Mail Exchange): Directs emails to the appropriate mail server.
- NS (Name Server): Specifies the authoritative name servers for a domain.
- TXT (Text): Adds text-based information, commonly used for verification.
- SRV (Service): Specifies the location of a service.
- Alias: A Route 53-specific record type that points to AWS resources like CloudFront distributions, ELBs, or S3
  buckets.

Route 53 can config routing policy to decide return which record:

- Simple
- latency
- failover
- geo
- weights

Route 53 provide 2 kinds of hoste zone to host the records:

- public hosted zone: domains accessible over the internet.
- private hosted zone: DNS resolution within one or more VPCs, best to associate to all the VPCs which need it.

### Health check and monitoring:

- Monitors the health of endpoints (e.g., web servers, AWS resources).
- Configurable for HTTP, HTTPS, or TCP checks.
- DNS Failover: Automatically routes traffic away from unhealthy endpoints to healthy ones.
- Calculated Health Checks: Aggregates results from other health checks.
- ntegrates with CloudWatch Alarms for proactive monitoring.

## Route 53 Resolver

designed for DNS query resolution between AWS and hybrid environments. It enables communication between on-premises data
centers and AWS VPCs or across multiple VPCs.

- Inbound DNS queries: resolve from on-prem to aws resources.
- Outbound DBS queries: resolve from aws VPC to on-prem
- support forward queries to another DNS servers

## CloudFront

Fast CDN provide by AWS. it can:

- Globald distribution through edge locations worldwide to deliver content closer to users.
- Cache: store content in local edge to reduce load to origin server
- the orgin can be : S3/EC2/API Gateway/ELB/other non AWS http service
- Access control: use Signed URl/Signed cookie to control who can access the content
- CloundFront functions or lambda@edge custom routing
- work with WAF/Shield/IAM/OAI for security

## Direct Connection

Establish a dedicated connection from an on-premises network to one or more VPCs.

- uses industry-standard 802.1Q VLANs to connect to Amazon VPC using private IP addresses. configure three different
  types of VIFs:Public/Transit/Private.
- The installation of a Direct Connect Dedicated Connection can take from several weeks to a few months.
- Direct Connect Gateway can be used for multi-VPC connectivity, connect to mulri vpc's virtuak private gateway

## Site-to-Site VPN

AWS managed VPN endpoint, creating an IPsec VPN connection between your remote networks and Amazon VPC over the
internet.

- it connected to virtual private gateway in VPC. virtual private gateway support multiple user gateway
  connections.which means we can implement redundancy and failover
- support using AWS Global Accelerator accelerated VPN connection
- public accessable service.

## Client VPN

an AWS managed high availability and scalability service enabling secure software remote access

## Software VPN

creating a VPN connection between your remote network and a software VPN appliance running in your Amazon VPC network

- customer connect vpn software running in ec2 instance through Internet Gateway.
- recommended if you must manage both ends of the VPN connection

## Transit Gateway

an AWS managed high availability and scalability regional network transit hub used to interconnect VPCs and customer
networks.

- can work together with VPN, Direct connect to connect multi VPCs with local network.
- supports and encourages multiple user gateway connections so that you can implement redundancy and failover

## VPN CloudHub

uses an Amazon VPC virtual private gateway with multiple customer gateways, each using unique BGP autonomous system
numbers (ASNs). The remote sites must not have overlapping IP ranges.

- operates on a simple hub-and-spoke model that you can use with or without a VPC.

## VPC peering

a networking connection between two VPCs that enables routing using each VPC’s private IP addresses

- Support cross-account, cross-region peering
- Do not support transitive peering, A peering with B and C, doesn't mean B peering with C
- Both IPv4 and IPv6 traffic is supported

## Elastic IP

use to assign a public ip to AWS services, make it can be accessible from internet. support:

- EC2/ECS/AppRunner/RDS/NAT Gateway/ELB/Lambda/Workspaces/Global Accelerator
- not support API Gateway nor Cloud Front

## Internet Gateway

a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the
internet.

- provides a target in your VPC route tables for internet-routable traffic
- supports IPv4 and IPv6 traffic
- enables resources in your public subnets (such as EC2 instances) to connect to the internet if the resource has a
  public IPv4 address or an IPv6 address

## Egress-only Gateway

a horizontally scaled, redundant, and highly available VPC component that allows outbound communication over IPv6 from
instances in your VPC to the internet,

- only outbound, no inbound
- support ip v6 only, use NAT Gateway for IP v4

## NAT Gateway

a Network Address Translation (NAT) service that support instances in a private subnet connect to services outside VPC
but external services cannot initiate a connection with those instances.

- only outbound, no inbound
- support Ip v4 only
- has public(for internet through IGW) /private (for on-pre or other vpc through VPG or transit gateway) types

## NAT Instance

use an instance to run network address translation (NAT) service. Not recommend, suggest migrate to NAT gateway.

## Interface/Gateway Endpoint

Both of them are using to connect to AWS services from within your Virtual Private Cloud (VPC) without using the public
internet. This service no need to update routable as it get a private ip in the subnet. they have a little difference:

- Interface Endpoint:
  - implementde by add ENI in your VPC. so it has a private Ip
  - support most of AWS services: S3, DynamoDB, Lambda, and more.
- Gateway Endpoint:
  - Routes traffic to services through private IPs via route tables.
  - only support S3 and DynamoDB.

## Private Link

a highly available, scalable technology that you can use to privately connect your VPC to services and resources as if
they were in your VPC.

- can use to connect another VPC service, AWS managed service, Market Parter service.
- powered by Interface VPC Endpoints
- only supported in the AWS region where the VPCs reside, if need to cross region, need to additional setup, like VPC
  peering.

# The types of connectivity

For a complicated system There are serval parts will be involved:

1. Internet (Public services, End users)
2. AWS managed services(S3/API Gateway/CloudFront, Market service providersetc)
3. Resources in VPCs
4. On-prem data center

As an AWS Solution Architect, when we talk about network connectivity, it is more related how to make sure these parts
can connect with each other via the aws services described above.

## Connecting remote networks with your Amazon VPC environment

- Client VPN can be used for singe point connect to VPC
- Site-to-Site VPN can be user for a location (office) connect to VPC
- CloudHub can be used for multiple user connect to VPC in hub-and-spoke model
- Direct connect can be used for a location (office/on-prem) connect to VPC via a private dedicated network
- Transit Gateway/Direct Connect Gateway can be used to connect multiple VPCs.

## Connecting VPC with Internet

- Internet Gateway can help connection between VPC public subnet resources and internet
- Resources in private subnets need to use NAT gateway or Egress-Only Internet Gateway to reach internet resources.
- Resources in private subnets can use other AWS services (ELB/API Gateway etc) for internet connectivity, this is
  powered by Internet Gateway.

## Integrate multiple Amazon VPCs into a larger virtual network

- Two VPCs can use VPC peering connect with each other
- VPC can use PrivateLink to expose resources to another VPC
- VPCs can use Transit Gateway to connect with each other.
- VPC resources can build software site-to-site VPN for connection
- For simplify architecture, you can build a transit VPC for reducing customer side connections.

## Connecting VPC with AWS managed Services

- VPC can use interface/Gateway endpoint connect to AWS managed services.
- AWS managed services can access VPC public subnet resources same as what internet service do.
- For private resources, some AWS managed services like Lambda/ELB can access by attach to vpc. other services need to
  use these service as middle layer. or you can create a private Link for the service in the private subnet.

# Monitoring

AWS provided serveral services to monitor the network traffic, As a solution architect you need to know how to choose
the right tool based on business requirement.

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
- Management Events (config, security) and Data Events (access to the data)
- Use Cases:
  - Auditing changes to VPCs, security groups, and routing tables.
  - Tracking unauthorized or unusual changes to network configurations.

## Amazon CloudWatch

- Purpose: Monitor network-related metrics, such as data transfer rates, errors, and latency.
- Use Cases:
  - Monitoring performance of Load Balancers, NAT Gateways, and Transit Gateways.
  - Setting up alarms for unusual traffic volumes.

## Amazon CloudWatch Internet Monitor

- Purpose: visibility into how internet issues impact the performance and availability between your applications hosted
  on AWS and your end users.

## Amazon VPC IP Address Manager (IPAM)

- Purpose: plan, track, and monitor IP addresses for your workloads. For more information, see IP Address Manager.

## Reachability Analyzer

- Purpose: analyze and debug network reachability between two resources in your VPC.

## Network Access Analyzer

- Purpose: understand network access to your resources, identify improvements to your network security posture and
  demonstrate that your network meets specific compliance requirements.

## AWS Network Manager

- Purpose: Provides a centralized view of your global network.
- Use Cases:
  - Monitor network connections between AWS environments and on-premises networks.
  - Visualize network health and traffic flows.
- Key Features:
  - Real-time network topology visualization.
  - Centralized performance monitoring for Site-to-Site VPN and Direct Connect.

# Conclusion

Based all the info above, the steps to build your network environment will be:

1. Understand what parts are involed in your system

- where is your user(Regions, global infra)?
- do you need connect to on-prem data center?
- any public internet services used?
- any AWS managed service involed?
- how many vpc will be used? cross account, cross region?
- ...

2. Choose the network services to build network topology

- Try to limit the network inside AWS network as much as you can
- Make the network topology as simple as you can

3. Config monitoring for the network traffic for debugging and tracing
