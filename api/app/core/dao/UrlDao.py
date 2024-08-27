from uuid import uuid4

from fastapi import Depends
from sqlalchemy.orm import Session

from api.app.core.dao.utils.BaseDao import BaseDao
from api.app.core.models.Url import Url
from api.app.core.schemas.UrlSchemas import UrlCreate
from api.app.core.database import get_db


class UrlDao(BaseDao):
    def __init__(self, db: Session = Depends(get_db)):
        super().__init__(db, Url)

    def create(self, payload: UrlCreate):
        url_id = str(uuid4())
        return super().create({**payload.model_dump(), "id": url_id})
