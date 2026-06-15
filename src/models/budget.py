from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime
from decimal import Decimal
from datetime import datetime, timezone
from typing import TYPE_CHECKING
from src.models.base import Basemodel, Base

if TYPE_CHECKING:
    from src.models.company import Company


class Budget(Basemodel, Base):
    __tablename__="budgets"
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone.utc), nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone.utc), nullable=False)
    amount: Mapped[Decimal] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)


    company: Mapped["Company"] = relationship(back_populates="budgets")
    