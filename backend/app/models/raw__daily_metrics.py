from sqlalchemy import Column, Integer, String, Float, Date, TIMESTAMP, func

from .base import RawSchema

class RawDailyMetrics(RawSchema):
    __tablename__= "raw__daily_metrics"

    longitude = Column("longitude", Float, nullable=False, primary_key=True)
    latitude = Column("latitude", Float, nullable=False, primary_key=True)
    measurment_date = Column("measurement_date", Date, nullable=False, primary_key=True)
    temperature_2m_max_in_C = Column("temperature_2m_max_in_C", Float, nullable=False)
    temperature_2m_min_in_C = Column("temperature_2m_min_in_C", Float, nullable=False)
    daylight_duration_in_s = Column("daylight_duration_in_s", Float, nullable=False)
    uv_index_max = Column("uv_index_max", Float, nullable=False)
    precipatition_sum_in_mm = Column("precipatition_sum_in_mm", Float, nullable=False)
    precipatition_hours_in_h = Column("precipatition_hours_in_h", Float, nullable=False)
    precipatition_probability_max_in_p = Column("precipatition_probability_max_in_p", Float, nullable=False)
    wind_speed_10m_max_in_kmph = Column("wind_speed_10m_max_in_kmph", Float, nullable=False)
    wind_direction_10m_dominant_in_degree = Column("wind_direction_10m_dominant_in_degree", Integer, nullable=False)
    inserted_at = Column("inserted_at", TIMESTAMP, nullable=False, server_default=func.now())
