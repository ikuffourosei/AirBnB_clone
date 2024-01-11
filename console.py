#!/usr/bin/python3
"""console.py"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        return True

    def help_quit(self):
        print('\n'.join(['quit',
                          'To quit the program',
                          ]))

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_create(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
