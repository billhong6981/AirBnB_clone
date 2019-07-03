#!/usr/bin/python3
"""my unittest for Amenity class module"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_AmenityClass(unittest.TestCase):
    """my unittest for Amenity Class"""

    def test_issubclass(self):
        """test for subclass"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_issubclass_1(self):
        """test for subclass"""
        self.assertFalse(issubclass(Amenity, User))

    def test_issubclass_2(self):
        """test for subclass"""
        self.assertFalse(issubclass(Amenity, State))

    def test_issubclass_3(self):
        """test for subclass"""
        self.assertFalse(issubclass(Amenity, City))

    def test_issubclass_4(self):
        """test for subclass"""
        self.assertFalse(issubclass(Amenity, Place))

    def test_issubclass_5(self):
        """test for subclass"""
        self.assertFalse(issubclass(Amenity, Review))

    def test_exceptions(self):
        """test for type error"""
        user1 = Amenity(my_number = 89)
        with self.assertRaises(TypeError):
            user1_dic = user1.to_dict(12345)

    def test_dictionary(self):
        """test for dictionary"""
        kwargs = {'first_name':'Ben', 'last_name':'Zhu', 'age':'a'}
        user1 = Amenity(**kwargs)
        user1_dic = user1.to_dict()
        user1_load = Amenity(**user1_dic)
        user1_load_dic = user1_load.to_dict()
        self.assertTrue(isinstance(user1_dic, dict))
        self.assertTrue(isinstance(user1_load_dic, dict))
        self.assertFalse(kwargs == user1_dic)
        self.assertTrue(kwargs == user1_load.__dict__)
        self.assertEqual(kwargs, user1.__dict__)
        self.assertTrue(user1.__dict__ == user1_load.__dict__)
