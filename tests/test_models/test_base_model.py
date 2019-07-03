#!/usr/bin/python3
"""
The unit test module for class bae_model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """
    start the unit test for thre BaseModel class.
    """

    def test_class_id(self):
        """
        test to see if id is a str
        """
        bill = BaseModel()
        self.assertEqual(type(bill.id), str)

    def test_createdAt_type(self):
        """
        test to see if created_at is a datetime type
        """
        bill = BaseModel()
        self.assertEqual(type(bill.created_at), datetime)

    def test_updateat_type(self):
        """
        test to see if updated_at is a datetime type
        """
        bill = BaseModel()
        self.assertEqual(type(bill.updated_at), datetime)

    def test_the_str(self):
        """
        test the output of the __str__
        """
        bill = BaseModel()
        self.assertEqual(print(bill), None)

    def test_the_lengthOf_id(self):
        """
        test if the length of the id is 36
        """
        bill = BaseModel()
        self.assertEqual(len(bill.id), 36)

    def test_forTo_dict(self):
        """
        test if the to_dict works and converts into a dict
        """
        bill = BaseModel()
        bill_json = bill.to_dict()
        self.assertEqual(type(bill_json), dict)

    def test_class_inDict(self):
        bill = BaseModel()
        bill_json = bill.to_dict()
        self.assertIn("__class__", bill_json)

    def test_saveWorks(self):
        """
        test to see if the save method works
        """
        bill = BaseModel()
        old_time = bill.updated_at
        bill.save()
        self.assertNotEqual(bill.updated_at, old_time)

    def test_toDict_toNonDict(self):
        """
        test to see if to_dict can convert back
        """
        bill = BaseModel()
        bill_json = bill.to_dict()
        my_new_model = BaseModel(**bill_json)
        self.assertNotEqual(type(my_new_model), dict)

    def test_jsonType(self):
        """
        test to see if to_dict can be used as an argument
        """
        bill = BaseModel()
        bill_json = bill.to_dict()
        my_new_model = BaseModel(**bill_json)
        self.assertEqual(type(my_new_model), BaseModel)

if __name__ == "__main__":
    unittest.main()
