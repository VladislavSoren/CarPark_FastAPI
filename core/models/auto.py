from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base


class Auto(Base):
    brand: Mapped[str] = mapped_column(String(50), unique=False)

    park_id: Mapped[int] = mapped_column(ForeignKey("park.id"))

    # relationships
    park = relationship("Park", back_populates="auto")
