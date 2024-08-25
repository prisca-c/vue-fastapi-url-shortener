from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.app.core.database import Base


class Url(Base):
    __tablename__ = "urls"

    id = Column(String, primary_key=True, index=True)
    url = Column(String, index=True)
    short_url = Column(String, index=True)
    created_at = Column(String)
    updated_at = Column(String)
    user_id = Column(String, ForeignKey("users.id"))
    clicks = Column(Integer)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(String)
    deleted_by = Column(String)
    updated_by = Column(String)
    created_by = Column(String)
    user = relationship("User", back_populates="urls")
