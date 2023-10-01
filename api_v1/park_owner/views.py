from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.park.schemas import Park
from api_v1.park_owner import crud
from api_v1.park_owner.dependencies import parkowner_by_id
from api_v1.park_owner.schemas import ParkOwner, ParkOwnerCreate
from core.models import db_helper

router = APIRouter(
    tags=["ParkOwner"],
)


@router.post("/", response_model=ParkOwner, status_code=status.HTTP_201_CREATED)
async def create_parkowner(
    parkowner_in: ParkOwnerCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_parkowner(session, parkowner_in)


@router.get("/", response_model=list[ParkOwner])
async def get_parkowners(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_parkowners(session=session)


@router.get("/{parkowner_id}/", response_model=ParkOwner)
async def get_parkowner(
    parkowner: ParkOwner = Depends(parkowner_by_id),
):
    return parkowner


@router.get("/{parkowner_id}/parks/", response_model=list[Park])
async def get_all_owner_parks(
    parkowner_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    _: Park = Depends(parkowner_by_id),  # check if park is exist
):
    return await crud.get_all_owner_parks(session, parkowner_id)
