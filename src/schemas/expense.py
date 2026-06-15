from pydantic import BaseModel
from decimal import Decimal


class LogExpenseSchema(BaseModel):
    company_id: str
    # employee_name: str
    department: str
    category_id: str
    description: str
    amount: Decimal
 