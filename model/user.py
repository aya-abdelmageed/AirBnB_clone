#!/usr/bin/python3
"""class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class  User.

    Attributes:
        email (str): The email of the user "empty str".
        password (str): The password of the user "empty str".
        first_name (str): The first name of the user "empty str".
        last_name (str): The last name of the user "empty str".
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
