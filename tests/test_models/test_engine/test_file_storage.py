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
