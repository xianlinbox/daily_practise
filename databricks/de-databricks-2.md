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

## Move the Raw Data to bronze

Based above information, we have know where the data stored, how can we access it and how to manage the data. The next
step is moving raw data into databricks.

Databricks provide bunch of ways for customer:

1. Auto Loader (Recommended for Cloud Object Storage)

Efficiently and incrementally processes new data files as they arrive in your cloud object storage (like AWS S3, Azure
Data Lake Storage Gen2, or Google Cloud Storage). It's designed to simplify and automate the ingestion of large volumes
of data from external file systems into Delta Lake tables, forming the foundation of many Bronze layer pipelines in a
Lakehouse architecture.,

Suitable for: continuous, high-volume, low-latency streaming scenarios

An example:

```SQL
-- SQL to create a managed volume for Auto Loader state (if not already existing)
USE CATALOG my_catalog;
USE SCHEMA raw_schema;
CREATE MANAGED VOLUME IF NOT EXISTS autoloader_state
  COMMENT 'Managed volume for Auto Loader schema and checkpoint locations.';

-- Create a STREAMING TABLE for raw event data.
-- DLT automatically manages Auto Loader and Structured Streaming for this.

CREATE OR REFRESH STREAMING TABLE events_raw
COMMENT 'Raw event data ingested from S3 landing zone via Auto Loader.'
AS SELECT
    _metadata.file_path, -- Auto Loader automatically adds metadata columns
    _metadata.file_name,
    _metadata.file_size,
    CAST(_metadata.file_modification_time AS TIMESTAMP) AS file_modified_time,
    -- Assuming your JSON files have 'id', 'timestamp', 'event_type', 'data' fields
    CAST(id AS STRING) AS event_id,
    CAST(timestamp AS TIMESTAMP) AS event_timestamp,
    CAST(event_type AS STRING) AS event_type,
    CAST(data AS STRING) AS event_data, -- Storing 'data' as raw string for now
    current_timestamp() AS ingestion_timestamp -- Add ingestion timestamp
   FROM cloud_files(
     's3://my-raw-data-bucket/events/', -- **Source path for raw files**
     'json',                            -- Specify the file format
     map(                                -- Auto Loader options
       'cloudFiles.schemaLocation', '/Volumes/my_catalog/raw_schema/autoloader_state/events_raw_schema_location', -- **UC Managed Volume path for schema state**
       'cloudFiles.inferColumnTypes', 'true', -- Instruct Auto Loader to infer data types
       'cloudFiles.includeFileName', 'true',  -- Include the source filename in the output
       'cloudFiles.maxFilesPerTrigger', '100', -- Optional: Process up to 100 files per micro-batch
       'cloudFiles.partitionColumns', 'event_type' -- Optional: Specify partition columns for better performance
     )
   );
```

2. COPY INTO Command (Recommended for Idempotent Batch Ingestion from Object Storage)

a SQL command introduced in Databricks that loads data from files in a specified cloud storage location into a Delta
Lake table.

Suitable for: simpler, idempotent, and scheduled batch ingestion needs where real-time processing isn't a strict
requirement.

An example:

```SQL
-- Step 1: Ensure your target table exists in Unity Catalog (you can let COPY INTO infer schema later)
USE CATALOG my_catalog;
USE SCHEMA raw_schema;

CREATE TABLE IF NOT EXISTS customers_raw; -- We'll let COPY INTO define schema on first run

-- Step 2: Run COPY INTO to ingest data
COPY INTO my_catalog.raw_schema.customers_raw
FROM (
    SELECT
        CAST(col0 AS INT) AS customer_id, -- Explicit casting from inferred types if needed
        CAST(col1 AS STRING) AS first_name,
        CAST(col2 AS STRING) AS last_name,
        CAST(col3 AS STRING) AS email,
        file_name() AS source_file, -- Add file metadata
        current_timestamp() AS ingestion_timestamp
    FROM 's3://my-raw-data-bucket/customers/' -- This path must be covered by an External Location
)
FILEFORMAT = CSV
FORMAT_OPTIONS (
    'header' = 'true',
    'inferSchema' = 'true',
    'delimiter' = ',',
    'recursiveFileLookup' = 'true' -- If CSVs are in subfolders
)
COPY_OPTIONS (
    'mergeSchema' = 'true' -- Allow schema evolution (e.g., if new columns appear)
);

-- After first run, schema will be defined for customers_raw.
-- Subsequent runs will only process new CSV files in 's3://my-raw-data-bucket/customers/'.
```

