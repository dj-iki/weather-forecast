from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.daily__wind_measurements import DailyWindMeasurements
from ..models.daily__measurement_context import DailyMeasurementContext
from ..models.raw__daily_metrics import RawDailyMetrics
from ..utils.logger import logger

def add_daily__wind_measurements(db: Session, daily__wind_measurements: DailyWindMeasurements):
    try:
        db.add(daily__wind_measurements)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while adding DailyWindMeasurements - {e}")

def get_daily__wind_measurements(db: Session, daily__measurement_context: DailyMeasurementContext) -> DailyWindMeasurements:
    return db.query(DailyWindMeasurements).filter(DailyWindMeasurements.daily__measurement_context_id == daily__measurement_context.id).first()

def update_daily__wind_measurements(db: Session, daily__wind_measurements: DailyWindMeasurements, data: RawDailyMetrics):
    try:
        daily__wind_measurements.wind_speed_10m_max = (data.wind_speed_10m_max_in_kmph*3.6)
        daily__wind_measurements.wind_direction_10m_dominant = data.wind_direction_10m_dominant_in_degree
        daily__wind_measurements.inserted_at = data.inserted_at
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while updating DailyWindMeasurements - {e}")