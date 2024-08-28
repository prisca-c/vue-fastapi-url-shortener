from pydantic import BaseModel
from pydantic import UUID4


class UrlBase(BaseModel):
    url: str
    short_url: str
    created_by: str


class UrlCreate(UrlBase):
    pass


class Url(UrlBase):
    id: UUID4
    clicks: int
    is_deleted: bool

    class Config:
        orm_mod = True
