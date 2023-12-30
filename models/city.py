#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), default="", nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        places = relationship("Place", back_populates="cities", cascade="all,\
                               delete-orphan")
