# Basic Concepts

CIDR (Classless Inter-Domain Routing): a block of ip address
Private IP: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
Public IP: all the rest
VPC:

- Has a predefined list of CIDR which can't change
- In VPC, CIDR min-size /28, maxium-size /16 (65535)
- VPC is private, only under private ip range is allowed.

Subnets:

- Within VPC, define as a sub-set of VPC CIDR
- all instances in subnets get private ip
- first 4 and last subset ip is reserved by AWS.

Routing Table: control where the network traffic direct to

Internet Gateway: Help VPC talk to the Internet.act as NAT instance for public ip instance
An egress-only internet gatewayis a horizontally scaled, redundant, and highly available VPC component that allows outbound communication over IPv6 from instances in your VPC to the internet, and prevents the internet from initiating an IPv6 connection with your instances.

Public Subnets: the instance has a public ip address
Private subnets: access internet throgh NAT instance or NAT gateway.

NAT instance: an instance created in public subnets and attached public ip. all private subnets traffic go through it to the internet. the internet will treat it as single source.

NAT Gateway: AWS managed NAT services. resilient in singe AZ, multi-zone need to create multiple NAT gateway

NACL(Network access control): stateless firewall rules apply to all the instances in the subnet; support allow/deny rules.
Security Group: apply at instance level and only allow rule, no deny rule; can reference each other, ALB & Cloud Front are all insaynces and can use security group.

- the defaut security group are assign to instance if you didn't assign one, this default allow inbound traffic from the same group.
- The user create security group by default allow no inbound traffic and ll outbound traffic.

VPC Flow logs: can define at vpc, subnet, eni level, destination can be Cloudwatch, S3, Firehose.
Bastion Host: an public ec2 instance help you ssh into an private ec2 instance. AWS proviece SSM session manager for this task in a more secure way.

IPV6:

- it is all public
- private subnet instances can't be reach by IPV6, but can reach to an ipv6 service, by Egress only internet gateway.

# VPC Peering

