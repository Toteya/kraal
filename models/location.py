#!/usr/bin/python3
"""
contains the Location class definition
"""
from models.base_model import Base, BaseModel, Column
from sqlalchemy import Double
from sqlalchemy.orm import relationship


class Location(BaseModel, Base):
    """
    Defines a Location object
    """
    __tablename__ = 'locations'

    latitude = Column('latitude', Double)
    longitude = Column('longitude', Double)
    # alternatively use coordinates - POINT '2D SPACIAL INDEX' datatype

    user = relationship('User', back_populates='location', uselist=False)
