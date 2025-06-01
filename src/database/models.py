from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, Integer
from datetime import date


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(50), index=True)
    last_name: Mapped[str] = mapped_column(String(50), index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    phone_number: Mapped[str] = mapped_column(String(20))
    birthday: Mapped[date]
    additional_info: Mapped[str | None] = mapped_column(String(255), nullable=True)
