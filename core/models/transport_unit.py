from typing import List

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.park import Park


class TransportUnit(Base):
    # fields
    driver_id: Mapped[int] = mapped_column(ForeignKey("driver.id"), primary_key=True)
    auto_id: Mapped[int] = mapped_column(ForeignKey("auto.id"), primary_key=True)

    # relationships
    driver: Mapped["Driver"] = relationship(back_populates="auto")
    auto: Mapped["Auto"] = relationship(back_populates="driver")

    # additional properties
    __table_args__ = (UniqueConstraint("driver_id", "auto_id", name="unique_transport_unit"),)


class Driver(Base):
    name: Mapped[str] = mapped_column(String(50), unique=False)

    # relationships
    auto: Mapped[List["TransportUnit"]] = relationship(back_populates="driver")


class Auto(Base):
    # fields
    brand: Mapped[str] = mapped_column(String(50), unique=False)
    park_id: Mapped[int] = mapped_column(ForeignKey("park.id"))  # Mto1

    # relationships
    park: Mapped["Park"] = relationship(back_populates="auto")
    driver: Mapped[List["TransportUnit"]] = relationship(back_populates="auto")
