#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from shlex import split
from models import *
import json

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        return True
    do_EOF = do_quit

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create classes"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg == "BaseModel":
            o = BaseModel()
            o.save()
            print(o.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        line = split(line)
        dfo = storage.all()
        print(len(line))
        print(line)
        if len(line) == 0:
            print("** class name missing **")
            return
        print(line[0])
        print(type(line[0]))
        print(dfo)
        if line[0] in dfo:
            print("YES!!!!!!!!!!")
            items = dfo.items()
            print(items)
            if line[2] in items:
                #new_key = dfo
                print("YEAHH!")
            else:
                return
        else:
            print("** class doesn't exist **")

            #print(dfo[key].__class__.__name__)
#        if len(line) > 0:
           # for item in line:
            #    if item == "BaseModel":

            #        print("** class name missing **")

if __name__ == '__main__':
    cmd = HBNBCommand()
    cmd.cmdloop()
