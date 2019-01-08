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
from sqlalchemy.orm import sessionmaker
from os import getenv
from sqlalchemy.orm import scoped_session


class DBStorage():
    """The engine for the sqlalchemy database"""
    __session = None
    __engine = None

    def __init__(self):
        usr = getenv("HBNB_MYSQL_USER")
        pswd = getenv("HBNB_MYSQL_PWD")
        hst = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                usr, pswd, hst, db, pool_pre_ping=True))
        Base.metadata.create_all(self.__engine)
        if getenv("HBND_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns all instances of a class if the class name is passed.
        If it's empty, return all instances of valid classes.
        """
        all_dict = {}
        # classes = ['Places', 'State', 'Review', 'City', 'User', 'Amenity']
        if cls:
            result = self.__session.query(eval(cls)).all()
            for item in result:
                key = '{}.{}'.format(item.__class__.__name__, item.id)
                all_dict[key] = item
        else:
            for x in Base.__subclasses__():
                result = self.__session.query(x).all()
                for item in result:
                    key = '{}.{}'.format(item.__class__.__name__, item.id)
                    all_dict[key] = item
        return all_dict

    def new(self, obj):
        """
        Adds a new object to the database
        """
        if obj:
            try:
                self.__session.add(obj)
            except:
                pass

    def save(self):
        """
        Saves whatever changes have not yet been committed to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes and object if obj is not none.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        ses_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses_fact)
        self.__session = Session()
