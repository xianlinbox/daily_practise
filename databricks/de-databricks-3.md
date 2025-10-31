# Databricks Series(3): The engineering part

## CI/CD

### Version Control (Databricks Repos)

Integrate your Databricks notebooks and other code files (Python, Scala, R, SQL) with an external Git provider (GitHub,
GitLab, Azure DevOps, Bitbucket, AWS CodeCommit). It maps a folder in your Databricks workspace to a Git repository.

### Pipeline

Once your tests are in a Git repo, your CI/CD pipeline (e.g., GitHub Actions, Azure DevOps, GitLab CI) can:

1. Checkout the Repo: Clone your Databricks Repo.
2. Spin up a Databricks Job: Create a Databricks Job that runs your test notebook or a test script (which, in turn,
   executes pytest).
3. Run pytest: The Databricks Job can execute pytest against your modularized .py test files.
4. Report Results: Capture the test results (JUnit XML, etc.) and report them back to your CI/CD system.

Databricks Asset Bundles (DABs): A newer, more streamlined way to manage and deploy entire Databricks projects,
including tests, through a manifest file and the Databricks CLI.

## Databricks Connect

Connect local dev environment to Databricks cluster. you can run your local code on databricks cluster.

## Orchestration

In many modern Lakehouse architectures, you'll often see DLT pipelines running as tasks within a larger Databricks Job.
This allows DLT to handle the core ETL logic reliably and automatically, while the parent Job orchestrates DLT with
other pre- or post-processing tasks, external system integrations, or diverse workloads.

## Databricks Jobs

Databricks Jobs is a general-purpose orchestration service for running arbitrary code on Databricks clusters. A "Job"
can consist of one or more "Tasks," where each task can be a notebook, JAR, Python script, DLT pipeline, SQL file, or
even an external task. Jobs define a DAG (Directed Acyclic Graph) of tasks with dependencies.

When to use:

1. Diverse worklods
2. Fine grained task control
3. integrated with other DLT
4. complex batch jobs

we can set Trigger, notification, permissions, Alerts

### Delta Live Table

DLT is a framework for building highly reliable, maintainable, and testable ETL/ELT pipelines. You declaratively define
the transformations using SQL or Python, and DLT automates infrastructure management, data lineage, error handling, and
data quality (Expectations).

When to use:

1. Just for an ETL pipeline

## Goverance

## Profiling

1. Spark UI (again, but with a profiling mindset):

- DAG Visualization: Analyze the physical plan. Look for expensive stages, shuffles, and joins.
- SQL Tab -> Query Plan: Understand how Spark optimized your SQL. Look for filter pushdowns, broadcast joins, and
  repartitioning.
- Stages Tab -> Task Details: Data Skew: Look for wide variations in task durations within a stage. One or a few tasks
  running much longer than others indicates data skew.
- Shuffle Read/Write: High shuffle activity is often a sign of expensive operations (joins, aggregations,
  repartitioning).
- Garbage Collection (GC) Time: Excessive GC time indicates memory pressure.
- Spill to Disk: If tasks are spilling data to disk, it means they are running out of memory.
- Executor Tab: Monitor executor health, memory usage, and thread activity.

2. Databricks Query Profile (for Databricks SQL Warehouses):

- Purpose: Provides an intuitive, graphical query profiler for SQL queries, simplifying performance analysis. Details:
  Visualizes the query plan with execution metrics (time, rows, memory) for each node.
- Hotspot Identification: Easily identify the slowest parts of your query (e.g., specific joins, scans, aggregations).
- Recommendations: Sometimes provides hints for optimization.
- Access: Click on a query in Query History or view directly from a SQL editor.

3. Databricks System Tables (Preview):

- Purpose: Provides operational data about your Databricks account, including audit logs, billing, and usage.
- Details: You can query tables like system.access.audit_log (for DDL/DML, access, etc.), system.billing.usage (for DBU
  consumption), system.workflow.job_runs to gain deeper insights into resource usage, performance, and cost trends
  across your entire environment.
- Value: Powerful for trend analysis, chargeback, and identifying patterns of inefficiency.

4. Delta Lake DESCRIBE HISTORY:

- Purpose: Track changes and operations on your Delta tables.
- Details: Shows who performed an operation, when, what operation it was (WRITE, UPDATE, MERGE), and key operation
  metrics.
- Value: Helps identify which operations are performing poorly or causing unexpected changes to data.

## Alerts

- Databricks Workflows (Jobs) Alerts
- Delta Live Tables (DLT) Pipeline Alerts
- Databricks SQL Alerts
- System Tables for Advanced Monitoring and Alerts

## Databricks Asset Bundles (DABs):

A relatively new and highly recommended feature for managing, deploying, and running Databricks projects in a
structured, automated, and repeatable way.

A DAB is a manifest file (YAML) that defines an entire Databricks project, including its:

- Source code: Notebooks, Python/Scala modules in Databricks Repos.
- Infrastructure: Clusters, jobs, DLT pipelines, Unity Catalog objects (catalogs, schemas, volumes, external locations,
  storage credentials).
- Deployments: How to deploy the project to different environments (development, staging, production).
- Tests: Commands to run unit or integration tests.

```yaml
# databricks.yml
bundle:
  name: my-lakehouse-etl-bundle

resources:
  jobs:
    etl_job:
      name: ${bundle.target}-my-lakehouse-etl-job
      tasks:
        - task_key: bronze_ingestion
          new_cluster:
            spark_version: 13.3.x-scala2.12
            node_type_id: Standard_DS3_v2
            num_workers: 2
          notebook_task:
            notebook_path: ../notebooks/bronze_ingestion_notebook.py
            base_parameters:
              catalog_name: ${var.catalog}
              schema_name: ${var.bronze_schema}
        - task_key: silver_transform
          depends_on: [bronze_ingestion]
          pipeline_task:
            pipeline_id: ${resources.dlt_pipelines.silver_pipeline.id} # Reference DLT pipeline
  dlt_pipelines:
    silver_pipeline:
      name: ${bundle.target}-silver-data-pipeline
      target: ${var.catalog}.${var.silver_schema}
      libraries:
        - notebook:
            path: ../notebooks/silver_dlt_pipeline.py
      # ... other DLT settings

  catalog: # Unity Catalog resources defined directly in the bundle
    schemas:
      bronze_schema:
        name: ${var.catalog}.bronze
        comment: "Raw data landing zone"
      silver_schema:
        name: ${var.catalog}.silver
        comment: "Cleaned and transformed data"

targets:
  dev:
    workspace:
      host: https://adb-xxx.azuredatabricks.net
    variables:
      catalog: dev_catalog # Environment-specific catalog
      bronze_schema: bronze_dev
      silver_schema: silver_dev
    # ... more environment specific settings

  prod:
    workspace:
      host: https://adb-yyy.azuredatabricks.net
    variables:
      catalog: prod_catalog # Environment-specific catalog
      bronze_schema: bronze
      silver_schema: silver
    # ... more environment specific settings
```

Then we can use DataBricks cli to interact with a databricks workspace

```shell
databricks bundle validate: Checks the databricks.yml for syntax errors.
databricks bundle deploy --target <env>: Deploys all defined resources (jobs, pipelines, UC objects) to the specified environment.
databricks bundle run <job-or-pipeline-key> --target <env>: Triggers a specific job or pipeline defined in the bundle.
databricks bundle destroy --target <env>: Tears down all resources deployed by the bundle in that environment (use with extreme caution!).
```
