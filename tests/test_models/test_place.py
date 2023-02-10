#!/usr/bin/python3
'''unit tests for ``Place`` klas'''

from unittest import TestCase
from models.base_model import BaseModel
from models.place import Place


class AmenityTestCase(TestCase):
    '''TestCase for ``Place`` klas'''

    def setUp(self):
        '''initializes a ``Place`` instance'''
        self.place = Place()

    def test_is_subclass(self):
        '''checks that klas inherits from ``BaseModel``'''
        self.assertIsInstance(self.place, BaseModel)

    def test_attrs_are_correct(self):
        '''checks that attrs are correctly initialized'''
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
