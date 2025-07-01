from ..utils.logger import logger
from ..models.raw__daily_metrics import RawDailyMetrics
from ..models.raw__hourly_metrics import RawHourlyMetrics
from ..repository.raw__hourtly_metrics_repository import add_raw__hourly_metrics, get_raw__hourly_metrics, update_raw__hourly_metrics
from ..repository.raw__daily_metrics_repository import add_raw__daily_metrics, get_raw__daily_metrics, update_raw__daily_metrics
from ..dependencies.session import get_db
from datetime import datetime
from ..settings import settings
import requests


# latitude=44.804 longitude=20.4651 kordinate Beograda

def get_raw__daily_data():
    url = f"{settings.api_url}latitude=44.804&longitude=20.4651&daily=temperature_2m_max,temperature_2m_min,daylight_duration,uv_index_max,precipitation_sum,precipitation_hours,precipitation_probability_max,wind_speed_10m_max,wind_direction_10m_dominant&timezone=auto&forecast_days=7"

    response = requests.get(url)
     
    data = response.json()
     
    if response.ok:
        
        logger.info("Hourly weather-forecast information gathered successfully")

        db = next(get_db())

        for i in range(7):

            timestamp = datetime.strptime(data["daily"]["time"][i], "%Y-%m-%d")
            measturements = get_raw__daily_metrics(db, data["longitude"], data["latitude"], timestamp)

            if not measturements:
                add_raw__daily_metrics(db, data, i)
            else:
                update_raw__daily_metrics(db, measturements, data, i)

    else:
        logger.warning(f"Api request for daily weather forecast failed. Status code={response.status_code}. Error={data['reason']}")
        # raise HTTPException(status_code=response.status_code, detail="Api request failed")


def get_raw_hourly_data():
    url = f"{settings.api_url}latitude=44.804&longitude=20.4651&hourly=temperature_2m,relative_humidity_2m,precipitation,precipitation_probability,cloud_cover_low,cloud_cover,cloud_cover_mid,cloud_cover_high,visibility,wind_speed_10m,wind_direction_10m,wind_speed_80m,wind_speed_120m,wind_speed_180m,wind_direction_80m,wind_direction_120m,wind_direction_180m,temperature_120m,temperature_80m,temperature_180m,soil_temperature_0cm,soil_temperature_6cm,soil_temperature_18cm,soil_temperature_54cm,soil_moisture_0_to_1cm,soil_moisture_1_to_3cm,soil_moisture_3_to_9cm,soil_moisture_9_to_27cm,soil_moisture_27_to_81cm&timezone=auto&forecast_hours=2"

    response = requests.get(url)
     
    data = response.json()

    if response.ok:

        logger.info("Hourly weather-forecast information gathered successfully")
        db = next(get_db())
        for i in range(2):

            timestamp = datetime.strptime(data["hourly"]["time"][i], "%Y-%m-%dT%H:%M")

            measturements = get_raw__hourly_metrics(db, data["longitude"], data["latitude"], timestamp)
            if not measturements:
                add_raw__hourly_metrics(db, data, i)
            else:
                update_raw__hourly_metrics(db, measturements, data, i)

    else:
        logger.warning(f"Api request for daily weather forecast failed. Status code={response.status_code}. Error={data['reason']}")