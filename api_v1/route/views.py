from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.route import crud
from api_v1.route.dependencies import route_by_id
from api_v1.route.schemas import Route, RouteCreate
from core.models import db_helper

router = APIRouter(
    tags=["Route"],
)


@router.post("/", response_model=Route, status_code=status.HTTP_201_CREATED)
async def create_product(
    route_in: RouteCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_route(session, route_in)


@router.get("/", response_model=list[Route])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_routes(session=session)


@router.get("/{route_id}/", response_model=Route)
async def get_product(
    route: Route = Depends(route_by_id),
):
    return route
