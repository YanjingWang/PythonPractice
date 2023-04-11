"""
print(value(s), sep= ' ', end = '\n', file=file, flush=flush)
Parameters: 

value(s): Any value, and as many as you like. Will be converted to a string before printed
sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
file : (Optional) An object with a write method. Default :sys.stdout
flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False
"""
# # This line will automatically add a new line before the
# # next print statement
# print ("GeeksForGeeks is the best platform for DSA content")
 
# # This print() function ends with "**" as set in the end argument.
# print ("GeeksForGeeks is the best platform for DSA content", end= "**")
# print("Welcome to GFG")
############################################################################
############################################################################
"""
flush Argument
The I/Os in python are generally buffered, meaning they are used in chunks. 
This is where flush comes in as it helps users to decide if they need the written content to be buffered or not. By default, it is set to false. 
If it is set to true, the output will be written as a sequence of characters one after the other. 
This process is slow simply because it is easier to write in chunks rather than writing one character at a time. 
To understand the use case of the flush argument in the print() function, let’s take an example.
"""
# import time
 
# count_seconds = 3
# for i in reversed(range(count_seconds + 1)):
#     if i > 0:
#         print(i, end='>>>') #3>>>2>>>1>>>Start
#         time.sleep(1)
#     else:
#         print('Start')

# import time
 
# count_seconds = 3
# for i in reversed(range(count_seconds + 1)):
#     if i > 0:
#         print(i, end='>>>', flush = True)
#         time.sleep(1)
#     else:
#         print('Start')

"""
seperator
"""
# a=12
# b=12
# c=2022
# print(a,b,c,sep="-")

"""
file Argument
Contrary to popular belief, the print() function doesn’t convert the messages into text on the screen. 
These are done by lower-level layers of code, that can read data(message) in bytes. 
The print() function is an interface over these layers, that delegates the actual printing to a stream or file-like object. 
By default, the print() function is bound to sys.stdout through the file argument. 
"""
# import io
 
# # declare a dummy file
# dummy_file = io.StringIO()
 
# # add message to the dummy file
# print('Hello Geeks!!', file=dummy_file) #'Hello Geeks!!\n'
 
# # get the value from dummy file
# dummy_file.getvalue()

"""
with print() function to write content directly to text file.
"""
# print('Welcome to GeeksforGeeks Python world.!!', file=open('Testfile.txt', 'w'))

"""
Using print() function in Python
"""
# # how to print data on
# # a screen
# # One object is passed
# print("GeeksForGeeks")
 
# x = 5
# # Two objects are passed
# print("x =", x)
 
# # code for disabling the softspace feature
# print('G', 'F', 'G', sep='')
 
# # using end argument
# print("Python", end='@')
# print("GeeksforGeeks")

"""
print() without new line
"""
# # Python 3 code for printing
# # on the same line printing
# # geeks and geeksforgeeks
# # in the same line
 
# print("geeks", end =" ")
# print("geeksforgeeks")
 
# # array
# a = [1, 2, 3, 4]
 
# # printing a element in same
# # line
# for i in range(4):
#     print(a[i], end =" ")

# # Print without newline in Python 3.x without using for loop
# l=[1,2,3,4,5,6]
# # using * symbol prints the list
# # elements in a single line
# print(*l)
# #This code is contributed by anuragsingh1022

"""
Output Formatting
Let’s take a look at the placeholders in our example.  

The first placeholder “%2d” is used for the first component of our tuple, i.e. the integer 1. The number will be printed with 2 characters. As 1 consists only of one digit, the output is padded with 1 leading blanks.
The second one “%5.2f” is a format description for a float number. Like other placeholders, it is introduced with the % character. This is followed by the total number of digits the string should contain. This number includes the decimal point and all the digits, i.e. before and after the decimal point.
Our float number 05.333 has to be formatted with 5 characters. The decimal part of the number or the precision is set to 2, i.e. the number following the “.” in our placeholder. Finally, the last character “f” of our placeholder stands for “float”.
"""
# # string modulo operator(%) to print
# # fancier output 
# # print integer and float value
# print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))
# # print integer value
# print("Total students : %3d, Boys : %2d" % (240, 120))
# # print octal value
# print("%7.3o" % (25))
# # print exponential value
# print("%10.3E" % (356.08977))
##############################################################
###############################################################
# # use of format() method 
# # using format() method
# print('I love {} for "{}!"'.format('Geeks', 'Geeks'))
# # using format() method and referring
# # a position of the object
# print('{0} and {1}'.format('Geeks', 'Portal'))
# print('{1} and {0}'.format('Geeks', 'Portal'))
# # the above formatting can also be done by using f-Strings
# # Although, this features work only with python 3.6 or above.
# print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
# # using format() method and referring
# # a position of the object
# print(f"{'Geeks'} and {'Portal'}")
##############################################################
###############################################################
# # a use of format() method
# # combining positional and keyword arguments
# print('Number one portal is {0}, {1}, and {other}.'
#      .format('Geeks', 'For', other ='Geeks')) 
# # using format() method with number
# print("Geeks :{0:2d}, Portal :{1:8.2f}".
#       format(12, 00.546)) 
# # Changing positional argument
# print("Second argument: {1:3d}, first one: {0:7.2f}".
#       format(47.42, 11))
# print("Geeks: {a:5d},  Portal: {p:8.2f}".
#      format(a = 453, p = 59.058))
##############################################################
###############################################################
# # show format() is used in dictionary
# tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678} 
# # using format() in dictionary
# print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
#     'Geeks: {0[geek]:d}'.format(tab))
# data = dict(fun ="GeeksForGeeks", adj ="Portal")
# # using format() in dictionary
# print("I love {fun} computer {adj}".format(**data))
##############################################################
###############################################################
# format a output using
# string() method
cstr = "I love geeksforgeeks"  
# Printing the center aligned 
# string with fillchr
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '#'))
# Printing the left aligned 
# string with "-" padding 
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))
# Printing the right aligned string
# with "-" padding 
print ("The right aligned string is : ")
print (cstr.rjust(40, '-'))