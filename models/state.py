#!/usr/bin/python3
""" State Module for HBNB project """

from os import environ
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __table_args__ = ({'mysql_default_charset': 'latin1'})
    __tablename__ = "states"
    name = Column(String(128), default="", nullable=False)
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="all,\
                              delete-orphan")
    else:
        @property
        def cities(self):
            """will fetch cities from a given state"""
            from models import storage
            return [
                    v for _, v in storage.all(City).items()
                    if v.state_id == self.id
                   ]
