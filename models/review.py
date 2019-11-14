#!/usr/bin/python3
"""Review Class"""

import models
from models.base_model import BaseModel


class Review(BaseModel):
    """class that inherits of BaseModels"""

    place_id = ""
    user_id = ""
    text = ""
