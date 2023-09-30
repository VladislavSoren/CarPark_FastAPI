from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.traffic_unit import crud
from api_v1.traffic_unit.dependencies import traffic_unit_by_id
from api_v1.traffic_unit.schemas import TrafficUnit, TrafficUnitCreate
from core.models import db_helper

router = APIRouter(
    tags=["TrafficUnit"],
)


@router.post("/", response_model=TrafficUnit, status_code=status.HTTP_201_CREATED)
async def create_product(
    traffic_unit_in: TrafficUnitCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_traffic_unit(session, traffic_unit_in)


@router.get("/", response_model=list[TrafficUnit])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_traffic_units(session=session)


@router.get("/{traffic_unit_id}/", response_model=TrafficUnit)
async def get_product(
    traffic_unit: TrafficUnit = Depends(traffic_unit_by_id),
):
    return traffic_unit
