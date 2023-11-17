#!/usr/bin/python3
"""
contains the Location class definition
"""
from models.base_model import BaseModel


class Location(BaseModel):
    """
    Defines a User account object
    """
    latitude = 0.0 # Use DECIMAL data type for MySQL
    longitude = 0.0 # Use DECIMAL data type for MySQL
    # alternatively use coordinates - POINT '2D SPACIAL INDEX' datatype
