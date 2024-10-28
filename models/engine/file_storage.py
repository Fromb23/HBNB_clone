#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os

class FileStorage():
    __file_path = os.path.join(os.getcwd(), 'file.json')
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON format and save to a file."""
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, 'r') as file:
                    existing_data = json.load(file)
            else:
                existing_data = {}
            existing_data = {key: obj.to_dict() for key, obj in self.__objects.items()}
            with open(self.__file_path, 'w') as file:
                json.dump(existing_data, file)
        except Exception as e:
            print(f"Error loading from file: {e}")

    def reload(self):
        """Deserializes the JSON file to `__objects`, if it exists."""
        if os.path.exists(self.__file_path):
            try:
                    with open(self.__file_path, 'r') as file:
                        data = json.load(file)
                        for key, obj in data.items():
                            class_name = obj["__class__"]
                            self.__objects[key] = eval(class_name)(**obj)
            except Exception as e:
                print("There's nothing here")

