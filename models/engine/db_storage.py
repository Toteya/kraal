#!/usr/bin/python3
"""
Contains the DBStorage engine class definition
"""
from models.base_model import Base
from sqlalchemy import create_engine


class DBStorage:
    """
    Defines the storage engine used to interact with the MySQL database,
    which stores the data for the web application
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiate a DBStorage instance
        """
        KRAAL_MYSQL_USER = 'root'
        KRAAL_MYSQL_PWD = 'root'
        KRAAL_MYSQL_HOST = 'root'
        KRAAL_MYSQL_DB = 'root'

        db_url = 'mysql+mysqldb://{}:{}@{}/{}'.format(
                                                      KRAAL_MYSQL_USER,
                                                      KRAAL_MYSQL_PWD,
                                                      KRAAL_MYSQL_HOST,
                                                      KRAAL_MYSQL_DB)
        
        self.__engine = create_engine(db_url)
        Base.metadat.create_all(self.__engine)
