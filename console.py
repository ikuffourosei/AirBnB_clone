#!/usr/bin/python3
"""console.py"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from shlex import split


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            brac_lex = split(arg[:brackets.span()[0]])
            com_strip = [i.strip(",") for i in brac_lex]
            com_strip.append(brackets.group())
            return com_strip
    else:
        brac_lex = split(arg[:curly_braces.span()[0]])
        com_strip = [i.strip(",") for i in brac_lex]
        com_strip.append(curly_braces.group())
        return com_strip


class HBNBCommand(cmd.Cmd):
    """HBNBCommand command interpreter for HBNB project"""
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    # Methods

    def do_quit(self, arg):
        """Quit Command to exit the command interpreter"""
        return True

    def help_quit(self):
        print('\n'.join(['Usage: quit',
                         'Quit command to exit the program',
                         ]))

    def do_all(self, arg):
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def help_all(self):
        """
        Prints the string representation of all instances
        or all instances of a class.
        """

        print('\n'.join(['Usage: all <class name> or all',
                         '\n'
                         'Prints the string representation of all instances',
                         'or all instances of a class.',
                         ]))

    def do_create(self, arg):
        """
        Creates an Instance according to a specified class
        with attributes
         """
        if arg:
            if arg == BaseModel.__name__:
                print(BaseModel.__name__)
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)

            if arg != BaseModel.__name__:
                print(f"** class doesn't exist **")

        else:
            print(f"** class name missing **")

    def help_create(self):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        print('\n'.join(['Usage: create <class name>',
                         '\n'
                         'Creates a new instance of BaseModel',
                         'saves it (to the JSON file) and prints the id.',
                         ]))

    def do_show(self, arg):
        """
        Show information about an instance of BaseModel.

        Parameters:
            *args: Variable length argument list.

        Returns:
            None
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])


    def help_show(self):
        """
        Prints the string representation of an instance based on the class
        name and id.
        """

        print('\n'.join(['Usage: show <class name> <instance id>',
                         '\n'
                         'Prints the string representation',
                         'of an instance based on the class name and id.',
                         ]))

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print("")
        return True

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()
    
    def help_update(self):
        print('\n'.join(['Usage: update <class name> <id> <attribute name> \
"<attribute value>"',
                         '\n'
                         'Updates an instance based on the class name and id',
                         'by adding or updating attribute',
                         '(save the change into the JSON file).',
                         ]))
    
    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def help_destroy(self):
        print('\n'.join(['Usage: destroy <class name> <instance id>',
                         '\n',
                         'Deletes an instance based on the class name',
                         'and id (save the change into the JSON file).',
                         ]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
