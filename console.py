#!/usr/bin/python3
"""console.py"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        return True

    def help_quit(self):
        print('\n'.join(['Quit command to exit the program']))

    def do_create(self, arg):
        if arg:
            if arg == BaseModel.__name__:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)

            if arg != BaseModel.__name__:
                print(f"** class doesn't exist **")

        else:
            print(f"** class name missing **")

    def help_create(self):
        print('\n'.join(['Creates a new instance of BaseModel',
                         'saves it (to the JSON file) and prints the id.',
                         ]))

    def do_show(self, *args):
        n = len(args)
        if args:
            if n > 0 and args[0] == BaseModel.__name__:
                new = BaseModel()
                if n == 1:
                    print("** instance id missing **")
                elif n == 2 and args[1] != new.id:
                    print("** no instance found **")
                elif n == 2 and args[1] == new.id:
                    print(str(new))  # Corrected: Call __str__ method
            elif n > 0 and args[0] != BaseModel.__name__:
                print("** class doesn't exist **")
        elif not args:
            print("** class name missing **")

    def help_show(self):
        print('\n'.join(['Prints the string representation',
                         'of an instance based on the class name and id.',
                         ]))

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
