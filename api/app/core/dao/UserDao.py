from uuid import uuid4

from fastapi import Depends
from sqlalchemy.orm import Session

from api.app.core.dao.utils.BaseDao import BaseDao
from api.app.core.models.User import User
from api.app.core.schemas.UserSchemas import UserCreate
from api.app.core.database import get_db


class UserDao(BaseDao):
    def __init__(self, db: Session = Depends(get_db)):
        super().__init__(db, User)

    def create(self, payload: UserCreate):
        user_id = str(uuid4())
        return super().create({**payload.model_dump(), "id": user_id})
