#!/usr/bin/python3
'''A module for the ``State`` klas
...
Classes
------
State
    A model implementation of a state
'''

from models.base_model import BaseModel


class State(BaseModel):
    '''``State`` model klas

    Attributes
    ---------
    name: str
        name of the state
    '''

    name = ''
