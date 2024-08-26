from fastapi import Depends
from sqlalchemy.orm import Session

from api.app.core.database import get_db


class BaseDao:

    def __init__(self, session, model):
        self.session = session
        self.model = model

    def get(self, entity_identifier):
        return self.session.query(self.model).get(entity_identifier)

    def get_all(self):
        return self.session.query(self.model).all()

    def create(self, payload):
        entity = self.model(**payload)
        self.session.add(entity)
        self.session.commit()
        return entity

    def update(self, payload):
        entity = self.get(payload['id'])
        for key, value in payload.items():
            setattr(entity, key, value)
        self.session.commit()
        return entity

    def delete(self, entity_id):
        entity = self.get(entity_id)
        self.session.delete(entity)
        self.session.commit()
        return entity
