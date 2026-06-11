from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.base_repo import BaseRepository
from src.models.category import Category
from src.schemas.category import AddCategory



class CategoryRepository(BaseRepository[Category]):
    def __init__(self, session: AsyncSession):
        super().__init__(Category, session)
    
    async def add_category(self, category_data: AddCategory):
        data = category_data.model_dump()
        category = Category(**data)
        new_category = await self.create(category)
        return new_category
        