from fastapi import APIRouter

from user import crud
from user.schemas import CreateUser

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user)
