from typing import Any, Optional

import dlt
from dlt.common.pendulum import pendulum
from dlt.sources.rest_api import (
    RESTAPIConfig,
    check_connection,
    rest_api_resources,
    rest_api_source,
)


def load_pokemon() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="rest_api_pokemon",
        destination=dlt.destinations.duckdb("/Users/affanzafar/Desktop/datawarehouse/data-warehouse/data.duckdb"),
        dataset_name="rest_api_data",
        dev_mode=False
    )

    pokemon_source = rest_api_source(
        {
            "client": {
                "base_url": "https://pokeapi.co/api/v2/",
                # If you leave out the paginator, it will be inferred from the API:
                # "paginator": "json_link",
            },
            "resource_defaults": {
                "endpoint": {
                    "params": {
                        "limit": 1000,
                    },
                },

                "write_disposition": "replace",
            },
            "resources": ["pokemon"],
        }
    )

    load_info = pipeline.run(pokemon_source)
    return pokemon_source


if __name__ == "__main__":
    load_pokemon()
