from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.transport_unit.schemas import TransportUnitCreate
from core.models import TransportUnit


async def create_transport_unit(session: AsyncSession, transport_unit_in: TransportUnitCreate) -> TransportUnit:
    transport_unit = TransportUnit(**transport_unit_in.model_dump())
    session.add(transport_unit)
    await session.commit()
    # await session.refresh(product)
    return transport_unit


async def get_transport_units(session: AsyncSession) -> list[TransportUnit]:
    stmt = select(TransportUnit).order_by(TransportUnit.id)
    result: Result = await session.execute(stmt)
    transport_units = result.scalars().all()
    return list(transport_units)


async def get_transport_unit(session: AsyncSession, transport_unit_id) -> TransportUnit | None:
    return await session.get(TransportUnit, transport_unit_id)
