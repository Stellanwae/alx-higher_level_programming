#!/usr/bin/python3
"""
class "Student"
"""


class Student:
    """The student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representationStudent instance
        with specified attributes"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except Exception:
                pass
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except Exception:
                pass
