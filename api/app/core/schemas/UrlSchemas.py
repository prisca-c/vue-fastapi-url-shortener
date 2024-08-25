from pydantic import BaseModel


class UrlBase(BaseModel):
    url: str
    short_url: str
    user_id: str


class UrlCreate(UrlBase):
    pass


class Url(UrlBase):
    id: str
    created_at: str
    updated_at: str
    clicks: int
    is_active: bool
    is_deleted: bool
    deleted_at: str
    deleted_by: str
    updated_by: str
    created_by: str

    class Config:
        orm_mod = True
