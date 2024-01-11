#!/usr/bin/python3
"""FileStorage class"""


import json
import os
import glob


class FileStorage:
    """a class that serializes instances to a JSON file
    and deserializes JSON file to instances
    Class Attributes:
        __file_path (str): stores the path of a file. ex (file.json)
        __objects (dict): stores the class with id. ex(BaseModel.1254668)
    """
    __file_path = os.path.abspath(glob.glob("*.json")) #private class attribute
    __objects = {} #private class attribute

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects
    
    
    def new(self, obj):
        """sets in __object the obj with the key <obj class name.id>"""
        obj_class_name = type(obj).__name__
        idn = obj.id
        dict_key = f"{obj_class_name}.{idn}"
        FileStorage.__objects[dict_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as file:
            json.dump(self.__objects, file)
    
    def reload(self):
        """
        deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists ; otherwise, do nothing. 
        If the file doesn’t exist, no exception should be raised)
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
        else:
            pass
