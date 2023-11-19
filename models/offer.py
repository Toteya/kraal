#!/usr/bin/python3
"""
Contains the Offer class defintion
"""
from models.base_model import Base, BaseModel, Column
from sqlalchemy import Float, ForeignKey, String


class Offer(BaseModel, Base):
    """
    Defines an Offer object that allows a producer to make an offer to
    requests that have been made
    """
    __tablename__ = 'offers'

    user_id = Column('user_id', String(45), ForeignKey('users.id'))
    request_id = Column('request_id', String(45), ForeignKey('requests.id'))
    price = Column('price', Float)
    delivery_fee = Column('delivery_fee', Float)
