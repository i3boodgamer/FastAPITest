from .base import Base

from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column


class Order(Base):
    promocode: Mapped[int]
    create_at: Mapped[datetime] = mapped_column(
        server_default = func.now(),
        default = datetime.now,
    )
    