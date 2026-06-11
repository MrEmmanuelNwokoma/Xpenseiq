from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.company_repo import CompanyRepository
from src.repositories.category_repo import CategoryRepository
from src.repositories.expense_repo import ExpenseRepository


class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session

        self.category_repo = CategoryRepository(session)
        self.expense_repo = ExpenseRepository(session)
        self.company_repo = CompanyRepository(session)
    
    async def __aenter__(self):
        await self.session.begin()
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        if exc_type is not None:
            await self.session.rollback()
            # self._pending_event.clear()
            await self.session.close()
        else:
            await self.session.commit()
