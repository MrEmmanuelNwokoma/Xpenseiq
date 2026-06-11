from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.base_repo import BaseRepository
from src.models.company import Company
from src.schemas.company import AddCompany



class CompanyRepository(BaseRepository[Company]):
    def __init__(self, session: AsyncSession):
        super().__init__(Company, session)
    
    async def add_company(self, company_data: AddCompany, api_key):
        data = company_data.model_dump()
        company = Company(
            **data,
            api_key=api_key
        )
        new_company = await self.create(company)
        return new_company
        