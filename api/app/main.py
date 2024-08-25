from typing import Union

from fastapi import FastAPI

from api.app.core import database
from api.app.core.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


# Define a dependency to obtain a database session
def get_db():
    db = database.connect()
    try:
        yield db
    finally:
        db.disconnect()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}