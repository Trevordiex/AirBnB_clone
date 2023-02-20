#!/usr/bin/python3
'''unittest for ``User`` class'''

from unittest import TestCase
from models.user import User
from models.base_model import BaseModel


class TestUser(TestCase):
    '''TestCase for User class'''
    def setUp(self):
        self.base = User()

    def test_user(self):
        '''Tests if User instance is valid and exists'''
        self.assertIsInstance(self.base, User)
        self.assertIsInstance(self.base, BaseModel)

    def test_attributes(self):
        '''Test for public attributes'''
        self.assertIsInstance(self.base.email, str)
        self.assertIsInstance(self.base.password, str)
        self.assertEqual(self.base.first_name, self.base.last_name)
        self.base.email = "abc@gmail.com"
        self.assertEqual(self.base.email, "abc@gmail.com")

    def test_id_is_string(self):
        '''checks that id is correctly casted to string'''
        self.assertIsInstance(self.base.id, str)

    def test_id_is_unique(self):
        '''checks that each instance have a unique id'''
        a = User()
        b = User()
        self.assertNotEqual(a.id, b.id)
        self.assertNotEqual(a.id, self.base.id)
        self.assertNotEqual(b.id, self.base.id)
