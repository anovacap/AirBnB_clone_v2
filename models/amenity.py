#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
    # Come back to number 10

    else:
        name = ""
