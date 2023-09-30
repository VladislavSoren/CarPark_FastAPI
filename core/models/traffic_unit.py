from typing import List

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.transport_unit import TransportUnit


class TrafficUnit(Base):
    # fields
    transport_unit_id: Mapped[int] = mapped_column(ForeignKey("transportunit.id"))
    route_id: Mapped[int] = mapped_column(ForeignKey("route.id"))

    # additional properties
    __table_args__ = (UniqueConstraint("transport_unit_id", "route_id", name="unique_traffic_unit"),)

    # relationships
    transport_unit: Mapped["TransportUnit"] = relationship(back_populates="route")
    route: Mapped["Route"] = relationship(back_populates="transport_unit")


class Route(Base):
    name: Mapped[str] = mapped_column(String(100), unique=False)
    start_point: Mapped[str] = mapped_column(String(50), unique=False)
    end_point: Mapped[str] = mapped_column(String(50), unique=False)

    # relationships
    transport_unit: Mapped[List["TrafficUnit"]] = relationship(back_populates="route")
