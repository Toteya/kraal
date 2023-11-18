#!/usr/bin/python3
"""
Contains the tests for the db_storage module
"""
import unittest
from os import environ


class TestDBStorage(unittest.TestCase):
    """
    Tests the database storage engine
    """

    def setUp(self):
        """
        Sets up the initial conditions of each test
        """
        environ['KRAAL_MYSQL_USER'] = 'root'
        environ['KRAAL_MYSQL_PWD'] = 'password'
        environ['KRAAL_MYSQL_HOST'] = 'localhost'
        environ['KRAAL_MYSQL_DB'] = 'kraal_test_db'
        environ['KRAAL_ENV'] = 'test'
        from models import storage
        self.storage = storage
        self.storage.load()
        super().setUp()
    
    def tearDown(self):
        self.storage.close()
        super().tearDown()
    
    def test_all(self):
        """
        Tests that this call to the storage engine returns all the instances
        that are stored in the database
        """
        # from models.product import Product
        # # self.assertEqual(environ['KRAAL_ENV'], 'test')
        # self.assertEqual(len(self.storage.all()), 0)
        # self.storage.new(Product({'name': 'Goat'}))
        # self.storage.save()
        # self.assertEqual(len(self.storage.all()), 1)
        pass

    def test_get(self):
        """
        Tests that the method that returns an object based on the specified
        class and object id
        """
        pass