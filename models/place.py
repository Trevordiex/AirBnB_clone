#!/usr/bin/python3
'''``Place`` module
...
Classes
------
Place
    A model of a given place or area
'''

from models.base_model import BaseModel


class Place(BaseModel):
    '''A model class for a given place
    ...
    Attributes
    ---------
    city_id: str
        the id of the parent city. Empty by default
    user_id: str
        the id of the owning user. '' by default
    name: str
        the name of the place. '' by default
    description: str
        a description of the place: '' by default
    number_rooms: int
        the number of rooms in a place. 0 by default
    number_of_bathrooms: int
        the number of baths in a place. 0 by default
    max_guest: int
        the number of guests a place can contain.
        0 by default
    price_by_night: int
        cost of a night in a place. 0 by default
    latitude: float
        latitude of its cordinate
    longitude: float
        longitude of a its cordinate
    amenity_ids: list
        list of the ids of amenities available in a place
    '''

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
