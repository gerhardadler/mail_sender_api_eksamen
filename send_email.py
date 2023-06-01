import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

from models.mail import Mail

load_dotenv(".env")

if os.getenv("MAIL_PORT") is None or os.getenv("MAIL_SERVER") is None:
    raise ValueError("Missing environment variables")


class Env:
    MAIL_PORT: int = int(os.getenv("MAIL_PORT"))  # type: ignore
    MAIL_SERVER: str = os.getenv("MAIL_SERVER")  # type: ignore


def send_email(mail: Mail):
    msg = MIMEText(mail.body)
    msg["Subject"] = mail.subject
    msg["From"] = mail.sender
    msg["To"] = mail.recipients
    with smtplib.SMTP_SSL(Env.MAIL_SERVER, Env.MAIL_PORT) as smtp_server:
        smtp_server.login(mail.sender, mail.password)
        smtp_server.sendmail(mail.sender, mail.recipients, msg.as_string())
