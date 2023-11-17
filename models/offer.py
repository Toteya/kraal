#!/usr/bin/python3
"""
Contains the Offer class defintion
"""
from models.base_model import BaseModel


class Offer(BaseModel):
    """
    Defines an Offer object that allows a producer to make an offer to
    requests that have been made
    """
    user_id = ""
    request_id = ""
    price = 0.0
    delivery_fee = 0.0
