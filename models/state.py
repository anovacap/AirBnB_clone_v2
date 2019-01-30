#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete, delete-orphan',
                              backref='state')
    else:
        name = ""

    if getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self):
            """func cities getter"""
            citi_list = []
            for citi in models.storage.all(City).values():
                if citi.state_id == self.id:
                    citi_list.append(citi)
            return citi_list
