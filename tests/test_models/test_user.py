#!/usr/bin/python3
"""
Contains test for the user class
"""
from models.base_model import BaseModel
from models.user import Order
import unittest


class TestUser(unittest.TestCase):
    """
    Tests the User class
    """

    def setUp(self):
        """
        Sets up the initial conditions for each test case
        """
        self.user1 = Order()
        pass

    def tearDown(self):
        """
        Tears down changes after each test
        """
        super().tearDown()

    def test_User(self):
        """
        Tests that a User instance is instantiated and initialised correctly
        """
        self.assertIsInstance(self.user1, BaseModel)
