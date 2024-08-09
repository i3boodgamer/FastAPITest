from .base import Base
from .mixins import UserRelationMixin

from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from .user import User

class Post(UserRelationMixin, Base):
    _user_back_populates = "posts"
    
    title: Mapped[str] = mapped_column(String(100), unique = True)
    body: Mapped[str] = mapped_column(
        Text,
        default = "",
        server_default = "",
    )
    
    def __str__(self):
        return f"{self.__class__.__name__} (id = {self.id}) (title = ){self.title!r}"
    
    def __repr__(self):
        return str(self)