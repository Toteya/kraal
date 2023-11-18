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
        del self.b1
        del self.b2
        super().tearDown()

    def test_BaseModel(self):
        """
        Tests that that a BaseModel instance is created correctly
        """
        
        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertEqual(bm1.updated_at, bm1.created_at)
        self.assertIsInstance(bm1.id, str)
        self.assertNotEqual(bm1.id, self.b1.id)
        
        bm2_dict = {
                'id': '1b3c52b7-1981-4e81-a75e-63af749ecb54',
                'created_at': '2023-11-18T10:46:06.603808',
                'updated_at': '2023-11-18T10:46:06.603808',
                '__class__': 'BaseModel',
                'random_attribute': 'random'
            }
        bm3 = BaseModel(**bm2_dict)
        self.assertNotIn('__class__', bm3.__dict__)
        self.assertNotIn('random_attribute', bm3.__dict__)
        self.assertIsInstance(bm3.created_at, datetime)
        self.assertIsInstance(bm3.updated_at, datetime)
        self.assertEqual(bm3.created_at.day, 18)
        self.assertEqual(bm3.created_at.hour, 10)
        self.assertEqual(bm3.created_at.minute, 46)

    def test_update(self):
        """
        Tests the method that updates the attributes
        """
        self.assertEqual(self.b1.created_at, self.b1.updated_at)
        self.b1.update()
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)
    
    def test_to_dict(self):
        """
        Tests the method that returns a dictionary representation of an
        instance
        """
        b1_dict = self.b1.to_dict()
        self.assertIsInstance(b1_dict, dict)
        self.assertEqual(b1_dict['__class__'], self.b1.__class__.__name__)
        self.assertIsInstance(b1_dict['created_at'], str)
        self.assertIsInstance(b1_dict['updated_at'], str)
