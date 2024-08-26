from api.app.core.routes.utils.BaseRouter import BaseRouter


class UserRouter(BaseRouter):
    def __init__(self, app, prefix=None, name=None):
        super().__init__(app, prefix, name)

    def register(self):
        @self.router.get("/")
        async def read_users():
            return [{"username": "Rick"}, {"username": "Morty"}]
