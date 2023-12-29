#!/usr/bin/python3
""" State Module for HBNB project """

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", back_populates="states", cascade="all,\
                              delete-orphan")
    else:
        @property
        def cities(self):
            """will fetch cities from a given state"""
            from models import storage
            return [
                    v for _, v in storage.all(State).items()
                    if cities.state_id == self.id
                   ]
