🚀 Modern Data Pipeline: ELT with dlt, dbt, DuckDB & Dagster
A lightweight, open-source data engineering stack for end-to-end analytics—from raw data to business insights.

✨ Key Features
✅ Extract & Load: Automated data ingestion with dlt (Python-friendly)
✅ Transform: SQL-based modelling with dbt + Duckdb
✅ Orchestrate: Pipeline monitoring/scheduling via Dagster
✅ Analyse: Blazing-fast queries with embedded Duckdb (no servers!)
✅ Portable: Runs locally or scales to cloud (AWS/GCP/Azure)

🌐 Ideal For
Building self-service analytics for small/medium datasets

Prototyping data products without heavy infrastructure

Learning modern data tools with a fully open-source stack

![Data Stack Architecture](Data-Stack.jpeg) 

## 🚀 Project Structure
```plaintext
.
├── dagster/                  # Dagster pipelines and assets
├── data-warehouse/           # Raw data and processed outputs 
├── dlt/                      # Data extraction and loading scripts
├── models/                   # dbt models
├── Data-Stack.jpeg           # Architecture diagram
├── .gitignore                # Git ignore rules
├── README.md                 # Project documentation          
```
