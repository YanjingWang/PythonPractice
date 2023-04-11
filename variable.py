# # This function uses global variable s
# def f():
# 	s += 'GFG'
# 	print("Inside Function", s)


# # Global scope
# s = "I love Geeksforgeeks"
# f()

"""
We only need to use the global keyword in a function if we want to do assignments or change the global variable. 
global is not needed for printing and accessing. Python “assumes” that we want a local variable due to the assignment to s inside of f(), so the first statement throws the error message. 
Any variable which is changed or created inside of a function is local if it hasn’t been declared as a global variable. 
To tell Python, that we want to use the global variable, we have to use the keyword “global”, as can be seen in the following example: 
"""
# This function modifies the global variable 's'
def f():
	global s
	s += ' GFG'
	print(s)
	s = "Look for Geeksforgeeks Python Section"
	print(s)

# Global Scope
s = "Python is great!"
f()
print(s)

###############################################
###############################################
a = 1

# Uses global because there is no local 'a'
def f():
	print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
	a = 2
	print('Inside g() : ', a)

# Uses global keyword to modify global 'a'
def h():
	global a
	a = 3
	print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)

#####################################################################
#####################################################################
"""
Unpacking 
We can use * to unpack the list so that all elements of it can be passed as different parameters.
"""
# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
	print(a, b, c, d)

# Driver Code
my_list = [1, 2, 3, 4]

# Unpacking list into four arguments
fun(*my_list)

args = [3, 6]
range(*args)
######################################################################
######################################################################
"""
Packing 
When we don’t know how many arguments need to be passed to a python function, we can use Packing to pack all arguments in a tuple. 
"""
# A Python program to demonstrate use
# of packing

# This function uses packing to sum
# unknown number of arguments
def mySum(*args):
	return sum(args)

# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))

"""
Packing and Unpacking 
"""
# A Python program to demonstrate both packing and
# unpacking.

# A sample python function that takes three arguments
# and prints them
def fun1(a, b, c):
	print(a, b, c)

# Another sample function.
# This is an example of PACKING. All arguments passed
# to fun2 are packed into tuple *args.
def fun2(*args):

	# Convert args tuple to a list so we can modify it
	args = list(args)

	# Modifying args
	args[0] = 'Geeksforgeeks'
	args[1] = 'awesome'

	# UNPACKING args and calling fun1()
	fun1(*args)

# Driver code
fun2('Hello', 'beautiful', 'world!')

###################################################
####################################################
"""
** is used for dictionaries 
"""
# A sample program to demonstrate unpacking of
# dictionary items using **
def fun(a, b, c):
	print(a, b, c)

# A call with unpacking of dictionary
d = {'a':2, 'b':4, 'c':10}
fun(**d)

