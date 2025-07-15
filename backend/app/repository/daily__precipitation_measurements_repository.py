from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.daily__precipitation_measurements import DailyPrecipitationMeasurements
from ..models.daily__measurement_context import DailyMeasurementContext
from ..models.raw__daily_metrics import RawDailyMetrics
from ..utils.logger import logger
def add_daily__percipitation_measurements(db: Session, daily__percipitation_measurements: DailyPrecipitationMeasurements):
    try:
        db.add(daily__percipitation_measurements)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while adding DailyPrecipitationMeasuremnts - {e}")

def get_daily__precipitation_measurements(db: Session, daily__measurement_context: DailyMeasurementContext) -> DailyPrecipitationMeasurements:
    return db.query(DailyPrecipitationMeasurements).filter(DailyPrecipitationMeasurements.daily__measurement_context_id == daily__measurement_context.id).first()

def update_daily__precipitation_measurements(db: Session, daily__precipitation_measurements: DailyPrecipitationMeasurements, data: RawDailyMetrics):
    try:
        daily__precipitation_measurements.precipitation_sum = (data.precipatition_sum_in_mm/1000)
        daily__precipitation_measurements.precipitation_length = (data.precipatition_hours_in_h*3600)
        daily__precipitation_measurements.precipitation_probability_max = data.precipatition_probability_max_in_p
        daily__precipitation_measurements.inserted_at = data.inserted_at
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while updating DailyPrecipitationMeasuremnts - {e}")