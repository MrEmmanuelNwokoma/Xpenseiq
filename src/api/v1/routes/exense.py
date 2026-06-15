from fastapi import APIRouter, Depends
from src.api.v1.dependencies import get_current_company_api_key, get_expense_service
from src.models.company import Company
from src.schemas.expense import LogExpenseSchema
from src.services.expense_service import ExpenseService



expense_router = APIRouter(prefix="/api/v1/expenses", tags=["Expenses"])

@expense_router.post("/")
async def log_expense(
    expense_data: LogExpenseSchema,
    current_api_key: Company = Depends(get_current_company_api_key),
    expense_service: ExpenseService = Depends(get_expense_service)
):
    response = await expense_service.log_expense(expense_data)
    return response