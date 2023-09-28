from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.product import crud
from api_v1.product.schemas import (
    Product,
    ProductCreate,
    ProductUpdate,
    ProductUpdatePartial,
)
from core.models.db_helper import db_helper

router = APIRouter(
    tags=["Product"],
)


@router.get("/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    # нам в автомате возвращаются объекты SQLAlchemy, но нам нужны pydantic (model_config в schemas)
    return await crud.get_products(session=session)


@router.get("/{product_id}/", response_model=Product)
async def get_product(
    product_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    product = await crud.get_product(session=session, product_id=product_id)
    if product is not None:
        return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product {product_id} not found!")


@router.post("/", response_model=Product)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_product(session, product_in)


@router.put("/update/", response_model=Product)
async def update_product(
    product_in: ProductUpdate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_product(session, product_in)


@router.patch("/update_part/", response_model=Product)
async def update_product_partial(
    product_in: ProductUpdatePartial,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_product(session, product_in, partial=True)
