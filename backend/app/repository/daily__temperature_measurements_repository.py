from sqlalchemy.orm import Session
from ..models.daily__temperature_measurements import DailyTemperatureMeasurements
from ..models.daily__measurement_context import DailyMeasurementContext
from ..models.raw__daily_metrics import RawDailyMetrics

def add_daily__temperature_measurements(db: Session, daily__temperaturem_measurements: DailyTemperatureMeasurements):
    db.add(daily__temperaturem_measurements)
    db.commit()

def get_daily__temperature_measurements(db: Session, daily__measurement_context: DailyMeasurementContext) -> DailyTemperatureMeasurements:
    return db.query(DailyTemperatureMeasurements).filter(DailyTemperatureMeasurements.daily__measurement_context_id == daily__measurement_context.id).first()

def update_daily__temperature_measurements(db: Session, daily__temperature_measurements: DailyTemperatureMeasurements, data: RawDailyMetrics):
    daily__temperature_measurements.temperature_2m_max = data.temperature_2m_max_in_C
    daily__temperature_measurements.temperature_2m_min = data.temperature_2m_min_in_C
    daily__temperature_measurements.inserted_at = data.inserted_at
    db.commit()