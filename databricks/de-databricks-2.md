# Databricks Series(2): The ETL pipeline implementation in Databricks

After get the foundation knowledge about databricks, let's dive into the implementation details in databricks.

## Create Unity Catalog Structure

As mentioned in previous article, Unity Catalog organised files in three-level namespace (catalog.schema.table/volume).
Before start a data project, a clear catalog structure will help a lot on data management.

The catalog are the highest level of the hierarchy and should be used for the broadest logical divisions. it can used
for:

- Environments(prod, dev, qa, sandbox)
- Major domains( marketing, finance...)
- Data Products (for Data Mesh Architectures)
- Share/Common

```SQL
-- Note: If you omit MANAGED LOCATION, Unity Catalog will use a root storage location configured for your metastore. It's generally better to be explicit.
CREATE CATALOG [IF NOT EXISTS] catalog_name
  [MANAGED LOCATION 's3://<bucket-name>/<path>/' | MANAGED LOCATION '<external_location_name>']
  [COMMENT 'catalog_comment'];

GRANT <privilege> ON CATALOG <catalog_name> TO <user_or_group_or_role>.

```

Schemas (also called databases) reside within catalogs and are used to group related tables, views, volumes, and
functions. They are critical for applying the Medallion Architecture and organizing data by domain or stage. it can be:

- Data Processing Stages(bronze, silver, gold)
- Business Domains/Sub-domains
- source systems

```SQL
CREATE SCHEMA [IF NOT EXISTS] [catalog_name.]schema_name
  [MANAGED LOCATION 's3://<bucket-name>/<path>/' | MANAGED LOCATION '<external_location_name>']
  [COMMENT 'schema_comment'];
  GRANT <privilege> ON SCHEMA <schema_name> TO <user_or_group_or_role>.
```

## Storage Location Management

To operated inside dababricks, all the related data storage need to be located with a reference. There are mainly 4
types of storage we need to reference:

### 1. Metastore storage

Metastore is the central brain and metadata repository of Unity Catalog. It's a foundational component that manages all
the metadata for your data assets (tables, views, volumes, functions, external locations, storage credentials, shares,
recipients) and the access control policies applied to them, across all your Databricks workspaces.

Metastores are explicitly created and configured by an Account Admin at the Databricks account level. Normally we create
one metastore per cloud region. It can be be attached to multiple Databricks workspaces within the same region

### 2. Managed Location

A cloud storage location that Databricks Unity Catalog manages on your behalf for storing the actual data files of your
managed tables and managed volumes. This includes the Delta Lake Parquet files, transaction logs, and actual
unstructured files.

You don't directly create a "managed location" with a dedicated SQL command. Instead, you specify a managed location
when you create a Catalog or a Schema.

```SQL
CREATE CATALOG [ IF NOT EXISTS ] catalog_name
    [ USING SHARE provider_name . share_name |
      MANAGED LOCATION location_path |
      COMMENT comment |
      DEFAULT COLLATION default_collation_name |
      OPTIONS ( { option_name = option_value } [ , ... ] ) ] [...]
```

But The specified MANAGED LOCATION path must be contained within an existing, pre-configured Unity Catalog External
Location. to make 'location_path' available you need to:

1. Cloud Provider Side:

- Create an Identity for Databricks Access
- Grant Storage Permissions to the Identity

2. Databricks Unity Catalog Side(AWS as example, different provider may have diffent syntax):

```SQL
-- Create a Storage Credential
CREATE STORAGE CREDENTIAL IF NOT EXISTS <credential_name>
  COMMENT '<your_comment_here>'
  WITH IDENTITY 'arn:aws:iam::<account_id>:role/<iam_role_name>';

-- Create an External Location
CREATE EXTERNAL LOCATION IF NOT EXISTS s3_raw_data_location
  URL 's3://<your-s3-bucket-name>/<optional-path>/'
  WITH (CREDENTIAL aws_s3_storage_credential);

-- Grant Permissions on the External Location
GRANT READ FILES, WRITE FILES ON EXTERNAL LOCATION s3_raw_data_location TO `data_engineers_group`;

```

### 3. External Managed Location

To access data stored in another cloud provider or another account. the steps are similiar as managed location, the only
difference is the cloud provider side need to a more complicated role priviledges.

### 4. Data from Legacy data warehouse

For data residing in external relational databases (like PostgreSQL, MySQL, Snowflake, Redshift, etc.) or other data
warehouses, Databricks provides Lakehouse Federation. we need to:

```SQL
-- Step 1: Create a Connection (requires Metastore Admin or CREATE CONNECTION privilege)
CREATE CONNECTION IF NOT EXISTS my_postgres_db
  TYPE 'POSTGRESQL'
  OPTIONS (
    host 'my-postgres-host.com',
    port '5432',
    user 'my_user',
    password (SELECT secret_string FROM system.secrets WHERE scope = 'my_secret_scope' AND key = 'postgres_password'),
    database 'my_external_database'
  );

-- Step 2: Create a Foreign Catalog (requires CREATE CATALOG privilege on the metastore)
CREATE FOREIGN CATALOG IF NOT EXISTS postgres_catalog
  USING CONNECTION my_postgres_db
  OPTIONS (database 'my_external_database');

-- Now, query tables in the foreign catalog as if they were Unity Catalog tables
SELECT * FROM postgres_catalog.public.external_table_in_postgres LIMIT 10;
```

### 5.Data from Another Databricks Workspace (with a different Unity Catalog Metastore)

To share live Delta tables or volumes between Databricks workspaces, Delta Sharing is the recommended approach:

1. Provider Side: Creates a Share in their Unity Catalog, adds tables/volumes to it, and defines a Recipient.
2. Recipient Side: Creates a Foreign Catalog in their Unity Catalog from the received share.

```SQL
-- Step 1: Create a recipient (if not already done by provider)
-- This is typically handled by the provider in their UC metastore.
-- The recipient would receive an activation link or credentials from the provider.

-- Step 2: Create a Foreign Catalog from the Share
CREATE FOREIGN CATALOG IF NOT EXISTS shared_data_from_partner
  USING SHARE <provider_metastore_id>.<share_name>; -- Example: 'abcdef1234567890.partner_org.sales_share'

-- Now, query tables within the shared catalog
SELECT * FROM shared_data_from_partner.sales_schema.partner_transactions LIMIT 10;
```

Reminder: All the external reference's metadata are stored in the metastore storage, and Remove/Drop these reference
will only impact the metadata, the data in the external storage stay there.

## Move the Raw Data to bronze (streaming, history)

For this stage, we

## Move the bronze data to silver (filter, clean, augment)

## Move the silver data to gold (aggreation)
