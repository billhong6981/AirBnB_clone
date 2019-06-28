#!/usr/bin/python3
"""
"""
from models import to_dic()
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

    @object.setter
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
        banjo = self.__class__.__name__ + "." + obj.id
        return self.__objects[banjo] = obj

    def save(self):
        """
        """
        dictionary = {}
        for key, value in _objects.items():
            dictionary[key] = self.__objects[k].to_dict()

        with open(__file_path, 'w') as f:
            json.dumps(dictionary, f)

    def reload(self):
        """
        """
        if os.path.exist(__file_path) is True:
            with open(__file_path, 'r') as f:
                json.loads(__objects)
