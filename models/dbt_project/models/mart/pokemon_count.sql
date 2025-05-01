{{ config(materialized='view') }}

select name , COUNT(*) as pokemon_count

from {{ ref('src_pokemon') }}

group by name