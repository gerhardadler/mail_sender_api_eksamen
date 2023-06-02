from dataclasses import dataclass
from typing import Union

from fastapi import Form, UploadFile


@dataclass
class Mail:
    subject: str = Form(...)
    body: str = Form(...)
    recipients: Union[str, None] = Form(None)
    csv_recipients: Union[UploadFile, None] = None
    sender: str = Form(...)
    password: str = Form(...)
    email_server: str = Form(...)
    email_port: int = Form(...)
