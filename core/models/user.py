from .base import Base

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    name: Mapped[str] = mapped_column(String(32), unique = True)