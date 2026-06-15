from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime
from typing import TYPE_CHECKING
from datetime import datetime, timezone
from decimal import Decimal
from src.models.base import Basemodel, Base
from src.models.company import Company



if TYPE_CHECKING:
    from src.models.category import Category

class Expense(Basemodel, Base):
    __tablename__="expenses"

    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"), nullable=False)
    # employee_ref: Mapped[str] = mapped_column(nullable=True)
    # employee_name: Mapped[str] = mapped_column(nullable=False)
    department: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    amount: Mapped[Decimal] = mapped_column(nullable=False)
    



    company: Mapped["Company"] = relationship(back_populates="expenses")
    
    category: Mapped["Category"] = relationship(back_populates="expenses")
