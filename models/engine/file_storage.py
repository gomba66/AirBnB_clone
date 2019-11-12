#!/usr/bin/python3
""" FileStorage class """
import json
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import 

class FileStorage:
    """FileStorage json convertion"""

    __file_path = "file.json"
    __objects = {}
    classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
               'Review']

    def all(self):
        """Returns the objects dictionary"""
        return (self.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key"""

        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """A function that serializes JSON file"""
        sjson = {}
        for key in self.__objects:
            sjson[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(sjson, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
            for key, value in data.items():
                self.__objects[key] = eval(value["__class__"])(**value)
        except:
            pass