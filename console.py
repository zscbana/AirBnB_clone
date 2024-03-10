#!/usr/bin/python3
""" console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """hbnb  command line interface."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
