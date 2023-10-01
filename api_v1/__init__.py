from fastapi import APIRouter

from .park.views import router as park_router
from .park_owner.views import router as parkowner_router
from .product.views import router as product_router
from .auto.views import router as auto_router
from .driver.views import router as driver_router
from .transport_unit.views import router as transport_unit_router
from .route.views import router as route_router
from .traffic_unit.views import router as traffic_unit_router

router = APIRouter()
router.include_router(router=parkowner_router, prefix="/park_owner")
router.include_router(router=park_router, prefix="/park")
router.include_router(router=auto_router, prefix="/auto")
router.include_router(router=driver_router, prefix="/driver")
router.include_router(router=transport_unit_router, prefix="/transport-unit")
router.include_router(router=route_router, prefix="/route")
router.include_router(router=traffic_unit_router, prefix="/traffic-unit")
router.include_router(router=product_router, prefix="/product")
