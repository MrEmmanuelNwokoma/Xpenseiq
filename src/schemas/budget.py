from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal



class AddBudget(BaseModel):
    company_id: str
    start_time: datetime
    end_time: datetime
    amount: Decimal