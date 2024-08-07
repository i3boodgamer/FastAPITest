from .base import Base
from .mixins import UserRelationMixin

from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship



class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = "profile"
    
    first_name: Mapped[str | None] = mapped_column(String(50))
    last_name: Mapped[str | None] = mapped_column(String(50))
    bio: Mapped[str | None] = mapped_column(String(50))