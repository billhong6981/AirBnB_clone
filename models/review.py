#!/usr/bin/python3
"""my review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """my Review class, child of BaseModel class"""
    place_id = ""
    text = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
        """
        instance of class constructor
        """
        super().__init__(**kwargs)
