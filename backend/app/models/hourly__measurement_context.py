from .base import HourlySchema
from sqlalchemy import Column, Integer, TIMESTAMP, String, func

class HourlyMesurementContext(HourlySchema):
    __tablename__ = "hourly__measurement_context"

    id = Column("id", Integer, primary_key=True)
    place_name = Column("place_name", String, nullable=False)
    measurement_date_and_time = Column("measurement_date_and_time", TIMESTAMP, nullable=False)
    inserted_at = Column("inserted_at", TIMESTAMP, nullable=False, server_default=func.now())
    
