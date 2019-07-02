#!/usr/bin/python3
"""my place module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """my amenity class, child of BaseModel class"""
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        instance of class constructor
        """
        super().__init__(**kwargs)
