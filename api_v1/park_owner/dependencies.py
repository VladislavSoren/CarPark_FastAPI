from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import ParkOwner, db_helper

from . import crud


async def parkowner_by_id(
    parkowner_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> ParkOwner:
    parkowner = await crud.get_parkowner(session=session, parkowner_id=parkowner_id)
    if parkowner is not None:
        return parkowner

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"ParkOwner {parkowner_id} not found!",
    )
