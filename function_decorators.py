"""
In Python, we can define a function inside another function.
In Python, a function can be passed as parameter to another function (a function can also return another function).
"""
# A Python program to demonstrate that a function
# can be defined inside another function and a
# function can be passed as parameter.

# Adds a welcome message to the string


def messageWithWelcome(str):

    # Nested function
    def addWelcome():
        return "Welcome to "

    # Return concatenation of addWelcome()
    # and str.
    return addWelcome() + str

# To get site name to which welcome is added


def site(site_name):
    return site_name


print(messageWithWelcome(site("GeeksforGeeks")))
##########################################################
##########################################################
"""
A decorator is a function that takes a function as its only parameter and returns a function. This is helpful to “wrap” functionality with the same code over and over again. 
For example, above code can be re-written as following.
We use @func_name to specify a decorator to be applied on another function.
"""
# Adds a welcome message to the string
# returned by fun(). Takes fun() as
# parameter and returns welcome().


def decorate_message(fun):

    # Nested function
    def addWelcome(site_name):
        return "Welcome to " + fun(site_name)

    # Decorator returns a function
    return addWelcome


@decorate_message
def site(site_name):
    return site_name

# Driver code


# This call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter
print(site("GeeksforGeeks"))

###############################################################
###############################################################
# A Python example to demonstrate that
# decorators can be useful attach data

# A decorator function to attach
# data to func


def attach_data(func):
    func.data = 3
    return func


@attach_data
def add(x, y):
    return x + y

# Driver code


# This call is equivalent to attach_data()
# with add() as parameter
print(add(2, 3))

print(add.data)
