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

### Delta Live Table

DLT is a framework for building highly reliable, maintainable, and testable ETL/ELT pipelines. You declaratively define
the transformations using SQL or Python, and DLT automates infrastructure management, data lineage, error handling, and
data quality (Expectations).

When to use:

1. Just for an ETL pipeline

## Goverance & Monitoring

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

## Databricks Asset Bundles (DABs):

A newer, more streamlined way to manage and deploy entire Databricks projects, including tests, through a manifest file
and the Databricks CLI.
