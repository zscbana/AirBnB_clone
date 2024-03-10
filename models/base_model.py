#!/usr/bin/python3
""" Base model"""
import datetime
import uuid
from models import storage

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Initialization of  Base Model """
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

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
