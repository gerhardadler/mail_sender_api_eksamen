from dataclasses import dataclass
from typing import Union

from fastapi import Form, UploadFile


@dataclass
class Mail:
    subject: str = Form(...)
    body: str = Form(...)
    recipients: str = Form(...)
    csv_recipients: Union[UploadFile, None] = None
    sender: str = Form(...)
    password: str = Form(...)
