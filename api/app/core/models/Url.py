from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .utils.Base import Base
from .utils.BasicMixins import BasicMixins


class Url(Base, BasicMixins):
    __tablename__ = "urls"

    id = Column(String, primary_key=True, index=True)
    url = Column(String, index=True)
    short_url = Column(String, index=True)
    clicks = Column(Integer)
    created_by = Column(String, ForeignKey("users.id"))

    user = relationship("User", back_populates="urls")
