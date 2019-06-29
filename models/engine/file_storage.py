#!/usr/bin/python3
"""
"""
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
    """
    def __init__(self):
        """
        """
        self.file_path = "file.json"
        self.objects = {}

    @property
    def file_path(self):
        """
        """
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        """
        """
        self.__file_path = value

    @property
    def objects(self):
        """
        """
        return self.__objects

    @objects.setter
    def objects(self, value):
        """
        """
        self.__objects = value

    def all(self):
        """
        """
        return self.objects

    def new(self, obj):
        """
        """
        banjo = obj.__class__.__name__ + "." + obj.id
        self.__objects[banjo] = obj

    def save(self):
        """
        """
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(dictionary, f)

    def reload(self):
        """
        """
        dictOfdict = {}
        try:
        # if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                dictOfdict = json.load(f)
                for k, v in dictOfdict.items():
                    self.__objects[k] = BaseModel(**v)

        except:
            pass
