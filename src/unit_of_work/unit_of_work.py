from sqlalchemy.ext.asyncio import AsyncSession
from src.events.bus import event_bus
from src.events.base import DomainEvent
from src.repositories.company_repo import CompanyRepository
from src.repositories.category_repo import CategoryRepository
from src.repositories.expense_repo import ExpenseRepository
from src.repositories.budget_repo import BudgetRepository


class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.event_bus = event_bus
        self._pending_event: list[DomainEvent] = []

        self.category_repo = CategoryRepository(session)
        self.expense_repo = ExpenseRepository(session)
        self.company_repo = CompanyRepository(session)
        self.budget_repo = BudgetRepository(session)
    
    async def collect_event(self, event: DomainEvent):
        self._pending_event.append(event)
    
    async def __aenter__(self):
        await self.session.begin()
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        if exc_type is not None:
            await self.session.rollback()
            self._pending_event.clear()
            await self.session.close()
        else:
            await self.session.commit()

        if self.event_bus:
            for ev in self._pending_event:
                await self.event_bus.publish_event(ev)
