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


async def send_email(mail: Mail):
    msg = MIMEText(mail.body)
    msg["Subject"] = mail.subject
    msg["From"] = mail.sender
    recipent_list = [x.strip() for x in mail.recipients.split(",")]
    if mail.csv_recipients is not None:
        csv_recipients_string = (await mail.csv_recipients.read()).decode("utf-8") 
        recipent_list += [x.strip() for x in csv_recipients_string.split(",")]
    with smtplib.SMTP_SSL(Env.MAIL_SERVER, Env.MAIL_PORT) as smtp_server:
        smtp_server.login(mail.sender, mail.password)
        smtp_server.sendmail(mail.sender, recipent_list, msg.as_string())
