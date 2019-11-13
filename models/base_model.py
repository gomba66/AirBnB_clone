#!/usr/bin/python3

"""This module has the base class"""

import uuid
from datetime import datetime
import models

class BaseModel:

    """ BaseModel Class is the base model"""

    def __init__(self, *args, **kwargs):

        """Method that inicialize the class """

        if len(kwargs) != 0:
            for keys in kwargs:
                if keys == 'name':
                    self.name = kwargs[keys]
                if keys == 'my_number':
                    self.my_number = kwargs[keys]
                if keys == 'id':
                    self.id = kwargs[keys]
                if keys == 'created_at':
                    self.created_at = kwargs[keys]
                    self.created_at = datetime.strptime(self.created_at,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if keys == 'updated_at':
                    self.updated_at = kwargs[keys]
                    self.updated_at = datetime.strptime(self.updated_at,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            models.storage.new(self)

    def __str__(self):

        """ Method that returns a description formated of my class"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):

        """ Method that save the objects"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):

        """Method that converts the data in a dictionary"""

        self.created_at = str(self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.updated_at = str(self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        return dic
