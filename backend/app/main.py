from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .scheduled.scheduler import scheduled_hourly, scheduled_daily
from .utils.logger import logger
from datetime import datetime


# needed for Alembic migrations to work
# TODO - Add schemas import here for Alembic
# TODO - Import routers

from .routers import dummy
from .models.base import RawSchema, DailySchema, HourlySchema, UtilSchema


description = """

# Weather Forecast
## Endpoints - TODO
"""






app = FastAPI(
    title="Weather-Forecast",
    description=description,
    summary="Internship",
    version="0.0.1",
    contact={
        "name": "Milutin Đikandić",
        "email": "milutindjikandic@gmail.com",
    },
    license_info={
        "name": "Apache 2.0 - License information",
        "identifier": "MIT",
    },
    docs_url="/documentation",
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# TODO - Add routers with app.include_router(name.router)

app.include_router(dummy.router)



# TODO - Add scheduler and tasks

scheduler = BackgroundScheduler()


@app.on_event("startup")
def start_scheduler():
    scheduler.add_job(
        scheduled_daily,
        CronTrigger(minute="0",hour="21",day_of_week="sun"),
        id="get_raw_daily_data",
        replace_existing=True
    )
    scheduler.add_job(
        scheduled_hourly,
        CronTrigger(minute="15"),
        id="get_raw_hourly_data",
        replace_existing=True
    )

    scheduler.start()
    logger.info(f"[{datetime.now()}] scheduler started")


@app.on_event("shutdown")
def stop_scheduler():
    scheduler.shutdown()
    logger.info(f"[{datetime.now()}] scheduler stopped")
