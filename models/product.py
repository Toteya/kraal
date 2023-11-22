#!/usr/bin/python3
"""
Contains the class definition of a product
"""
from models.base_model import Base, BaseModel, Column
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    """
    A product
    """
    __tablename__ = 'products'

    name = Column('name', String(45))
    unit = Column('unit', String(10), default='kg')
    category_id = Column('category_id', String(45), ForeignKey('categories.id'))

    requests = relationship('Request', backref='product')
