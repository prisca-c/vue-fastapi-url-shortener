from pydantic import BaseModel
from pydantic.v1 import UUID4


class UrlBase(BaseModel):
    url: str
    short_url: str
    created_by: str


class UrlCreate(UrlBase):
    pass


class Url(UrlBase):
    id: UUID4
    created_at: str
    updated_at: str
    clicks: int
    is_deleted: bool
    deleted_at: str
    deleted_by: str

    class Config:
        orm_mod = True
