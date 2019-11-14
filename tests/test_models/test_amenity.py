#!/usr/bin/python3
""" test for class BaseModel """

from models.amenity import Amenity
import unittest


class TestBaseModelDocs(unittest.TestCase):
    """ validate docstring in the class """

    def test_doc_class(self):
        """ validate documentation class """
        doc = Amenity.__doc__
        assert doc is not None

    def test_instance(self):
        """ pass """
        a = Amenity()
        assert isinstance(a, Amenity)

    def test_hasattribute(self):
        """Tests if the instance of BaseModel"""
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))

    def test_type(self):
        a = Amenity()
        self.assertEqual(type(a.name), str)
