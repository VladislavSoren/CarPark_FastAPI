from pydantic import BaseModel, ConfigDict


class TransportUnitBase(BaseModel):
    driver_id: int
    auto_id: int


class TransportUnitCreate(TransportUnitBase):
    pass


class TransportUnit(TransportUnitBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
