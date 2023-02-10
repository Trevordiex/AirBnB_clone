#!/usr/bin/python3
'''A module for the entry point of the command interpreter
'''

import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    indentchars = 4
    models = ["BaseModel", "User"]

    def emptyline(self):
        """Method called when an empty line is entered in response to prompt"""
        pass

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True
    do_quit = do_EOF

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg == "BaseModel":
            new = BaseModel()
        elif arg == "User":
            new = User()
        else:
            print("** class doesn't exist **")
            return
        new.save()
        print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on
           the class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            key = f'{args[0]}.{args[1]}'
            if key in all_obj:
                print(all_obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
            (save the change into the JSON file
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            key = f'{args[0]}.{args[1]}'
            if key not in all_obj:
                print("** no instance found **")
            else:
                all_obj.pop(key)
                storage.save()

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name
        """
        if arg:
            if arg not in models:
                print("** class doesn't exist **")
                return
        mods = []
        all_objs = storage.all()
        for i in all_objs.keys():
            obj = all_objs[i]
            mods.append(str(obj))
        print(mods)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
           by adding or updating attribute and save the changes
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = f'{args[0]}.{args[1]}'
        all_obj = storage.all()
        if key not in all_obj:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = all_obj[key]
            value = args[3].strip('"')
            setattr(obj, args[2], value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
