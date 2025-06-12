from sqlalchemy import Column, Integer, Float, TIMESTAMP, func, ForeignKey
from .base import DailySchema

class DailyTemperatureMeasurements(DailySchema):
    __tablename__ = "daily__temperature_measurements"

    id = Column("id", Integer, primary_key = True)
    temperature_2m_max = Column("temperature_2m_max", Float, nullable = False)
    temperature_2m_min = Column("temperature_2m_min", Float, nullable = False)
    inserted_at = Column("inserted_at", TIMESTAMP, server_default = func.now())
    daily__measurement_context_id = Column(
        "daily__measurement_context_id", Integer, ForeignKey("daily__measurement_context.id")
    ) 