from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime
from typing import TYPE_CHECKING
from datetime import datetime, timezone
from src.models.base import Basemodel, Base
from src.models.company import Company



if TYPE_CHECKING:
    from src.models.category import Category

class Expense(Basemodel, Base):
    __tablename__="expenses"

    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"), nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    amount: Mapped[str] = mapped_column(nullable=False)
    verified_at: Mapped[datetime] = mapped_column(DateTime(timezone), nullable=True)



    company: Mapped["Company"] = relationship(back_populates="expenses")
    
    category: Mapped["Category"] = relationship(back_populates="expenses")
