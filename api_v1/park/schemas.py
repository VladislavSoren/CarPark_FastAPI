from pydantic import BaseModel, ConfigDict


class ParkBase(BaseModel):
    name: str
    parkowner_id: int


class ParkCreate(ParkBase):
    pass


class Park(ParkBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
