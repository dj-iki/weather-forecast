from sqlalchemy import String, Date, func
from sqlalchemy.orm import Session
from ..models.daily__measurement_context import DailyMeasurementContext


def get_daily__measurement_context(db: Session, place_name: String, measurement_date: Date):
    return db.query(DailyMeasurementContext).filter(DailyMeasurementContext.place_name == place_name,
                                                    DailyMeasurementContext.measurement_date == measurement_date).first()

def add_daily__measurement_context(db: Session, place_name: String, measurement_date: Date) -> DailyMeasurementContext:
    daily__measurement_context = DailyMeasurementContext(
        place_name = place_name,
        measurement_date = measurement_date
    )
    db.add(daily__measurement_context)
    db.commit()
    db.refresh(daily__measurement_context)
    return daily__measurement_context

def update_daily__measurement_context(db: Session, daily__measurement_context: DailyMeasurementContext):
    daily__measurement_context.inserted_at = func.now()
    db.commit()