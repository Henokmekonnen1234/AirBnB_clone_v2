#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", back_populates="place",
                               cascade="all, delete-orphan")
    else:
        @property
        def reviews(self):
            """returns the value of foreign key or key of Place
                and the environment varible value must be different
                from db
            """
            from models import storage
            reviews = [v for _, v in storage.all(Review).items()
                       if v.place_id == self.id]
