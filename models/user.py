#!/usr/bin/python3
"""class User; inherits from BaseModel"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Initiating the User information
    """
    email = ""  # public class attribute
    password = ""  # public class attribute
    first_name = ""  # public class attribute
    last_name = ""  # public class attribute
