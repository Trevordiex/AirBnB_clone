#!/usr/bin/python3
'''A module for the entry point of the command interpreter
'''

import cmd
import re
import json
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    indentchars = 4
    models = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        "State": State
    }

    def emptyline(self):
        """Method called when an empty line is entered in response to prompt"""
        pass

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True
    do_quit = do_EOF

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg not in self.models:
            print("** class doesn't exist **")
            return

        new = self.models[arg]()
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
        if args[0] not in self.models:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

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
        if args[0] not in self.models:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        all_obj = storage.all()
        key = f'{args[0]}.{args[1]}'
        if key not in all_obj:
            print("** no instance found **")
        else:
            all_obj.pop(key)
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
            based or not on the class name
        """
        if arg:
            if arg not in self.models:
                print("** class doesn't exist **")
                return
            items = storage.all().items()
            mods = [
                str(value) for key, value in items if key.startswith(f'{arg}.')
            ]
        else:
            mods = [str(obj) for obj in storage.all().values()]
        print(mods)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
           by adding or updating attribute and save the changes
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.models:
            print("** class doesn't exist **")
            return
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

    def default(self, line):
        '''when command is not defined explicitly'''
        args = line.split(".", maxsplit=1)
        klas = args[0]
        if klas in self.models:
            command = args[1]
            if command == "all()":
                return self.do_all(klas)
            elif command == "count()":
                total = len([
                    value for key, value in storage.all().items()
                    if key.startswith(f'{klas}.')
                    ])
                print(total)
            elif command.startswith('show('):
                print(command)
                m = re.search(r'show\((?P<argument>[^)]*)\)', command)
                parsed_args = f"{klas} {m.group('argument')}"
                return self.do_show(parsed_args)
            elif command.startswith('destroy('):
                m = re.search(r'destroy\((?P<argument>[^)]*)\)', command)
                parsed_args = f"{klas} {m.group('argument')}"
                return self.do_destroy(parsed_args)
            elif command.startswith('update('):
                m = re.search(r'update\((?P<argument>[^)]*)\)', command)
                # split the matched string into two. first string is the id
                # second string is the rest of the argument
                parsed_args = m.group('argument')
                parsed_args = [
                    s.strip(" ")
                    for s in parsed_args.split(",", maxsplit=1)
                ]
                if len(parsed_args) < 2:
                    print('** incomplete argument **')
                    return
                instance_id = parsed_args[0]
                parsed_args = parsed_args[1]
                if parsed_args.startswith("{"):
                    parsed_args = parsed_args.replace("'", '"')
                    arg_dict = json.loads(parsed_args)
                    for key, value in arg_dict.items():
                        self.do_update(f"{klas} {instance_id} {key} {value}")
                else:
                    key_val_string = " ".join(parsed_args.split(","))
                    self.do_update(
                        f"{klas} {instance_id}" + " " + key_val_string
                    )
            else:
                print(f"** unsupported command: {command}")

        else:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
