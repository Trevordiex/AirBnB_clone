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
        self.__objects[key] = str(obj)

    def save(self):
        '''serializes ``__objects`` to ``__file_path``'''
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        '''reloads objects from ``__file_path`` using json'''
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path) as f:
            self.__objects = json.load(f)
