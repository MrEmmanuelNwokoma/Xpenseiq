from datetime import datetime, timezone, timedelta
from src.unit_of_work.unit_of_work import UnitOfWork
from src.auth.jwt import retrieve_token
from src.auth.security import hash, verify
from src.schemas.company import AddCompany, LoginCompany
from src.core.exceptions import EntityAlreadyExist, EntityNotFound, InvalidCredentialsError, InvalidResetTokenError
from src.utils.token_utils import TokenUtils


class AuthService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory
        self.token_utils= TokenUtils()

    
    async def register_company(self, company_data: AddCompany):
        async with self.uow_factory as uow:
            company = await uow.company_repo.get_by_email(company_data.email)
            if company:
                raise EntityAlreadyExist(
                    message="Company already exist",
                    details={
                        "recommendation": "Pass the correct credentials"
                    }
                )
            api_key = hash(self.token_utils.generate_key())
            company_data.password = hash(company_data.password)
            new_company = await uow.company_repo.add_company(company_data, api_key)
            verification_token = await self.token_utils.generate_company_verfication_token(new_company)
            print(verification_token)
            return new_company


    async def login(self, login_details: LoginCompany):

        """Function for login which supports email and phonenumber"""
        async with self.uow_factory:
            password = login_details.password
            company = await self.uow_factory.company_repo.get_by_email(login_details.email)
            
            if not company:
                raise EntityNotFound(
                    message="Company not found",
                    details={
                        "recommendation": "Pass the correct credentials"
                    }
                )
            if not verify(password, company.password):
                raise InvalidCredentialsError(
                    message="Invalid credentials",
                    details={
                        "recommendation": "Pass the correct password"
                    }
                )
            company.last_login = datetime.now(timezone.utc)
            access_token = retrieve_token(company)
            return{
                "access_token": access_token
            }
    
    async def request_password_reset_token(self, email):
        async with self.uow_factory as uow:
            company = await uow.company_repo.get_by_email(email)
            if not company:
                raise EntityNotFound(
                    message="User with the provided email does not exist",
                    details={
                        "recommendations": "Ensure user passes the correct email"
                    })
            token = await self.token_utils.generate_company_verfication_token(company)
            updated_data = {
                "verification_token": token,
                "verification_token_expires_at": company.verification_token_expires_at
            }
            await uow.company_repo.update(id=company.id, data=updated_data)
            return {
                "status": "success",
                "message": "Token successfully sent"
            }
    
    async def verify_token(self, token):
        async with self.uow_factory:
            company = await self.uow_factory.company_repo.verify_token(token)
            if not company:
                raise EntityNotFound(
                    message="Company not found",
                    details={
                        "recommendation": "Pass the correct token"
                    }
                )
            expiry_time = company.verification_token_expires_at
            if not expiry_time:
                raise InvalidResetTokenError(
                    message="Invalid token",
                    details={
                        "recommendation": "Pass the correct token"
                    }
                )
            if expiry_time.tzinfo is None:
                expiry_time = expiry_time.replace(tzinfo=timezone.utc)
            
            if expiry_time < datetime.now(timezone.utc):
                raise InvalidResetTokenError(
                    message="Token has expired",
                    details={
                        "recommendation": "Request a new token"
                    }
                )
            company.verification_token = None
            company.verification_token_expires_at = None
            return (company)
        
    async def change_password(self, company_id: str, new_password: str):
        company = await self.uow_factory.company_repo.get_by_id(company_id)
        if not company:
            raise EntityNotFound(
                message="Company not found",
                details={
                    "recommendation": "Pass the correct user_id"
                }
            )

        hashed_password = hash(new_password)

        await self.uow_factory.company_repo.update(company_id, data={"password": hashed_password})
        return {
            "status": "success",
            "message": "Your password has been successfully updated."
        }
