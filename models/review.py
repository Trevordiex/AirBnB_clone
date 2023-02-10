#!/usr/bin/python3
'''``Review`` klas module
...
Classes
-------
Review
    a model klas for a review
'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''``Review`` klas
    ...
    Attributes
    ----------
    place_id: str
        id of a given place
    user_id: str
        id of the user
    text: str
        comment of the user
    '''
    place_id = ''
    user_id = ''
    text = ''
