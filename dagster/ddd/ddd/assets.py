from dagster import AssetExecutionContext , AssetKey
from dagster_dbt import DbtCliResource, dbt_assets
import dagster as dg
import dlt
from .project import dbtlearn_project
from dagster import asset
from dagster_dlt import DagsterDltResource, dlt_assets
from dlt import pipeline
from .rest_api_pipeline import load_pokemon


@dlt_assets(
    dlt_source=load_pokemon(),
    dlt_pipeline = pipeline(
        pipeline_name="rest_api_pokemon",
        destination=dlt.destinations.duckdb("/Users/affanzafar/Desktop/datawarehouse/data-warehouse/data.duckdb"),
        dataset_name="rest_api_data",
        dev_mode=False,
    )
)
def dagster_pokemon_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)


@dbt_assets(manifest=dbtlearn_project.manifest_path)
def dbtlearn_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    

