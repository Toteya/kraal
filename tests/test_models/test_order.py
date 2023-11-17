#!/usr/bin/python3
"""
Contains test for the Order class
"""
from models.base_model import BaseModel
from models.order import Order
import unittest


class TestOrder(unittest.TestCase):
    """
    Tests the Order class
    """

    def setUp(self):
        """
        Sets up the initial conditions for each test case
        """
        self.order1 = Order()
        pass

    def tearDown(self):
        """
        Tears down changes after each test
        """
        super().tearDown()

    def test_Order(self):
        """
        Tests that a Order instance is instantiated and initialised correctly
        """
        self.assertIsInstance(self.order1, BaseModel)
