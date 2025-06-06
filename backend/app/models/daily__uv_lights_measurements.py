from sqlalchemy import Column, Integer, Float, TIMESTAMP, func, ForeignKey
from .base import DailySchema

class DailyUVLightsMeasurements(DailySchema):
    __tablename__ = "daily__uv_lights_measurements"

    id = Column("id", Integer, primary_key = True)
    daylight_duration = Column("daylight_duration", Float, nullable = False)
    uv_index_max = Column("uv_index_max", Float, nullable = False)
    inserted_at = Column("inserte_at", TIMESTAMP, server_default = func.now())
    daily__measurement_context_id = Column(
        "daily__measurement_context_id", Integer, ForeignKey("daily__measurement_context.id")
    ) 