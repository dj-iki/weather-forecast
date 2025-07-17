from sqlalchemy.orm import Session
from sqlalchemy import Integer, select, func
from sqlalchemy.exc import SQLAlchemyError
from ..models.raw__hourly_metrics import RawHourlyMetrics
from ..models.hourly__soil_measurements import HourlySoilMeasurements
from ..utils.logger import logger


def add_hourly__soil_measurements(
    db: Session, hourly__soil_measurements: HourlySoilMeasurements
):
    try:
        db.add(hourly__soil_measurements)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while adding HourlySoilMeasurements - {e}")


def get_hourly__soil_measurements(
    db: Session, hourly_mesurement_context_id: Integer
) -> HourlySoilMeasurements:
    return (
        db.query(HourlySoilMeasurements)
        .filter(
            HourlySoilMeasurements.hourly_measurement_context_id
            == hourly_mesurement_context_id
        )
        .first()
    )


def update_hourly__soil_measurements(
    db: Session,
    hourly__soil_measurements: HourlySoilMeasurements,
    data: RawHourlyMetrics,
):
    try:
        hourly__soil_measurements.soil_temperature_0cm = data.soil_temperature_0cm_in_C
        hourly__soil_measurements.soil_temperature_6cm = data.soil_temperature_6cm_in_C
        hourly__soil_measurements.soil_temperature_18cm = (
            data.soil_temperature_18cm_in_C
        )
        hourly__soil_measurements.soil_temperature_54cm = (
            data.soil_temperature_54cm_in_C
        )
        hourly__soil_measurements.soil_moisture_0cm_to_1cm = (
            data.soil_moisture_0cm_to_1cm_in_percentage
        )
        hourly__soil_measurements.soil_moisture_1cm_to_3cm = (
            data.soil_moisture_1cm_to_3cm_in_percentage
        )
        hourly__soil_measurements.soil_moisture_3cm_to_9cm = (
            data.soil_moisture_3cm_to_9cm_in_percentage
        )
        hourly__soil_measurements.soil_moisture_9cm_to_27cm = (
            data.soil_moisture_9cm_to_27cm_in_percentage
        )
        hourly__soil_measurements.soil_moisture_27cm_to_81cm = (
            data.soil_moisture_27cm_to_81cm_in_percentage
        )
        hourly__soil_measurements.inserted_at = data.inserted_at
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"There was an error while updating HourlySoilMeasurements - {e}")


def get_soil_temperature_0cm_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlySoilMeasurements.soil_temperature_0cm),
        func.max(HourlySoilMeasurements.soil_temperature_0cm),
        func.avg(HourlySoilMeasurements.soil_temperature_0cm),
    ).where(HourlySoilMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_soil_temperature_6cm_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlySoilMeasurements.soil_temperature_6cm),
        func.max(HourlySoilMeasurements.soil_temperature_6cm),
        func.avg(HourlySoilMeasurements.soil_temperature_6cm),
    ).where(HourlySoilMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_soil_temperature_18cm_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlySoilMeasurements.soil_temperature_18cm),
        func.max(HourlySoilMeasurements.soil_temperature_18cm),
        func.avg(HourlySoilMeasurements.soil_temperature_18cm),
    ).where(HourlySoilMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_soil_temperature_54cm_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlySoilMeasurements.soil_temperature_54cm),
        func.max(HourlySoilMeasurements.soil_temperature_54cm),
        func.avg(HourlySoilMeasurements.soil_temperature_54cm),
    ).where(HourlySoilMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_soil_moisture_0_to_1cm_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlySoilMeasurements.soil_moisture_0cm_to_1cm),
        func.max(HourlySoilMeasurements.soil_moisture_0cm_to_1cm),
        func.avg(HourlySoilMeasurements.soil_moisture_0cm_to_1cm),
    ).where(HourlySoilMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_soil_moisture_1_to_3cm_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlySoilMeasurements.soil_moisture_1cm_to_3cm),
        func.max(HourlySoilMeasurements.soil_moisture_1cm_to_3cm),
        func.avg(HourlySoilMeasurements.soil_moisture_1cm_to_3cm),
    ).where(HourlySoilMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_soil_moisture_3_to_9cm_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlySoilMeasurements.soil_moisture_3cm_to_9cm),
        func.max(HourlySoilMeasurements.soil_moisture_3cm_to_9cm),
        func.avg(HourlySoilMeasurements.soil_moisture_3cm_to_9cm),
    ).where(HourlySoilMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_soil_moisture_9_to_27cm_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlySoilMeasurements.soil_moisture_9cm_to_27cm),
        func.max(HourlySoilMeasurements.soil_moisture_9cm_to_27cm),
        func.avg(HourlySoilMeasurements.soil_moisture_9cm_to_27cm),
    ).where(HourlySoilMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result


def get_soil_moisture_27_to_81cm_for_report(db: Session, id: Integer):
    query = select(
        func.min(HourlySoilMeasurements.soil_moisture_27cm_to_81cm),
        func.max(HourlySoilMeasurements.soil_moisture_27cm_to_81cm),
        func.avg(HourlySoilMeasurements.soil_moisture_27cm_to_81cm),
    ).where(HourlySoilMeasurements.hourly_measurement_context_id >= id)

    result = db.execute(query).one()

    return result
