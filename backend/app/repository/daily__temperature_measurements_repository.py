from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from ..models.daily__temperature_measurements import DailyTemperatureMeasurements
from ..models.daily__measurement_context import DailyMeasurementContext
from ..models.raw__daily_metrics import RawDailyMetrics
from ..utils.logger import logger


def add_daily__temperature_measurements(db: Session, daily__temperaturem_measurements: DailyTemperatureMeasurements):
    try:
        db.add(daily__temperaturem_measurements)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while adding DailyTemperatureMeasurements - {e}")
def get_daily__temperature_measurements(db: Session, daily__measurement_context: DailyMeasurementContext) -> DailyTemperatureMeasurements:
    return db.query(DailyTemperatureMeasurements).filter(DailyTemperatureMeasurements.daily__measurement_context_id == daily__measurement_context.id).first()

def update_daily__temperature_measurements(db: Session, daily__temperature_measurements: DailyTemperatureMeasurements, data: RawDailyMetrics):
    try:
        daily__temperature_measurements.temperature_2m_max = data.temperature_2m_max_in_C
        daily__temperature_measurements.temperature_2m_min = data.temperature_2m_min_in_C
        daily__temperature_measurements.inserted_at = data.inserted_at
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while updating DailyTemperatureMeasurements - {e}")