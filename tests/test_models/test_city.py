#!/usr/bin/python3
""" test for class BaseModel """

from models.city import City
import unittest


class TestBaseModelDocs(unittest.TestCase):
    """ validate docstring in the class """

    def test_doc_class(self):
        """ validate documentation class """
        doc = City.__doc__
        assert doc is not None

    def test_instance(self):
        """ pass """
        c = City()
        assert isinstance(c, City)

    def test_hasattribute(self):
        """Tests if the instance of BaseModel"""
        c = City()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertTrue(hasattr(c, "name"))

    def test_type(self):
        c = City()
        self.assertEqual(type(c.state_id), str)
        self.assertEqual(type(c.name), str)
