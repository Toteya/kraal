#!/usr/bin/python3
"""
Contains test for the location class
"""
from models.base_model import BaseModel
from models.location import Location
import unittest


class TestLocation(unittest.TestCase):
    """
    Tests the Location class
    """

    def setUp(self):
        """
        Sets up the initial conditions for each test case
        """
        self.loc1 = Location()
        pass
    
    def tearDown(self):
        """
        Tears down changes after each test
        """
        super().tearDown()

    def test_Location(self):
        """
        Tests that a Location instance is instantiated and initialised correctly
        """
        self.assertIsInstance(self.loc1, BaseModel)