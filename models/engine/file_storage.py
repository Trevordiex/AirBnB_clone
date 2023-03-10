#!/usr/bin/python3
'''An implementation of a file storage engine
...

Classes
-------
FileStorage
    manages persistence of objects
    by serializing and saving them in a file
'''

import os
import json


class FileStorage:
    '''A storage engine that stores and retrieves
    objects from a file
    ...

    Attributes
    ----------
    __file_path: str
        a private attribute that stores that file path
    __objects: dict
        dictionary that stores all objects by using
        <class name>.id as key. ``id`` is object id

    Methods
    -------
    all():
        returns the dictionary __objects
    new(obj):
        sets in __objects the obj with key
        <obj class name>.id
    save():
        serializes __objects to the JSON file
        (path: __file_path)
    reload():
        deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists ; otherwise, do
        nothing. If the file doesn’t exist, no exception
        should be raised)
    '''

    def __init__(self):
        '''initializes  a storage engine'''
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''adds the new object to __objects'''
        if not obj:
            return
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        '''serializes ``__objects`` to ``__file_path``'''
        str_dict = {
            key: value.to_dict()
            for key, value in self.__objects.items()
        }
        with open(self.__file_path, 'w') as f:
            json.dump(str_dict, f)

    def reload(self):
        '''reloads objects from ``__file_path`` using json'''
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        models = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "State": State
        }
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path) as f:
            str_dict = json.load(f)
            for key, value in str_dict.items():
                model = key.split(".")[0]
                self.__objects[key] = models[model](**value)
