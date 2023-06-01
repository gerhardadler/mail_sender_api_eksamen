from dataclasses import dataclass

from fastapi import Form


@dataclass
class Mail:
    subject: str = Form(...)
    body: str = Form(...)
    recipients: str = Form(...)
    sender: str = Form(...)
    password: str = Form(...)
