from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import api.app.core.models
from api.app.core.config import Config
from api.app.core.routes.UrlRouter import UrlRouter
from api.app.core.routes.UserRouter import UserRouter


class AppFactory:
    def __init__(self):
        self.app = FastAPI()

    def run(self):
        self.register_routes()

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=Config.CORS_ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=Config.HEADERS,
        )

        return self.app

    def register_routes(self):
        UserRouter(self.app, prefix="/users", name="users")
        UrlRouter(self.app, prefix="/urls", name="urls")

