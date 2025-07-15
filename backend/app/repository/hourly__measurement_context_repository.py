from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import String, TIMESTAMP, func
from ..models.hourly__measurement_context import HourlyMesurementContext
from ..utils.logger import logger


def get_hourly_measurement_context(db: Session, place_name: String, measurement_date_and_time: TIMESTAMP):
    hourly__measurement_context = \
    db.query(HourlyMesurementContext) \
    .filter(HourlyMesurementContext.place_name == place_name,
            HourlyMesurementContext.measurement_date_and_time == measurement_date_and_time) \
    .first()

    if hourly__measurement_context:
        return hourly__measurement_context
    else:
        return None
    
def add_hourly__measurement_context(db: Session, hourly__measurement_context: HourlyMesurementContext) -> HourlyMesurementContext:
    try:
        db.add(hourly__measurement_context)
        db.commit()
        db.refresh(hourly__measurement_context)
        return hourly__measurement_context
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while adding HourlyMesurementContext - {e}")

def update_hourly__measurement_context(db: Session, hourly__measurement_context: HourlyMesurementContext) -> HourlyMesurementContext:
    try:
        hourly__measurement_context = db.merge(hourly__measurement_context)
        hourly__measurement_context.inserted_at = func.now()
        db.commit()
        return hourly__measurement_context
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while updating HourlyMesurementContext - {e}")