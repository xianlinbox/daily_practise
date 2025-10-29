# Databricks Intelligence Platform

## Lakehouse Platform

Data Lakehouse. = Data Lake (flexity, scalability, cost efficiency) + Data Warehouse (Data management, ACID
transaction). it can support both BI & ML requirements.

Date Warehouse:

Data Lake:

Delta Lake

Medallion Architecture

- Bronze
- Silver
- Gold
- Platium

## Databricks Architecture

### Control Plane

1. User interface
2. Compute orchestration
3. Unity Catalog
4. Query & Code

### Compute Plane

1. Classic Compute

- All Purpose Cluster
- Job Cluster

2. Serverless Compute

### Storage

1. Workspace Cloud storage
2. Customer owned Resources

## Workspace

## Unity Catalog

A abstraction layer on Cloud storage, provide table, view, function

- Legacy: DBFS, Hive Metastore

Metastore

- Storage Credentials
- External Location
- Catalog
  - Schema
    - Tables
      - managed
      - external
    - Views
    - Volumes (which contain files)
      - managed
      - external
    - Functions
- Service Credential
- Connections
- Share
- Provider
- Recipents

### Object Model

Metastore -> Catalog -> Schema(Database) -> (Volume, table, view, function)

Delta Table?

Dimension, Fact

Slowly Change Dimension

Type 1 (no history) Type 2 (all history) Type 3(only latest change)

# Development and Ingestion

## Spark

## Delta Lake

## Delta Live Tables(DLT)

- DLT Architecture
- DLT pipeline
- production mode vs development mode (inactive termination, auto retry)

- Streaming tables vs MaterizedView vs View

## Work loads

- Notebooks
- Pipelines
- Jobs

## Lakeflow

# Data Processing and Transformations

# Productionizing Data Pipelines

# Data Goverance and Quality

## Delta Sharing

## Lakehouse Federation

- Query Federation
- Catalog Federation

## Databricks Connect

Connect local dev env to databricks workspace to get compute cluster with familiar dev env. It will run/debug code in
local. Databrick connect will decide run which code in cluster, which in local. make sure both env are using same python
verison.

## Databricks Asset Bundles

The engineering with Databricks:

- bundle:
- resource:
- target:

Use Databricks Cli to execute the code:

- databricks bundle init
- databricks bundle validate
- databricks bundle run job
- databricks bundle deploy -t <target>
- databricks bundle destroy
