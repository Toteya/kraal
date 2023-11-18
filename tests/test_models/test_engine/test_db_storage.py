#!/usr/bin/python3
"""
Contains the tests for the db_storage module
"""
import unittest


class TestDBStorage(unittest.TestCase):
    """
    Tests the database storage engine
    """

    def setUp(self):
        """
        Sets up the initial conditions of each test
        """
        super().setUp()
    
    def tearDown(self):
        super().tearDown()
    
    def test_all(self):
        """
        Tests that this call to the storage engine returns all the instances
        that are stored in the database
        """
        pass

    def test_get(self):
        """
        Tests that the method that returns an object based on the specified
        class and object id
        """
        pass