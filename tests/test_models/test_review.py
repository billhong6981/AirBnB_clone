#!/usr/bin/python3
"""my unittest for Review class module"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_ReviewClass(unittest.TestCase):
    """my unittest for Review Class"""

    def test_issubclass(self):
        """test for subclass"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_issubclass_1(self):
        """test for subclass"""
        self.assertFalse(issubclass(Review, City))

    def test_issubclass_2(self):
        """test for subclass"""
        self.assertFalse(issubclass(Review, Amenity))

    def test_issubclass_3(self):
        """test for subclass"""
        self.assertFalse(issubclass(Review, State))

    def test_issubclass_4(self):
        """test for subclass"""
        self.assertFalse(issubclass(Review, Place))

    def test_issubclass_5(self):
        """test for subclass"""
        self.assertFalse(issubclass(Review, User))

    def test_exceptions(self):
        """test for type error"""
        user1 = Review(my_number = 89)
        with self.assertRaises(TypeError):
            user1_dic = user1.to_dict(12345)

    def test_dictionary(self):
        """test for dictionary"""
        kwargs = {'first_name':'Ben', 'last_name':'Zhu', 'age':'a'}
        user1 = Review(**kwargs)
        user1_dic = user1.to_dict()
        user1_load = Review(**user1_dic)
        user1_load_dic = user1_load.to_dict()
        self.assertTrue(isinstance(user1_dic, dict))
        self.assertTrue(isinstance(user1_load_dic, dict))
        self.assertFalse(kwargs == user1_dic)
        self.assertTrue(kwargs == user1_load.__dict__)
        self.assertEqual(kwargs, user1.__dict__)
        self.assertTrue(user1.__dict__ == user1_load.__dict__)
        self.assertTrue(user1_dic, user1_load_dic)
