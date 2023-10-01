from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api_v1.park.schemas import ParkCreate
from core.models import Auto, Park


async def create_park(session: AsyncSession, park_in: ParkCreate) -> Park:
    park = Park(**park_in.model_dump())
    session.add(park)
    await session.commit()
    # await session.refresh(product)
    return park


async def get_parks(session: AsyncSession) -> list[Park]:
    stmt = select(Park).order_by(Park.id)
    result: Result = await session.execute(stmt)
    parks = result.scalars().all()
    return list(parks)


async def get_park(session: AsyncSession, park_id) -> Park | None:
    return await session.get(Park, park_id)


async def get_all_park_autos(session: AsyncSession, park_id) -> list[Auto]:
    stmt = select(Park).options(selectinload(Park.auto)).where(Park.id == park_id)
    result: Result = await session.execute(stmt)
    park_with_autos = result.scalars().one()
    autos = park_with_autos.auto
    return list(autos)
