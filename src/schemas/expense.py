from pydantic import BaseModel


class AddExpense(BaseModel):
    company_id: str
    employee_id: str
    category_id: str
    description: str
    amount: str
 