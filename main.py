from fastapi import FastAPI
from models.mail import Mail
from send_email import send_email

app = FastAPI(title="How to Send Email")


@app.get("/")
def index():
    return "I'm a teapot"

@app.post("/send-email")
def send_email_route(mail: Mail):
    send_email(mail)
    return "Success"
