#!/bin/bash

# Run Python script (in current directory)
echo "Running Python script..."
python data-warehouse/duckdb_utils.py

# Run a command in a specific directory (e.g., /path/to/dir)
echo "Running 'ls -l' in /target/directory..."
(
    cd dagster/ddd|| exit 1  # Exit if directory doesn't exist
    dagster dev
)

# Rest of the script continues in the original directory
echo "Back in original directory: $(pwd)"