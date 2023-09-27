from fastapi import status

from user.schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:
    user_dict = user_in.model_dump()
    return {
        "status_code": status.HTTP_201_CREATED,
        "user": user_dict,
    }
