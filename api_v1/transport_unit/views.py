from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.transport_unit import crud
from api_v1.transport_unit.dependencies import transport_unit_by_id
from api_v1.transport_unit.schemas import TransportUnit, TransportUnitCreate
from core.models import db_helper

router = APIRouter(
    tags=["TransportUnit"],
)


@router.post("/", response_model=TransportUnit, status_code=status.HTTP_201_CREATED)
async def create_product(
    transport_unit_in: TransportUnitCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_transport_unit(session, transport_unit_in)


@router.get("/", response_model=list[TransportUnit])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_transport_units(session=session)


@router.get("/{transport_unit_id}/", response_model=TransportUnit)
async def get_product(
    transport_unit: TransportUnit = Depends(transport_unit_by_id),
):
    return transport_unit
