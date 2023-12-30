#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), default="", nullable=False)
    password = Column(String(128), default="", nullable=False)
    first_name = Column(String(128), default="", nullable=False)
    last_name = Column(String(128), default="", nullable=False)
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        places = relationship("Place", back_populates="user", cascade="all,\
                               delete-orphan")
        reviews = relationship("Review", back_populates="user", cascade="all,\
                                delete-orphan")
