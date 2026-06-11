from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING
from src.models.base import Basemodel, Base
from src.models.expense import Expense


if TYPE_CHECKING:
    from src.models.company import Company


class Category(Basemodel, Base):
    __tablename__="categories"
    
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)



    company: Mapped["Company"] = relationship(back_populates="categories")
    expenses: Mapped[list["Expense"]] = relationship(back_populates="category")