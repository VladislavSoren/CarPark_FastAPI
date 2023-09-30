from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.driver import crud
from api_v1.driver.dependencies import driver_by_id
from api_v1.driver.schemas import Driver, DriverCreate
from core.models import db_helper

router = APIRouter(
    tags=["Driver"],
)


@router.post("/", response_model=Driver, status_code=status.HTTP_201_CREATED)
async def create_product(
    driver_in: DriverCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_driver(session, driver_in)


@router.get("/", response_model=list[Driver])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_drivers(session=session)


@router.get("/{driver_id}/", response_model=Driver)
async def get_product(
    driver: Driver = Depends(driver_by_id),
):
    return driver
