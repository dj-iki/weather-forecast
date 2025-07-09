from sqlalchemy.orm import Session
from sqlalchemy import Integer
from ..models.raw__hourly_metrics import RawHourlyMetrics
from ..models.hourly__percipitation_measurements import HourlyPercipitationMeasurements

def add_hourly__percipitation_measurements(db: Session, hourly__percipitation_measurements: HourlyPercipitationMeasurements):
    db.add(hourly__percipitation_measurements)
    db.commit()

def get_hourly__percipitation_measurements(db: Session, hourly_measurement_context_id: Integer) -> HourlyPercipitationMeasurements:
    return db.query(HourlyPercipitationMeasurements).filter(HourlyPercipitationMeasurements.hourly_measurement_context_id == hourly_measurement_context_id).first()

def update_hourly__percipitation_measurements(db: Session, hourly__percipitation_measurements: HourlyPercipitationMeasurements, data: RawHourlyMetrics):
    hourly__percipitation_measurements.percipitation = data.percipitation_in_mm
    hourly__percipitation_measurements.percipitation_probability = data.percipitation_probability_in_percentage
    hourly__percipitation_measurements.relative_humidity_2m = data.relative_humidity_2m_in_percentage
    hourly__percipitation_measurements.inserted_at = data.inserted_at
    db.commit()