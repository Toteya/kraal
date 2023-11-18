#!/usr/bin/python3
"""
Contains test for the user class
"""
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """
    Tests the User class
    """

    def setUp(self):
        """
        Sets up the initial conditions for each test case
        """
        self.user1 = User()
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


        user2_dict = {
                'first_name': 'Mary-Jane',
                'last_name': 'Skwach',
                'age': '31',
                '__class__': 'User'
            }
        user2 = User(**user2_dict)
        self.assertNotIn('__class__', user2.__dict__)
        self.assertNotIn('age', user2.__dict__)
        self.assertIsInstance(user2.id, str)
        self.assertIsInstance(user2.created_at, datetime)
        self.assertIsInstance(user2.updated_at, datetime)
        self.assertEqual(user2.first_name, 'Mary-Jane')
        self.assertEqual(user2.last_name, 'Skwach')
