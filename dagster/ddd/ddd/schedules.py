"""
To add a daily schedule that materializes your dbt assets, uncomment the following lines.
"""
import dagster as dg
from .assets import daily_refresh_job

daily_schedule = dg.ScheduleDefinition(
    job=daily_refresh_job,
    cron_schedule="0 0 * * *",  # Runs at midnight daily
)