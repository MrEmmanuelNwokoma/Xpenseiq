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
    name: str
    email: EmailStr
    is_email_verified: bool
    last_login: datetime | None = None

class UpdateCompany(BaseModel):
    name: str
    