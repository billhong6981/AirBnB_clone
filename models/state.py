#!/usr/bin/python3
"""my state module"""
from models.base_model import BaseModel


class State(BaseModel):
    """my state class, child of BaseModel class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        instance of class constructor
        """
        super().__init__(**kwargs)
