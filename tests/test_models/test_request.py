#!/usr/bin/python3
"""
Contains test for the Request class
"""
from models.base_model import BaseModel
from models.offer import Offer
import unittest


class TestRequest(unittest.TestCase):
    """
    Tests the Request class
    """

    def setUp(self):
        """
        Sets up the initial conditions for each test case
        """
        self.req1 = Offer()

    def tearDown(self):
        """
        Cleans up test conditions and resources that were
        """
        super().tearDown()

    def test_Request(self):
        """
        Tests the instantiation of a Request instance
        """
        self.assertIsInstance(self.req1, BaseModel)
