#!/usr/bin/python3
"""defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """represents a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
