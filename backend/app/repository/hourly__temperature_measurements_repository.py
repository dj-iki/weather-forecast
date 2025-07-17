from sqlalchemy.orm import Session
from sqlalchemy import Integer, select, func
from sqlalchemy.exc import SQLAlchemyError
from ..models.hourly__temperature_measurements import HourlyTemperatureMeasurements
from ..models.raw__hourly_metrics import RawHourlyMetrics
from ..utils.logger import logger


def add_hourly__temperature_measurements(
    db: Session, hourly__temperature_measurements: HourlyTemperatureMeasurements
):
    try:
        db.add(hourly__temperature_measurements)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(
            f"There was an error while adding HourlyTemperatureMeasurements - {e}"
        )


def get_hourly__temperature_measurements(
    db: Session, hourly_measurement_context_id: Integer
) -> HourlyTemperatureMeasurements:
    return (
        db.query(HourlyTemperatureMeasurements)
        .filter(
            HourlyTemperatureMeasurements.hourly_measurement_context_id
            == hourly_measurement_context_id
        )
        .first()
    )


def update_hourly__temperature_measurements(
    db: Session,
    hourly__temperature_measurements: HourlyTemperatureMeasurements,
    data: RawHourlyMetrics,
):
    try:
        hourly__temperature_measurements.temperature_2m = data.temperature_2m_in_C
        hourly__temperature_measurements.temperature_80m = data.temperature_80m_in_C
        hourly__temperature_measurements.temperature_120m = data.temperature_120m_in_C
        hourly__temperature_measurements.temperature_180m = data.temperature_180m_in_C
        hourly__temperature_measurements.inserted_at = data.inserted_at
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(
            f"There was an error while updating HourlyTemperatureMeasurements - {e}"
        )


def get_tmeperature_2m_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyTemperatureMeasurements.temperature_2m),
        func.max(HourlyTemperatureMeasurements.temperature_2m),
        func.avg(HourlyTemperatureMeasurements.temperature_2m),
    ).where(HourlyTemperatureMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_tmeperature_80m_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyTemperatureMeasurements.temperature_80m),
        func.max(HourlyTemperatureMeasurements.temperature_80m),
        func.avg(HourlyTemperatureMeasurements.temperature_80m),
    ).where(HourlyTemperatureMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_tmeperature_120m_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyTemperatureMeasurements.temperature_120m),
        func.max(HourlyTemperatureMeasurements.temperature_120m),
        func.avg(HourlyTemperatureMeasurements.temperature_120m),
    ).where(HourlyTemperatureMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_tmeperature_180m_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlyTemperatureMeasurements.temperature_180m),
        func.max(HourlyTemperatureMeasurements.temperature_180m),
        func.avg(HourlyTemperatureMeasurements.temperature_180m),
    ).where(HourlyTemperatureMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result
