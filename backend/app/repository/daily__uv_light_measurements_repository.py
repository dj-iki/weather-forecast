from sqlalchemy.orm import Session
from ..models.daily__uv_lights_measurements import DailyUVLightsMeasurements
from ..models.daily__measurement_context import DailyMeasurementContext
from ..models.raw__daily_metrics import RawDailyMetrics

def add_daily__uv_light_measurements(db: Session, daily__uv_light_measurements: DailyUVLightsMeasurements):
    db.add(daily__uv_light_measurements)
    db.commit()

def get_daily__uv_light_measurements(db: Session, daily__measurement_context: DailyMeasurementContext) -> DailyUVLightsMeasurements:
    return db.query(DailyUVLightsMeasurements).filter(DailyUVLightsMeasurements.daily__measurement_context_id == daily__measurement_context.id).first()

def update_daily__uv_light_measurements(db: Session, daily__uv_light_measurements: DailyUVLightsMeasurements, data: RawDailyMetrics):
    daily__uv_light_measurements.daylight_duration = data.daylight_duration_in_s
    daily__uv_light_measurements.uv_index_max = data.uv_index_max
    daily__uv_light_measurements.inserted_at = data.inserted_at
    db.commit()