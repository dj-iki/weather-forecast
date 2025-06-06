from sqlalchemy import Column, Integer, Float, TIMESTAMP, func, ForeignKey
from .base import DailySchema

class DailyPrecipitationMeasurements(DailySchema):
    __tablename__ = "daily__precipitation_measurements"

    id = Column("id", Integer, primary_key = True)
    precipitation_sum = Column("precipitation_sum", Float, nullable = False)
    precipitation_length = Column("precipitation_length", Float, nullable = False)
    precipitation_probability_max = Column("precipitation_probability_max", Float, nullable = False)
    inserted_at = Column("inserte_at", TIMESTAMP, server_default = func.now())
    daily__measurement_context_id = Column(
        "daily__measurement_context_id", Integer, ForeignKey("daily__measurement_context.id")
    ) 