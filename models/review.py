#!/usr/bin/python3
"""class that inherit from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
