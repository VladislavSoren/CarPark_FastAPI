from pydantic import BaseModel, ConfigDict


class TrafficUnitBase(BaseModel):
    transport_unit_id: int
    route_id: int


class TrafficUnitCreate(TrafficUnitBase):
    pass


class TrafficUnit(TrafficUnitBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
