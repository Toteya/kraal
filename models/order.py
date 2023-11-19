#!/usr/bin/python3
"""
Contains the Order class definition
"""
from models.base_model import Base, BaseModel, Column
from sqlalchemy import Boolean, ForeignKey, String


class Order(BaseModel, Base):
    """
    Defines an Order object which is created when a user accepts a
    product offer and makes an order
    """
    __tablename__ = 'orders'

    offer_id = Column('offer_id', String(45), ForeignKey('offers.id'))
    completed = Column('completed', Boolean, default=False)
