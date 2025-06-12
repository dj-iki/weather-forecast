from .base import HourlySchema
from sqlalchemy import Column, Integer, Float, TIMESTAMP, ForeignKey, func

class HourlySoilMeasurements(HourlySchema):
    __tablename__ = "hourly__soil_measurements"

    id = Column("id", Integer, primary_key=True)
    soil_temperature_0cm = Column("soil_temperature_0cm", Float, nullable=False)
    soil_temperature_6cm = Column("soil_temperature_6cm", Float, nullable=False)
    soil_temperature_18cm = Column("soil_temperature_18cm", Float, nullable=False)
    soil_temperature_54cm = Column("soil_temperature_54cm", Float, nullable=False)
    soil_moisture_0cm_to_1cm = Column("soil_moisture_0cm_to_1cm", Float, nullable=False)
    soil_moisture_1cm_to_3cm = Column("soil_moisture_1cm_to_3cm", Float, nullable=False)
    soil_moisture_3cm_to_9cm = Column("soil_moisture_3cm_to_9cm", Float, nullable=False)
    soil_moisture_9cm_to_27cm = Column("soil_moisture_9cm_to_27cm", Float, nullable=False)
    soil_moisture_27cm_to_81cm = Column("soil_moisture_27cm_to_81cm", Float, nullable=False)
    hourly_measurement_context_id = Column(
        "hourly_measurement_context_id", Integer, ForeignKey("hourly__measurement_context.id")
        )
    inserted_at = Column("inserted_at", TIMESTAMP, nullable=False, server_default=func.now())