from typing import List

from fastapi import Depends

from api.app.core.routes.utils.BaseRouter import BaseRouter
from api.app.core.schemas.UrlSchemas import UrlCreate, Url
from api.app.contracts.repositories.UrlRepositories import UrlRepository, UrlDatabaseRepository


class UrlRouter(BaseRouter):
    def __init__(self, app, prefix=None, name=None):
        super().__init__(app, prefix, name)

    def register(self):
        @self.router.get("/", response_model=List[Url])
        async def read_urls(url_repository: UrlRepository = Depends(UrlDatabaseRepository)):
            return url_repository.get_urls()

        @self.router.post("/", response_model=Url)
        async def create_url(url: UrlCreate, url_repository: UrlRepository = Depends(UrlDatabaseRepository)):
            return url_repository.create_url(url)
