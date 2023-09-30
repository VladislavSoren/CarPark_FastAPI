from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.auto.schemas import AutoCreate
from core.models import Auto


async def create_auto(session: AsyncSession, auto_in: AutoCreate) -> Auto:
    auto = Auto(**auto_in.model_dump())
    session.add(auto)
    await session.commit()
    # await session.refresh(product)
    return auto


async def get_autos(session: AsyncSession) -> list[Auto]:
    stmt = select(Auto).order_by(Auto.id)
    result: Result = await session.execute(stmt)
    autos = result.scalars().all()
    return list(autos)


async def get_auto(session: AsyncSession, auto_id) -> Auto | None:
    return await session.get(Auto, auto_id)
