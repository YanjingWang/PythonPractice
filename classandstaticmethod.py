"""
Class method vs Static Method
The difference between the Class method and the static method is:

A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.
When to use the class or static method?
We generally use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.
"""
# class method:
from datetime import date


class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


# Static method: Create an instance of MyClass
obj = MyClass(10)
# Call the get_value method on the instance
print(obj.get_value())  # Output: 10


class MyClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def get_max_value(x, y):
        return max(x, y)


# Create an instance of MyClass
obj = MyClass(10)
print(MyClass.get_max_value(20, 30))
print(obj.get_max_value(20, 30))

# Python program to demonstrate
# use of class method and static method.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
