#!/usr/bin/python3
""" test for class BaseModel """

from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
import unittest


class TestBaseModelDocs(unittest.TestCase):
    """ validate docstring in the class """

    def test_instance(self):
        """ pass """
        f = FileStorage()
        assert isinstance(f, FileStorage)

    def test_reload(self):
        """ Test reload method """
        self.assertIsNotNone(storage.reload)
        try:
            os.remove("file.json")
        except BaseException:
            pass

def test_saves_new_instance(self):
        """Tests if file is being created """
        b1 = BaseModel()
        models.storage.new(b1)
        models.storage.save()
        file_exist = os.path.exists(self.file_path)
        self.assertTrue(file_exist)

def test_new(self):
        """Tests the new method"""
        temp_storage = FileStorage()
        temp_dict = temp_storage.all()
        Holberton = User()
        Holberton.id = 972
        Holberton.name = "Holberton"
        temp_storage.new(Holberton)
        class_name = Holberton.__class__.__name__
        key = "{}.{}".format(class_name, str(Holberton.id))
        self.assertIsNotNone(temp_dict[key])
