#!/usr/bin/python3
"""my city module"""
from models.base_model import BaseModel


class City(BaseModel):
    """my city class, child of BaseModel class"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """
        instance of class constructor
        """
        super().__init__(**kwargs)
