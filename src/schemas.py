from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date
from typing import Optional


class ContactModel(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date
    additional_info: Optional[str] = None


class ContactResponse(ContactModel):
    id: int

    model_config = ConfigDict(from_attributes=True)
