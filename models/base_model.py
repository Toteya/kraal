#!/usr/bin/python3
"""
contains the BaseModel class definition
"""
import uuid
from datetime import datetime


class BaseModel():
    """
    The parent class for all objects used in the project
    """

    id = ""
    created_at = ""
    updated_at = ""

    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update(self):
        """
        Update the attributes of the instance
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Return a dictionary representation of an instance
        """
        return self.__dict__
