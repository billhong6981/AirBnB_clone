#!/usr/bin/python3
"""my serialization and deserialization module"""
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """my serialization/deserialization class"""

    def __init__(self):
        """instance of class constructor"""
        self.file_path = "file.json"
        self.objects = {}

    @property
    def file_path(self):
        """
        private attribute getter function
        """
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        """
        private attribute setter function
        """
        self.__file_path = value

    @property
    def objects(self):
        """
        private attribute getter function
        """
        return self.__objects

    @objects.setter
    def objects(self, value):
        """
        privat attribute setter function
        """
        self.__objects = value

    def all(self):
        """
        returns the dictionary of objects
        """
        return self.objects

    def new(self, obj):
        """
        add a key and value of obj to objects dictionary
        """
        banjo = obj.__class__.__name__ + "." + obj.id
        self.__objects[banjo] = obj

    def save(self):
        """
        converts python object to Json string and save to file
        """
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        string = json.dumps(dictionary)

        with open(self.__file_path, 'w') as f:
            f.write(string)

    def reload(self):
        """
        load from file and convert Json string to python object
        """
        dictOfdict = {}
        try:
            with open(self.__file_path, 'r') as f:
                dictOfdict = json.load(f)
            for k, v in dictOfdict.items():
                self.__objects[k] = BaseModel(**v)

        except:
            pass
