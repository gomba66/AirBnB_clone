#!/usr/bin/python3
""" test for class BaseModel """

from models.user import User
import unittest


class TestBaseModelDocs(unittest.TestCase):
    """ validate docstring in the class """

    def test_doc_class(self):
        """ validate documentation class """
        doc = User.__doc__
        assert doc is not None

    def test_instance(self):
        """ pass """
        u = User()
        assert isinstance(u, User)

    def test_hasattribute(self):
        """Tests if the instance of BaseModel"""
        u = User()
        self.assertTrue(hasattr(u, "__init__"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))
        self.assertTrue(hasattr(u, "id"))

    def test_type(self):
        u = User()
        self.assertEqual(type(u.email), str)
        self.assertEqual(type(u.password), str)
        self.assertEqual(type(u.first_name), str)
        self.assertEqual(type(u.last_name), str)
