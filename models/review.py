#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String,  ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __table_args__ = ({'mysql_default_charset': 'latin1'})
    __tablename__ = "reviews"
    text = Column(String(1024), default="", nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
