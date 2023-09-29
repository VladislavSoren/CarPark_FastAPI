from fastapi import APIRouter

from .park.views import router as park_router
from .park_owner.views import router as parkowner_router
from .product.views import router as product_router

router = APIRouter()
router.include_router(router=product_router, prefix="/product")
router.include_router(router=parkowner_router, prefix="/park_owner")
router.include_router(router=park_router, prefix="/park")
