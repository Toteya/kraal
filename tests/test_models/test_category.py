#!/usr/bin/python3
"""
Contains test for the category class
"""
from models.base_model import BaseModel
from models.category import Category
import unittest


class TestCategory(unittest.TestCase):
    """
    Tests the Product class
    """

    def setUp(self):
        """
        Sets up the initial conditions for each test case
        """
        self.cat1 = Category(name='Dairy')
        self.cat2 = Category(name='Livestock')
        pass

    def tearDown(self):
        """
        Tears down changes after each test
        """
        super().tearDown()

    def test_Category(self):
        """
        Tests that a Category object is instantiated correctly
        """
        self.assertIsInstance(self.cat1, BaseModel)
        self.assertEqual(self.cat1.unit, 'litres')
        self.assertEqual(self.cat2.unit, 'units')

