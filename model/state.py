#!/usr/bin/python3
"""class that inherit from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """class state.

    Attributes:
        name (str): The name of the state. "empty"
    """

    name = ""
