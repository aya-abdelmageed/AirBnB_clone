#!/usr/bin/python3
"""class that inherit from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str): The email of the user."empty"
        password (str): The password of the user."empty"
        first_name (str): The first name of the user."empty"
        last_name (str): The last name of the user."empty"
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
