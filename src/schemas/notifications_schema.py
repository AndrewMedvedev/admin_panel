from pydantic import BaseModel


class NotificationAllSchema(BaseModel):
    text: str


class NotificationPhoneNumberSchema(BaseModel):
    text: str
    phone_number: str
