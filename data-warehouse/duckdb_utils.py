import duckdb

# Connect to the created DuckDB file
conn = duckdb.connect("/Users/affanzafar/Desktop/datawarehouse/data-warehouse/data.duckdb")

print(conn.execute("SELECT * FROM information_schema.tables LIMIT 5").fetchdf())
print(conn.execute("SELECT * FROM rest_api_data.orders LIMIT 5").fetchdf())

# conn.execute("CREATE SCHEMA IF NOT EXISTS rest_api_data")