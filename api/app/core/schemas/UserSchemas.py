from pydantic import BaseModel, UUID4


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID4

    class Config:
        orm_mod = True
