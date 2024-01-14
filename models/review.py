#!/usr/bin/python3
"""class Amenity"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Collecting reviews"""
    place_id = ""
    user_id = ""
    text = ""
