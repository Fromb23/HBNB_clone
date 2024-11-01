#!/usr/bin/python3
import sys
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """HBNB Command Interpreter"""
    class_dict = {
            "BaseModel": BaseModel,
            "Rombo": "Rombo"
            }

    prompt = '(hbnb) '

    def do_create(self, obj):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not obj:
            print("** class name missing **")
            return
        if obj in self.class_dict:
            self.new_instance = self.class_dict[obj]()
            self.new_instance.save()
            print(self.new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        obj = arg.split()

        if len(obj) < 1:
            print("** class name is missing **")
            return
        elif len(obj) < 2:
            print("** instance id missing **")
            return

        key = obj[0] + '.' + obj[1]
        filestorage = FileStorage()
        if key in filestorage.all():
            print(f"{filestorage.all()[key]}")
        else:
            print("** class doesn't exist **")

    def do_quit(self, obj):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, obj):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing"""
        pass

    def help_quit(self):
        """Help for quit command"""
        print("Quit the program.")

    def help_EOF(self):
        """Help for EOF command"""
        print("Exit on EOF (Ctrl+D).")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
