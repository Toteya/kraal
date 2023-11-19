#!/usr/bin/python3
"""
Contains the tests for the db_storage module
"""
import unittest
from os import environ
from models import storage


class TestDBStorage(unittest.TestCase):
    """
    Tests the database storage engine
    """

    def setUp(self):
        """
        Sets up the initial conditions of each test
        """
        storage.load()
        super().setUp()

    def tearDown(self):
        storage.close()
        super().tearDown()

    def test_all(self):
        """
        Tests that this call to the storage engine returns all the instances
        that are stored in the database
        """
        from models.product import Product
        self.assertEqual(len(storage.all()), 0)
        storage.new(Product(name='Goat'))
        storage.save()
        self.assertEqual(len(storage.all()), 1)
        pass

    def test_get(self):
        """
        Tests that the method that returns an object based on the specified
        class and object id
        """
        pass
