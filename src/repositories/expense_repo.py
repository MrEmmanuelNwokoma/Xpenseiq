from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.base_repo import BaseRepository
from src.models.expense import Expense
from src.schemas.expense import AddExpense

class ExpenseRepository(BaseRepository[Expense]):
    def __init__(self, session: AsyncSession):
        super().__init__(Expense, session)
    
    async def log_expense(self, expense_data: AddExpense):
        data = expense_data.model_dump()
        expense = Expense(**data)
        new_expense = await self.create(expense)
        return new_expense
    