#!/usr/bin/python3
"""my first user module"""

from models.base_model import BaseModel


class User(BaseModel):
    """my first user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        instance of class constructor
        """
        super().__init__(**kwargs)
