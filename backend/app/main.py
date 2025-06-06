from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import dummy

# needed for Alembic migrations to work
# TODO - Add schemas import here for Alembic
# TODO - Import routers

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