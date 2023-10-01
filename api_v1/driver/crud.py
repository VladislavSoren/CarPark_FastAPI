from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api_v1.driver.schemas import DriverCreate
from core.models import Auto, Driver


async def create_driver(session: AsyncSession, driver_in: DriverCreate) -> Driver:
    driver = Driver(**driver_in.model_dump())
    session.add(driver)
    await session.commit()
    # await session.refresh(product)
    return driver


async def get_drivers(session: AsyncSession) -> list[Driver]:
    stmt = select(Driver).order_by(Driver.id)
    result: Result = await session.execute(stmt)
    drivers = result.scalars().all()
    return list(drivers)


async def get_driver(session: AsyncSession, driver_id) -> Driver | None:
    return await session.get(Driver, driver_id)


async def get_all_driver_autos(session: AsyncSession, driver_id) -> list[Auto]:
    stmt = select(Driver).options(selectinload(Driver.auto)).where(Driver.id == driver_id)
    result: Result = await session.execute(stmt)

    transport_unit_with_driver = result.scalars().one()
    transport_units_with_id_autos = transport_unit_with_driver.auto
    id_autos_list = [transport_unit.auto_id for transport_unit in transport_units_with_id_autos]

    stmt = select(Auto).where(Auto.id.in_(id_autos_list))
    result: Result = await session.execute(stmt)
    autos = result.scalars().all()

    return list(autos)
