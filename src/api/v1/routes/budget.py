from fastapi import APIRouter, Depends
from src.schemas.budget import AddBudget
from src.api.v1.dependencies import get_budget_service, get_current_company_api_key
from src.models.company import Company
from src.services.budget_service import BudgetService


budget_router = APIRouter(prefix="/api/v1/budgets", tags=["BUdgets"])


@budget_router.post("/")
async def add_budget(
    budget_data: AddBudget,
    current_api_key: Company = Depends(get_current_company_api_key),
    budget_service: BudgetService = Depends(get_budget_service),
    
    
):
    response = await budget_service.add_budget(budget_data)
    return response
