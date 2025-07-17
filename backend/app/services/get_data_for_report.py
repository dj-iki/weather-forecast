from ..repository.hourly__measurement_context_repository import get_hmc_data_for_report
from ..repository.hourly__visibility_measurements_repository import (
    get_cloud_cover_low_for_report,
    get_cloud_cover_for_report,
    get_cloud_cover_mid_for_report,
    get_cloud_cover_high_for_report,
    get_visibilty_for_report,
)
from ..repository.hourly__wind_measurements_repository import (
    get_wind_direction_10m_for_report,
    get_wind_direction_80m_for_report,
    get_wind_direction_120m_for_report,
    get_wind_direction_180m_for_report,
    get_wind_speed_10m_for_report,
    get_wind_speed_80m_for_report,
    get_wind_speed_120m_for_report,
    get_wind_speed_180m_for_report,
)
from ..repository.hourly__temperature_measurements_repository import (
    get_tmeperature_2m_for_report,
    get_tmeperature_80m_for_report,
    get_tmeperature_120m_for_report,
    get_tmeperature_180m_for_report,
)
from ..repository.hourly__soil_measurements_repository import (
    get_soil_temperature_0cm_for_report,
    get_soil_temperature_6cm_for_report,
    get_soil_temperature_18cm_for_report,
    get_soil_temperature_54cm_for_report,
    get_soil_moisture_0_to_1cm_for_report,
    get_soil_moisture_1_to_3cm_for_report,
    get_soil_moisture_3_to_9cm_for_report,
    get_soil_moisture_9_to_27cm_for_report,
    get_soil_moisture_27_to_81cm_for_report,
)
from ..repository.hourly__precipitation_measurements_repository import (
    get_precipitation_for_report,
    get_precipitation_probability_for_report,
    get_relative_humidity_2m_for_report,
)
from ..dependencies.session import get_db


db = next(get_db())


