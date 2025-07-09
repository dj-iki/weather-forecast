from ..dependencies.session import get_db
from ..repository.raw__hourtly_metrics_repository import get_raw__hourly_metrics_after
from ..repository.update_log_repository import get__hourly_update_log, update__hourly_update_log
from ..models.hourly__measurement_context import HourlyMesurementContext
from ..models.hourly__percipitation_measurements import HourlyPercipitationMeasurements
from ..models.hourly__soil_measurements import HourlySoilMeasurements
from ..models.hourly__temperature_measurements import HourlyTemperatureMeasurements
from ..models.hourly__visibility_measurements import HourlyVisibilityMeasurements
from ..models.hourly__wind_measurements import HourlyWindMeasurements
from ..repository.hourly__measurement_context_repository import get_hourly_measurement_context, add_hourly__measurement_context, update_hourly__measurement_context
from ..repository.hourly__wind_measurements_repository import add_hourly__wind_measurements, get_hourly__wind_measurements, update_hourly__wind_measurements
from ..repository.hourly__visibility_measurements_repository import add_hourly__visibility_measurements, get_hourly__visibility_measurements, update_hourly__visibility_measurements
from ..repository.hourly__temperature_measurements_repository import add_hourly__temperature_measurements, get_hourly__temperature_measurements, update_hourly__temperature_measurements
from ..repository.hourly__soil_measurements_repository import add_hourly__soil_measurements, get_hourly__soil_measurements, update_hourly__soil_measurements
from ..repository.hourly__percipitation_measurements_repository import add_hourly__percipitation_measurements, get_hourly__percipitation_measurements, update_hourly__percipitation_measurements
from geopy.geocoders import Nominatim
from ..utils.logger import logger

