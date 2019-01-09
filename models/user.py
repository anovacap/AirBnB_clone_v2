#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This is the class for user.
    Depending on the value of HBNB_TYPE_STORAGE, the new user will
    be saved into either a mysql database, or into a file storage system.

    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
<<<<<<< HEAD
        places = relationship('Place', backref="user",
                              cascade="all, delete, delete-orphan")
=======
        reviews = relationship('Review', backref="user",
                               cascade="all, delete, delete-orphan")
>>>>>>> 95417551526c6b2dcec46f66bc327d9e88d1d451

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
