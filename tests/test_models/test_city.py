#!/usr/bin/python3
'''TestCase for City'''

from unittest import TestCase
from models.base_model import BaseModel
from models.city import City


class CityTestCase(TestCase):
    def setUp(self):
        '''initializes a city instance'''
        self.city = City()
    def test_is_subclass(self):
        '''checks that instance is from ``BaseModel``'''
        self.assertIsInstance(self.city, BaseModel)

    def test_attrs_are_correct(self):
        '''checks that attrs are correctly initialized'''
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
