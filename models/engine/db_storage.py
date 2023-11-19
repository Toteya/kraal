#!/usr/bin/python3
"""
Contains the DBStorage engine class definition
"""
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import environ
from models.location import Location
from models.offer import Offer
from models.order import Order
from models.product import Product
from models.request import Request
from models.user import User


class DBStorage:
    """
    Defines the storage engine used to interact with the MySQL database,
    which stores the data for the web application
    """
    __engine = None
    __session = None
    __classes = {
        'location': Location,
        'offer': Offer,
        'order': Order,
        'product': Product,
        'request': Request,
        'user': User
    }

    def __init__(self):
        """
        Instantiate a DBStorage instance
        """
        user = environ.get('KRAAL_MYSQL_USER')
        password = environ.get('KRAAL_MYSQL_PWD')
        host = environ.get('KRAAL_MYSQL_HOST')
        database = environ.get('KRAAL_MYSQL_DB')

        db_url = 'mysql+mysqldb://{}:{}@{}/{}'.format(
                                                      user,
                                                      password,
                                                      host,
                                                      database)

        self.__engine = create_engine(db_url)
        if environ.get('KRAAL_ENV') == 'test':
            print("TESTING MODE")
            Base.metadata.drop_all(self.__engine)

    def all(self, clss=None):
        """
        Returns a dictionary containing all objects of the specified class.
        If no class is given return all objects from all classes
        """
        obj_list = []
        if clss is not None:
            obj_list = self.__session.query(clss).all()
        else:
            for clss_ in self.__classes.values():
                objs = self.__session.query(clss_).all()
                obj_list.extend(objs)

        obj_dict = {}
        for obj in obj_list:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj
        return obj_dict

    def get(self, clss=None, id=None):
        """
        Returns an object based on the given class and id
        """
        if not all([clss, id]):
            return None
        obj = self.__session.query(clss).filter(clss.id == id).first()
        return obj

    def new(self, obj=None):
        """
        Adds a new object to the session
        """
        if obj is not None:
            self.__session.add(obj)

    def delete(self, obj=None):
        """
        Deletes an object from the current session
        """
        if obj is not None:
            self.__session.delete(obj)

    def save(self):
        """
        Commits all changes from the current session
        """
        self.__session.commit()

    def load(self):
        """
        Loads data from the database and creates new session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """
        Closes/Removes the current session
        """
        self.__session.remove()
