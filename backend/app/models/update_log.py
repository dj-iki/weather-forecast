from .base import UtilSchema
from sqlalchemy import Column, Integer, TIMESTAMP, UniqueConstraint, CheckConstraint, String


class UpdateLog(UtilSchema):
    __tablename__ = "update_log"

    id = Column("id", Integer, primary_key=True)
    data_type = Column("data_type", String, nullable=False)
    last_updated = Column("last_updated", TIMESTAMP, nullable=False)

    __table_args__ = (
        UniqueConstraint("data_type", name="uq_data_type"),
        CheckConstraint("data_type IN ('hourly','daily')", name="check_data_type")
    )