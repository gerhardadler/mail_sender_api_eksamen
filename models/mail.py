from pydantic import BaseModel

class Mail(BaseModel):
    subject: str
    body: str
    recipients: list[str]
    sender: str
    password: str