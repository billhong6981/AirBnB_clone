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
        c = ["BaseModel", "User", "Place", "City", "State", "Amenity", "Review"]
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
        c = ["BaseModel", "User", "Place", "City", "State", "Amenity", "Review"]
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
        c = ["BaseModel", "User", "Place", "City", "State", "Amenity", "Review"]
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
            storage.save() #obj.save()
        except KeyError:
            print("** no instance found **")
            return False

    def do_all(self, line):
        """
        display all instances of the same class
        """
        c = ["BaseModel", "User", "Place", "City", "State", "Amenity", "Review"]
        string = ""
        list_a = []
        l = []
        if line is not None and line != "":
            arg = line.split()
            l = [i for i in c if i == arg[0]]
            if l == []:
                print("** class doesn't exist **")
                return False
        all_objs = storage.all()
        for k, v in all_objs.items():
            list_a.append(str(v))
        print(list_a)

    def do_update(self, line):
        """
        updates the new info to the existing instance
        """
        c = ["BaseModel", "User", "Place", "City", "State", "Amenity", "Review"]
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
        #all_objs = storage.objects
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
            #obj.save()
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
