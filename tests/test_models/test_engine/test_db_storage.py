#!/usr/bin/python3
"""
Contains the tests for the db_storage module
"""
import unittest
from models import storage
from models.category import Category
from models.location import Location
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
        that are stored in the database.
        Also tests the methods new() and save(), which add a new object to a
        session and commit changes respectively.
        """
        self.assertEqual(len(storage.all()), 0)
        storage.new(Category(name='Dairy'))
        storage.new(Location(latitude=21.3, longitude=-17.8))
        storage.save()
        # return only objects of the specified class
        self.assertEqual(len(storage.all(Category)), 1)
        self.assertEqual(len(storage.all(Location)), 1)
        # no arguments -> returns all objects
        self.assertEqual(len(storage.all()), 2)

    def test_get(self):
        """
        Tests the method that returns an object based on the specified
        class and object id
        """
        
        dairy = Category(name='Livestock')
        storage.new(dairy)
        storage.save()

        storage.new(Product(id='54321f01-f641', name='Goat', category_id=dairy.id))
        storage.save()
        # Object exists -> return correct object
        obj = storage.get(Product, '54321f01-f641')
        self.assertEqual(obj.name, 'Goat')
        # Object ID doesn't exist ->  return None
        obj = storage.get(Product, 98)
        self.assertIsNone(obj)
        # No arguments -> return None
        self.assertIsNone(storage.get())
        # Only one argument -> return None
        self.assertIsNone(storage.get(Product))
    
    def test_delete(self):
        """
        Tests whether an object is deleted properly
        """
        fruit_veg = Category(name='Fruit_Veg')
        storage.new(fruit_veg)
        storage.save()
        storage.new(Product(name='Tomato', category_id=fruit_veg.id))
        objs = list(storage.all().values())
        count_before = len(objs)
        obj = objs[0]
        obj.delete()
        storage.save()
        count_after = len(storage.all())
        self.assertEqual(count_after, count_before - 1)
