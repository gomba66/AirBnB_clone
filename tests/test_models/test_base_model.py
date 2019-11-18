#!/usr/bin/python3
"""
Unittest for base_model
"""


import unittest
from models.base_model import BaseModel
import os
import pep8


class Test_BaseModel(unittest.TestCase):

    def setUp(self):
        """
        Setups test
        """
        pass

    def tearDown(self):
        """
        Resets tests
        """
        try:
            os.remove("file.json")
        except:
            pass

    def test_init_arg(self):
        """Pass an arg into the instance"""
        b1 = BaseModel(12)
        self.assertEqual(type(b1).__name__, "BaseModel")
        self.assertFalse(hasattr(b1, "12"))

    def test_init_kwarg(self):
        """Pass kwargs into the instance"""
        b1 = BaseModel(name="Red")
        self.assertEqual(type(b1).__name__, "BaseModel")
        self.assertTrue(hasattr(b1, "name"))
        self.assertTrue(hasattr(b1, "__class__"))
        self.assertFalse(hasattr(b1, "id"))
        self.assertFalse(hasattr(b1, "created_at"))
        self.assertFalse(hasattr(b1, "updated_at"))

    def test_before_todict(self):
        """Tests the instance before using the todict conversion"""
        b1 = BaseModel()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "BaseModel")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.base_model.BaseModel'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')

    def test_after_todict(self):
        """Tests instances after using to_dict conversion"""
        my_model = BaseModel()
        new_model = BaseModel()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, BaseModel)
        self.assertEqual(type(my_model).__name__, "BaseModel")
        self.assertEqual(test_dict['__class__'], "BaseModel")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_hasattribute(self):
        """Tests if the instance of BaseModel """
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "__init__"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))
