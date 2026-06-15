from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.api.v1.dependencies import get_auth_service
from src.auth.services import AuthService
from src.schemas.company import AddCompany, LoginCompany

auth_router = APIRouter(prefix="/api/v1/auth")

@auth_router.post("/")
async def register_company(
    company_data: AddCompany,
    auth_service: AuthService = Depends(get_auth_service)
):
    response = await auth_service.register_company(company_data)
    return response

@auth_router.post('/login')
async def login(
    login_details: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
):
    

    credentials = LoginCompany(
        email=login_details.username,
        password=login_details.password
    )

    return await auth_service.login(credentials)