from .base import Base

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from .post import Post
    from .profile import Profile


class User(Base):
    name: Mapped[str] = mapped_column(String(32), unique = True)
    
    posts: Mapped[list["Post"]] = relationship(back_populates = "user")
    profile: Mapped["Profile"] = relationship(back_populates = "user")