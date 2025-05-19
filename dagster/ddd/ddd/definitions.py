from dagster import Definitions,job
import dagster as dg
from dagster_dbt import DbtCliResource
from .assets import dbtlearn_dbt_assets , dagster_pokemon_assets 
from .project import dbtlearn_project
from dagster_duckdb import DuckDBResource
from dagster_dlt import DagsterDltResource
from dagster import define_asset_job, ScheduleDefinition
from dagster_dbt import build_dbt_asset_selection

dlt_resource = DagsterDltResource()

# Create a selection for dbt assets with a specific tag
tagged_dbt_selection = build_dbt_asset_selection(
    dbt_assets=[dbtlearn_dbt_assets],
    dbt_select="tag:pokemon"  # Replace with your actual tag name
)

tagged_dbt_selection = tagged_dbt_selection.upstream().downstream()

# Define a job that only includes dbt assets with the specific tag
tagged_dbt_job = define_asset_job(
    name="tagged_dbt_job",
    selection=tagged_dbt_selection,
)

all_assets_job = dg.define_asset_job(name="all_assets_job" , selection=[dbtlearn_dbt_assets , dagster_pokemon_assets])

daily_schedule_all = dg.ScheduleDefinition(
    job=all_assets_job,
    cron_schedule="0 0 * * *",  # Runs at midnight daily
)

daily_schedule_dbt_tagged = dg.ScheduleDefinition(
    job=tagged_dbt_job,
    cron_schedule="0 0 * * *",  # Runs at midnight daily
)

defs = Definitions(
    assets=[dagster_pokemon_assets, dbtlearn_dbt_assets],
    jobs=[all_assets_job ,tagged_dbt_job],
    schedules=[daily_schedule_all , daily_schedule_dbt_tagged],
    resources={
        "dbt": DbtCliResource(project_dir=dbtlearn_project.project_dir ,
                              profiles_dir=dbtlearn_project.profiles_dir),
        "duckdb": DuckDBResource(
            database="/Users/affanzafar/Desktop/datawarehouse/data-warehouse/data.duckdb",  # required
        ) ,
        "dlt": dlt_resource,
    },
)