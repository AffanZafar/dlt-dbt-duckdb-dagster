

{{ config(materialized='table') }}

select *

from {{ source('dlt_rest_api' , 'pokemon')}}
