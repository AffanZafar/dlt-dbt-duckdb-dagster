import duckdb

# Connect to the created DuckDB file
conn = duckdb.connect("/Users/affanzafar/Desktop/datawarehouse/data-warehouse/data.duckdb")

# print(conn.execute("SELECT * FROM information_schema.tables").fetchdf())
# print(conn.execute("SELECT * FROM rest_api_data.my_second_dbt_model").fetchdf())

# conn.execute("CREATE SCHEMA IF NOT EXISTS rest_api_data")