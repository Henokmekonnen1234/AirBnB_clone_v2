#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Basei
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_reference="state", cascade="all,\
                          delete_orphan")
