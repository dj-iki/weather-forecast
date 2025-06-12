from sqlalchemy import Column, Integer, Float, TIMESTAMP, func, ForeignKey
from .base import DailySchema

class DailyWindMeasurements(DailySchema):
    __tablename__ = "daily__wind_measurements"

    id = Column("id", Integer, primary_key = True)
    wind_speed_10m_max = Column("wind_speed_10m_max", Float, nullable = False)
    wind_direction_10m_dominant = Column("wind_direction_10m_dominant", Integer, nullable = False)
    inserted_at = Column("inserted_at", TIMESTAMP, server_default = func.now())
    daily__measurement_context_id = Column(
        "daily__measurement_context_id", Integer, ForeignKey("daily__measurement_context.id")
    ) 