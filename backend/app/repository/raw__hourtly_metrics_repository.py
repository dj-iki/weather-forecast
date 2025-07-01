from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from ..utils.logger import logger
from ..models.raw__hourly_metrics import RawHourlyMetrics
from datetime import datetime

# INSERT INTO raw__hourly_metrics(nazivi kolona) VALUES(ovde idu sve vrednosti)
def add_raw__hourly_metrics(db: Session, data: dict, i: int):
    try:
        raw__hourly_metrics = RawHourlyMetrics()

        raw__hourly_metrics.latitude = data["latitude"]
        raw__hourly_metrics.longitude = data["longitude"]
        hourly_data = data["hourly"]
        raw__hourly_metrics.measurements_date_and_time = hourly_data["time"][i]
        raw__hourly_metrics.temperature_2m_in_C = hourly_data["temperature_2m"][i]
        raw__hourly_metrics.temperature_80m_in_C = hourly_data["temperature_80m"][i]
        raw__hourly_metrics.temperature_120m_in_C = hourly_data["temperature_120m"][i]
        raw__hourly_metrics.temperature_180m_in_C = hourly_data["temperature_180m"][i]
        raw__hourly_metrics.relative_humidity_2m_in_percentage = hourly_data["relative_humidity_2m"][i]
        raw__hourly_metrics.percipitation_in_mm = hourly_data["precipitation"][i]
        raw__hourly_metrics.percipitation_probability_in_percentage = hourly_data["precipitation_probability"][i]
        raw__hourly_metrics.cloud_cover_low_in_percentage = hourly_data["cloud_cover_low"][i]
        raw__hourly_metrics.cloud_cover_in_percentage = hourly_data["cloud_cover"][i]
        raw__hourly_metrics.cloud_cover_mid_in_percentage = hourly_data["cloud_cover_mid"][i]
        raw__hourly_metrics.cloud_cover_high_in_percentage = hourly_data["cloud_cover_high"][i]
        raw__hourly_metrics.visibility_in_m = hourly_data["visibility"][i]
        raw__hourly_metrics.wind_speed_10m_in_kmph = hourly_data["wind_speed_10m"][i]
        raw__hourly_metrics.wind_speed_80m_in_kmph = hourly_data["wind_speed_80m"][i]
        raw__hourly_metrics.wind_speed_120m_in_kmph = hourly_data["wind_speed_120m"][i]
        raw__hourly_metrics.wind_speed_180m_in_kmph = hourly_data["wind_speed_180m"][i]
        raw__hourly_metrics.wind_direction_10m_in_degree = hourly_data["wind_direction_10m"][i]
        raw__hourly_metrics.wind_direction_80m_in_degree = hourly_data["wind_direction_80m"][i]
        raw__hourly_metrics.wind_direction_120m_in_degree = hourly_data["wind_direction_120m"][i]
        raw__hourly_metrics.wind_direction_180m_in_degree = hourly_data["wind_direction_180m"][i]
        raw__hourly_metrics.soil_temperature_0cm_in_C = hourly_data["soil_temperature_0cm"][i]
        raw__hourly_metrics.soil_temperature_6cm_in_C = hourly_data["soil_temperature_6cm"][i]
        raw__hourly_metrics.soil_temperature_18cm_in_C = hourly_data["soil_temperature_18cm"][i]
        raw__hourly_metrics.soil_temperature_54cm_in_C = hourly_data["soil_temperature_54cm"][i]
        raw__hourly_metrics.soil_moisture_0cm_to_1cm_in_percentage = hourly_data["soil_moisture_0_to_1cm"][i]
        raw__hourly_metrics.soil_moisture_1cm_to_3cm_in_percentage = hourly_data["soil_moisture_1_to_3cm"][i]
        raw__hourly_metrics.soil_moisture_3cm_to_9cm_in_percentage = hourly_data["soil_moisture_3_to_9cm"][i]
        raw__hourly_metrics.soil_moisture_9cm_to_27cm_in_percentage = hourly_data["soil_moisture_9_to_27cm"][i]
        raw__hourly_metrics.soil_moisture_27cm_to_81cm_in_percentage = hourly_data["soil_moisture_27_to_81cm"][i]
        db.add(raw__hourly_metrics)
        db.commit()
        db.refresh(raw__hourly_metrics)
        logger.info(f" - {raw__hourly_metrics.latitude}, {raw__hourly_metrics.longitude}, {raw__hourly_metrics.measurements_date_and_time} - inserted successfully")
        return raw__hourly_metrics
    except IntegrityError:
        db.rollback()
        logger.warning(f"{raw__hourly_metrics} already exists or is invalid data")



