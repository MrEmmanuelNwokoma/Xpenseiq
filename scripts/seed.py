from src.storage import db
import asyncio

from scripts.data import CATEGORIES
from src.repositories.category_repo import CategoryRepository
from src.models.category import Category


async def seed_data():
    await db.drop_tables()
    await db.create_tables()

    async with db.get_session() as session:
        category_repo = CategoryRepository(session)
        
        categories = []
        for category in CATEGORIES:

            categories.append(Category(**category))

        await category_repo.bulk_create(categories)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(seed_data())