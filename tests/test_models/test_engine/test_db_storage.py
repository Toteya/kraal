#!/usr/bin/python3
"""
Contains the tests for the db_storage module
"""
import unittest
from os import environ
from models import storage
from models.product import Product


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
        self.assertEqual(len(storage.all()), 0)
        storage.new(Product(name='Goat'))
        storage.save()
        self.assertEqual(len(storage.all()), 1)

    def test_get(self):
        """
        Tests the method that returns an object based on the specified
        class and object id
        """
        storage.new(Product(id='54321', name='Goat'))
        storage.save()
        # Object exists -> return correct object
        obj = storage.get(Product, 54321)
        self.assertEqual(obj.name, 'Goat')
        # Object ID doesn't exist ->  return None
        obj = storage.get(Product, 98)
        self.assertIsNone(obj)
        # No arguments -> return None
        self.assertIsNone(storage.get())
        # Only one argument -> return None
        self.assertIsNone(storage.get(Product))
