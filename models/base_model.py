#!/usr/bin/python3
""" Base model"""
import datetime
import uuid
from models import storage

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Initialization of  Base Model """
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value, time)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = self.created_at
                storage.new(self)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        """str [<class name>] (<self.id>) <self.__dict__> """
        return "[[{}] ({}) {}]".format(self.__class__.__name__, self.id,
                                       self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime  """
        self.updated_at = datetime.datetime.utcnow()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""
        dict = self.__dict__.copy()
        if "created_at" in dict:
            dict["created_at"] = dict["created_at"].strftime(time)
        if "updated_at" in dict:
            dict["updated_at"] = dict["updated_at"].strftime(time)
        dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
