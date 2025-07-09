from sqlalchemy.orm import Session
from sqlalchemy import Integer
from ..models.raw__hourly_metrics import RawHourlyMetrics
from ..models.hourly__soil_measurements import HourlySoilMeasurements

def add_hourly__soil_measurements(db: Session, hourly__soil_measurements: HourlySoilMeasurements):
    db.add(hourly__soil_measurements)
    db.commit()

def get_hourly__soil_measurements(db: Session, hourly_mesurement_context_id: Integer) -> HourlySoilMeasurements:
    return db.query(HourlySoilMeasurements).filter(HourlySoilMeasurements.hourly_measurement_context_id == hourly_mesurement_context_id).first()

def update_hourly__soil_measurements(db: Session, hourly__soil_measurements: HourlySoilMeasurements, data: RawHourlyMetrics):
    hourly__soil_measurements.soil_temperature_0cm = data.soil_temperature_0cm_in_C
    hourly__soil_measurements.soil_temperature_6cm = data.soil_temperature_6cm_in_C
    hourly__soil_measurements.soil_temperature_18cm = data.soil_temperature_18cm_in_C
    hourly__soil_measurements.soil_temperature_54cm = data.soil_temperature_54cm_in_C
    hourly__soil_measurements.soil_moisture_0cm_to_1cm = data.soil_moisture_0cm_to_1cm_in_percentage
    hourly__soil_measurements.soil_moisture_1cm_to_3cm = data.soil_moisture_1cm_to_3cm_in_percentage
    hourly__soil_measurements.soil_moisture_3cm_to_9cm = data.soil_moisture_3cm_to_9cm_in_percentage
    hourly__soil_measurements.soil_moisture_9cm_to_27cm = data.soil_moisture_9cm_to_27cm_in_percentage
    hourly__soil_measurements.soil_moisture_27cm_to_81cm = data.soil_moisture_27cm_to_81cm_in_percentage
    hourly__soil_measurements.inserted_at = data.inserted_at
    db.commit()