import uuid

from sqlalchemy import UUID, BigInteger, Column, Text, UniqueConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import DateTime

Base = declarative_base()

###########
# Схема БД
###########


class UsersVladimir(Base):
    __tablename__ = "users_vladimir"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    user_id = Column(
        BigInteger,
        primary_key=True,
        nullable=False,
    )
    first_name = Column(Text, nullable=True)
    username = Column(Text, nullable=True)
    chat_id = Column(
        BigInteger,
        nullable=False,
    )
    reg_time = Column(DateTime, nullable=True)
    town = Column(Text, nullable=False)
    platform = Column(Text, nullable=False)

    __table_args__ = (UniqueConstraint("user_id", "username", name=f"Uniq_{__tablename__}"),)
