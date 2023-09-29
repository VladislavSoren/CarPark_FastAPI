from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Park, db_helper

from . import crud


async def park_by_id(
    park_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Park:
    park = await crud.get_park(session=session, park_id=park_id)
    if park is not None:
        return park

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Park {park_id} not found!",
    )
