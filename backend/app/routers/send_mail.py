from fastapi import APIRouter, status, Query, Depends
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from ..settings import settings
from ..dependencies.get_data_for_report import get_data_for_report_dependencie
import os
from sqlalchemy.orm import Session
from sqlalchemy import select, and_, func
from datetime import datetime, timedelta
from ..models.hourly__measurement_context import HourlyMesurementContext
from ..models.hourly__visibility_measurements import HourlyVisibilityMeasurements
from ..dependencies.session import get_db

db: Session = next(get_db())

router = APIRouter(
    prefix="/send-mail",
    tags=["send-mail"],
)

config = ConnectionConfig(
    MAIL_USERNAME=settings.mail_username,
    MAIL_PASSWORD=settings.mail_password,
    MAIL_FROM=settings.mail_from,
    MAIL_PORT=settings.mail_port,
    MAIL_SERVER=settings.mail_server,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=settings.use_credentials,
    VALIDATE_CERTS=True,
    MAIL_DEBUG=1,
)



env = Environment(loader=FileSystemLoader("/backend/app/templates"))


@router.get("/", status_code=status.HTTP_200_OK)
async def send_mail(num_days: int = 1, place_name: str = "Београд", data = Depends(get_data_for_report_dependencie)):
    if data != "NESTO NE VALJA":
        template = env.get_template("testreport.html")
        html_content = template.render(data=data)

        HTML(string=html_content).write_pdf("/backend/app/reports/generated.pdf")

        message = MessageSchema(
            subject="Report",
            recipients=["example@email.com"],
            body="Ipak sam uspeo da napravim dependecy, malko sam glup jbg. Nadam se da ovo valja, ovo je za hourly weather-forecast.",
            subtype="plain",
            attachments=["/backend/app/reports/generated.pdf"],
        )
        fm = FastMail(config)
        await fm.send_message(message)
        return {"message": "Report sent!"}
    else:
        return {"message": "DOSLO JE DO GRESKE"}