def get_data_for_report(days: int, place_name: str):
    hourly__measurement_context_id = get_hmc_data_for_report(db, days * 24, place_name)
    if hourly__measurement_context_id:
        data = []
        # WIND_DIRECTION_10m
        wind_direction_10m_min, wind_direction_10m_max, wind_direction_10m_avg = (
            get_wind_direction_10m_for_report(db, hourly__measurement_context_id)
        )
        wind_direction_10m = {
            "name": "wind_direction_10m",
            "min": wind_direction_10m_min,
            "max": wind_direction_10m_max,
            "avg": wind_direction_10m_avg,
        }
        data.append(wind_direction_10m)

        # WIND_DIRECTION_80m
        wind_direction_80m_min, wind_direction_80m_max, wind_direction_80m_avg = (
            get_wind_direction_80m_for_report(db, hourly__measurement_context_id)
        )
        wind_direction_80m = {
            "name": "wind_direction_80m",
            "min": wind_direction_80m_min,
            "max": wind_direction_80m_max,
            "avg": wind_direction_80m_avg,
        }
        data.append(wind_direction_80m)

        # WIND_DIRECTION_120m
        wind_direction_120m_min, wind_direction_120m_max, wind_direction_120m_avg = (
            get_wind_direction_120m_for_report(db, hourly__measurement_context_id)
        )
        wind_direction_120m = {
            "name": "wind_direction_120m",
            "min": wind_direction_120m_min,
            "max": wind_direction_120m_max,
            "avg": wind_direction_120m_avg,
        }
        data.append(wind_direction_120m)

        # WIND_DIRECTION_180m
        wind_direction_180m_min, wind_direction_180m_max, wind_direction_180m_avg = (
            get_wind_direction_180m_for_report(db, hourly__measurement_context_id)
        )
        wind_direction_180m = {
            "name": "wind_direction_180m",
            "min": wind_direction_180m_min,
            "max": wind_direction_180m_max,
            "avg": wind_direction_180m_avg,
        }
        data.append(wind_direction_180m)

        # WIND_SPEED_10m
        wind_speed_10m_min, wind_speed_10m_max, wind_speed_10m_avg = (
            get_wind_speed_10m_for_report(db, hourly__measurement_context_id)
        )
        wind_speed_10m = {
            "name": "wind_speed_10m",
            "min": wind_speed_10m_min,
            "max": wind_speed_10m_max,
            "avg": wind_speed_10m_avg,
        }
        data.append(wind_speed_10m)

        # WIND_SPEED_80m
        wind_speed_80m_min, wind_speed_80m_max, wind_speed_80m_avg = (
            get_wind_speed_80m_for_report(db, hourly__measurement_context_id)
        )
        wind_speed_80m = {
            "name": "wind_speed_80m",
            "min": wind_speed_80m_min,
            "max": wind_speed_80m_max,
            "avg": wind_speed_80m_avg,
        }
        data.append(wind_speed_80m)

        # WIND_SPEED_120m
        wind_speed_120m_min, wind_speed_120m_max, wind_speed_120m_avg = (
            get_wind_speed_120m_for_report(db, hourly__measurement_context_id)
        )
        wind_speed_120m = {
            "name": "wind_speed_120m",
            "min": wind_speed_120m_min,
            "max": wind_speed_120m_max,
            "avg": wind_speed_120m_avg,
        }
        data.append(wind_speed_120m)

        # WIND_SPEED_180m
        wind_speed_180m_min, wind_speed_180m_max, wind_speed_180m_avg = (
            get_wind_speed_180m_for_report(db, hourly__measurement_context_id)
        )
        wind_speed_180m = {
            "name": "wind_speed_180m",
            "min": wind_speed_180m_min,
            "max": wind_speed_180m_max,
            "avg": wind_speed_180m_avg,
        }
        data.append(wind_speed_180m)

        # CLOUD_COVER_LOW
        cloud_cover_low_min, cloud_cover_low_max, cloud_cover_low_avg = (
            get_cloud_cover_low_for_report(db, hourly__measurement_context_id)
        )
        cloud_cover_low = {
            "name": "cloud_cover_low",
            "min": cloud_cover_low_min,
            "max": cloud_cover_low_max,
            "avg": cloud_cover_low_avg,
        }
        data.append(cloud_cover_low)

        # CLOUD_COVER
        cloud_cover_min, cloud_cover_max, cloud_cover_avg = get_cloud_cover_for_report(
            db, hourly__measurement_context_id
        )
        cloud_cover = {
            "name": "cloud_cover",
            "min": cloud_cover_min,
            "max": cloud_cover_max,
            "avg": cloud_cover_avg,
        }
        data.append(cloud_cover)

        # CLOUD_COVER_MID
        cloud_cover_mid_min, cloud_cover_mid_max, cloud_cover_mid_avg = (
            get_cloud_cover_mid_for_report(db, hourly__measurement_context_id)
        )
        cloud_cover_mid = {
            "name": "cloud_cover_mid",
            "min": cloud_cover_mid_min,
            "max": cloud_cover_mid_max,
            "avg": cloud_cover_mid_avg,
        }
        data.append(cloud_cover_mid)

        # CLOUD_COVER_HIGH
        cloud_cover_high_min, cloud_cover_high_max, cloud_cover_high_avg = (
            get_cloud_cover_high_for_report(db, hourly__measurement_context_id)
        )
        cloud_cover_high = {
            "name": "cloud_cover_high",
            "min": cloud_cover_high_min,
            "max": cloud_cover_high_max,
            "avg": cloud_cover_high_avg,
        }
        data.append(cloud_cover_high)

        # VISIBILITY
        visibilty_min, visibilty_max, visibility_avg = get_visibilty_for_report(
            db, hourly__measurement_context_id
        )
        visibility = {
            "name": "visibility",
            "min": visibilty_min,
            "max": visibilty_max,
            "avg": visibility_avg,
        }
        data.append(visibility)

        # TEMPERATURE_2m
        temperature_2m_min, temperature_2m_max, temperature_2m_avg = (
            get_tmeperature_2m_for_report(db, hourly__measurement_context_id)
        )
        temperature_2m = {
            "name": "temperature_2m",
            "min": temperature_2m_min,
            "max": temperature_2m_max,
            "avg": temperature_2m_avg,
        }
        data.append(temperature_2m)

        # TEMPERATURE_80m
        temperature_80m_min, temperature_80m_max, temperature_80m_avg = (
            get_tmeperature_80m_for_report(db, hourly__measurement_context_id)
        )
        temperature_80m = {
            "name": "temperature_80m",
            "min": temperature_80m_min,
            "max": temperature_80m_max,
            "avg": temperature_80m_avg,
        }
        data.append(temperature_80m)

        # TEMPERATURE_120m
        temperature_120m_min, temperature_120m_max, temperature_120m_avg = (
            get_tmeperature_120m_for_report(db, hourly__measurement_context_id)
        )
        temperature_120m = {
            "name": "temperature_120m",
            "min": temperature_120m_min,
            "max": temperature_120m_max,
            "avg": temperature_120m_avg,
        }
        data.append(temperature_120m)

        # TEMPERATUER_180m
        temperature_180m_min, temperature_180m_max, temperature_180m_avg = (
            get_tmeperature_180m_for_report(db, hourly__measurement_context_id)
        )
        temperature_180m = {
            "name": "temperature_180m",
            "min": temperature_180m_min,
            "max": temperature_180m_max,
            "avg": temperature_180m_avg,
        }
        data.append(temperature_180m)

        # SOIL_MOISTURE_0_TO_1cm
        (
            soil_moisture_0_to_1cm_min,
            soil_moisture_0_to_1cm_max,
            soil_moisture_0_to_1cm_avg,
        ) = get_soil_moisture_0_to_1cm_for_report(db, hourly__measurement_context_id)
        soil_moisture_0_to_1cm = {
            "name": "soil_moisture_0_to_1cm",
            "min": soil_moisture_0_to_1cm_min,
            "max": soil_moisture_0_to_1cm_max,
            "avg": soil_moisture_0_to_1cm_avg,
        }
        data.append(soil_moisture_0_to_1cm)

        # SOIL_MOISTURE_1_TO_3cm
        (
            soil_moisture_1_to_3cm_min,
            soil_moisture_1_to_3cm_max,
            soil_moisture_1_to_3cm_avg,
        ) = get_soil_moisture_1_to_3cm_for_report(db, hourly__measurement_context_id)
        soil_moisture_1_to_3cm = {
            "name": "soil_moisture_1_to_3cm",
            "min": soil_moisture_1_to_3cm_min,
            "max": soil_moisture_1_to_3cm_max,
            "avg": soil_moisture_1_to_3cm_avg,
        }
        data.append(soil_moisture_1_to_3cm)
        
        # SOIL_MOISTURE_3_TO_9cm
        (
            soil_moisture_3_to_9cm_min,
            soil_moisture_3_to_9cm_max,
            soil_moisture_3_to_9cm_avg,
        ) = get_soil_moisture_3_to_9cm_for_report(db, hourly__measurement_context_id)
        soil_moisture_3_to_9cm = {
            "name": "soil_moisture_3_to_9cm",
            "min": soil_moisture_3_to_9cm_min,
            "max": soil_moisture_3_to_9cm_max,
            "avg": soil_moisture_3_to_9cm_avg,
        }
        data.append(soil_moisture_3_to_9cm)
        
        # SOIL_MOISTURE_9_TO_27cm
        (
            soil_moisture_9_to_27cm_min,
            soil_moisture_9_to_27cm_max,
            soil_moisture_9_to_27cm_avg,
        ) = get_soil_moisture_9_to_27cm_for_report(db, hourly__measurement_context_id)
        soil_moisture_9_to_27cm = {
            "name": "soil_moisture_9_to_27cm",
            "min": soil_moisture_9_to_27cm_min,
            "max": soil_moisture_9_to_27cm_max,
            "avg": soil_moisture_9_to_27cm_avg,
        }
        data.append(soil_moisture_9_to_27cm)
        
        # SOIL_MOISTURE_27_TO_81cm
        (
            soil_moisture_27_to_81cm_min,
            soil_moisture_27_to_81cm_max,
            soil_moisture_27_to_81cm_avg,
        ) = get_soil_moisture_27_to_81cm_for_report(db, hourly__measurement_context_id)
        soil_moisture_27_to_81cm = {
            "name": "soil_moisture_27_to_81cm",
            "min": soil_moisture_27_to_81cm_min,
            "max": soil_moisture_27_to_81cm_max,
            "avg": soil_moisture_27_to_81cm_avg,
        }
        data.append(soil_moisture_27_to_81cm)

        # SOIL_TEMPERATURE_0cm
        soil_temperature_0cm_min, soil_temperature_0cm_max, soil_temperature_0cm_avg = (
            get_soil_temperature_0cm_for_report(db, hourly__measurement_context_id)
        )
        soil_temperature_0cm = {
            "name": "soil_temperature_0cm",
            "min": soil_temperature_0cm_min,
            "max": soil_temperature_0cm_max,
            "avg": soil_temperature_0cm_avg,
        }
        data.append(soil_temperature_0cm)

        # SOIL_TEMPERATURE_6cm
        soil_temperature_6cm_min, soil_temperature_6cm_max, soil_temperature_6cm_avg = (
            get_soil_temperature_6cm_for_report(db, hourly__measurement_context_id)
        )
        soil_temperature_6cm = {
            "name": "soil_temperature_6cm",
            "min": soil_temperature_6cm_min,
            "max": soil_temperature_6cm_max,
            "avg": soil_temperature_6cm_avg,
        }
        data.append(soil_temperature_6cm)

        # SOIL_TEMPERATURE_18cm
        (
            soil_temperature_18cm_min,
            soil_temperature_18cm_max,
            soil_temperature_18cm_avg,
        ) = get_soil_temperature_18cm_for_report(db, hourly__measurement_context_id)
        soil_temperature_18cm = {
            "name": "soil_temperature_18cm",
            "min": soil_temperature_18cm_min,
            "max": soil_temperature_18cm_max,
            "avg": soil_temperature_18cm_avg,
        }
        data.append(soil_temperature_18cm)

        # SOIL_TEMPERATURE_54cm
        (
            soil_temperature_54cm_min,
            soil_temperature_54cm_max,
            soil_temperature_54cm_avg,
        ) = get_soil_temperature_54cm_for_report(db, hourly__measurement_context_id)
        soil_temperature_54cm = {
            "name": "soil_temperature_54cm",
            "min": soil_temperature_54cm_min,
            "max": soil_temperature_54cm_max,
            "avg": soil_temperature_54cm_avg,
        }
        data.append(soil_temperature_54cm)

        # PRECIPITATION
        precipitation_min, precipitation_max, precipitation_avg = (
            get_precipitation_for_report(db, hourly__measurement_context_id)
        )
        precipitation = {
            "name": "precipitation",
            "min": precipitation_min,
            "max": precipitation_max,
            "avg": precipitation_avg,
        }
        data.append(precipitation)

        # PRECIPITATION_PROBABILITY
        (
            precipitation_probability_min,
            precipitation_probability_max,
            precipitation_probability_avg,
        ) = get_precipitation_probability_for_report(db, hourly__measurement_context_id)
        precipitation_probability = {
            "name": "precipitation_probability",
            "min": precipitation_probability_min,
            "max": precipitation_probability_max,
            "avg": precipitation_probability_avg,
        }
        data.append(precipitation_probability)

        # RELATIVE_HUMIDITY_2m
        relative_humidity_2m_min, relative_humidity_2m_max, relative_humidity_2m_avg = (
            get_relative_humidity_2m_for_report(db, hourly__measurement_context_id)
        )
        relative_humidity_2m = {
            "name": "relative_humidity_2m",
            "min": relative_humidity_2m_min,
            "max": relative_humidity_2m_max,
            "avg": relative_humidity_2m_avg,
        }
        data.append(relative_humidity_2m)

        return data

    return "NESTO NE VALJA"
