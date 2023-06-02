import smtplib
import socket
from fastapi import Depends, FastAPI, HTTPException
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
async def send_email_route(mail: Mail = Depends()):
    try:
        await send_email(mail)
    except smtplib.SMTPRecipientsRefused:
        raise HTTPException(status_code=400, detail="Error with recipients")
    except smtplib.SMTPAuthenticationError:
        raise HTTPException(status_code=402, detail="Sender and password not accepted")
    except socket.gaierror:
        raise HTTPException(status_code=400, detail="Email server not found")
    except Exception as e:
        print(type(e))
        print(e)
        raise HTTPException(status_code=500, detail="Unknown exception")
    return "Success"
