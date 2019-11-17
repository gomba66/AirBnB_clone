#!/usr/bin/python3
import cmd
import json
from shlex import split
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    dict_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                    "City": City, "Amenity": Amenity, "Place": Place,
                    "Review": Review}

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        return True
    do_EOF = do_quit

    def emptyline(self):
        pass

    def do_create(self, line):
        """Create classes"""
        line = split(line)
        if len(line) == 0:
            print("** class name missing **")
            return
        if line[0] in self.dict_classes:
                o = self.dict_classes[line[0]]()
                o.save()
                print(o.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Command for show an object """
        c = False
        all_objs = storage.all()
        line = split(line)
        if len(line) == 2:
            if line[0] in self.dict_classes:
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    if line[1] == obj.id:
                        print(obj)
                        c = True
                        break
                    else:
                        c = False
                if c == False:
                    print("** no instance found **")
            else:
                print("** no instance found **")
        elif len(line) == 1:
            if line[0] in self.dict_classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):

        c = False
        all_objs = storage.all()
        line = split(line)
        if len(line) == 2:
            if line[0] in self.dict_classes:
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    if line[1] == obj.id:
                        del all_objs[obj_id]
                        obj.save()
                        c = True
                        break
                    else:
                        c = False
                if c == False:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(line) == 1:
            if line[0] in self.dict_classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        list_objs = []
        all_objs = storage.all()
        line = split(line)
        if len(line) == 0:
            for key_id in all_objs.keys():
                item = all_objs[key_id]
                item = str(item)
                list_objs.append(item)
            print(list_objs)
        else:
            c = False
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                if line[0] == obj.__class__.__name__:
                    list_objs.append(str(obj))
                    c = True
            if c == False:
                print("** class doesn't exist **")
                return
            print(list_objs)

if __name__ == '__main__':
    cmd = HBNBCommand()
    cmd.cmdloop()
