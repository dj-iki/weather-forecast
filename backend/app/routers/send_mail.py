from fastapi import APIRouter, status, Query
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from ..settings import settings
import os


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
    MAIL_DEBUG=1
)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
REPORT_PATH = os.path.join(BASE_DIR, "reports", "generated.pdf")


env = Environment(loader=FileSystemLoader("/backend/app/templates"))




@router.get("/", status_code=status.HTTP_200_OK)
async def send_mail(num_days: int = 1, place_name: str = "Београд"):
    data = [{"name": "nesto", "min": "min", "max": "max", "average": "avg"}]

    print("Loading templates from:", TEMPLATE_DIR)
    print("Files in template dir:", os.listdir(TEMPLATE_DIR))


    template = env.get_template("testreport.html")
    html_content = template.render(data=data)

    HTML(string=html_content).write_pdf(REPORT_PATH)

    message = MessageSchema(
        subject="Report",
        recipients=["milutindjikandic@gmail.com"],
        body="SMRDIM",
        subtype="plain",
        attachments=["/backend/app/reports/generated.pdf"]
    )
    fm = FastMail(config)
    await fm.send_message(message)
    return {"message": "Report sent!"}
