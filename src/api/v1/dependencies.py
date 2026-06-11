from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from src.unit_of_work.unit_of_work import UnitOfWork
from src.storage import db
from src.auth.jwt import decode_access_token
from src.schemas.company import CompanyProfile
from src.auth.services import AuthService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

async def get_session()->AsyncGenerator[AsyncSession, None]:
    async with db.get_session() as session:
        yield session

def get_uow(session: AsyncSession = Depends(get_session)):
    return UnitOfWork(session)

def get_auth_service(uow: UnitOfWork = Depends(get_uow)):
    return AuthService(uow)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    uow: UnitOfWork = Depends(get_uow)
)-> CompanyProfile:
    credential_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate token",
        headers={
            "WWW-Authenticate": "Bearer"
        }
    )
    payload = decode_access_token(token, credential_exceptions)
    company_id = payload.get("sub")
    if company_id is None:
        raise credential_exceptions
    async with uow:
        company = await uow.company_repo.get_by_id(company_id)
    if not company:
        raise credential_exceptions
    return CompanyProfile.model_validate(company)