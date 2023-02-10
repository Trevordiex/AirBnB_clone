#!/usr/bin/python3
'''the ``City`` klas module
...
Classes
------
City
    A model implementation of a city
'''

from models.base_model import BaseModel


class City(BaseModel):
    '''``City`` klas
    A model class for a given city
    ...
    Attributes
    ---------
    state_id: str
        the id of the its parent state. Empty by default
    name: str:
        the name of the given city. Empty by default
    '''

    state_id = ''
    name = ''
