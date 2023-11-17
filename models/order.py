#!/usr/bin/python3
"""
Contains the Order class definition
"""
from models.base_model import BaseModel


class Order(BaseModel):
    """
    Defines an Order object which is created when a user accepts a
    product offer and makes an order
    """
    offer_id = ""
    request_id = ""
    completed = False
