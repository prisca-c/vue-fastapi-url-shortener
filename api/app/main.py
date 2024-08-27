from fastapi import FastAPI

import api.app.core.models
from api.app.core.routes.UrlRouter import UrlRouter
from api.app.core.routes.UserRouter import UserRouter


class AppFactory:
    def __init__(self):
        self.app = FastAPI()

    def run(self):
        self.register_routes()
        return self.app

    def register_routes(self):
        UserRouter(self.app, prefix="/users", name="users")
        UrlRouter(self.app, prefix="/urls", name="urls")

