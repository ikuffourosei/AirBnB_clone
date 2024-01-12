#!/usr/bin/python3
"""the BaseModel class"""


import uuid
from . import storage
from datetime import datetime


class BaseModel:
    """
    defines all common attributes/methods for other classes in this file
    """
    def __init__(self, *args, **kwargs):
        """
        Initiating the BaseModel class
        Creates a new id, records a time for creation,
        and records time for updates
        Args:
            *args: list containing positional arguments
            **kwargs: dictionary containing key/value arguments
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        if kwargs:
            kwargs.pop("__class__")
            format = "%Y-%m-%dT%H:%M:%S.%f"
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "created_at" in kwargs:
                value = datetime.strptime(kwargs["updated_at"], format)
                self.created_at = value
            if "updated_at" in kwargs:
                value = datetime.strptime(kwargs["updated_at"], format)
                self.updated_at = value

    def __str__(self):
        """Return the print() and str() representation of the BaseModel"""
        return (f"[BaseModel] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        dict_form = self.__dict__.copy()
        dict_form['__class__'] = self.__class__.__name__
        dict_form['created_at'] = self.created_at.isoformat()
        dict_form['updated_at'] = self.updated_at.isoformat()
        return dict_form
