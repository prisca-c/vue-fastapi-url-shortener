from datetime import datetime

from sqlalchemy import DateTime, Column, Boolean, String


class BasicMixins:

    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(String)

    @classmethod
    def to_dict(cls):
        return {c.name: getattr(cls, c.name) for c in cls.__table__.columns()}

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.to_dict()})>"

    def __str__(self):
        return self.__repr__()
