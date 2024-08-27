from abc import abstractmethod
from typing import List

from fastapi import Depends

from api.app.core.dao.UrlDao import UrlDao
from api.app.core.schemas.UrlSchemas import Url, UrlCreate


class UrlRepository:
    @abstractmethod
    def get_url(self, url_id: int) -> Url:
        pass

    @abstractmethod
    def get_urls(self) -> List[Url]:
        pass

    @abstractmethod
    def create_url(self, url: UrlCreate) -> Url:
        pass


class UrlDatabaseRepository(UrlRepository):
    def __init__(self, url_dao: UrlDao = Depends(UrlDao)):
        self.url_dao = url_dao

    def get_url(self, url_id: int) -> Url:
        return self.url_dao.get({id: url_id})

    def get_urls(self) -> List[Url]:
        return self.url_dao.get_all()

    def create_url(self, url: UrlCreate) -> Url:
        return self.url_dao.create(url)
