from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .utils.Base import Base
from .utils.BasicMixins import BasicMixins


class User(Base, BasicMixins):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    last_password = Column(String, nullable=True)
    last_login_at = Column(DateTime, nullable=True)
