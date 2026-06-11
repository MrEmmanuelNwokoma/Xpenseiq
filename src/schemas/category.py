from pydantic import BaseModel
from typing import Optional


class AddCategory(BaseModel):
    company_id: Optional[str] = None
    name: str
    description: str
    
