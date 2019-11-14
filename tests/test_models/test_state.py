#!/usr/bin/python3
""" test for class BaseModel """

from models.state import State
import unittest


class TestBaseModelDocs(unittest.TestCase):
    """ validate docstring in the class """

    def test_doc_class(self):
        """ validate documentation class """
        doc = State.__doc__
        assert doc is not None

    def test_instance(self):
        """ pass """
        s = State()
        assert isinstance(s, State)

    def test_hasattribute(self):
        """Tests if the instance of BaseModel"""
        s = State()
        self.assertTrue(hasattr(s, "name"))

    def test_type(self):
        s = State()
        self.assertEqual(type(s.name), str)
