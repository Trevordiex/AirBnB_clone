#!/usr/bin/python3
'''unittest for ``User`` class'''

from unittest import TestCase
from models.user import User
import uuid
from datetime import datetime

class TestUser(TestCase):
    '''TestCase for User class'''
    def setUp(self):
        self.base = User()

    def test_user(self):
        '''Tests if User instance is valid and exists'''
        self.assertIsInstance(self.base, User)

    def test_id(self):
        '''Test if it actually inherits from BaseModel'''

    def test_attributes(self):
        '''Test for public attributes'''
        self.assertIsInstance(self.base.email, str)
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

    def test_id_is_valid_uuid_in_string(self):
        '''checks that ``id`` is casted from uuid4'''
        try:
           valid = uuid.UUID(self.base.id, version=4)
        except ValueError:
            self.fail("invalid uuid string")

        self.assertIsInstance(valid, uuid.UUID)

    def test_create_at_is_valid_datetime(self):
        '''checks that created_at is a valid datetime'''
        self.assertIsInstance(self.base.created_at, datetime)
 
    def test_updated_at_is_valid_datetime(self):
        '''checks that updated_at is a valid datetime'''
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_dates_are_correctly_initialized(self):
        '''checks that updated_at is correctly set to creeated_at'''
        b = self.base
        self.assertEqual(b.created_at, b.updated_at)
        self.assertGreater(datetime.now(), b.created_at)

    def test_str_returns_expected(self):
        '''checks that str method formats as expected'''
        b = self.base
        self.assertEqual(
            str(b),
            "[{}] ({}) {}".format(
                b.__class__.__name__,
                b.id,
                b.__dict__
            )
        )
