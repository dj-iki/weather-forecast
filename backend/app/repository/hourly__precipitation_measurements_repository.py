from sqlalchemy.orm import Session
from sqlalchemy import Integer
from ..models.raw__hourly_metrics import RawHourlyMetrics
from ..models.hourly__precipitation_measurements import HourlyPrecipitationMeasurements

def add_hourly__precipitation_measurements(db: Session, hourly__precipitation_measurements: HourlyPrecipitationMeasurements):
    db.add(hourly__precipitation_measurements)
    db.commit()

def get_hourly__precipitation_measurements(db: Session, hourly_measurement_context_id: Integer) -> HourlyPrecipitationMeasurements:
    return db.query(HourlyPrecipitationMeasurements).filter(HourlyPrecipitationMeasurements.hourly_measurement_context_id == hourly_measurement_context_id).first()

def update_hourly__precipitation_measurements(db: Session, hourly__percipitation_measurements: HourlyPrecipitationMeasurements, data: RawHourlyMetrics):
    hourly__percipitation_measurements.precipitation = data.precipitation_in_mm
    hourly__percipitation_measurements.precipitation_probability = data.precipitation_probability_in_percentage
    hourly__percipitation_measurements.relative_humidity_2m = data.relative_humidity_2m_in_percentage
    hourly__percipitation_measurements.inserted_at = data.inserted_at
    db.commit()