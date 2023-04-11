"""When input() function executes program flow will be stopped until the user has given input.
The text or message displayed on the output screen to ask a user to enter an input value is optional i.e. the prompt, which will be printed on the screen is optional.
Whatever you enter as input, the input function converts it into a string. if you enter an integer value still input() function converts it into a string. You need to explicitly convert it into an integer in your code using typecasting. """
# name = input('What is your name?\n')     # \n ---> newline  ---> It causes a line break
# print(name)

# # input
# num1 = int(input())
# num2 = int(input())
# # printing the sum in integer
# print(num1 + num2)
# # input
# num1 = float(input())
# num2 = float(input()) 
# # printing the sum in float
# print(num1 + num2)
# # input
# string = str(input())
# # output
# print(string)


"""
Using split() method : 
This function helps in getting multiple inputs from users. It breaks the given input by the specified separator. 
If a separator is not provided then any white space is a separator. 
Generally, users use a split() method to split a Python string but one can use it in taking multiple inputs.
"""
# # multiple input using split
  
# # taking two inputs at a time
# x, y = input("Enter two values: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)
# print()
  
# # taking three inputs at a time
# x, y, z = input("Enter three values: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)
# print()
  
# # taking two inputs at a time
# a, b = input("Enter two values: ").split()
# print("First number is {} and second number is {}".format(a, b))
# print()
  
# # taking multiple inputs at a time 
# # and type casting using list() function
# x = list(map(int, input("Enter multiple values: ").split()))
# print("List of students: ", x)
#######################################################################
########################################################################
# # using List comprehension
# # taking two input at a time
# x, y = [int(x) for x in input("Enter two values: ").split()]
# print("First Number is: ", x)
# print("Second Number is: ", y)
# print()
  
# # taking three input at a time
# x, y, z = [int(x) for x in input("Enter three values: ").split()]
# print("First Number is: ", x)
# print("Second Number is: ", y)
# print("Third Number is: ", z)
# print()
  
# # taking two inputs at a time
# x, y = [int(x) for x in input("Enter two values: ").split()]
# print("First number is {} and second number is {}".format(x, y))
# print()
  
# # taking multiple inputs at a time 
# x = [int(x) for x in input("Enter multiple values: ").split()]
# print("Number of list is: ", x) 
#######################################################################
########################################################################

# taking multiple inputs at a time separated by comma
x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x) 


#####################################################################
#########################################################################
# Python program to take space
# separated input as a string
# split and store it to a list
# and print the string list
 
# input the list as string
string = input("Enter elements (Space-Separated): ")
 
# split the strings and store it to a list
lst = string.split() 
print('The list is:', lst)   # printing the list