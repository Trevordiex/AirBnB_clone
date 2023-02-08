#!/usr/bin/python3
'''A module for BaseModel that defines all
common attributes/methods for other classes
'''

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''A base klas implementing all common attributes
    ...

    Attributes
    ----------
    id : str
        a uuid string identifier (uuid4 used)
    created_at : datetime
        the date and time the instance was created
    updated_at : datetime
        the last time the instance was updated

    Methods
    -------
    save():
        updates the instance ``updated_at`` attr with current datetime
    to_dict():
        returns a dictionary containing all keys/values of
        __dict__ of the instance. The returned dict contains a `__class__`
        whose value is the class name
    '''

    def __init__(self, *args, **kwargs):
        '''Initializes an instance of this klas.
        assigns a uuid to every instance

        persists the object to storage if it new
        '''
        if kwargs:
            kwargs.pop('__class__')
            for d in ['created_at', 'updated_at']:
                kwargs[d] = datetime.fromisoformat(kwargs[d])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        '''returns a string representation of instance'''
        return '[{}] ({}) {}'.format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        '''updates the public instance attribute
        updated_at with the current datetime

        resaves the instance to storage
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Returns a dictionary repr of the instance
        Returns
        -------
        ret (dict): a dictionary representation of instance
        '''
        ret = self.__dict__.copy()
        for key in ret.keys():
            if isinstance(ret[key], datetime):
                ret[key] = ret[key].isoformat()
        ret['__class__'] = self.__class__.__name__
        return ret
