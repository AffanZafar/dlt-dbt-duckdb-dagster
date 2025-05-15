from dagster import AssetExecutionContext , AssetKey
from dagster_dbt import DbtCliResource, dbt_assets , DagsterDbtTranslator
from dagster_dbt import DbtProject
import dagster as dg
from typing import Mapping, Any, Optional
import dlt
from dagster import asset
from dagster_dlt import DagsterDltResource, dlt_assets
from dlt import pipeline
from .rest_api_pipeline import load_pokemon
from .jaffleshop import jaffleshop

@dlt_assets(
    dlt_source=load_pokemon(),
    dlt_pipeline = pipeline(
        pipeline_name="rest_api_pokemon",
        destination=dlt.destinations.duckdb("/Users/affanzafar/Desktop/datawarehouse/data-warehouse/data.duckdb"),
        dataset_name="rest_api_data",
        dev_mode=False,
    ),
    group_name="dlt_pokemon",
)
def dagster_pokemon_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)

@dlt_assets(
    dlt_source=jaffleshop(),
    dlt_pipeline = pipeline(
    pipeline_name="orders_pipeline",
    destination=dlt.destinations.duckdb("/Users/affanzafar/Desktop/datawarehouse/data-warehouse/data.duckdb"),
    dataset_name="jaffleshop",
    dev_mode=True,
),
    group_name="jaffleshop",
)
def dagster_jaffleshop_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)


# @dbt_assets(manifest=dbtlearn_project.manifest_path)
# def dbtlearn_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
#     yield from dbt.cli(["build"], context=context).stream()

dbtlearn_project = DbtProject(
    project_dir="/Users/affanzafar/Desktop/datawarehouse/models/dbt_project",
    profiles_dir="/Users/affanzafar/Desktop/datawarehouse/models/dbt_project",
)

class CustomTranslator(DagsterDbtTranslator):
    def get_group_name(self, dbt_resource_props: Mapping[str, Any]) -> Optional[str]:
        meta = dbt_resource_props.get("meta", {})
        dagster_meta = meta.get("dagster", {}) if isinstance(meta, dict) else {}

        return dagster_meta.get("layer", "dbt_models")


dbtlearn_project.prepare_if_dev()


@dbt_assets(
    manifest=dbtlearn_project.manifest_path, dagster_dbt_translator=CustomTranslator()
)
def dbtlearn_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    


