from sqlalchemy.orm import Session
from sqlalchemy import Integer
from sqlalchemy.exc import SQLAlchemyError
from ..models.raw__hourly_metrics import RawHourlyMetrics
from ..models.hourly__precipitation_measurements import HourlyPrecipitationMeasurements
from ..utils.logger import logger

def add_hourly__precipitation_measurements(db: Session, hourly__precipitation_measurements: HourlyPrecipitationMeasurements):
    try:
        db.add(hourly__precipitation_measurements)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while adding HourlyPrecipitationMeasurements - {e}")

def get_hourly__precipitation_measurements(db: Session, hourly_measurement_context_id: Integer) -> HourlyPrecipitationMeasurements:
    return db.query(HourlyPrecipitationMeasurements).filter(HourlyPrecipitationMeasurements.hourly_measurement_context_id == hourly_measurement_context_id).first()

def update_hourly__precipitation_measurements(db: Session, hourly__precipitation_measurements: HourlyPrecipitationMeasurements, data: RawHourlyMetrics):
    try:
        hourly__precipitation_measurements.precipitation = data.precipitation_in_mm
        hourly__precipitation_measurements.precipitation_probability = data.precipitation_probability_in_percentage
        hourly__precipitation_measurements.relative_humidity_2m = data.relative_humidity_2m_in_percentage
        hourly__precipitation_measurements.inserted_at = data.inserted_at
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while updating HourlyPrecipitaionMeasurements - {e}")