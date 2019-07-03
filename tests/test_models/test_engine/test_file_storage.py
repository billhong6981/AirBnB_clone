#!/usr/bin/python3
"""
unit test module for file storage class
"""
import unittest
from models.base_model import BaseModel
from models.user import User
import models
from models.engine.file_storage import FileStorage
from os import path
import json
import os

class Test_FileStorage(unittest.TestCase):
    """
    unit test for FileStorage class
    """

    def test_private_class_attr_1(self):
        """
        test to see if __file_path is type of str
        """
        filename = models.storage._FileStorage__file_path
        self.assertEqual(type(filename), str)

    def test_private_class_attr_2(self):
        """
        test to see if __objects is type of dict
        """
        obj = models.storage._FileStorage__objects
        self.assertEqual(type(obj), dict)

    def test_class_objects(self):
        """
        test to see if __objects store all class obj with key
        """
        ben = BaseModel()
        obj = models.storage._FileStorage__objects
        key = ben.__class__.__name__ + "." + ben.id
        self.assertEqual(obj[key], ben)

    def test_method_all(self):
        """
        test to see if method all is return dict type object
        """
        ben = models.storage.all()
        self.assertEqual(type(ben), dict)

    def test_method_all_1(self):
        """
        test to see if all method is a dictionary
        """
        dic = models.storage.all()
        obj = models.storage._FileStorage__objects
        self.assertEqual(dic, obj)

    def test_method_new(self):
        """
        test to see if obj.__class__.__name__ is in dictionary
        """
        ben = BaseModel()
        models.storage.new(ben)
        obj = models.storage._FileStorage__objects
        key = ben.__class__.__name__ + "." + ben.id
        self.assertEqual(obj[key], ben)

    def test_save_reload_method(self):
        """
        test save and reload method
        """
        ben = BaseModel()
        ben.my_number = 89
        models.storage.save()
        models.storage.reload()
        obj = models.storage._FileStorage__objects
        key = ben.__class__.__name__ + "." + ben.id
        dic = obj[key]
        with self.assertRaises(TypeError):
            v = dic[ben.my_number]

    def test_file_exist_1(self):
        """
        test for json file existence
        """
        ben = BaseModel()
        models.storage.save()
        self.assertTrue(path.exists("file.json"))

    def test_file_exist_2(self):
        """
        test for json file existence
        """
        ben = BaseModel()
        models.storage.reload()
        self.assertTrue(path.exists("file.json"))

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

    def test_reload_method(self):
        """
        test if the reload method works
        """
        bill = FileStorage()
        bill_dict = {"BaseModel.497328": {"id": 497328}}
        bill_dict["BaseModel.693892"] = {"id": 497328}

        with open("file.json", 'w+') as f:
            json.dumps(bill_dict, f)
        bill.reload()
        self.assertEqual(len(bill_dict), 2)

if __name__ == "__main__":
    unittest.main()
