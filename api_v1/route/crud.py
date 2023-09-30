from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.route.schemas import RouteCreate
from core.models import Route


async def create_route(session: AsyncSession, route_in: RouteCreate) -> Route:
    route = Route(**route_in.model_dump())
    session.add(route)
    await session.commit()
    # await session.refresh(product)
    return route


async def get_routes(session: AsyncSession) -> list[Route]:
    stmt = select(Route).order_by(Route.id)
    result: Result = await session.execute(stmt)
    routes = result.scalars().all()
    return list(routes)


async def get_route(session: AsyncSession, route_id) -> Route | None:
    return await session.get(Route, route_id)
