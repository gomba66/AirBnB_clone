#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        r = {}
        with open(self.__file_path, "w") as f:
            for k, v in self.__objects.items():
                r[k] = v.to_dict()
            f.write(json.dumps(r))

    def reload(self):

        obj_dict = {"BaseModel": BaseModel, "User": User}
        print(BaseModel)
        try:
            with open(self.__file_path, "r") as f:
                m = json.loads(f.read())
                for key, value in m.items():
                    self.__objects[key] = obj_dict[value["__class__"]](**value)
        except FileNotFoundError:
            pass
