from pydantic import BaseModel, ConfigDict


class RouteBase(BaseModel):
    name: str
    start_point: str
    end_point: str


class RouteCreate(RouteBase):
    pass


class RouteUpdate(RouteBase):
    pass


class Route(RouteBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
