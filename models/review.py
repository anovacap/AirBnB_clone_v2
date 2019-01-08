#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Review(BaseModel):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = "reviews"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), nullable=False, ForeignKey(places.id))
        user_id = Column(String(60), nullable=False, ForeignKey(users.id))
        # Need to update relationships. come back to number 9.

    else:
        place_id = ""
        user_id = ""
        text = ""