Connect 2 VPC like they are one,
CIDR of these 2 VPC can't overlap
Connection not transitive, you need to build peering for all connection
Can cross region and cross account
If 2 VPC has same CIDR, the longest prefix match will use to decide which VPC traffic go to.
No Transtive Peering/No Edge Routing (Peering can't make your private subsets use another VPC NAT Gateway)

# VPC sharing

Sharing VPCs is useful when network isolation between teams does not need to be strictly managed by the VPC owner, but the account level users and permissions must be. With Shared VPC, multiple AWS accounts create their application resources (such as Amazon EC2 instances) in shared, centrally managed Amazon VPCs. In this model, the account that owns the VPC (owner) shares one or more subnets with other accounts (participants). After a subnet is shared, the participants can view, create, modify, and delete their application resources in the subnets shared with them. Participants cannot view, modify, or delete resources that belong to other participants or the VPC owner. Security between resources in shared VPCs is managed using security groups, network access control lists (NACLs), or through a firewall between the subnets.

# Transit Gateway

AS the name, it's a transitive gateway. any VPC connect to this Gateway, can talk with each other

- reginal resources, can work cross region
- can peering with each other, inter/intra region
- using routable table to limit VPC connection
- support ip multicast
- can work with other gateways, like DirectConnect, VPN

# VPC Endpoints

enables VPC connected to AWS services or powered by Private Link services

Endpoint gateway: one per VPC/ only works for S3 and DynamoDB/need to update routetable/DNS resolution must be enabled. can only for aws internal service, A gateway endpoint is a gateway that is a target for a route in your route table used for traffic destined to either Amazon S3 or DynamoDB. There is no charge for using gateway endpoints. currently don't support access from anothe region

Endpoint Interface: An interface endpoint is an elastic network interface with a private IP address from the IP address range of your subnet. It serves as an entry point for traffic destined to a service that is owned by AWS or owned by an AWS customer or partner, not for VPC intern connection. You are billed for hourly usage and data processing charges.

Policies: an json defines how to access the services

1. it can't override other policies
2. S3 can only deny access from a public ip, for private ip, we can use sourceVpc/sourceVpce to limit

connection trouble shooting steps:

1. check Ec2 instance security group allow traffic out.
2. check Endpoints Gateway policy allow
3. route table can route to S3
4. Enabled DNS resolution
5. S3 Bucket policy allow connection

DNS hostnames and DNS resolution are disabled by default. enable them for private hosted zone. The DNS match is based on specific match and follow precedence rule, will not cause an error.

when create public zone, A NS and SOA is created and configured

# Private Link

A highly available, scalable technology that enables you to privately connect your VPC to supported AWS services, services hosted by other AWS accounts (VPC endpoint services), and supported by AWS Marketplace Partner Service

An AWS PrivateLink consists of a VPC endpoint (VPCE) and a corresponding Endpoint Service:

# Site 2 Site VPN

On-prem VPN
Customer gateway
Vitual Private Gateway
Using BGP and ASN
can use NAT instance to share internet connection with VPN
provide IPsec-encrypted private connection that also reduces network costs, increases bandwidth throughput, and provides a more consistent network experience than internet-based VPN connections.

## Cloud Hub

1. connect 10 customer gateway through Vitual private gateway
2. 1 Customer gateway can connect to multi VGW also (not recommend), use direct connect and one for each.
3. operates on a simple hub-and-spoke model that you can use with or without a VPC.

Shared service vpc: building a proxy vpc talk to on-prem.

Use this approach if you have multiple branch offices and existing internet connections and would like to implement a convenient, potentially low-cost hub-and-spoke model for primary or backup connectivity between these remote offices.

# Client VPN

# Direct Connect

Build a dedicated connection between AWS direct connection location and on-prem data center. this is a seprate connection which will not be limited by existing internet bandwidth.

1. dedicated connection
2. more expensive
3. bypass ISP,private access to service through VIF (virtual inteface)
4. not redundunt by default
5. can't provide encryption

Connect Types:

- dedicated connection
- hosted connection

leader time for new connection can be 1 month
Link aggreagtion group can aggreagte multi DC into one:

1. must be dedicated connection
2. must be same capacity
3. must teminated at same Direct Connect endpoint

Direct Connect Gateway: connect to many VPC in different region
SiteLink: allow you send data from on Direct connect bypass aws regions

Provided virtual Interface:

- Public: using public IP access all AWS public services
- Private: access VPC using private IP
- Transit: access one or more transit Gateway.

Connect with vpc in different region:

1. provision a direct connect gateway.
2. use priavte VIF connect to dX gateway,
3. provision vitrual private gateway in vpc of each regions.
4. use DX gateway connect to the virtual private gateways above.

Solution to build Site to Site VPN on DX:

1. Build virtual private gateway in VPC
2. Build Public virtual interface in DX to connect to Virtual private gateway IPsec endpoint (this is a public resource).
3. Create the S2S VPN between on-prem customer gateway to Virtual private gateway

VPC Flow Log: using it to identify network issues, can work with cloudwatch, athena, S3 together

# Network protection

the service we have seen:

1. NACL
2. Security Group
3. WAF
4. Shield
5. Firewall Manager

Network Firewall : up to 1000 rules

# Transit VPC

Transit VPC uses customer-managed Amazon Elastic Compute Cloud (Amazon EC2) VPN instances in a dedicated transit VPC with an Internet gateway

# Tips

VPC Endpoint not allow cross region connection

# VPC Connection

## internet to VPC:

1. Site to site VPN/ software VPN (running on EC2)
2. VPN + transit gateway
3. Direct connect
4. Direct connect + VPN
5. Direct connect + transit gateway
6. Direct connect + transit gateway +VPN
7. Cloud Hub

## VPC to VPC

1. VPC peering
2. Transit Gateway
3. PrivateLink
4. VPN

## VPC access internet/AWS services

1. NAT Gateway or Instance connect to internet gateway
2. Endpoint gateway (only S3 & Dynamo)/interface to internal services.

## Traffic Mirror

Traffic Mirroring is an Amazon VPC feature that you can use to copy network traffic from an elastic network interface of type interface. You can then send the traffic to out-of-band security and monitoring appliances for:

- Content inspection

- Threat monitoring

- Troubleshooting
