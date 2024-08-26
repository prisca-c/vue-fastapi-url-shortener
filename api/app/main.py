from fastapi import FastAPI, Depends, APIRouter

import api.app.core.models
from api.app.core.routes.UserRouter import UserRouter


class AppFactory:
    def __init__(self):
        self.app = FastAPI()

    def run(self):
        self.register_routes()
        return self.app

    def register_routes(self):
        UserRouter(self.app, prefix="/users", name="users")

