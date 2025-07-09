from sqlalchemy.orm import Session
from sqlalchemy import Integer, func
from ..models.hourly__wind_measurements import HourlyWindMeasurements
from ..models.raw__hourly_metrics import RawHourlyMetrics


def add_hourly__wind_measurements(db: Session, hourly__wind_measurements: HourlyWindMeasurements):
    db.add(hourly__wind_measurements)
    db.commit()

def get_hourly__wind_measurements(db: Session, hourly_measurement_context_id: Integer) -> HourlyWindMeasurements:
    return db.query(HourlyWindMeasurements).filter(HourlyWindMeasurements.hourly_measurement_context_id == hourly_measurement_context_id).first()

def update_hourly__wind_measurements(db: Session, hourly__wind_measurements: HourlyWindMeasurements, data: RawHourlyMetrics):
    hourly__wind_measurements.wind_speed_10m = data.wind_speed_10m_in_kmph
    hourly__wind_measurements.wind_speed_80m = data.wind_speed_80m_in_kmph
    hourly__wind_measurements.wind_speed_120m = data.wind_speed_120m_in_kmph
    hourly__wind_measurements.wind_speed_180m = data.wind_speed_180m_in_kmph
    hourly__wind_measurements.wind_direction_10m = data.wind_direction_10m_in_degree
    hourly__wind_measurements.wind_direction_80m = data.wind_direction_80m_in_degree
    hourly__wind_measurements.wind_direction_120m = data.wind_direction_120m_in_degree
    hourly__wind_measurements.wind_direction_180m = data.wind_direction_180m_in_degree
    hourly__wind_measurements.inserted_at = data.inserted_at
    db.commit()