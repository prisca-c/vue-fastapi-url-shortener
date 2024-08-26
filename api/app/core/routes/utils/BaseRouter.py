from fastapi import FastAPI, APIRouter


class BaseRouter:

    def __init__(self, app: FastAPI, prefix: str = None, name: str = None):
        self.router = APIRouter()
        self.app = app
        self.prefix = prefix
        self.name = name
        self.register()
        self.app.include_router(self.router,
                                prefix=self.prefix,
                                tags=[self.name])

    def register(self):
        raise NotImplementedError("register method must be implemented")
