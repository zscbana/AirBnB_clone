#!/usr/bin/python3
"""A simple command-line interpreter."""

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB console"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits console when Ctrl+D is pressed."""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
