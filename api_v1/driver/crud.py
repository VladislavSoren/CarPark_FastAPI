from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.driver.schemas import DriverCreate
from core.models import Driver


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
