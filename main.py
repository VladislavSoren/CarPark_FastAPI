from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api_v1 import router as router_v1
from core.config import settings
from core.models import Base
from core.models.db_helper import db_helper
from item_views import router as item_router
from user.views import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(item_router)
app.include_router(user_router)


@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
