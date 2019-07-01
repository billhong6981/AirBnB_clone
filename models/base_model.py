#!/usr/bin/python3                                                                                                      """my base models"""
import os
import json
import uuid
from datetime import datetime as d
import models


class BaseModel:
    """my basemodel class"""

    def __init__(self, *args, **kwargs):
        """base instance constructor"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "updated_at" or k == "created_at":
                    setattr(self, k, d.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = d.utcnow()
            self.updated_at = d.utcnow()
            models.storage.new(self)

    def __str__(self):
        """return string for print function"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update the attribute updated_at with current datetime"""
        self.updated_at = d.utcnow()
        models.storage.save()

    def to_dict(self):
        """return the instance attributes dictionary"""

        dic = {}
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                dic[k] = d.strftime(v, "%Y-%m-%dT%H:%M:%S.%f")
            else:
                dic[k] = v
        dic["__class__"] = self.__class__.__name__

        return dic
