#!/usr/bin/python3
"""
contains the BaseModel class definition
"""
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel():
    """
    The parent class for all objects used in the project       
    """

    id = Column('id', String(45), primary_key=True, nullable=False)
    created_at = Column('created_at',
                        DateTime,
                        default=datetime.utcnow,
                        nullable=False)
    updated_at = Column('updated_at',
                        DateTime,
                        default=datetime.utcnow,
                        nullable=False)

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, time_format)
                    continue
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, time_format)
                    continue
                if hasattr(self, key):
                    setattr(self, key, value)

    def update(self):
        """
        Update the instance attributes
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Return a dictionary representation of an instance
        """
        dictionary = self.__dict__.copy()
        dictionary['created_at'] = datetime.isoformat(self.created_at)
        dictionary['updated_at'] = datetime.isoformat(self.updated_at)
        dictionary['__class__'] = self.__class__.__name__
        return dictionary
    
    def save(self):
        """
        Saves an instance and any changes to the storage engine
        """
        pass

    def delete(self):
        """
        Deletes an instance from the storage engine
        """
        pass
