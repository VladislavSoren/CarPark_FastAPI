from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter(prefix="/item", tags=["item"])


@router.get("/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@router.get("/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(gt=0, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id,
        },
    }