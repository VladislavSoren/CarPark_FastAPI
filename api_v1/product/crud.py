from sqlalchemy import select, update
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.product.schemas import ProductCreate, ProductUpdate, ProductUpdatePartial
from core.models import Product


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    # scalars нужно чтобы из картежа (Product) получить Product
    # если select(Product, Product.id) -> Gen -> (Product, Product.id)
    # .all() -> Gen ->  [P1, P2 ...]
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(**product_in.model_dump())
    # добавляем в отслеживание сессии
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product


async def update_product(
    session: AsyncSession,
    product_in: ProductUpdate | ProductUpdatePartial,
    partial: bool = False,
) -> Product | None:
    stmt = update(Product).where(Product.id == product_in.id).values(**product_in.model_dump(exclude_unset=partial))
    await session.execute(stmt)
    await session.commit()

    product = await session.get(Product, product_in.id)
    return product
