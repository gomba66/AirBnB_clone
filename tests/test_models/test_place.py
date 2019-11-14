#!/usr/bin/python3
""" test for class BaseModel """

from models.place import Place
import unittest


class TestBaseModelDocs(unittest.TestCase):
    """ validate docstring in the class """

    def test_doc_class(self):
        """ validate documentation class """
        doc = Place.__doc__
        assert doc is not None

    def test_instance(self):
        """ pass """
        p = Place()
        assert isinstance(p, Place)

    def test_hasattribute(self):
        """Tests if the instance of BaseModel"""
        p = Place()
        self.assertTrue(hasattr(p, "city_id"))
        self.assertTrue(hasattr(p, "user_id"))
        self.assertTrue(hasattr(p, "name"))
        self.assertTrue(hasattr(p, "description"))
        self.assertTrue(hasattr(p, "number_rooms"))
        self.assertTrue(hasattr(p, "number_bathrooms"))
        self.assertTrue(hasattr(p, "max_guest"))
        self.assertTrue(hasattr(p, "price_by_night"))
        self.assertTrue(hasattr(p, "latitude"))
        self.assertTrue(hasattr(p, "longitude"))
        self.assertTrue(hasattr(p, "amenity_ids"))

    def test_type(self):
        p = Place()
        self.assertEqual(type(p.city_id), str)
        self.assertEqual(type(p.user_id), str)
        self.assertEqual(type(p.name), str)
        self.assertEqual(type(p.description), str)
        self.assertEqual(type(p.number_rooms), int)
        self.assertEqual(type(p.number_bathrooms), int)
        self.assertEqual(type(p.max_guest), int)
        self.assertEqual(type(p.price_by_night), int)
        self.assertEqual(type(p.latitude), float)
        self.assertEqual(type(p.longitude), float)
        self.assertEqual(type(p.amenity_ids), list)
