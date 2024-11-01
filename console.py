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

    filestorage = FileStorage()

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
        if key in self.filestorage.all():
            print(f"{self.filestorage.all()[key]}")
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        obj = arg.split()

        if len(obj) < 1:
            print("** class name is missing **")
            return
        elif len(obj) < 2:
            print("** instance id missing **")
            return

        key = obj[0] + '.' + obj[1]

        if key in self.filestorage.all():
            del self.filestorage.all()[key]
            self.filestorage.save()

    def do_all(self, arg):
        obj = arg.split()

        if len(obj) < 1:
            print("** class name missing **")
            return

        print(self.filestorage.all())

    def do_update(self, arg):
        obj = arg.split()

        if len(obj) < 1:
            print("** class name missing **")
            return
        else:
            if obj[0] not in self.class_dict:
                print("** class doesn't exist **")
                return
            
        if len(obj) < 2:
            print("** instance id missing **")
            return
        else:
            key = obj[0] + '.' + obj[1]
            if key not in self.filestorage.all():
                print("** no instance found **")
                return
            else:
                pass

        if len(obj) < 3:
            print("** attribute name missing **")
            return
        elif len(obj) < 4:
            print("** value missing **")
            return

        new_attr = {}
        new_attr[obj[2]] = obj[3]

        if key in self.filestorage.all():
            basemodel_dict = self.filestorage.all()[key]
            my_dict = basemodel_dict.__dict__
            my_dict.update(new_attr)
            print(basemodel_dict)
            self.filestorage.save()

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
