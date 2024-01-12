#!/usr/bin/python3
"""console.py"""
import cmd
import sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '

    models = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.models:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

