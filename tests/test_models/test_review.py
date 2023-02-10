#!/usr/bin/python3
'''unit tests for ``Review`` klas'''

from unittest import TestCase
from models.base_model import BaseModel
from models.review import Review


class AmenityTestCase(TestCase):
    '''TestCase for ``Review`` klas'''

    def setUp(self):
        '''initializes an ``Review`` instance'''
        self.review = Review()

    def test_is_subclass(self):
        '''checks that klas inherits from ``Review``'''
        self.assertIsInstance(self.review, BaseModel)

    def test_attrs_are_correct(self):
        '''checks that attrs are correctly initialized'''
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
