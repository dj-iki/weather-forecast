from .base import HourlySchema
from sqlalchemy import Column, Integer, Float, TIMESTAMP, ForeignKey, func

class HourlyTemperatureMeasurements(HourlySchema):
    __tablename__ = "hourly__temperature_measurements"

    id = Column("id", Integer, primary_key=True)
    temperature_2m = Column("temperature_2m", Float, nullable=False)
    temperature_80m = Column("temperature_80m", Float, nullable=False)
    temperature_120m = Column("temperature_120m", Float, nullable=False)
    temperature_180m = Column("temperature_180m", Float, nullable=False)
    hourly_measurement_context_id = Column(
        "hourly_measurement_context_id", Integer, ForeignKey("hourly__measurement_context.id")
        )
    inserted_at = Column("inserted_at", TIMESTAMP, nullable=False, server_default=func.now())