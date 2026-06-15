from typing import Type
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.base_repo import BaseRepository
from src.models.budget import Budget
from src.schemas.budget import AddBudget


class BudgetRepository(BaseRepository[Budget]):
    def __init__(self, session: AsyncSession):
        super().__init__(Budget, session)
    
    async def get_active_budgets(self, company_id: str):
        result = await self.session.execute(select(self.model)
        .where(self.model.company_id == company_id)
        .where(self.model.is_active == True))
        return result.scalars().all()
    
    async def add_budget(self, budget_data: AddBudget):
        data = budget_data.model_dump()
        budget = Budget(**data)
        new_budget = await self.create(budget)
        return new_budget
    
    
    