#!/usr/bin/python3
"""
contains the User class definition
"""
from models.base_model import Base, BaseModel, Column
from sqlalchemy import Boolean, ForeignKey, String


class User(BaseModel, Base):
    """
    Defines a User account object
    """
    __tablename__ = 'users'

    username = Column('username', String(45))
    first_name = Column('first_name', String(45))
    last_name = Column('last_name', String(45))
    email = Column('email', String(45))
    password = Column('password', String(45))
    # location_id = Column('location_id',
    #                      String(45),
    #                      ForeignKey('locations.id'))
    guest_account = Column('guest_account', Boolean, default=True)
