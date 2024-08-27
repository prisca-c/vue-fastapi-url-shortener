from typing import List

from fastapi import Depends

from api.app.core.dao.UserDao import UserDao
from api.app.core.routes.utils.BaseRouter import BaseRouter
from api.app.core.schemas.UserSchemas import UserCreate, User
from api.app.contracts.repositories.UserRepositories import UserRepository, UserDatabaseRepository


class UserRouter(BaseRouter):
    def __init__(self, app, prefix=None, name=None):
        super().__init__(app, prefix, name)

    def register(self):
        @self.router.get("/", response_model=List[User])
        async def read_users(user_repository: UserRepository = Depends(UserDatabaseRepository)):
            return user_repository.get_users()

        @self.router.post("/", response_model=User)
        async def create_user(user: UserCreate, user_repository: UserRepository = Depends(UserDatabaseRepository)):
            return user_repository.create_user(user)
