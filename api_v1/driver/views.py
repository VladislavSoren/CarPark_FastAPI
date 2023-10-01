from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.auto.schemas import Auto
from api_v1.driver import crud
from api_v1.driver.dependencies import driver_by_id
from api_v1.driver.schemas import Driver, DriverCreate
from api_v1.route.schemas import Route
from core.models import db_helper

router = APIRouter(
    tags=["Driver"],
)


@router.post("/", response_model=Driver, status_code=status.HTTP_201_CREATED)
async def create_driver(
    driver_in: DriverCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_driver(session, driver_in)


@router.get("/", response_model=list[Driver])
async def get_drivers(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_drivers(session=session)


@router.get("/{driver_id}/", response_model=Driver)
async def get_driver(
    driver: Driver = Depends(driver_by_id),
):
    return driver


@router.get("/{driver_id}/autos/", response_model=list[Auto])
async def get_all_driver_autos(
    driver_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    _: Driver = Depends(driver_by_id),  # check if auto is exist
):
    return await crud.get_all_driver_autos(session, driver_id)


@router.get("/{driver_id}/routes/", response_model=list[Route])
async def get_all_driver_routes(
    driver_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    _: Driver = Depends(driver_by_id),  # check if auto is exist
):
    return await crud.get_all_driver_routes(session, driver_id)
