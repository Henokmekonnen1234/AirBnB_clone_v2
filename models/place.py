#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Table, Column, String, Integer, ForeignKey, Float
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ This class contains intances that accept values passed
        for the  Place class
    """
    __table_args__ = ({'mysql_default_charset': 'latin1'})
    __tablename__ = "places"
    city_id = Column(String(60),
                    ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60),
                    ForeignKey("users.id"), nullable=False)
    name = Column(String(128), default="", nullable=False)
    description = Column(String(1024), default="", nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, default=0.0, nullable=False)
    longitude = Column(Float, default=0.0, nullable=False)
    amenity_ids = []
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        place_amenity = Table("place_amenity", Base.metadata,
                              Column("place_id", String(60),
                                     ForeignKey("places.id"),
                                     nullable=False),
                              Column("amenity_id", String(60),
                                     ForeignKey("amenities.id"),
                                     nullable=False),
                              mysql_charset="latin1",)
        reviews = relationship("Review", backref="places",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """returns the value of foreign key or key of Place
                and the environment varible value must be different
                from db

            Returns:
                list: instances of review linked with place instaces
            """
            from models import storage
            return [v for _, v in storage.all(Review).items()
                    if v.place_id == self.id]

        @property
        def amenities(self):
            """return the list of Amenity instances
               that are linked with Place instances

            Returns:
                list: instances of amenity class linked with this class
            """
            from models import storage
            from models.amenity import Amenity
            return [v for _, v in storage.all(Amenity).items()
                    for value in amenity_ids
                    if v.id == value]

        @amenities.setter
        def amenities(self, cls):
            """ this will add amenity class id with respect to the
                value of place linked to it

            Attrib:
                cls (cls): class instance of Amenity
            """
            from models.amenity import Amenity
            if isinstance(cls, Amenity):
                amenity_ids.append(cls.id)
            else:
                pass
