#!/usr/bin/python3
'''unit tests for ``Amenity`` klas'''

from unittest import TestCase
from models.base_model import BaseModel
from models.amenity import Amenity


class AmenityTestCase(TestCase):
    '''TestCase for ``Amenity`` klas'''

    def setUp(self):
        '''initializes an ``Amenity`` instance'''
        self.amenity = Amenity()

    def test_is_subclass(self):
        '''checks that klas inherits from ``BaseModel``'''
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attrs_are_correct(self):
        '''checks that attrs are correctly initialized'''
        self.assertEqual(self.amenity.name, "")
