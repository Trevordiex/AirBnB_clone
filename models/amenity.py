#!/usr/bin/python3
'''The ``Amenity`` klas module
...
Classes
-------
Amenity
    A model for a given amenity class
'''

from models.base_model import BaseModel


class Amenity(BaseModel):
    '''``Amenity`` klas
    ...
    Attributes
    ----------
    name: str
        name of the amenity. Empty by default
    '''

    name = ''
