#!/usr/bin/python3
"""Defines the BaseModel class."""
from uuid import uuid4
import datetime
import models


class BaseModel:
    """This is the BaseModel of the AirBnB project"""

    def __init__(self, *args, **kwargs):
        """
        Args and kwargs are used just incase
        out class gets input.
        """
        timeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()
        if len(kwargs) != 0:
            for firstArg, secondArg in kwargs.items():
                if firstArg == "created_at" or firstArg == "updated_at":
                    self.__dict__[firstArg] = datetime.strptime(
                        secondArg, timeFormat)
                else:
                    self.__dict__[firstArg] = secondArg
        else:
            models.storage.new(self)

        def save(self):
            """Update updated_at time stamp."""
            self.updated_at = datetime.datetime.now()
            models.storage.save()

        def to_dict(self):
            """Returns dictionary of BaseModel instances"""
            BSDict = self.__dict__.copy()
            BSDict["created_at"] = self.created_at
            BSDict["updated_at"] = self.updated_at
            BSDict["__class__"] = self.__class__.__name__
            return BSDict

        def __str__(self):
            """Return representation of the BaseModel class"""
            className = self.__class__.__name__
            return f"{className} {self.id} {self.__dict__}"
