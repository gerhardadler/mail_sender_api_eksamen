import smtplib
from email.mime.text import MIMEText

from models.mail import Mail


async def send_email(mail: Mail):
    msg = MIMEText(mail.body)
    msg["Subject"] = mail.subject
    msg["From"] = mail.sender
    recipent_list = []
    if mail.recipients is not None:
        recipent_list = [x.strip() for x in mail.recipients.split(",")]
    if mail.csv_recipients is not None:
        csv_recipients_string = (await mail.csv_recipients.read()).decode("utf-8")
        recipent_list += [x.strip() for x in csv_recipients_string.split(",")]
    with smtplib.SMTP_SSL(mail.email_server, mail.email_port) as smtp_server:
        smtp_server.login(mail.sender, mail.password)
        smtp_server.sendmail(mail.sender, recipent_list, msg.as_string())
