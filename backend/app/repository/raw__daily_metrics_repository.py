from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy import func, Date
from ..utils.logger import logger
from ..models.raw__daily_metrics import RawDailyMetrics
from ..models.update_log import UpdateLog
from datetime import datetime


# SELECT * FROM raw__daily_metrics where longitude=? and latitude=? and measurement_date=?
def get_raw__daily_metrics(db: Session, longitude: float, latitude: float, measurement_date: datetime):
    try:
        measurement = db.query(RawDailyMetrics).filter(RawDailyMetrics.longitude == longitude,
                                         RawDailyMetrics.latitude == latitude,
                                         RawDailyMetrics.measurment_date == measurement_date).first()
        if not measurement:
            logger.info(f"There is no entities with primary key - '{longitude}', '{latitude}', '{measurement_date}'")
            return None
        else:
            logger.info(f"There is already an entity with primary key - '{longitude}', '{latitude}', '{measurement_date}' - in database ")
            return measurement
    except SQLAlchemyError as e:
        logger.warning(f"Database error occurred: {e}")


# INSERT INTO raw__daily_metrics(nazivi kolona) VALUES(ovde idu sve vrednosti)
def add_raw__daily_metrics(db: Session, data: dict, i: int):
    try:
        raw__daily_metrics = RawDailyMetrics()
        raw__daily_metrics.latitude = data["latitude"]
        raw__daily_metrics.longitude = data["longitude"]
        daily_data = data["daily"]
        raw__daily_metrics.measurment_date = daily_data["time"][i]
        raw__daily_metrics.temperature_2m_min_in_C = daily_data["temperature_2m_min"][i]
        raw__daily_metrics.temperature_2m_max_in_C = daily_data["temperature_2m_max"][i]
        raw__daily_metrics.daylight_duration_in_s = daily_data["daylight_duration"][i]
        raw__daily_metrics.uv_index_max = daily_data["uv_index_max"][i]
        raw__daily_metrics.precipatition_sum_in_mm = daily_data["precipitation_sum"][i]
        raw__daily_metrics.precipatition_probability_max_in_p = daily_data["precipitation_probability_max"][i]
        raw__daily_metrics.precipatition_hours_in_h = daily_data["precipitation_hours"][i]
        raw__daily_metrics.wind_speed_10m_max_in_kmph = daily_data["wind_speed_10m_max"][i]
        raw__daily_metrics.wind_direction_10m_dominant_in_degree = daily_data["wind_direction_10m_dominant"][i]
        db.add(raw__daily_metrics)
        db.commit()
        db.refresh(raw__daily_metrics)
        logger.info(f" - {raw__daily_metrics.latitude}, {raw__daily_metrics.longitude}, {raw__daily_metrics.measurment_date} - inserted successfully")
        return raw__daily_metrics
    except(IntegrityError):
        db.rollback()
        logger.warning(f" - {raw__daily_metrics.latitude}, {raw__daily_metrics.longitude}, {raw__daily_metrics.measurment_date} - already exists or is invalid data")


# UPDATE raw__daily_metrics set (ovde idu sve kolone koje ne ulaze u pk) where longiutde=? and latitude=? and measurement_date=?
def update_raw__daily_metrics(db: Session, raw__daily_metrics: RawDailyMetrics, data: dict, i: int):
    try:
        db.merge(raw__daily_metrics)
        daily_data = data["daily"]
        raw__daily_metrics.temperature_2m_min_in_C = daily_data["temperature_2m_min"][i]
        raw__daily_metrics.temperature_2m_max_in_C = daily_data["temperature_2m_max"][i]
        raw__daily_metrics.daylight_duration_in_s = daily_data["daylight_duration"][i]
        raw__daily_metrics.uv_index_max = daily_data["uv_index_max"][i]
        raw__daily_metrics.precipatition_sum_in_mm = daily_data["precipitation_sum"][i]
        raw__daily_metrics.precipatition_probability_max_in_p = daily_data["precipitation_probability_max"][i]
        raw__daily_metrics.precipatition_hours_in_h = daily_data["precipitation_hours"][i]
        raw__daily_metrics.wind_speed_10m_max_in_kmph = daily_data["wind_speed_10m_max"][i]
        raw__daily_metrics.wind_direction_10m_dominant_in_degree = daily_data["wind_direction_10m_dominant"][i]
        raw__daily_metrics.inserted_at = func.now()
        db.commit()
        db.refresh(raw__daily_metrics)
        logger.info(f" - {raw__daily_metrics.latitude}, {raw__daily_metrics.longitude}, {raw__daily_metrics.measurment_date} - updated successfully")
        return raw__daily_metrics
    except SQLAlchemyError as e:
        db.rollback()
        logger.warning(f"Database error occurred: {e}")

def get_raw__daily_metrics_after(db: Session, update_log: UpdateLog):
    raw__daily_metrics = db.query(RawDailyMetrics).filter(RawDailyMetrics.inserted_at > update_log.last_updated).all()

    if raw__daily_metrics:
        return raw__daily_metrics
    else:
        logger.error("")