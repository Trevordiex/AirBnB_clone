#!/usr/bin/python3
'''A module for User class that
   inherits from BaseModel
'''

from models.base_model import BaseModel


class User(BaseModel):
    '''a class User that inherits from BaseModel
    ...
    Attributes
    ----------
    email : str
    password : str
    first_name : sr
    last_name : str
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
