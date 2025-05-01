from pathlib import Path

from dagster_dbt import DbtProject

dbtlearn_project = DbtProject(
    project_dir="/Users/affanzafar/Desktop/datawarehouse/models/dbt_project",
    profiles_dir="/Users/affanzafar/Desktop/datawarehouse/models/dbt_project",
)
