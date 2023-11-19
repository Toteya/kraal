#!/usr/bin/python3
"""
Contains the definition for the Request class
"""
from models.base_model import Base, BaseModel, Column
from sqlalchemy import Date, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import relationship


class Request(BaseModel, Base):
    """
    Defines a Request object which allows users to make requests for products
    """
    __tablename__ = 'requests'

    user_id = Column('user_id', String(45), ForeignKey('users.id'))
    product_id = Column('product_id', String(45), ForeignKey('products.id'))
    quantity = Column('quantity', Integer)
    supply_by_date = Column('supply_by_date', Date)
    location_search_radius = Column('location_search_radius', SmallInteger)

    offers = relationship('Offer', backref='request')
