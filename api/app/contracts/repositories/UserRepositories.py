from abc import abstractmethod
from typing import List

from fastapi import Depends
from pydantic import UUID4

from api.app.core.dao.UserDao import UserDao
from api.app.core.schemas.UserSchemas import User, UserCreate, UserUpdate


class UserRepository:
    @abstractmethod
    def get_user(self, user_id: UUID4) -> User:
        pass

    @abstractmethod
    def get_users(self) -> List[User]:
        pass

    @abstractmethod
    def create_user(self, user: UserCreate) -> User:
        pass

    @abstractmethod
    def update_user(self, user_id: int, user: UserUpdate) -> User:
        pass


class UserDatabaseRepository(UserRepository):
    def __init__(self, user_dao: UserDao = Depends(UserDao)):
        self.user_dao = user_dao

    def get_user(self, user_id: UUID4) -> User:
        return self.user_dao.get({id: user_id})

    def get_users(self) -> List[User]:
        return self.user_dao.get_all()

    def create_user(self, user: UserCreate) -> User:
        return self.user_dao.create(user)

    def update_user(self, user_id: int, user: UserUpdate) -> User:
        return self.user_dao.update(user)
