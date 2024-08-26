from fastapi import Depends

from api.app.core.dao.UserDao import UserDao
from api.app.core.routes.utils.BaseRouter import BaseRouter
from api.app.core.schemas.UserSchemas import UserCreate, User


class UserRouter(BaseRouter):
    def __init__(self, app, prefix=None, name=None):
        super().__init__(app, prefix, name)

    def register(self):
        @self.router.get("/")
        async def read_users():
            return [{"username": "Rick"}, {"username": "Morty"}]

        @self.router.post("/", response_model=User)
        async def create_user(user: UserCreate, user_dao: UserDao = Depends(UserDao)):
            return user_dao.create(user)
