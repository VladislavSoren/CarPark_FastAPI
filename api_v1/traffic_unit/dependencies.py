from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import TrafficUnit, db_helper

from . import crud


async def traffic_unit_by_id(
    traffic_unit_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> TrafficUnit:
    traffic_unit = await crud.get_traffic_unit(session=session, traffic_unit_id=traffic_unit_id)
    if traffic_unit is not None:
        return traffic_unit

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"TrafficUnit {traffic_unit_id} not found!",
    )
