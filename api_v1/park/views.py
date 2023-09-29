from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.park import crud
from api_v1.park.dependencies import park_by_id
from api_v1.park.schemas import Park, ParkCreate
from core.models import db_helper

router = APIRouter(
    tags=["Park"],
)


@router.post("/", response_model=Park, status_code=status.HTTP_201_CREATED)
async def create_product(
    parkowner_in: ParkCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_park(session, parkowner_in)


@router.get("/", response_model=list[Park])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_parks(session=session)


@router.get("/{park_id}/", response_model=Park)
async def get_product(
    park: Park = Depends(park_by_id),
):
    return park
