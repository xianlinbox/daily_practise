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

Public Subnets: the instance has a public ip address
Private subnets: access internet throgh NAT instance or NAT gateway.

NAT instance: an instance created in public subnets and attached public ip. all private subnets traffic go through it to the internet. the internet will treat it as single source.

NAT Gateway: AWS managed NAT services. resilient in singe AZ, multi-zone need to create multiple NAT gateway

NACL(Network access control): stateless firewall rules apply to all the instances in the subnet; support allow/deny rules.
Security Group: apply at instance level and only allow rule, no deny rule; can reference each other

VPC Flow logs: can define at vpc, subnet, eni level
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
