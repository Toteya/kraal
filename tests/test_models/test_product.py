#!/usr/bin/python3
"""
Contains test for the product class
"""
from models.base_model import BaseModel
from models.product import User
import unittest


class TestProduct(unittest.TestCase):
    """
    Tests the Product class
    """

    def setUp(self):
        """
        Sets up the initial conditions for each test case
        """
        self.p1 = User()
        pass

    def tearDown(self):
        """
        Tears down changes after each test
        """
        super().tearDown()

    def test_Product(self):
        """
        Tests that a Product instance is instantiated and initialised correctly
        """
        self.assertIsInstance(self.p1, BaseModel)
