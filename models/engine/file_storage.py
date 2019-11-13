#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj.to_dict()

    def save(self):
        with open(self.__file_path, "w") as f:
            dict_str = json.dumps(self.__objects)
            f.write(dict_str)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                content = f.read()
                self.__objects = json.loads(content)
        except FileNotFoundError:
            pass