def fill_hourly_zone():
    db = next(get_db())

    update_log = get__hourly_update_log(db)

    raw__hourly_metrics = get_raw__hourly_metrics_after(db, update_log)

    for data in raw__hourly_metrics:

        geolocator = Nominatim(user_agent="weather-forecast-app-demo")
        location = geolocator.reverse((data.latitude,data.longitude), exactly_one=True)
        if location and 'address' in location.raw:
            address = location.raw['address']
            place_name = address.get('city') or address.get('town') or address.get('village')

            measurement_date_and_time = data.measurements_date_and_time

            hourly__measurement_context = get_hourly_measurement_context(db, place_name, measurement_date_and_time)

            if not hourly__measurement_context:
                # ADD - HOURLY__MEASUREMENT_CONTEXT
                hourly__measurement_context = HourlyMesurementContext(
                    place_name = place_name,
                    measurement_date_and_time = measurement_date_and_time
                )
                hourly__measurement_context = add_hourly__measurement_context(db, hourly__measurement_context)

                # ADD - HOURLY__WIND_MEASUREMENTS
                hourly__wind_measurements = HourlyWindMeasurements(
                    wind_speed_10m = data.wind_speed_10m_in_kmph,
                    wind_speed_80m = data.wind_speed_80m_in_kmph,
                    wind_speed_120m = data.wind_speed_120m_in_kmph,
                    wind_speed_180m = data.wind_speed_180m_in_kmph,
                    wind_direction_10m = data.wind_direction_10m_in_degree,
                    wind_direction_80m = data.wind_direction_80m_in_degree,
                    wind_direction_120m = data.wind_direction_120m_in_degree,
                    wind_direction_180m = data.wind_direction_180m_in_degree,
                    hourly_measurement_context_id = hourly__measurement_context.id
                )
                add_hourly__wind_measurements(db,hourly__wind_measurements)
                
                # ADD - HOURLY__VISIBILITY_MEASUREMENTS
                hourly__visiblity_measurements = HourlyVisibilityMeasurements(
                    visibility = data.visibility_in_m,
                    cloud_cover_low = data.cloud_cover_low_in_percentage,
                    cloud_cover = data.cloud_cover_in_percentage,
                    cloud_cover_mid = data.cloud_cover_mid_in_percentage,
                    cloud_cover_high = data.cloud_cover_high_in_percentage,
                    hourly_measurement_context_id = hourly__measurement_context.id
                )
                add_hourly__visibility_measurements(db, hourly__visiblity_measurements)
                
                # ADD - HOURLY__TEMPERATURE_MEASUREMENTS
                hourly__temperature_measurements = HourlyTemperatureMeasurements(
                    temperature_2m = data.temperature_2m_in_C,
                    temperature_80m = data.temperature_80m_in_C,
                    temperature_120m = data.temperature_120m_in_C,
                    temperature_180m = data.temperature_180m_in_C,
                    hourly_measurement_context_id = hourly__measurement_context.id
                )
                add_hourly__temperature_measurements(db, hourly__temperature_measurements)

                # ADD - HOURLY__SOIL_MEASUREMENTS
                hourly__soil_measurements = HourlySoilMeasurements(
                    soil_temperature_0cm = data.soil_temperature_0cm_in_C,
                    soil_temperature_6cm = data.soil_temperature_6cm_in_C,
                    soil_temperature_18cm = data.soil_temperature_18cm_in_C,
                    soil_temperature_54cm = data.soil_temperature_54cm_in_C,
                    soil_moisture_0cm_to_1cm = data.soil_moisture_0cm_to_1cm_in_percentage,
                    soil_moisture_1cm_to_3cm = data.soil_moisture_1cm_to_3cm_in_percentage,
                    soil_moisture_3cm_to_9cm = data.soil_moisture_3cm_to_9cm_in_percentage,
                    soil_moisture_9cm_to_27cm = data.soil_moisture_9cm_to_27cm_in_percentage,
                    soil_moisture_27cm_to_81cm = data.soil_moisture_27cm_to_81cm_in_percentage,
                    hourly_measurement_context_id = hourly__measurement_context.id
                )
                add_hourly__soil_measurements(db, hourly__soil_measurements)

                # ADD - HOURLY__PERCIPITATION_MEASUREMENTS
                hourly__percipitation_measurements = HourlyPercipitationMeasurements(
                    percipitation = data.percipitation_in_mm,
                    percipitation_probability = data.percipitation_probability_in_percentage,
                    relative_humidity_2m = data.relative_humidity_2m_in_percentage,
                    hourly_measurement_context_id = hourly__measurement_context.id
                )
                add_hourly__percipitation_measurements(db, hourly__percipitation_measurements)

            else:
                hourly__measurement_context = update_hourly__measurement_context(db, hourly__measurement_context)

                # UPDATE - HOURLY__WIND_MEASUREMENTS
                hourly__wind_measurements = get_hourly__wind_measurements(db, hourly__measurement_context.id)
                update_hourly__wind_measurements(db, hourly__wind_measurements, data)

                # UPDATE - HOURLY__VISIBILITY_MEASUREMENTS
                hourly__visiblity_measurements = get_hourly__visibility_measurements(db, hourly__measurement_context.id)
                update_hourly__visibility_measurements(db, hourly__visiblity_measurements, data)

                # UPDATE - HOURLY__TEMPERATURE_MEASUREMENTS
                hourly__temperature_measurements = get_hourly__temperature_measurements(db, hourly__measurement_context.id)
                update_hourly__temperature_measurements(db, hourly__temperature_measurements, data)

                # UPDATE - HOURLY__SOIL_MEASUREMENTS
                hourly__soil_measurements = get_hourly__soil_measurements(db, hourly__measurement_context.id)
                update_hourly__soil_measurements(db, hourly__soil_measurements, data)

                # UPDATE - HOURLY__PERCIPITATION_MEASUREMETNS
                hourly__percipitation_measurements = get_hourly__percipitation_measurements(db, hourly__measurement_context.id)
                update_hourly__percipitation_measurements(db, hourly__percipitation_measurements, data)
            
            update__hourly_update_log(db)
        else:
            logger.warning("CITY NOT FOUND")