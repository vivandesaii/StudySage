from datetime import datetime

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from .db import Base


class Document(Base):
    __tablename__ = "documents"

    # Auto-incrementing integer primary key
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Required title, max 200 characters
    title: Mapped[str] = mapped_column(String(200), nullable=False)

    # Optional long text description
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Set by the database with timezone support (server-side default)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
