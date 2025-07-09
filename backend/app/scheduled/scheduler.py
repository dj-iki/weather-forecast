from .fill_raw_zone import get_raw_hourly_data, get_raw__daily_data
from .fill_hourly_zone import fill_hourly_zone
from .fill_daily_zone import fill_daily_zone

def scheduled_hourly():
    get_raw_hourly_data()
    fill_hourly_zone()

def scheduled_daily():
    get_raw__daily_data()
    fill_daily_zone()    
