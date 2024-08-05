from .base import Base

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Post(Base):
    title: Mapped[str] = mapped_column(String(100), unique = True)
    body: Mapped[str] = mapped_column(
        Text,
        default = "",
        server_default = "",
    )
    
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
    )