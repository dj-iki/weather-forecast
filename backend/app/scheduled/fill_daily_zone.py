from ..models.raw__daily_metrics import RawDailyMetrics
from ..models.update_log import UpdateLog
from ..models.daily__temperature_measurements import DailyTemperatureMeasurements
from ..models.daily__uv_lights_measurements import DailyUVLightsMeasurements
from ..models.daily__precipitation_measurements import DailyPrecipitationMeasurements
from ..models.daily__wind_measurements import DailyWindMeasurements
from ..repository.update_log_repository import get__daily_update_log, update__daily_update_log
from ..repository.raw__daily_metrics_repository import get_raw__daily_metrics_after
from ..repository.daily__measurement_context_repository import get_daily__measurement_context, add_daily__measurement_context, update_daily__measurement_context
from ..repository.daily__temperature_measurements_repository import add_daily__temperature_measurements, get_daily__temperature_measurements, update_daily__temperature_measurements
from ..repository.daily__uv_light_measurements_repository import add_daily__uv_light_measurements, get_daily__uv_light_measurements, update_daily__uv_light_measurements
from ..repository.daily__precipitation_measurements_repository import add_daily__percipitation_measurements, get_daily__precipitation_measurements, update_daily__precipitation_measurements
from ..repository.daily__wind_measurements_repository import add_daily__wind_measurements, get_daily__wind_measurements, update_daily__wind_measurements
from ..dependencies.session import get_db
from ..utils.logger import logger

from geopy.geocoders import Nominatim

def fill_daily_zone():

    db = next(get_db())

    update_log: UpdateLog = get__daily_update_log(db)

    raw__daily_metrics = get_raw__daily_metrics_after(db,update_log)

    for data in raw__daily_metrics:

        geolocator = Nominatim(user_agent="weather-forecast-app-demo")
        location = geolocator.reverse((data.latitude,data.longitude), exactly_one=True)
        if location and 'address' in location.raw:
            address = location.raw['address']
            place_name = address.get('city') or address.get('town') or address.get('village')
            measurement_date = data.measurment_date

            daily__measurement_context = get_daily__measurement_context(db, place_name, measurement_date)

            if not daily__measurement_context:
                daily__measurement_context = add_daily__measurement_context(db, place_name, measurement_date)

                # ADD - DAILY__TEMPERATURE_MEASUREMENTS
                daily__temperature_measurements = DailyTemperatureMeasurements(
                    temperature_2m_min = data.temperature_2m_min_in_C,
                    temperature_2m_max = data.temperature_2m_max_in_C,
                    daily__measurement_context_id = daily__measurement_context.id
                )
                add_daily__temperature_measurements(db, daily__temperature_measurements)

                # ADD - DAILY__UV_LIGHT_MEASUREMENTS
                daily__uv_light_measurements = DailyUVLightsMeasurements(
                    daylight_duration = data.daylight_duration_in_s,
                    uv_index_max = data.uv_index_max,
                    daily__measurement_context_id = daily__measurement_context.id
                )
                add_daily__uv_light_measurements(db, daily__uv_light_measurements)

                # ADD - DAILY__PERCIPITATION_MEASUREMENTS
                daily__percipitation_measurements = DailyPrecipitationMeasurements(
                    precipitation_sum = (data.precipatition_sum_in_mm/1000),
                    precipitation_length = (data.precipatition_hours_in_h*3600),
                    precipitation_probability_max = data.precipatition_probability_max_in_p,
                    daily__measurement_context_id = daily__measurement_context.id
                )
                add_daily__percipitation_measurements(db, daily__percipitation_measurements)

                # ADD - DAILY__WIND_MEASUREMETNS
                daily__wind_measurements = DailyWindMeasurements(
                    wind_speed_10m_max  = (data.wind_speed_10m_max_in_kmph*3.6),
                    wind_direction_10m_dominant = data.wind_direction_10m_dominant_in_degree,
                    daily__measurement_context_id = daily__measurement_context.id
                )
                add_daily__wind_measurements(db, daily__wind_measurements)

            else:
                update_daily__measurement_context(db, daily__measurement_context)

                # UPDATE - DAILY__TEMPERATURE_MEASUREMENTS
                daily__temperature_measurements = get_daily__temperature_measurements(db, daily__measurement_context)
                update_daily__temperature_measurements(db, daily__temperature_measurements, data)

                # UPDATE - DAILY__UV_LIGHT_MEASUREMENTS
                daily__uv_light_measurements = get_daily__uv_light_measurements(db, daily__measurement_context)
                update_daily__uv_light_measurements(db, daily__uv_light_measurements, data)

                # UPDATE - DAILY__PRECIPITAION_MEASUREMENTS
                daily__precipitation_measurements = get_daily__precipitation_measurements(db, daily__measurement_context)
                update_daily__precipitation_measurements(db, daily__precipitation_measurements, data)

                #UPDATE - DAILY__WIND_MEASUREMENTS
                daily__wind_measurements = get_daily__wind_measurements(db, daily__measurement_context)
                update_daily__wind_measurements(db, daily__wind_measurements, data)

            update__daily_update_log(db)
        else:
            logger.warning("CITY NOT FOUND")


# long 20.458527 lat 44.810673
# long 20.458527 lat 44.810673
