from pathlib import Path

from dagster_dbt import DbtProject

dbtlearn_project = DbtProject(
    project_dir="/Users/affanzafar/Desktop/datawarehouse/models/dbt_project",
    packaged_project_dir="/Users/affanzafar/Desktop/datawarehouse/models/dbt_project/models ",
)
dbtlearn_project.prepare_if_dev()