#!/usr/bin/python3
"""console.py"""
import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

