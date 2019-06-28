#!/usr/bin/python3
"""
The module for the base model class that all other class will inherit from.
"""
import uuid
from datetime import datetime as d


class BaseModel:
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        if kwargs:
            for ky, value in kwargs.items():
                if ky is "created_at" or ky is "updated_at":
                    setattr(self, ky, d.now().strftime("%Y-%m-%dT%H:%M:%S.%f"))

                else:
                    setattr(self, ky, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = d.now()
            self.updated_at = d.now()

    def __str__(self):
        """
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        """
        self.updated_at = d.now()

    def to_dict(self):
        """
        """
        dictionary = {}

        for key, value in self.__dict__.items():
            if key is "created_at" or key is "updated_at":
                dictionary[key] = d.isoformat(value)

            else:
                dictionary[key] = value

        dictionary["__class__"] = self.__class__.__name__
        return dictionary
