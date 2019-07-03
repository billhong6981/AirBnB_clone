#!/usr/bin/python3
"""my unittest for Place class module"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_PlaceClass(unittest.TestCase):
    """my unittest for Place Class"""

    def test_issubclass(self):
        """test for subclass"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_issubclass_1(self):
        """test for subclass"""
        self.assertFalse(issubclass(Place, State))

    def test_issubclass_2(self):
        """test for subclass"""
        self.assertFalse(issubclass(Place, Amenity))

    def test_issubclass_3(self):
        """test for subclass"""
        self.assertFalse(issubclass(Place, City))

    def test_issubclass_4(self):
        """test for subclass"""
        self.assertFalse(issubclass(Place, User))

    def test_issubclass_5(self):
        """test for subclass"""
        self.assertFalse(issubclass(Place, Review))

    def test_exceptions(self):
        """test for type error"""
        user1 = Place(my_number = 89)
        with self.assertRaises(TypeError):
            user1_dic = user1.to_dict(12345)

    def test_dictionary(self):
        """test for dictionary"""
        kwargs = {'first_name':'Ben', 'last_name':'Zhu', 'age':'a'}
        user1 = Place(**kwargs)
        user1_dic = user1.to_dict()
        user1_load = Place(**user1_dic)
        user1_load_dic = user1_load.to_dict()
        self.assertTrue(isinstance(user1_dic, dict))
        self.assertTrue(isinstance(user1_load_dic, dict))
        self.assertFalse(kwargs == user1_dic)
        self.assertTrue(kwargs == user1_load.__dict__)
        self.assertEqual(kwargs, user1.__dict__)
        self.assertTrue(user1.__dict__ == user1_load.__dict__)
        self.assertTrue(user1_dic, user1_load_dic)

    def test_city_id(self):
        """
        test the city_id call attribute
        """
        bill = Place()
        bill.city_id = "hug"
        self.assertEqual(type(Place.city_id), str)

    def test_user_id(self):
        """                                                                                                   test the user_id call attribute
        """
        bill = Place()
        bill.user_id = "hug"
        self.assertEqual(type(Place.user_id), str)

    def test_name(self):
        """                                                                                                   test the city_id call attribute
        """
        bill = Place()
        bill.name = "hug"
        self.assertEqual(type(Place.name), str)

    def test_description(self):
        """                                                                                                   test the city_id call attribute                                                                       """
        bill = Place()
        bill.description = "hug"
        self.assertEqual(type(Place.description), str)

    def test_number_rooms(self):
        """
        test the city_id call attribute
        """
        bill = Place()
        bill.number_rooms = 89
        self.assertEqual(type(Place.number_rooms), int)

    def test_number_bathrooms(self):
        """
        test the number_bathrooms call attribute
        """
        bill = Place()
        number_bathrooms = 89
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_max_guest(self):
        """
        test the city_id call attribute
        """
        bill = Place()
        bill.max_guest = 89
        self.assertEqual(type(Place.max_guest), int)

    def test_price_by_night(self):
        """
        test the price_by_night call attribute
        """
        bill = Place()
        bill.price_by_night = 89
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitude(self):
        """
        test the latitude call attribute
        """
        bill = Place()
        bill.latitude = 89.98
        self.assertEqual(type(Place.latitude), float)

    def test_longitude(self):
        """
        test the longitude call attribute
        """
        bill = Place()
        bill.longitude = 89.98
        self.assertEqual(type(Place.longitude), float)

    def test_amenity_ids(self):
        """
        test the amenity_ids call attribute
        """
        bill = Place()
        bill.amenity_ids = ["abc"]
        self.assertEqual(type(Place.amenity_ids), list)
