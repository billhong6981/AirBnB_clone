#!/usr/bin/python3
"""my unittest for User class module"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_UserClass(unittest.TestCase):
    """my unittest for User Class"""

    def test_issubclass(self):
        """test for subclass"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_issubclass_1(self):
        """test for subclass"""
        self.assertFalse(issubclass(User, City))

    def test_issubclass_2(self):
        """test for subclass"""
        self.assertFalse(issubclass(User, Amenity))

    def test_issubclass_3(self):
        """test for subclass"""
        self.assertFalse(issubclass(User, State))

    def test_issubclass_4(self):
        """test for subclass"""
        self.assertFalse(issubclass(User, Place))

    def test_issubclass_5(self):
        """test for subclass"""
        self.assertFalse(issubclass(User, Review))

    def test_exceptions(self):
        """test for type error"""
        user1 = User(my_number = 89)
        with self.assertRaises(TypeError):
            user1_dic = user1.to_dict(12345)

    def test_dictionary(self):
        """test for dictionary"""
        kwargs = {'first_name':'Ben', 'last_name':'Zhu', 'age':'a'}
        user1 = User(**kwargs)
        user1_dic = user1.to_dict()
        user1_load = User(**user1_dic)
        user1_load_dic = user1_load.to_dict()
        self.assertTrue(isinstance(user1_dic, dict))
        self.assertTrue(isinstance(user1_load_dic, dict))
        self.assertFalse(kwargs == user1_dic)
        self.assertTrue(kwargs == user1_load.__dict__)
        self.assertEqual(kwargs, user1.__dict__)
        self.assertTrue(user1.__dict__ == user1_load.__dict__)
        self.assertTrue(user1_dic, user1_load_dic)

    def test_email(self):
        """
        test the email call attribute
        """
        bill = User()
        bill.email = "hug@haoook"
        self.assertEqual(type(User.email), str)

    def test_password(self):
        """
        test the password class attribute
        """
        bill = User()
        bill.password = "abdlfah"
        self.assertEqual(type(User.password), str)

    def test_first_name(self):
        """
        test the first_name class attribute
        """
        bill = User()
        bill.first_name = "Bill Huang"
        self.assertEqual(type(User.first_name), str)

    def test_last_name(self):
        """
        test the last_name class attribute
        """
        bill = User()
        bill.last_name = "Huang"
        self.assertEqual(type(User.last_name), str)
