from .base import HourlySchema
from sqlalchemy import Column, Integer, Float, TIMESTAMP, ForeignKey, func

class HourlyPrecipitationMeasurements(HourlySchema):
    __tablename__ = "hourly__precipitation_measurements"

    id = Column("id", Integer, primary_key=True)
    precipitation = Column("precipitation", Float, nullable=False)
    precipitation_probability = Column("precipitation_probability", Integer, nullable=False)
    relative_humidity_2m = Column("relative_humidity_2m", Integer, nullable=False)
    hourly_measurement_context_id = Column(
        "hourly_measurement_context_id", Integer, ForeignKey("hourly__measurement_context.id")
        )
    inserted_at = Column("inserted_at", TIMESTAMP, nullable=False, server_default=func.now())