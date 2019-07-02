#!/usr/bin/python3
"""my console dashboard module"""

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    my console dashboard class
    """

    prompt = '(hbnb) '

    def cmdloop(self):
        """
        cmdloop function
        """
        return cmd.Cmd.cmdloop(self)

    def parseline(self, line):
        """
        parse command line function
        """
        ret = cmd.Cmd.parseline(self, line)
        return ret

    def emptyline(self):
        """
        avoid the last command output function
        """
        pass

    def default(self, line):
        """
        default executable command function
        """
        if line:
            line1 = line.split(".")
        if line1 and len(line1) > 1:
            line2 = line1[1].split("(")
            line = str(line2[0]) + " " + str(line1[0])
            if line2 and len(line2) > 1 and len(line2[1]) < 40:
                line = (str(line2[0]) + " " + str(line1[0]) +
                        " " + str(line2[1][1:-2]))
                print(line)
            if line2 and len(line2) > 1 and len(line2[1]) > 42:
                ln = line2[1].split(",")
                if len(ln) > 2:
                    s_1 = ln[0][:-1]
                    s_2 = ln[1][2:-1]
                    s_3 = ln[2][1:]
                    line2[1] = str(s_1) + " " + str(s_2) + " " + str(s_3)
                line = (str(line2[0]) + " " + str(line1[0]) +
                        " " + str(line2[1][1:-1]))
                print(line)
            return self.onecmd(line)
        else:
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

    def help_update(self):
        """
        help for update syntax
        """
        print('Usage: update <class name> <id> ', end='')
        print('<attribute name> "<attribute value>"')

    def help_count(self):
        """
        help for count command
        """
        print('Usage: <class name>.count()')

    def help_all(self):
        """
        help for all command
        """
        print("Usage: all <class name> or $ all")

    def help_destroy(self):
        """
        help for destroy command
        """
        print("Usage: destroy <class name> <id>")

    def help_create(self):
        """
        help for create command
        """
        print("Usage: create <class name>")

    def help_show(self):
        """
        help for show command
        """
        print("Usage: show <class name> <id>")

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
        c = ["BaseModel", "User", "Place", "City", "State",
             "Amenity", "Review"]
        l = []
        if line is None or line == "":
            print("** class name missing **")
            return False
        arg = line.split()
        l = [i for i in c if i == arg[0]]
        if l == []:
            print("** class doesn't exist **")
            return False
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
        c = ["BaseModel", "User", "Place", "City", "State",
             "Amenity", "Review"]
        l = []
        if line is None or line == "":
            print("** class name missing **")
            return False
        arg = line.split()
        l = [i for i in c if i == arg[0]]
        if l == []:
            print("** class doesn't exist **")
            return False

        if len(arg) < 2:
            print("** instance id missing **")
            return False

        all_objs = storage.all()
        search = (arg[0] + "." + arg[1])
        try:
            ins = all_objs[search]
            print(ins)
        except KeyError:
            print("** no instance found **")
            return False

    def do_destroy(self, line):
        """
        deletes the instance of class
        """
        c = ["BaseModel", "User", "Place", "City", "State",
             "Amenity", "Review"]
        l = []
        if line is None or line == "":
            print("** class name missing **")
            return False
        arg = line.split()
        l = [i for i in c if i == arg[0]]
        if l == []:
            print("** class doesn't exist **")
            return False

        if len(arg) < 2:
            print("** instance id missing **")
            return False

        all_objs = storage.all()
        search = (arg[0] + "." + arg[1])
        try:
            del all_objs[search]
            storage.save()
        except KeyError:
            print("** no instance found **")
            return False

    def do_all(self, line):
        """
        display all instances of the same class
        """
        c = ["BaseModel", "User", "Place", "City", "State",
             "Amenity", "Review"]
        string = ""
        list_a = []
        l = []
        if line:
            arg = line.split()
            l = [i for i in c if i == arg[0]]
            if l == []:
                print("** class doesn't exist **")
                return False
        all_objs = storage.all()
        if l != []:
            for k, v in all_objs.items():
                if (k.split("."))[0] == arg[0]:
                    list_a.append(str(v))
            print(list_a)
        else:
            for k, v in all_objs.items():
                list_a.append(str(v))
            print(list_a)

    def do_count(self, line):
        """
        display number of instances of the same class
        """
        c = ["BaseModel", "User", "Place", "City", "State",
             "Amenity", "Review"]
        string = ""
        list_a = []
        l = []
        cnt = 0
        if line:
            arg = line.split()
            l = [i for i in c if i == arg[0]]
            if l == []:
                print("** class doesn't exist **")
                return False
        all_objs = storage.all()
        if l != []:
            for k, v in all_objs.items():
                if (k.split("."))[0] == arg[0]:
                    cnt += 1
        print(cnt)

    def do_update(self, line):
        """
        updates the new info to the existing instance
        """
        c = ["BaseModel", "User", "Place", "City",
             "State", "Amenity", "Review"]
        l = []
        if line is None or line == "":
            print("** class name missing **")
            return False
        arg = line.split()
        l = [i for i in c if i == arg[0]]
        if l == []:
            print("** class doesn't exist **")
            return False

        if len(arg) < 2:
            print("** instance id missing **")
            return False

        all_objs = storage.all()

        search = (arg[0] + "." + arg[1])
        try:
            ins = all_objs[search]
        except KeyError:
            print("** no instance found **")
            return False

        if len(arg) < 3:
            print("** attribute name missing **")
            return False
        if len(arg) < 4:
            print("** value missing **")
            return False

        if search in all_objs:
            setattr(all_objs[search], arg[2], arg[3][1:-1])

            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
