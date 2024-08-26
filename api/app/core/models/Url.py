from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .utils.Base import Base
from .utils.BasicMixins import BasicMixins


class Url(Base, BasicMixins):
    __tablename__ = "urls"

    id = Column(String, primary_key=True, index=True)
    url = Column(String, index=True)
    short_url = Column(String, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    clicks = Column(Integer)
    is_active = Column(Boolean, default=True)
    deleted_by = Column(String)
    updated_by = Column(String)
    created_by = Column(String)
    
    user = relationship("User", back_populates="urls")
