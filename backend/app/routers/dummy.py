import requests
from fastapi import APIRouter, status, Depends, Query, HTTPException
from ..dependencies.dummy import get_print_dummy
from typing import Annotated
router = APIRouter(
    prefix="/dummy",
    tags=["dummy"],
)


@router.get("/", status_code=status.HTTP_200_OK)
def dummy(print_dummy=Depends(get_print_dummy)):
    return {"message": print_dummy()}

# https://api.open-meteo.com/v1/forecast?latitude=45.7704&longitude=19.277&hourly=temperature_2m,relative_humidity_2m,precipitation,precipitation_probability,cloud_cover_low,cloud_cover,cloud_cover_mid,cloud_cover_high,visibility,wind_speed_10m,wind_direction_10m,wind_speed_80m,wind_speed_120m,wind_speed_180m,wind_direction_80m,wind_direction_120m,wind_direction_180m,temperature_120m,temperature_80m,temperature_180m,soil_temperature_0cm,soil_temperature_6cm,soil_temperature_18cm,soil_temperature_54cm,soil_moisture_0_to_1cm,soil_moisture_1_to_3cm,soil_moisture_3_to_9cm,soil_moisture_9_to_27cm,soil_moisture_27_to_81cm&timezone=Europe%2FBerlin&forecast_days=1
@router.get("/api/get_hourly/")
def get_hourly(latitude: Annotated[float, Query(ge = (-180), le = 180)] = 45.7704, longitude: Annotated[float, Query(ge = (-90), le = 90)] = 19.277):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relative_humidity_2m,precipitation,precipitation_probability,cloud_cover_low,cloud_cover,cloud_cover_mid,cloud_cover_high,visibility,wind_speed_10m,wind_direction_10m,wind_speed_80m,wind_speed_120m,wind_speed_180m,wind_direction_80m,wind_direction_120m,wind_direction_180m,temperature_120m,temperature_80m,temperature_180m,soil_temperature_0cm,soil_temperature_6cm,soil_temperature_18cm,soil_temperature_54cm,soil_moisture_0_to_1cm,soil_moisture_1_to_3cm,soil_moisture_3_to_9cm,soil_moisture_9_to_27cm,soil_moisture_27_to_81cm&timezone=auto&forecast_days=1"

    response = requests.get(url)
     
    data = response.json()

    if response.ok:
        return data
    else:
        raise HTTPException(status_code=response.status_code, detail="Api request failed")
        
@router.get("/api/get_daily")
def get_daily(latitude: Annotated[float, Query(ge = (-180), le = 180)] = 45.7704, longitude: Annotated[float, Query(ge = (-90), le = 90)] = 19.277):

    url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,daylight_duration,uv_index_max,precipitation_sum,precipitation_hours,precipitation_probability_max,wind_speed_10m_max,wind_direction_10m_dominant&timezone=auto&forecast_days=3"

    response = requests.get(url)
     
    data = response.json()

    if response.ok:
        return data
    else:
        raise HTTPException(status_code=response.status_code, detail="Api request failed")