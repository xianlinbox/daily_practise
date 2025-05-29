# Region

a geographical area that contains one or more Azure datacenters that are connected via a low-latency network.

- Azure has over 60 regions worldwide (more than any other cloud provider).
- Each region is paired with another (called a regional pair) to support disaster recovery and data redundancy.
- Not all services are available in every region (check the Products by Region page).

## AZ

An Availability Zone (AZ) is a physically separate datacenter within a region, each with its own power, cooling, and
networking. Each region with zone support has at least 3 AZs.

Select region based service availability, geo, price

# Goverance

- Root Group: The top of the Azure hierarchy. Automatically created, contains all other management groups and
  subscriptions.

* Mangment Group: A container to group and manage multiple subscriptions. Policies, RBAC, and Blueprints can be applied
  at this level.

* Subscription: Logical container for Azure services. Billing boundary. Every service you deploy exists within a
  subscription.

* Resource Group: A logical container for Azure resources that share a lifecycle.

* Resource: The actual Azure service instances (VMs, Storage, Databases, etc.) you create and use

* Account: The user identity used to sign in. Tied to Azure Active Directory (AAD).
