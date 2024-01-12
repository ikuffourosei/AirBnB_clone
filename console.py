#!/usr/bin/python3
"""console.py"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand command interpreter for HBNB project"""
    prompt = '(hbnb) '

    # Methods

    def do_quit(self, arg):
        """Quit Command to exit the command interpreter"""
        return True

    def help_quit(self):
        print('\n'.join(['Quit command to exit the program']))

    def do_all(self, arg):
        """Prints the string representation of all instances on the class name"""
        # if not arg:
        #     print("** class name missing **")
        #     return

        if arg:
            if arg == BaseModel.__name__:
                print([str(obj) for obj in storage.all().values()])
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
            return


    def help_all(self):
        """
        Prints the string representation of all instances
        or all instances of a class.
        """

        print('\n'.join(['Prints the string representation of all instances',
                         'or all instances of a class.',
                         ]))

    def do_update(self, arg):
        """
        Update the attribute of an instance based on its ID.

        Parameters:
            arg (str): The argument containing the instance ID, attribute name, and
                attribute value separated by spaces.

        Raises:
            ValueError: If the argument is empty or missing the instance ID, or if the
                instance ID is not found in the instance dictionary, or if the argument
                is missing the attribute name, or if the argument is missing the
                attribute value.

        Returns:
            None
        """
        try:
            if not arg:
                raise ValueError("** instance id missing **")

            args = arg.split(' ')
            if args[0] != BaseModel.__name__:
                return

            if len(args) <= 1:
                raise ValueError("** instance id missing **")

            instance_id = args[1]
            instance_dict = storage.all()

            if instance_id not in instance_dict:
                raise ValueError("** no instance found **")

            if len(args) <= 2:
                raise ValueError("** attribute name missing **")

            attribute_name = args[2]

            if len(args) <= 3:
                raise ValueError("** value missing **")

            attribute_value = args[3]

            setattr(instance_dict[instance_id], attribute_name, attribute_value)
            instance_dict[instance_id].save()
        except ValueError as e:
            print(e)

    def do_create(self, arg):
        """Creates an Instance according to a specified class with attributes"""
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
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        print('\n'.join(['Creates a new instance of BaseModel',
                         'saves it (to the JSON file) and prints the id.',
                         ]))

    def do_show(self, *args):
        """
        Show information about an instance of BaseModel.

        Parameters:
            *args: Variable length argument list.

        Returns:
            None
        """

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
        """
        Prints the string representation of an instance based on the class name and id.
        """

        print('\n'.join(['Prints the string representation',
                         'of an instance based on the class name and id.',
                         ]))

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
