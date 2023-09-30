from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.traffic_unit.schemas import TrafficUnitCreate
from core.models import TrafficUnit


async def create_traffic_unit(session: AsyncSession, traffic_unit_in: TrafficUnitCreate) -> TrafficUnit:
    traffic_unit = TrafficUnit(**traffic_unit_in.model_dump())
    session.add(traffic_unit)
    await session.commit()
    # await session.refresh(product)
    return traffic_unit


async def get_traffic_units(session: AsyncSession) -> list[TrafficUnit]:
    stmt = select(TrafficUnit).order_by(TrafficUnit.id)
    result: Result = await session.execute(stmt)
    traffic_units = result.scalars().all()
    return list(traffic_units)


async def get_traffic_unit(session: AsyncSession, traffic_unit_id) -> TrafficUnit | None:
    return await session.get(TrafficUnit, traffic_unit_id)
