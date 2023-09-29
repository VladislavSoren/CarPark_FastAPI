from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.park_owner import crud
from api_v1.park_owner.dependencies import parkowner_by_id
from api_v1.park_owner.schemas import ParkOwner, ParkOwnerCreate
from core.models import db_helper

router = APIRouter(
    tags=["ParkOwner"],
)


@router.post("/", response_model=ParkOwner, status_code=status.HTTP_201_CREATED)
async def create_product(
    parkowner_in: ParkOwnerCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_parkowner(session, parkowner_in)


@router.get("/", response_model=list[ParkOwner])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_parkowners(session=session)


@router.get("/{parkowner_id}/", response_model=ParkOwner)
async def get_product(
    product: ParkOwner = Depends(parkowner_by_id),
):
    return product
