{# A basic example for a project-wide macro to cast a column uniformly #}


{% macro cents_to_dollars(column_name) -%}
    ({{ column_name }} / 100)::numeric(16, 2)
{%- endmacro %}
