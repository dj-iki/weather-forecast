from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base


RawSchema = declarative_base(
    metadata = MetaData(schema="raw_schema")
)

DailySchema = declarative_base(
    metadata = MetaData(schema="daily_schema")
)

HourlySchema = declarative_base(
    metadata = MetaData(schema="hourly_schema")
)