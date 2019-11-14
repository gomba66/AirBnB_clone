#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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

        obj_dict = {"BaseModel": BaseModel, "User": User, "State": State,
         "City": City, "Amenity": Amenity, "Place": Place,
         "Review": Review}
        try:
            with open(self.__file_path, "r") as f:
                m = json.loads(f.read())
                for key, value in m.items():
                    self.__objects[key] = obj_dict[value["__class__"]](**value)
        except FileNotFoundError:
            pass
