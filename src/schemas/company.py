from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from uuid import UUID



    
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

class ReadCompanySchema(BaseModel):
    id: UUID
    name: str
    email: str
    is_email_verified: bool
    is_active: bool
    last_login: str | None
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)

        