from pydantic import BaseModel, EmailStr
from datetime import datetime


class AddCompany(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginCompany(BaseModel):
    email: EmailStr
    password: str
    

class CompanyProfile(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    is_email_verified: bool
    last_login: datetime | None = None