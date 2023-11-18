#!/usr/bin/python3
"""
Contains the class definition of a product
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String

class Product(BaseModel, Base):
    """
    A product
    """
    __tablename__ = 'products'

    name = Column('name', String(45))
