#!/usr/bin/python3
"""my amenity module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """my amenity class, child of BaseModel class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        instance of class constructor
        """
        super().__init__(**kwargs)
