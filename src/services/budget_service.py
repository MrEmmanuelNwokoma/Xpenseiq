from src.unit_of_work.unit_of_work import UnitOfWork
from src.schemas.budget import AddBudget


class BudgetService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory
    
    async def add_budget(self, budget_data: AddBudget):
        async with self.uow_factory as uow:
            new_budget = await uow.budget_repo.add_budget(budget_data)
            return new_budget