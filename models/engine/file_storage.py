#!/usr/bin/python3
import json
from datetime import datetime
from models import *


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        self.reload()

    def all(self, cls=None):
        my_obj = {}
        if cls is None:
            return FileStorage.__objects
        else:
            for name in FileStorage.__objects.__class__:
                my_name = FileStorage.__objects.__class__.__name__
                if my_name == cls:
                    my_obj.update(my_name)
            return my_obj

    def new(self, obj):
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

    def save(self):
        store = {}
        for k in FileStorage.__objects.keys():
            store[k] = FileStorage.__objects[k].to_json()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as fd:
            fd.write(json.dumps(store))

    def reload(self):
        try:
            with open(FileStorage.__file_path,
                      mode="r+", encoding="utf-8") as fd:
                FileStorage.__objects = {}
                temp = json.load(fd)
                for k in temp.keys():
                    cls = temp[k].pop("__class__", None)
                    cr_at = temp[k]["created_at"]
                    cr_at = datetime.strptime(cr_at, "%Y-%m-%d %H:%M:%S.%f")
                    up_at = temp[k]["updated_at"]
                    up_at = datetime.strptime(up_at, "%Y-%m-%d %H:%M:%S.%f")
                    FileStorage.__objects[k] = eval(cls)(temp[k])
        except Exception as e:
            pass

    def delete(self, obj=None):
        FileStorage.__objects.pop(obj, None)

    def close(self):
        self.reload()