# SELECT * FROM raw__hourly_metrics where longitude=? and latitude=? and measurements_date_and_time=?
def get_raw__hourly_metrics(db: Session, longitude: float, latitude: float, measurements_date_and_time: datetime):
    try:
        measurements = db.query(RawHourlyMetrics).filter(RawHourlyMetrics.longitude == longitude,
                                          RawHourlyMetrics.latitude == latitude,
                                          RawHourlyMetrics.measurements_date_and_time == measurements_date_and_time).first()
        if not measurements:
            logger.info(f"There is no entities with primary key - '{longitude}', '{latitude}', '{measurements_date_and_time}'")
            return None
        else:
            logger.info(f"There is already an entity with primary key - '{longitude}', '{latitude}', '{measurements_date_and_time}' - in database ")
            return measurements
    except SQLAlchemyError as e:
        logger.warning("Query failed - ", e) 


# UPDATE raw__hourly_metrics set (ovde idu sve kolone koje ne ulaze u pk) where longiutde=? and latitude=? and measurements_date_and_time=?
def update_raw__hourly_metrics(db: Session, raw__hourly_metrics: RawHourlyMetrics, data: dict, i: int):
    try:
        db.merge(raw__hourly_metrics)
        hourly_data = data["hourly"]
        raw__hourly_metrics.temperature_2m_in_C = hourly_data["temperature_2m"][i]
        raw__hourly_metrics.temperature_80m_in_C = hourly_data["temperature_80m"][i]
        raw__hourly_metrics.temperature_120m_in_C = hourly_data["temperature_120m"][i]
        raw__hourly_metrics.temperature_180m_in_C = hourly_data["temperature_180m"][i]
        raw__hourly_metrics.relative_humidity_2m_in_percentage = hourly_data["relative_humidity_2m"][i]
        raw__hourly_metrics.percipitation_in_mm = hourly_data["precipitation"][i]
        raw__hourly_metrics.percipitation_probability_in_percentage = hourly_data["precipitation_probability"][i]
        raw__hourly_metrics.cloud_cover_low_in_percentage = hourly_data["cloud_cover_low"][i]
        raw__hourly_metrics.cloud_cover_in_percentage = hourly_data["cloud_cover"][i]
        raw__hourly_metrics.cloud_cover_mid_in_percentage = hourly_data["cloud_cover_mid"][i]
        raw__hourly_metrics.cloud_cover_high_in_percentage = hourly_data["cloud_cover_high"][i]
        raw__hourly_metrics.visibility_in_m = hourly_data["visibility"][i]
        raw__hourly_metrics.wind_speed_10m_in_kmph = hourly_data["wind_speed_10m"][i]
        raw__hourly_metrics.wind_speed_80m_in_kmph = hourly_data["wind_speed_80m"][i]
        raw__hourly_metrics.wind_speed_120m_in_kmph = hourly_data["wind_speed_120m"][i]
        raw__hourly_metrics.wind_speed_180m_in_kmph = hourly_data["wind_speed_180m"][i]
        raw__hourly_metrics.wind_direction_10m_in_degree = hourly_data["wind_direction_10m"][i]
        raw__hourly_metrics.wind_direction_80m_in_degree = hourly_data["wind_direction_80m"][i]
        raw__hourly_metrics.wind_direction_120m_in_degree = hourly_data["wind_direction_120m"][i]
        raw__hourly_metrics.wind_direction_180m_in_degree = hourly_data["wind_direction_180m"][i]
        raw__hourly_metrics.soil_temperature_0cm_in_C = hourly_data["soil_temperature_0cm"][i]
        raw__hourly_metrics.soil_temperature_6cm_in_C = hourly_data["soil_temperature_6cm"][i]
        raw__hourly_metrics.soil_temperature_18cm_in_C = hourly_data["soil_temperature_18cm"][i]
        raw__hourly_metrics.soil_temperature_54cm_in_C = hourly_data["soil_temperature_54cm"][i]
        raw__hourly_metrics.soil_moisture_0cm_to_1cm_in_percentage = hourly_data["soil_moisture_0_to_1cm"][i]
        raw__hourly_metrics.soil_moisture_1cm_to_3cm_in_percentage = hourly_data["soil_moisture_1_to_3cm"][i]
        raw__hourly_metrics.soil_moisture_3cm_to_9cm_in_percentage = hourly_data["soil_moisture_3_to_9cm"][i]
        raw__hourly_metrics.soil_moisture_9cm_to_27cm_in_percentage = hourly_data["soil_moisture_9_to_27cm"][i]
        raw__hourly_metrics.soil_moisture_27cm_to_81cm_in_percentage = hourly_data["soil_moisture_27_to_81cm"][i]
        db.commit()
        db.refresh(raw__hourly_metrics)
        logger.info(f" - {raw__hourly_metrics.latitude}, {raw__hourly_metrics.longitude}, {raw__hourly_metrics.measurements_date_and_time} - updated successfully")
        return raw__hourly_metrics
    except SQLAlchemyError as e:
        db.rollback()
        logger.warning(f"Database error occurred: {e}")