#!/usr/bin/python3
"""Users Class"""


import models
from models.base_model import BaseModel


class User(BaseModel):
    """A user class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
