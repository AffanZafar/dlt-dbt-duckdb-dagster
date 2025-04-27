{{ config(materialized='view') }}

select name , COUNT(*) as pokemon_count

from {{ ref('my_first_dbt_model') }}

group by name