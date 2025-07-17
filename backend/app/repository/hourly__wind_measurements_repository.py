from sqlalchemy.orm import Session
from sqlalchemy import Integer, select, func
from sqlalchemy.exc import SQLAlchemyError
from ..models.hourly__wind_measurements import HourlyWindMeasurements
from ..models.raw__hourly_metrics import RawHourlyMetrics
from ..utils.logger import logger


def add_hourly__wind_measurements(
    db: Session, hourly__wind_measurements: HourlyWindMeasurements
):
    try:
        db.add(hourly__wind_measurements)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while adding HourlyWindMeasurements - {e}")


def get_hourly__wind_measurements(
    db: Session, hourly_measurement_context_id: Integer
) -> HourlyWindMeasurements:
    return (
        db.query(HourlyWindMeasurements)
        .filter(
            HourlyWindMeasurements.hourly_measurement_context_id
            == hourly_measurement_context_id
        )
        .first()
    )


def update_hourly__wind_measurements(
    db: Session,
    hourly__wind_measurements: HourlyWindMeasurements,
    data: RawHourlyMetrics,
):
    try:
        hourly__wind_measurements.wind_speed_10m = data.wind_speed_10m_in_kmph
        hourly__wind_measurements.wind_speed_80m = data.wind_speed_80m_in_kmph
        hourly__wind_measurements.wind_speed_120m = data.wind_speed_120m_in_kmph
        hourly__wind_measurements.wind_speed_180m = data.wind_speed_180m_in_kmph
        hourly__wind_measurements.wind_direction_10m = data.wind_direction_10m_in_degree
        hourly__wind_measurements.wind_direction_80m = data.wind_direction_80m_in_degree
        hourly__wind_measurements.wind_direction_120m = (
            data.wind_direction_120m_in_degree
        )
        hourly__wind_measurements.wind_direction_180m = (
            data.wind_direction_180m_in_degree
        )
        hourly__wind_measurements.inserted_at = data.inserted_at
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while updating HourlyWindMeasurements - {e}")


def get_wind_direction_10m_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyWindMeasurements.wind_direction_10m),
        func.max(HourlyWindMeasurements.wind_direction_10m),
        func.avg(HourlyWindMeasurements.wind_direction_10m),
    ).where(HourlyWindMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_wind_direction_80m_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyWindMeasurements.wind_direction_80m),
        func.max(HourlyWindMeasurements.wind_direction_80m),
        func.avg(HourlyWindMeasurements.wind_direction_80m),
    ).where(HourlyWindMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_wind_direction_120m_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyWindMeasurements.wind_direction_120m),
        func.max(HourlyWindMeasurements.wind_direction_120m),
        func.avg(HourlyWindMeasurements.wind_direction_120m),
    ).where(HourlyWindMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_wind_direction_180m_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyWindMeasurements.wind_direction_180m),
        func.max(HourlyWindMeasurements.wind_direction_180m),
        func.avg(HourlyWindMeasurements.wind_direction_180m),
    ).where(HourlyWindMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_wind_speed_10m_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyWindMeasurements.wind_speed_10m),
        func.max(HourlyWindMeasurements.wind_speed_10m),
        func.avg(HourlyWindMeasurements.wind_speed_10m),
    ).where(HourlyWindMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_wind_speed_80m_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyWindMeasurements.wind_speed_80m),
        func.max(HourlyWindMeasurements.wind_speed_80m),
        func.avg(HourlyWindMeasurements.wind_speed_80m),
    ).where(HourlyWindMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_wind_speed_120m_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyWindMeasurements.wind_speed_120m),
        func.max(HourlyWindMeasurements.wind_speed_120m),
        func.avg(HourlyWindMeasurements.wind_speed_120m),
    ).where(HourlyWindMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_wind_speed_180m_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyWindMeasurements.wind_speed_180m),
        func.max(HourlyWindMeasurements.wind_speed_180m),
        func.avg(HourlyWindMeasurements.wind_speed_180m),
    ).where(HourlyWindMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result