3. Spark Read API (for various sources)

The Spark Read API is the foundational and most flexible way to ingest raw data into Databricks using Apache Spark.
While Auto Loader and COPY INTO are specialized, higher-level abstractions built on top of Spark, the Spark Read API
provides granular control and versatility for connecting to a vast array of data sources.

Spark Read API (exposed through spark.read for batch and spark.readStream for streaming), it supports:

- Specify a data source format: format("csv"), format("json"), format("jdbc"), format("kafka"), etc.
- Provide options: Set various configurations specific to the format (e.g., option("header", "true") for CSV,
  option("inferSchema","true"), option("url", "...") for JDBC).
- Load data: Point to a path (for files) or connection details (for databases, message queues) using .load().
- Return a DataFrame: The result of a read operation is always a Spark DataFrame, which you can then transform and write

Suitable for:

- autoLoader and copy into doesn't support source
- custom or complex ingestion logic
- integrate with niche data sources.

4. Cloud-Native Data Ingestion Services

Using cloud migration tool to move data between cloud storage. like AWS DMS to move data from one S3 bucket to a managed
location in Datbricks. Excellent for moving data into your cloud landing zone before Databricks picks it up with Auto
Loader or COPY INTO

5. Upload files to cloud storage manually

## Move the bronze data to silver (filter, clean, augment)

### Data Discovering

- UI functions:

  - Databricks Data Explorer (UI-based)
  - Automatic Data Lineage(Visual Graph)
  - Databricks Search Bar: Search across notebooks, jobs, and critically, Unity Catalog objects (by name, comment, or
    tag).

- Commands:

```SQL
-- Show objects
SHOW Catalog/Schema/TABLES... [IN ...]
SHOW Grant On ...
DESCRIBE TABLE/History catalog.schema.table_name;

```

### Extract/Query Data

```SQL
-- Select Clause
SELECT
    [ALL | DISTINCT]
    expression_1 [AS column_alias_1],
    expression_2 [AS column_alias_2],
    ...
    expression_n [AS column_alias_n]
FROM
    [catalog_name.]schema_name.table_name [AS table_alias]
    [JOIN ...]
    [LATERAL VIEW ...]
WHERE
    condition
GROUP BY
    column_or_expression_1, ...
HAVING
    group_condition
WINDOW
    window_spec_definition
ORDER BY
    column_or_expression_1 [ASC | DESC] [NULLS FIRST | NULLS LAST], ...
LIMIT
    number
OFFSET
    number

--Select from file directly
Select * FROM <json|text|csv|binary>.<cloud_storage_path>
select * from read_files(
  's3://your-bucket/path/to/data.json',
  format => 'JSON',
  multiline => true -- Example option
);
```

### Tables

Most tables in Databricks should be Delta Lake tables, which provide a wealth of capabilities:

- ACID Transaction
- Schema enforce/envolvement
- Time Travel (Data Versioning):
- Change Data Feed (CDF)
- Unified Batch and Streaming

#### Operations

```SQL
CREATE TABLE [EXTERNAL] [IF NOT EXISTS] catalog.schema.table_name (...) [USING DELTA] [LOCATION ...];
WITH [ RECURSIVE ] common_table_expression [, ...]: Common table expression, Defines a temporary result set that you can reference possibly multiple times within the scope of a SQL statement
ALTER TABLE ...: Modify schema (add/drop/change columns), set table properties.
DROP TABLE ...: Delete the table (and data for managed tables).
TRUNCATE TABLE ...: Delete all data from a table, leaving the schema.

INSERT INTO ... VALUES (...) / INSERT INTO ... SELECT ...: Add new rows.
UPDATE ... SET ... WHERE ...: Modify existing rows.
DELETE FROM ... WHERE ...: Remove rows.
MERGE INTO ... USING ... ON ... WHEN MATCHED ... WHEN NOT MATCHED ...: Perform UPSERT (update or insert) operations efficiently.
```

#### Security

1. Grant priviledges on tables
2. Apply Row-Level Security (RLS) and Column-Level Security (CLS) to tables if needed, eg:

```SQL
-- 1. Create a SQL function for the RLS policy
CREATE FUNCTION my_catalog.security_policies.filter_by_region(region_column STRING)
  RETURN IF(
    IS_ACCOUNT_GROUP_MEMBER('finance_users') OR -- Finance can see all regions
    region_column = current_user(),             -- Or if region matches current user (assuming user ID is region)
    TRUE,                                       -- Allow access
    FALSE                                       -- Deny access
  );

-- 2. Apply the RLS policy to a table
ALTER TABLE my_catalog.gold_data.sales_transactions
  SET ROW FILTER my_catalog.security_policies.filter_by_region ON (region);
```

