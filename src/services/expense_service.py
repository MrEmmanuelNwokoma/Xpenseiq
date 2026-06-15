from sqlalchemy.ext.asyncio import AsyncSession
from src.unit_of_work.unit_of_work import UnitOfWork
from src.schemas.expense import LogExpenseSchema



class ExpenseService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    async def log_expense(self, expense_data: LogExpenseSchema):
        async with self.uow_factory as uow:
            expense = await uow.expense_repo.log_expense(expense_data)
            active_budgets = await uow.budget_repo.get_active_budgets(expense_data.company_id)
            print(active_budgets)
            for budget in active_budgets:
                print(budget)
                company_periodic_expense = await uow.expense_repo.get_expenses_by_period(expense_data.company_id, budget)
                percentage = (company_periodic_expense/budget.amount) * 100
                print(percentage)
                if percentage >= 100:
                    print("Budget exceeded")
                elif percentage >= 90:
                    print("Budget has reached 90%")
                elif percentage >= 70:
                    print("Budget has reached 70%")
                elif percentage >= 50:
                    print("Budget has reached 50%")
            return expense
