#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.base_model import BaseModel
from models.user import User 
from models.place import Place 
from models.review import Review 
from models.city import City 
from models.amenity import Amenity
from models.state import State
import os


classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "Review": Review,
           "City": City, "Amenity": Amenity,
           "State": State}

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