#### Performance Optimization for Tables

1. Z-Ordering/Partitioning (legacy): physically collocates related information (based on selected columns) into the same
   set of files.
2. Liquid Clustering (recommended): clustering technique that replaces static partitioning and Z-Ordering. It
   automatically adapts to data changes and query patterns. Define CLUSTERING BY (col1, col2) during CREATE TABLE. Run
   OPTIMIZE periodically to trigger clustering.
3. Vaccum: Removes data files that are no longer referenced by the Delta Lake transaction log. VACUUM table_name RETAIN
   7 HOURS; (Requires a RETAIN clause for safety, default is 7 days). Use with caution!
4. Photon Engine: Databricks' native vectorized query engine
5. Caching:

#### Quality & Validation

1. Delta Live Tables (DLT) Expectations: recommended approach for continuous data quality enforcement in your streaming
   or batch ETL pipelines.
2. Constraints: supports standard SQL constraints like NOT NULL, CHECK, PRIMARY KEY, and FOREIGN KEY

```SQL
EXPECT (constraint_name) ON (condition): Simply monitors the quality. Records violating the condition are counted and reported in DLT logs and UI. The pipeline continues.
EXPECT (constraint_name) ON (condition) EXPECTATIONS AS (FAIL UPDATE): Rows violating the condition are dropped from the target table, but the pipeline continues.
EXPECT (constraint_name) ON (condition) EXPECTATIONS AS (DROP ROW): Same as FAIL UPDATE, drops rows.
EXPECT (constraint_name) ON (condition) EXPECTATIONS AS (FAIL BATCH): If any row violates the condition, the entire batch processing fails. This is for critical data quality rules where any bad data is unacceptable.
```

### Views

View allowing you to present data in a user-friendly and controlled manner without duplicating storage. There are 2
types of View in Databricks:

1. Standar View: logical. The query is executed every time the view is referenced. this view has standard, temporary,
   global temporary scopes.

```SQL
CREATE [OR REPLACE] [TEMPORARY | GLOBAL TEMPORARY] VIEW [IF NOT EXISTS] [catalog_name.]schema_name.view_name
  [(column_list)]
  [COMMENT view_comment]
  [TBLPROPERTIES ( { key = val } [, ...] )]
  AS query_definition;

```

---

- **Summary of Differences:**

| Feature                 | Normal (Permanent) View in Unity Catalog                                | Temporary View                                      | Global Temporary View                    |
| :---------------------- | :---------------------------------------------------------------------- | :-------------------------------------------------- | :--------------------------------------- |
| **Scope of Visibility** | Account-wide (across all UC-enabled workspaces in the metastore region) | Single SparkSession (e.g., one notebook)            | All SparkSessions on a single cluster    |
| **Persistence**         | Persistent (stored in Unity Catalog)                                    | Session-scoped (disappears with session)            | Cluster-scoped (disappears with cluster) |
| **Governance**          | **Fully governed by Unity Catalog**                                     | Not governed by Unity Catalog                       | Not governed by Unity Catalog            |
| **Namespace**           | `catalog.schema.view_name`                                              | `view_name`                                         | `global_temp.view_name`                  |
| **Deletion**            | `DROP VIEW` command needed                                              | Automatic when session ends                         | Automatic when cluster terminates        |
| **Best Use Cases**      | Production data models, shared datasets, security views                 | Ad-hoc analysis, intermediate steps in one notebook | Shared intermediate data on one cluster  |

2. Materialized View: The data in an MV is derived from a source query and is automatically refreshed (either
   incrementally or fully) when the underlying source tables change. offer much better performance for repeated queries
   as data is pre-computed. However, they incur storage costs and refresh latency. MV doesn't support temporary scopes.

```SQL
CREATE MATERIALIZED VIEW [IF NOT EXISTS] [catalog_name.]schema_name.view_name
  [COMMENT view_comment]
  [TBLPROPERTIES ( { key = val } [, ...] )]
  [REFRESH { EVERY 'interval' | MANUAL | ON SCHEMA CHANGE }] -- Schedule for automatic refresh
  AS query_definition;
```

## Move the silver data to gold (aggreation)

### Aggreagtion

### User Define Functions(UDF)
