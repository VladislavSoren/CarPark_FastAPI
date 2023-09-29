from pydantic import BaseModel, ConfigDict


class ParkOwnerBase(BaseModel):
    name: str


class ParkOwnerCreate(ParkOwnerBase):
    pass


class ParkOwner(ParkOwnerBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
