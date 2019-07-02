#!/usr/bin/python3
"""my serialization and deserialization module"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models
import json
import os


class FileStorage:
    """my serialization/deserialization class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary of objects
        """
        return FileStorage.__objects

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
        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()
        string = json.dumps(dictionary)

        with open(FileStorage.__file_path, 'w') as f:
            f.write(string)

    def reload(self):
        """
        load from file and convert Json string to python object
        """
        dictOfdict = {}
        dic_temp = {}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dictOfdict = json.load(f)
            for k, v in dictOfdict.items():
                dic_temp[k] = (eval(v['__class__']))(**v)
            FileStorage.__objects = dic_temp
        except:
            pass
