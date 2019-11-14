#!/usr/bin/python3
""" test for class BaseModel """

from models.review import Review
import unittest


class TestBaseModelDocs(unittest.TestCase):
    """ validate docstring in the class """

    def test_doc_class(self):
        """ validate documentation class """
        doc = Review.__doc__
        assert doc is not None

    def test_instance(self):
        """ pass """
        r = Review()
        assert isinstance(r, Review)

    def test_hasattribute(self):
        """Tests if the instance of BaseModel"""
        r = Review()
        self.assertTrue(hasattr(r, "place_id"))
        self.assertTrue(hasattr(r, "user_id"))
        self.assertTrue(hasattr(r, "text"))

    def test_type(self):
        r = Review()
        self.assertEqual(type(r.place_id), str)
        self.assertEqual(type(r.user_id), str)
        self.assertEqual(type(r.text), str)
