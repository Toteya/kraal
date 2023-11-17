#!/usr/bin/python3
"""
Contains the definition for the Request class
"""
from models.base_model import BaseModel


class Offer(BaseModel):
    """
    Defines a Request object which allows users to make requests for products
    """
    user_id = ""
    product_id = ""
    quantity = ""
    supply_by_date = ""
    location_search_radius = 0