#!/usr/bin/python3
"""
Contains tests for the base_model module
"""
from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Tests the BaseModel class
    """

    def setUp(self):
        """
        Sets up the initial conditions for each test case
        """
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def tearDown(self):
        """
        Tears down / resets the conditions for the tests
        """
        pass

    def test_BaseModel(self):
        """
        Tests that that a BaseModel instance is created correctly
        """
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)
        self.assertEqual(bm.updated_at, bm.created_at)
        self.assertNotEqual(bm.id, self.b1.id)
    
    def test_update(self):
        """
        Tests the method that updates the attributes
        """
        self.assertEqual(self.b1.created_at, self.b1.updated_at)
        self.b1.update()
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)

