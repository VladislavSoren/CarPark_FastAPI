from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Route, db_helper

from . import crud


async def route_by_id(
    route_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Route:
    route = await crud.get_route(session=session, route_id=route_id)
    if route is not None:
        return route

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Route {route_id} not found!",
    )
