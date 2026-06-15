from src.unit_of_work.unit_of_work import UnitOfWork
from src.models.company import Company
from src.schemas.company import AddCompany, UpdateCompany
from src.core.exceptions import EntityNotFound


class CompanyService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory
    
    async def update_user(self, company_data: UpdateCompany, company_id: str):
        data = company_data.model_dump()
        async with self.uow_factory:
            company = await self.uow_factory.company_repo.get_by_id(company_id)
            if not company:
                raise EntityNotFound(
                    message="User not found",
                    details={
                        "recommendation": "Make sure you pass the correct user id"
                    }
                )
            await self.uow_factory.company_repo.update(company_id, data)
            return company_data
