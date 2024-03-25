#!/usr/bin/python3
"""DBStorage engine"""
import os
import models
from models import classes
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This manages the storage using database and tables"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates the storage engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        dbase = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passwd, host, dbase), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Query om the database session"""
        result = {}
        objs = []
        if cls:
            if isinstance(cls, str) and cls in classes:
                cls = classes[cls]
            objs.extend(self.__session.query(cls).all())
        else:
            classes_to_query = [User, City, State, Amenity, Place, Review]
            for cls_to_query in classes_to_query:
                objs.extend(self.__session.query(cls_to_query).all())

        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            result[key] = obj
        return (result)

    def new(self, obj):
        """Adds a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables and current session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Calls remove() method on the
        private session attribute (self.__session)
        or close() on the class Session
        """
        self.__session.close()
