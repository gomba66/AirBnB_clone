#!/usr/bin/python3
"""This module has the base class"""
import uuid
import time
from datetime import datetime


class BaseModel:
    """ BaseModel Class is the base model"""

    def __init__(self):
        """Method that inicialize the class """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.created_at = str(self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.updated_at = str(self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        return dic
