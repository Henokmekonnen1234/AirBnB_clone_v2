#!/usr/bin/python3
""" State Module for HBNB project """
from importlib import import_module
from models.base_model import BaseModel, Base
from models.place import Place
from os import environ
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenty class defined below are instances of Amenty
       class
    """
    __tablename__ = "amenities"
    name = Column(String(128), default="", nullable=False)
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship("Place",
                                       secondary=Place.place_amenity,
                                       back_populates="amenities")
