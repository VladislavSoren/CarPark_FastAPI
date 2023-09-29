from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class Park(Base):
    name: Mapped[str] = mapped_column(String(100), unique=False)

    parkowner_id: Mapped[int] = mapped_column(ForeignKey("parkowner.id"))
