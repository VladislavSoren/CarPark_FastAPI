from sqlalchemy import select
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
    product_update: ProductUpdate | ProductUpdatePartial,
    product: Product,
    session: AsyncSession,
    partial: bool = False,
) -> Product | None:
    # обновляем атрибуты
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()

    return product


async def delete_product(
    product: Product,
    session: AsyncSession,
) -> None:
    await session.delete(product)
    await session.commit()
