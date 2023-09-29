from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class ParkOwner(Base):
    name: Mapped[str] = mapped_column(String(100), unique=False)

    # user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
