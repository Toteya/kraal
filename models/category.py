#!/usr/bin/python3
"""
Contains the class definition of a Product Category
"""

from models.base_model import Base, BaseModel, Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


types = {'Dairy': 'litres', 'Livestock': 'units', 'Fruit_Veg': 'kilograms'}

class Category(BaseModel, Base):
    """
    A Product Category
    """
    __tablename__ = 'categories'

    name = Column('name', String(45))
    unit = Column('unit', String(10))
    products = relationship('Product', backref='category', 
                            cascade='all, delete')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unit = types[self.name]
