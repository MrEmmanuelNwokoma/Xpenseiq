from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING
from uuid import uuid4
from datetime import datetime, timezone
from sqlalchemy import DateTime
from src.models.base import Base, Basemodel


if TYPE_CHECKING:
    from src.models.category import Category
    
    from src.models.expense import Expense




class Company(Basemodel, Base):
    __tablename__="companies"

    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    api_key: Mapped[str] = mapped_column(nullable=True)
    last_login: Mapped[str] = mapped_column(nullable=True)
    is_email_verified: Mapped[bool] = mapped_column(nullable=True)
    verification_token: Mapped[str] = mapped_column(nullable=True)
    verification_token_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)


    categories: Mapped[list["Category"]] = relationship(back_populates="company")

    expenses: Mapped[list["Expense"]] = relationship(back_populates="company", cascade="all, delete-orphan")
    
