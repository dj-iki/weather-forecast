from .base import HourlySchema
from sqlalchemy import Column, Integer, Float, TIMESTAMP, ForeignKey, func

class HourlyWindMeasurements(HourlySchema):
    __tablename__ = "hourly__wind_measurements"

    id = Column("id", Integer, primary_key=True)
    wind_speed_10m = Column("wind_speed_10m", Float, nullable=False)
    wind_speed_80m = Column("wind_speed_80m", Float, nullable=False)
    wind_speed_120m = Column("wind_speed_120m", Float, nullable=False)
    wind_speed_180m = Column("wind_speed_180m", Float, nullable=False)
    wind_direction_10m = Column("wind_direction_10m", Integer, nullable=False)
    wind_direction_80m = Column("wind_direction_80m", Integer, nullable=False)
    wind_direction_120m = Column("wind_direction_120m", Integer, nullable=False)
    wind_direction_180m = Column("wind_direction_180m", Integer, nullable=False)
    hourly_measurement_context_id = Column(
        "hourly_measurement_context_id", Integer, ForeignKey("hourly__measurement_context.id")
        )
    inserted_at = Column("inserted_at", TIMESTAMP, nullable=False, server_default=func.now())