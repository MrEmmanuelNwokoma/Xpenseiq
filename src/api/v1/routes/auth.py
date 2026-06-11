from fastapi import APIRouter, Depends
from src.api.v1.dependencies import get_auth_service
from src.auth.services import AuthService
from src.schemas.company import AddCompany

auth_router = APIRouter(prefix="/api/v1/auth")

@auth_router.post("/")
async def register_company(
    company_data: AddCompany,
    auth_service: AuthService = Depends(get_auth_service)
):
    response = await auth_service.register_company(company_data)
    return response
