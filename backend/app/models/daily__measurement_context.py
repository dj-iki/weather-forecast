from sqlalchemy import Column, String, Date, TIMESTAMP, Integer, func
from .base import DailySchema

class DailyMeasurementContext(DailySchema):
    __tablename__ = "daily__measurement_context"

    id = Column("id", Integer, primary_key = True)
    place_name = Column("place_name", String, nullable = False)
    measurement_date = Column("measurement_date", Date, nullable = False)
    inserted_at = Column("inserted_at", TIMESTAMP, server_default = func.now())
