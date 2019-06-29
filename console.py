#!/usr/bin/python3
import cmd
import sys
"""
"""


class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        """
        sys.exit()
        return True

    def help_quit(self):
        print('Quit command to exit the program')
        return True

    def do_EOF(self, arg):
        """
        """
        print()
        return True

    def emptyline(self):
            pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
