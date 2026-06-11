from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from uuid import uuid4
from datetime import datetime, timezone
from sqlalchemy import DateTime


class Base(DeclarativeBase):
    pass


class Basemodel:
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda : str(uuid4()), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone), nullable=False, default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone), nullable=True)
    

