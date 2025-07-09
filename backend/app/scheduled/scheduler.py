from .fill_raw_zone import get_raw_hourly_data
from .fill_hourly_zone import fill_hourly_zone

def scheduled_hourly():
    get_raw_hourly_data()
    fill_hourly_zone()
