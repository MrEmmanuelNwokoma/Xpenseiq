from src.unit_of_work.unit_of_work import UnitOfWork
from src.schemas.category import AddCategory


class CategoryService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory

    async def add_category(self, category_data: AddCategory):
        async with self.uow_factory as uow:
            new_category = await uow.category_repo.add_category(category_data)
            return new_category
    
    