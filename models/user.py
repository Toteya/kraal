#!/usr/bin/python3
"""
contains the User class definition
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines a User account object
    """
    username = ""
    first_name = ""
    last_name = ""
    email = ""
    password = ""
    location_id = ""
    guest = False
