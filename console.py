#!/usr/bin/python3
"""my console dashboard module"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage
#from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    my console dashboard class"""

    prompt = '(hbnb) '

    def cmdloop(self):
        return cmd.Cmd.cmdloop(self)

    def parseline(self, line):
        ret = cmd.Cmd.parseline(self, line)
        return ret

    def onecmd(self, s):
        return cmd.Cmd.onecmd(self, s)

    def emptyline(self):
        pass

    def default(self, line):
        return cmd.Cmd.default(self, line)

    def do_quit(self, arg):
        """
        my quit function
        """
        sys.exit(0)

    def help_quit(self):
        """
        my help function
        """
        print('Quit command to exit the program')
        return True

    def do_EOF(self, arg):
        """
        my alternative quit function
        """
        print()
        return True

    def do_create(self, line):
        """
        create new instance function
        """
        if line is None or line == "":
            print("** class name missing **")
            return False
        arg = line.split()
        try:
            obj = (eval(arg[0]))()
            print(obj.id)
            obj.save()
        except NameError:
            print("** class doesn't exist **")
            return False

    def do_show(self, line):
        """
        display the information about instance of class
        """
        if line is None or line == "":
            print("** class name missing **")
            return False
        arg = line.split()
        try:
            obj = (eval(arg[0]))()
        except NameError:
            print("** class doesn't exist **")
            return False

        if arg[1] is None or arg[1] == "":
            print("** instance id missing **")
            return False

        all_objs = storage.all()
        search = (arg[0] + "." + arg[1])
        try:
            ins = all_objs[search]
            print(ins)
            return True
        except NameError:
            print("** no instance found **")
            return False

    def do_destroy(self, arg):
        """
        deletes the instance of class
        """
        pass

    def do_all(self, arg):
        """
        display all instances of the same class
        """
        pass

    def do_update(self, arg):
        """
        updates the new info to the existing instance
        """
        pass

    def do_greet(self, line):
        print("Hello, ", line)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
