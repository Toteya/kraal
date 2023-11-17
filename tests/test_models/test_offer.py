#!/usr/bin/python3
"""
Contains test for the Offer class
"""
from models.base_model import BaseModel
from models.offer import Offer
import unittest


class TestOffer(unittest.TestCase):
    """
    Tests the Offer class
    """
    
    def setUp(self):
        """
        Sets up the initial conditions for each test case
        """
        self.offer1 = Offer()

    def tearDown(self):
        """
        Cleans up test conditions and resources that were 
        """
        super().tearDown()
    
    def test_Offer(self):
        """
        Tests the instantiation of a Offer instance
        """
        self.assertIsInstance(self.offer1, BaseModel)
