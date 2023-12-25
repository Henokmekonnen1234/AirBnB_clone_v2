#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """
    #__tablename__ = "cities"
    name = " "# Column(String(128), nullable=False)
    state_id = " " #Column(String(60), ForeignKey("State.id"), nullable=False)
    #states = relationship("State", back_reference="cities")

    #def __init__(self, name=None, state_id=None):
        #"""this will initialize the class instances"""
        #if name is not None and state_id is not None:
            #self.name = name
            #self.state_id = state_id
