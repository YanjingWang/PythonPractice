# def hello_func():
#     pass
#
#
# hello_func()
# print(hello_func)  # in certain location in memory
# print(hello_func())  # no return value


def hello_func():
    print('hello function!')


hello_func()  # reuse code, keeping your code dry


def hola_function():
    return 'hola function.'


hola_function()  # just give string instead of doing anything else
# just give string instead of doing anything else, so we need print to execute it
print(hola_function().upper())


# we treat return value as datetype it is

def ciao_function(greeting, name='you'):
    return '{}, {} function.'.format(greeting, name)


print(ciao_function('ciao'))
print(ciao_function('ciao', name='Corey'))


def student_ifo(*args, **kwargs):
    print(args)  # tuple
    print(kwargs)  # keyword dictionary


courses = ['math', 'art']
info = {'name': 'john', 'age': 22}
student_ifo('math', 'art', name='John', age=22)

student_ifo(*courses, **info)  # unpack the list and dictionary value

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]


print(is_leap(2017))
print(days_in_month(2017, 2))
#############################################################################
# https://www.geeksforgeeks.org/python-functions/
############


def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True


print(is_prime(78), is_prime(79))

##### Variable-length arguments: *args (Non-Keyword Arguments) **kwargs (Keyword Arguments)###############
# Python program to illustrate *args for variable number of arguments


def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

#################### Docstring################################################
# A simple Python function to check
# whether x is even or odd


def evenOdd(x):
    """Function to check if the number is even or odd"""

    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code to call the function
print(evenOdd.__doc__)
################### return statement##########################################
"""The function return statement is used to exit from a function and go back to the function caller and return the specified value or data item to the caller. 
The return statement can consist of a variable, an expression,
or a constant which is returned to the end of the function execution. If none of the above is present with the return statement a None object is returned.
"""
################## Anonymous functions in Python Function######################
"""Anonymous function means that a function is without a name. 
The lambda keyword is used to create anonymous functions."""
def cube(x): return x*x*x


def cube_v2(x): return x*x*x


print(cube(7))
print(cube_v2(7))
################## Python Function within Functions###########################
"""
A function that is defined inside another function is known as the inner function or nested function. 
Nested functions are able to access variables of the enclosing scope.
Inner functions are used so that they can be protected from everything happening outside the function.
"""


def f1():
    s = 'I love GeeksforGeeks'

    def f2():
        print(s)
    f2()


# Driver's code
f1()

"""
args: definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list. 
kwargs:The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is that the double star allows us to pass through keyword arguments (and any number of them).

A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
"""


def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

############################################################


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')
# first == Geeks
# mid == for
# last == Geeks


def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun("Hi", first='Geeks', mid='for', last='Geeks')
# first == Geeks
# mid == for
# last == Geeks
