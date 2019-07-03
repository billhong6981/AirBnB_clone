#!/usr/bin/python3
"""
unit test module for file storage class
"""
import unittest
from models.base_model import BaseModel
from models.user import User
import models
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """
    unit test for FileStorage class
    """

    def test_class_attr_1(self):
        """
        test to see if __file_path is existing file for open
        """
        ben = BaseModel()
        ben.save()
        all_obj = models.storage.all()
        self.assertTrue(all_obj is not None)

    def test_class_attr_2(self):
        """
        test to see if __objects is dict type
        """
        ben = models.storage.all()
        self.assertEqual(type(ben), dict)

    def test_new_obj(self):
        """
        test to see if obj.__class__.__name__ is in dictionary
        """
        ben = BaseModel()
        models.storage.new(ben)
        dic = models.storage.all()
        key = ben.__class__.__name__ + "." + ben.id
        self.assertEqual(dic[key], ben)

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

    def test_Basemodel(self):
        """
        test the type of the instance
        """
        bill = BaseModel()
        bill_json = bill.to_dict()
        my_new_model = BaseModel(**bill_json)
        self.assertEqual(type(my_new_model), BaseModel)

    def test_jsonType(self):
        """
        test to see if the json is a str
        """
        bill = BaseModel()
        bill_json = bill.to_dict()
        for key in bill_json.keys():
            self.assertEqual(type(key), str)

    def test_json_convertBack(self):
        """
        test to see if to_dict can do the oppposite
        """
        bill = BaseModel()
        bill_json = bill.to_dict()
        my_new_model = BaseModel(**bill_json)
        self.assertNotEqual(bill, my_new_model)

    def test_createdAt_classes(self):
        """
        test the creeated_at atrribute with 2 instances
        """
        bill = BaseModel()
        bill_json = bill.to_dict()
        old_created = bill.created_at
        my_new_model = BaseModel(**bill_json)
        new_created = my_new_model.created_at
        self.assertEqual(old_created, new_created)

    def test_id_obj(self):
        """
        test the id atrribute with 2 instances
        """
        bill = BaseModel()
        bill_json = bill.to_dict()
        old_id = bill.created_at
        my_new_model = BaseModel(**bill_json)
        new_id = my_new_model.created_at
        self.assertEqual(old_id, new_id)

    def test_with_is(self):
        """
        test using the is operator
        """
        bill = BaseModel()
        bill_json = bill.to_dict()
        my_new_model = BaseModel(**bill_json)
        self.assertIsNot(my_new_model, BaseModel)

    def test_baseMode_class(self):
        """
        test to see if the class BaseModel is type class
        """
        bill = BaseModel()
        self.assertEqual(type(bill), BaseModel)

    def test_issubclass(self):
        """test for subclass"""
        self.assertFalse(issubclass(FileStorage, BaseModel))

    def test_issubclass_1(self):
        """test for subclass"""
        self.assertFalse(issubclass(FileStorage, User))

    def test_exceptions_1(self):
        """test for type error"""
        user1 = BaseModel(my_number=89)
        with self.assertRaises(TypeError):
            user1_dic = models.storage.all(12345)

    def test_exceptions_2(self):
        """test for type error"""
        user1 = BaseModel(my_number=89)
        with self.assertRaises(AttributeError):
            models.storage.new(user1)

    def test_exceptions_3(self):
        """test for type error"""
        user1 = BaseModel(my_number=89)
        with self.assertRaises(TypeError):
            models.storage.save(user1)

    def test_exceptions_4(self):
        """test for type error"""
        user1 = BaseModel(my_number=89)
        with self.assertRaises(TypeError):
            models.storage.reload(user1)

    def test_dictionary(self):
        """test for dictionary"""
        kwargs = {'first_name': 'Ben', 'last_name': 'Zhu', 'age': 'a'}
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

if __name__ == "__main__":
    unittest.main()
