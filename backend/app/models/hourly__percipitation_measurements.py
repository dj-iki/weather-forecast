from .base import HourlySchema
from sqlalchemy import Column, Integer, Float, TIMESTAMP, ForeignKey, func

class HourlyPercipitationMeasurements(HourlySchema):
    __tablename__ = "hourly__percipitation_measurements"

    id = Column("id", Integer, primary_key=True)
    percipitation = Column("percipitation", Float, nullable=False)
    percipitation_probability = Column("percipitation_probability", Integer, nullable=False)
    relative_humidity_2m = Column("relative_humidity_2m", Integer, nullable=False)
    hourly_measurement_context_id = Column(
        "hourly_measurement_context_id", Integer, ForeignKey("hourly__measurement_context.id")
        )
    inserted_at = Column("inserted_at", TIMESTAMP, nullable=False, server_default=func.now())