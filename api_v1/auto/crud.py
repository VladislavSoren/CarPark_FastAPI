from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api_v1.auto.schemas import AutoCreate
from core.models import Auto, Driver


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


async def get_all_auto_drivers(session: AsyncSession, auto_id) -> list[Driver]:
    stmt = select(Auto).options(selectinload(Auto.driver)).where(Auto.id == auto_id)
    result: Result = await session.execute(stmt)

    transport_unit_with_auto = result.scalars().one()
    transport_units_with_id_drivers = transport_unit_with_auto.driver
    id_drivers_list = [transport_unit.driver_id for transport_unit in transport_units_with_id_drivers]

    stmt = select(Driver).where(Driver.id.in_(id_drivers_list))
    result: Result = await session.execute(stmt)
    drivers = result.scalars().all()

    return list(drivers)
