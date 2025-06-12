from .base import HourlySchema
from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey, func

class HourlyVisibilityMeasurements(HourlySchema):
    __tablename__ = "hourly__visibility_measurements"

    id = Column("id", Integer, primary_key=True)
    visibility = Column("visibility", Integer, nullable=False)
    cloud_cover_low = Column("cloud_cover_low", Integer, nullable=False)
    cloud_cover = Column("cloud_cover", Integer, nullable=False)
    cloud_cover_mid = Column("cloud_cover_mid", Integer, nullable=False)
    cloud_cover_high = Column("cloud_cover_high", Integer, nullable=False)
    hourly_measurement_context_id = Column(
        "hourly_measurement_context_id", Integer, ForeignKey("hourly__measurement_context.id")
        )
    inserted_at = Column("inserted_at", TIMESTAMP, nullable=False, server_default=func.now())