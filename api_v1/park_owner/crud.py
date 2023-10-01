from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api_v1.park_owner.schemas import ParkOwnerCreate
from core.models import Park, ParkOwner


async def create_parkowner(session: AsyncSession, parkowner_in: ParkOwnerCreate) -> ParkOwner:
    parkowner = ParkOwner(**parkowner_in.model_dump())
    # добавляем в отслеживание сессии
    session.add(parkowner)
    await session.commit()
    # await session.refresh(product)
    return parkowner


async def get_parkowners(session: AsyncSession) -> list[ParkOwner]:
    stmt = select(ParkOwner).order_by(ParkOwner.id)
    result: Result = await session.execute(stmt)
    parkowners = result.scalars().all()
    return list(parkowners)


async def get_parkowner(session: AsyncSession, parkowner_id) -> ParkOwner | None:
    return await session.get(ParkOwner, parkowner_id)


async def get_all_owner_parks(session: AsyncSession, parkowner_id) -> list[Park]:
    stmt = select(ParkOwner).options(selectinload(ParkOwner.park)).where(ParkOwner.id == parkowner_id)
    result: Result = await session.execute(stmt)
    owner_with_parks = result.scalars().one()
    parks = owner_with_parks.park
    return list(parks)
