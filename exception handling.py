# """
# Code, raise error but we don’t have any except clause to handle it. So, clean-up action is taken first and then the error(by default) is raised by the compiler.
# """
# # Python code to illustrate
# # clean up actions


# def divide(x, y):
#     try:
#         # Floor Division : Gives only Fractional Part as Answer
#         result = x // y
#     except ZeroDivisionError:
#         print("Sorry ! You are dividing by zero ")
#     else:
#         print("Yeah ! Your answer is:", result)
#     finally:
#         print("I'm finally clause, always raised !! ")


# # Look at parameters and note the working of Program
# divide(3, "3")

# ###########################################################################
# # user-defined exception: https://www.geeksforgeeks.org/user-defined-exceptions-python-examples/

# # A python program to create user-defined exception
# # class MyError is derived from super class Exception
# class MyError(Exception):

# 	# Constructor or Initializer
# 	def __init__(self, value):
# 		self.value = value

# 	# __str__ is to print() the value
# 	def __str__(self):
# 		return(repr(self.value))


# try:
# 	raise(MyError(3*2))

# # Value of Exception is stored in error
# except MyError as error:
# 	print('A New Exception occurred: ', error.value)


# 1.User-Defined class with Multiple Inheritance
# define Python user-defined exceptions
# we have created a class named “Error” derived from the class Exception.
# This base class is inherited by various user-defined classes to handle different types of python raise an exception with message
class Error(Exception):
    """Base class for other exceptions"""
    pass


class zerodivision(Error):
    """Raised when the input value is zero"""
    pass


try:
    i_num = int(input("Enter a number: "))
    if i_num == 0:
        raise zerodivision
except zerodivision:
    print("Input value is zero, try again!")
    print()

# 2.Deriving Error from Super Class Exception
# Superclass Exceptions are created when a module needs to handle several distinct errors.
# One of the common ways of doing this is to create a base class for exceptions defined by that module.
# Further, various subclasses are defined to create specific exception classes for different error conditions.
# class Error is derived from super class Exception


class Error(Exception):

    # Error is derived class for Exception, but
    # Base class for exceptions in this module
    pass


class TransitionError(Error):

    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.next = nex

        # Error message thrown is saved in msg
        self.msg = msg


try:
    raise (TransitionError(2, 3*2, "Not Allowed"))

# Value of Exception is stored in error
except TransitionError as error:
    print('Exception occurred: ', error.msg)

######################################################
# 3. use standard Exceptions as a base class
# A runtime error is a class that is a standard exception that is raised when a generated error does not fall into any category.
# This program illustrates how to use runtime error as a base class and network error as a derived class.
# In a similar way, an exception can be derived from the standard exceptions of Python.
# NetworkError has base RuntimeError
# and not Exception


class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Error")

except Networkerror as e:
    print(e.args)
