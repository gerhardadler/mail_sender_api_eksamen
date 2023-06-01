import smtplib
from fastapi import FastAPI
from models.mail import Mail
from send_email import send_email
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="How to Send Email")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return "I'm a teapot"

@app.post("/send-email")
def send_email_route(mail: Mail):
    try:
        send_email(mail)
    except smtplib.SMTPRecipientsRefused as e:
        return "Error with recipients", 400
    except smtplib.SMTPAuthenticationError as e:
        return "Sender and password not accepted", 402
    except Exception as e:
        return "Unknown exception", 500
    return "Success", 200
