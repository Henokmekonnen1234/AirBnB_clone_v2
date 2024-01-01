#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __table_args__ = ({'mysql_default_charset': 'latin1'})
    __tablename__ = "users"
    email = Column(String(128), default="", nullable=False)
    password = Column(String(128), default="", nullable=False)
    first_name = Column(String(128), default="", nullable=False)
    last_name = Column(String(128), default="", nullable=False)
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        places = relationship("Place", cascade="all, delete-orphan",
                               backref="users")
        reviews = relationship("Review", backref="users", cascade="all,\
                                delete-orphan")
