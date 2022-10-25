#!/usr/bin/python3
class Student:
    """
    a class Student that defines a student by:

    Public instance attributes:
    first_name
    last_name
    age

    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    Public method def to_json(self):
    that retrieves a dictionary representation of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        init method that initialise attributes of Student class

        Args:
            first_name (str):
            last_name (str):
            age (str):

        Return:
            dictionary representation of a Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        a function that retrieves a dictionary representation of a
        Student instance

        Return:
            dictionary representation of a Student instance
        """
        dict_ = self.__dict__
        return dict_
