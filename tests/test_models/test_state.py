#!/usr/bin/python3
'''TestCase of ``State`` klas'''

from unittest import TestCase
from models.base_model import BaseModel
from models.state import State


class StateTestCase(TestCase):
    '''Testcase for ``State`` klas'''

    def setUp(self):
        '''initializes a State instance'''
        self.state = State()

    def test_is_subclass(self):
        '''checks that klas inherits from ``BaseModel``'''
        self.assertIsInstance(self.state, BaseModel)

    def test_attrs_are_correct(self):
        '''checks that attrs are correctly initialized'''
        self.assertEqual(self.state.name, "")
