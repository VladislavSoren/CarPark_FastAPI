from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import TransportUnit, db_helper

from . import crud


async def transport_unit_by_id(
    transport_unit_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> TransportUnit:
    transport_unit = await crud.get_transport_unit(session=session, transport_unit_id=transport_unit_id)
    if transport_unit is not None:
        return transport_unit

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Transport unit {transport_unit_id} not found!",
    )
