from sqlalchemy.orm import Session
from sqlalchemy import Integer, select, func
from sqlalchemy.exc import SQLAlchemyError
from ..models.hourly__visibility_measurements import HourlyVisibilityMeasurements
from ..models.raw__hourly_metrics import RawHourlyMetrics
from ..utils.logger import logger


def add_hourly__visibility_measurements(
    db: Session, hourly__visibility_measurements: HourlyVisibilityMeasurements
):
    try:
        db.add(hourly__visibility_measurements)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(
            f"There was an error while adding HourlyVisibilityMeasurements - {e}"
        )


def get_hourly__visibility_measurements(
    db: Session, hourly_measurement_context_id: Integer
) -> HourlyVisibilityMeasurements:
    return (
        db.query(HourlyVisibilityMeasurements)
        .filter(
            HourlyVisibilityMeasurements.hourly_measurement_context_id
            == hourly_measurement_context_id
        )
        .first()
    )


def update_hourly__visibility_measurements(
    db: Session,
    hourly__visibility_measurements: HourlyVisibilityMeasurements,
    data: RawHourlyMetrics,
):
    try:
        hourly__visibility_measurements.cloud_cover_low = (
            data.cloud_cover_low_in_percentage
        )
        hourly__visibility_measurements.cloud_cover = data.cloud_cover_in_percentage
        hourly__visibility_measurements.cloud_cover_mid = (
            data.cloud_cover_mid_in_percentage
        )
        hourly__visibility_measurements.cloud_cover_high = (
            data.cloud_cover_high_in_percentage
        )
        hourly__visibility_measurements.visibility = data.visibility_in_m
        hourly__visibility_measurements.inserted_at = data.inserted_at
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(
            f"There was an error while updating HourlyVisibilityMeasurements - {e}"
        )


def get_cloud_cover_low_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyVisibilityMeasurements.cloud_cover_low),
        func.max(HourlyVisibilityMeasurements.cloud_cover_low),
        func.avg(HourlyVisibilityMeasurements.cloud_cover_low),
    ).where(HourlyVisibilityMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_cloud_cover_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyVisibilityMeasurements.cloud_cover),
        func.max(HourlyVisibilityMeasurements.cloud_cover),
        func.avg(HourlyVisibilityMeasurements.cloud_cover),
    ).where(HourlyVisibilityMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_cloud_cover_high_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyVisibilityMeasurements.cloud_cover_high),
        func.max(HourlyVisibilityMeasurements.cloud_cover_high),
        func.avg(HourlyVisibilityMeasurements.cloud_cover_high),
    ).where(HourlyVisibilityMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_cloud_cover_mid_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyVisibilityMeasurements.cloud_cover_mid),
        func.max(HourlyVisibilityMeasurements.cloud_cover_mid),
        func.avg(HourlyVisibilityMeasurements.cloud_cover_mid),
    ).where(HourlyVisibilityMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_visibilty_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyVisibilityMeasurements.visibility),
        func.max(HourlyVisibilityMeasurements.visibility),
        func.avg(HourlyVisibilityMeasurements.visibility),
    ).where(HourlyVisibilityMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result
