from dagster import Definitions
import dagster as dg
from dagster_dbt import DbtCliResource
from .assets import dbtlearn_dbt_assets , dagster_pokemon_assets  , dagster_jaffleshop_assets
from .project import dbtlearn_project
from dagster_duckdb import DuckDBResource
from dagster_dlt import DagsterDltResource

dlt_resource = DagsterDltResource()

all_assets_job = dg.define_asset_job(name="all_assets_job")

daily_schedule = dg.ScheduleDefinition(
    job=all_assets_job,
    cron_schedule="0 0 * * *",  # Runs at midnight daily
)

defs = Definitions(
    assets=[dagster_pokemon_assets, dbtlearn_dbt_assets , dagster_jaffleshop_assets ],
    jobs=[all_assets_job],
    schedules=[daily_schedule],
    resources={
        "dbt": DbtCliResource(project_dir=dbtlearn_project.project_dir ,
                              profiles_dir=dbtlearn_project.profiles_dir),
        "duckdb": DuckDBResource(
            database="/Users/affanzafar/Desktop/datawarehouse/data-warehouse/data.duckdb",  # required
        ) ,
        "dlt": dlt_resource,
    },
)