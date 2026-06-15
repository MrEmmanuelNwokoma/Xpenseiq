from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from src.repositories.base_repo import BaseRepository
from src.models.expense import Expense
from src.schemas.expense import LogExpenseSchema
from src.models.budget import Budget

class ExpenseRepository(BaseRepository[Expense]):
    def __init__(self, session: AsyncSession):
        super().__init__(Expense, session)
    
    async def log_expense(self, expense_data: LogExpenseSchema):
        data = expense_data.model_dump()
        expense = Expense(**data)
        new_expense = await self.create(expense)
        return new_expense
    
    async def get_expenses_by_period(self, company_id: str, budget: Budget):
        result = await self.session.execute(
            select(func.sum(Expense.amount))
            .where(self.model.company_id == company_id)
            .where(Expense.created_at >= budget.start_time)
            .where(Expense.created_at <= budget.end_time)
        )
        return result.scalar_one_or_none() or 0
    