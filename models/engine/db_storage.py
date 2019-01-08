#!/usr/bin/python3
"""This is the database storage class for AirBnB"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import scoped_session


class DBStorage():
    """The engine for the sqlalchemy database"""
    __session = None
    __engine = None

    def __init__(self):
        usr = os.getenv(HBNB_MYSQL_USER)
        hst = os.getenv(HBNB_MYSQL_PWD)
        pswd = os.getenv(HBNB_MYSQL_HOST)
        db = os.getenv(HBNB_MYSQL_DB)
        
        self.__engine = create_engine("mysql+mysqldb://"
                                      "{}:{}@{}/{}".format(usr, pswd, hst, db)
                                      , pool_pre_ping=True)
        if os.getenv(HBND_ENV) == 'test':
            drop_all(self.__engine)

    def all(self, cls=None):
        all_dict = {}
        if cls:
            for request in self.__session(cls).order_by.all():
                all_dict[request.name] = request.id
