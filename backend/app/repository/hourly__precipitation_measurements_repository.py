from sqlalchemy.orm import Session
from sqlalchemy import Integer, select, func
from sqlalchemy.exc import SQLAlchemyError
from ..models.raw__hourly_metrics import RawHourlyMetrics
from ..models.hourly__precipitation_measurements import HourlyPrecipitationMeasurements
from ..utils.logger import logger
from datetime import datetime, timedelta


def add_hourly__precipitation_measurements(
    db: Session, hourly__precipitation_measurements: HourlyPrecipitationMeasurements
):
    try:
        db.add(hourly__precipitation_measurements)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(
            f"There was an error while adding HourlyPrecipitationMeasurements - {e}"
        )


def get_hourly__precipitation_measurements(
    db: Session, hourly_measurement_context_id: Integer
) -> HourlyPrecipitationMeasurements:
    return (
        db.query(HourlyPrecipitationMeasurements)
        .filter(
            HourlyPrecipitationMeasurements.hourly_measurement_context_id
            == hourly_measurement_context_id
        )
        .first()
    )


def update_hourly__precipitation_measurements(
    db: Session,
    hourly__precipitation_measurements: HourlyPrecipitationMeasurements,
    data: RawHourlyMetrics,
):
    try:
        hourly__precipitation_measurements.precipitation = data.precipitation_in_mm
        hourly__precipitation_measurements.precipitation_probability = (
            data.precipitation_probability_in_percentage
        )
        hourly__precipitation_measurements.relative_humidity_2m = (
            data.relative_humidity_2m_in_percentage
        )
        hourly__precipitation_measurements.inserted_at = data.inserted_at
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(
            f"There was an error while updating HourlyPrecipitaionMeasurements - {e}"
        )


def get_precipitation_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyPrecipitationMeasurements.precipitation),
        func.max(HourlyPrecipitationMeasurements.precipitation),
        func.avg(HourlyPrecipitationMeasurements.precipitation)
    ).where(HourlyPrecipitationMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result

def get_precipitation_probability_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyPrecipitationMeasurements.precipitation_probability),
        func.max(HourlyPrecipitationMeasurements.precipitation_probability),
        func.avg(HourlyPrecipitationMeasurements.precipitation_probability)
    ).where(HourlyPrecipitationMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result

def get_relative_humidity_2m_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyPrecipitationMeasurements.relative_humidity_2m),
        func.max(HourlyPrecipitationMeasurements.relative_humidity_2m),
        func.avg(HourlyPrecipitationMeasurements.relative_humidity_2m)
    ).where(HourlyPrecipitationMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result