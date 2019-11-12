#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        return True
    do_EOF = do_quit

    def emptyline(self):
        pass

if __name__ == '__main__':
    cmd = HBNBCommand()
    cmd.cmdloop()
