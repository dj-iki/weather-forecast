from sqlalchemy.orm import Session
from sqlalchemy import Integer, func
from ..models.hourly__visibility_measurements import HourlyVisibilityMeasurements
from ..models.raw__hourly_metrics import RawHourlyMetrics

def add_hourly__visibility_measurements(db: Session, hourly__visibility_measurements: HourlyVisibilityMeasurements):
    db.add(hourly__visibility_measurements)
    db.commit()

def get_hourly__visibility_measurements(db: Session, hourly_measurement_context_id: Integer) -> HourlyVisibilityMeasurements:
    return db.query(HourlyVisibilityMeasurements).filter(HourlyVisibilityMeasurements.hourly_measurement_context_id == hourly_measurement_context_id).first()

def update_hourly__visibility_measurements(db: Session, hourly__visibility_measurements: HourlyVisibilityMeasurements, data: RawHourlyMetrics):
    hourly__visibility_measurements.cloud_cover_low = data.cloud_cover_low_in_percentage
    hourly__visibility_measurements.cloud_cover = data.cloud_cover_in_percentage
    hourly__visibility_measurements.cloud_cover_mid = data.cloud_cover_mid_in_percentage
    hourly__visibility_measurements.cloud_cover_high = data.cloud_cover_high_in_percentage
    hourly__visibility_measurements.visibility = data.visibility_in_m
    hourly__visibility_measurements.inserted_at = data.inserted_at
    db.commit()