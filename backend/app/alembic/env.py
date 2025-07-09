from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from app.database.config import DATABASE_URL

from app.main import DailySchema, RawSchema, HourlySchema, UtilSchema
from app.models.daily__measurement_context import DailyMeasurementContext
from app.models.raw__daily_metrics import RawDailyMetrics
from app.models.raw__hourly_metrics import RawHourlyMetrics
from app.models.daily__wind_measurements import DailyWindMeasurements
from app.models.daily__precipitation_measurements import DailyPrecipitationMeasurements
from app.models.daily__temperature_measurements import DailyTemperatureMeasurements
from app.models.daily__uv_lights_measurements import DailyUVLightsMeasurements
from app.models.hourly__measurement_context import HourlyMesurementContext
from backend.app.models.hourly__precipitation_measurements import HourlyPercipitationMeasurements
from app.models.hourly__soil_measurements import HourlySoilMeasurements
from app.models.hourly__temperature_measurements import HourlyTemperatureMeasurements
from app.models.hourly__visibility_measurements import HourlyVisibilityMeasurements
from app.models.hourly__wind_measurements import HourlyWindMeasurements
from app.models.update_log import UpdateLog

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# TODO - Add schemas and models

# target_metadata = mymodel.Base.metadata
# TODO - Add schemas here (and public)
target_metadata = [RawSchema.metadata, DailySchema.metadata, HourlySchema.metadata]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

# TODO - Add schemas here
LIST_OF_SCHEMAS_TO_BE_SCANNED = ["public", "raw_schema", "daily_schema", "hourly_schema"]


def include_name(name, type_, parent_names):
    if type_ == "schema":
        return name in LIST_OF_SCHEMAS_TO_BE_SCANNED
    else:
        return True


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
        include_schemas=True,
        include_name=include_name,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = DATABASE_URL
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            include_schemas=True,
            include_name=include_name,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
