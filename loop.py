# """
# Ways1: Using enumerate():  enumerate() is used to loop through the containers printing the index number along with the value present in that particular index.
# """
# # python code to demonstrate working of enumerate()

# for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
# 	print(key, value)

# # python code to demonstrate working of enumerate()

# for key, value in enumerate(['Geeks', 'for', 'Geeks',
# 							'is', 'the', 'Best',
# 							'Coding', 'Platform']):
# 	print(value, end=' ')
# ###############################################################
# ###############################################################
# """
# Way2: Using zip(): zip() is used to combine 2 similar containers(list-list or dict-dict) printing the values sequentially. The loop exists only till the smaller container ends. A detailed explanation of zip() and enumerate() can be found here.
# """
# # python code to demonstrate working of zip()

# # initializing list
# questions = ['name', 'colour', 'shape']
# answers = ['apple', 'red', 'a circle']

# # using zip() to combine two containers
# # and print values
# for question, answer in zip(questions, answers):
# 	print('What is your {0}? I am {1}.'.format(question, answer))
# """
# Way 3: Using iteritem(): iteritems() is used to loop through the dictionary printing the dictionary key-value pair sequentially which is used before Python 3 version.
# Way 4: Using items(): items() performs the similar task on dictionary as iteritems() but have certain disadvantages when compared with iteritems().
# It is very time-consuming. Calling it on large dictionaries consumes quite a lot of time.
# It takes a lot of memory. Sometimes takes double the memory when called on a dictionary.
# """
# # python code to demonstrate working of items()

# d = {"geeks": "for", "only": "geeks"}

# # iteritems() is renamed to items() in python3
# # using items to print the dictionary key-value pair
# print("The key value pair using items is : ")
# for i, j in d.items():
# 	print(i, j)
# ############################################################
# ############################################################
# # python code to demonstrate working of items()

# king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya',
# 		'Modi': 'The Changer'}

# # using items to print the dictionary key-value pair
# for key, value in king.items():
# 	print(key, value)
# """
# Way 5: Using sorted():  sorted() is used to print the container is sorted order. It doesn’t sort the container but just prints the container in sorted order for 1 instance. 
# The use of set() can be combined to remove duplicate occurrences.
# """
# # python code to demonstrate working of sorted()

# # initializing list
# lis = [1, 3, 5, 6, 2, 1, 3]

# # using sorted() to print the list in sorted order
# print("The list in sorted order is : ")
# for i in sorted(lis):
# 	print(i, end=" ")

# print("\r")

# # using sorted() and set() to print the list in sorted order
# # use of set() removes duplicates.
# print("The list in sorted order (without duplicates) is : ")
# for i in sorted(set(lis)):
# 	print(i, end=" ")
# #################################################################################
# #################################################################################
# # python code to demonstrate working of sorted()

# # initializing list
# basket = ['guave', 'orange', 'apple', 'pear',
# 		'guava', 'banana', 'grape']

# # using sorted() and set() to print the list
# # in sorted order
# for fruit in sorted(set(basket)):
# 	print(fruit)
# ##################################################################################
# ##################################################################################
# """
# Way 6: Using reversed(): reversed() is used to print the values of the container in the reversed order. It does not reflect any changes to the original list
# """
# # python code to demonstrate working of reversed()

# # initializing list
# lis = [1, 3, 5, 6, 2, 1, 3]


# # using reversed() to print the list in reversed order
# print("The list in reversed order is : ")
# for i in reversed(lis):
# 	print(i, end=" ")


# # python code to demonstrate working of reversed()

# # using reversed() to print in reverse order
# for i in reversed(range(1, 10, 3)):
# 	print(i)

#################################################################
#################################################################
###https://www.geeksforgeeks.org/range-vs-xrange-in-python/
# Python code to demonstrate range() vs xrange()
# on basis of return type

# initializing a with range()
a = range(1,10000)
# testing the type of a
print ("The return type of range() is : ")
print (type(a))

#######################################################################
#######################################################################
"""
Patterns can be printed in python using simple for loops. 
First outer loop is used to handle the number of rows and the Inner nested loop is used to handle the number of columns. 
Manipulating the print statements, different number patterns, alphabet patterns, or star patterns can be printed. 
"""
###https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
	
	# outer loop to handle number of rows
	# n in this case
	for i in range(0, n):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ",end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
pypart(n)

#################################################################
#################################################################
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
	myList = []
	for i in range(1,n+1):
		myList.append("*"*i)
	print("\n".join(myList))

# Driver Code
n = 5
pypart(n)
##################################################################
##################################################################
#python3 code to print pyramid pattern using recursion
def pypart(n):
	if n==0:
		return
	else:
		pypart(n-1)
		print("* "*n)

# Driver Code
n = 5
pypart(n)
#######################################################################
#######################################################################
# python3 code to print pyramid pattern using while loop

# input
n=5

i=1;j=0
# while loop check the condition until the
# condition become false. if it is true then
# enter in to loop and print the pattern
while(i<=n):
	while(j<=i-1):
		print("* ",end="")
		j+=1
	# printing next line for each row
	print("\r")
	j=0;i+=1

########################################################################
########################################################################
# python3 code to print pyramid pattern using while loop

# input
n=5

i=1;j=0
# while loop check the condition until the
# condition become false. if it is true then
# enter in to loop and print the pattern
while(i<=n):
	while(j<=i-1):
		print("* ",end="")
		j+=1
	# printing next line for each row
	print("\r")
	j=0;i+=1
########################################################################
#########################################################################
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart2(n):
	
	# number of spaces
	k = 2*n - 2

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 2
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
pypart2(n)

#####################################################
#####################################################
# python3 code to print pyramid pattern using while loop
n=5;i=0
while(i<=n):
	print(" " * (n - i) +"*" * i)
	i+=1
#######################################################
#######################################################
#python3 code to implement above approach
height = 5
for row in range(1, height+ 1):
	print(" " * (height - row) +"*" * row)
#########################################################
#########################################################
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
triangle(n)
#####################################################################
#####################################################################
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
def numpat(n):
	
	# initialising starting number
	num = 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# re assigning num
		num = 1
	
		# inner loop to handle number of columns
			# values changing acc. to outer loop
		for j in range(0, i+1):
		
				# printing number
			print(num, end=" ")
		
			# incrementing number at each column
			num = num + 1
	
		# ending line after each row
		print("\r")

# Driver code
n = 5
numpat(n)
#####################################################################
#####################################################################
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
def contnum(n):
	
	# initializing starting number
	num = 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# not re assigning num
		# num = 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing number
			print(num, end=" ")
		
			# incrementing number at each column
			num = num + 1
	
		# ending line after each row
		print("\r")

n = 5

# sending 5 as argument
# calling Function
contnum(n)
##############################################################
##############################################################
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of alphabets
def alphapat(n):
	
	# initializing value corresponding to 'A'
	# ASCII value
	num = 65

	# outer loop to handle number of rows
	# 5 in this case
	for i in range(0, n):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# explicitly converting to char
			ch = chr(num)
		
			# printing char value
			print(ch, end=" ")
	
		# incrementing number
		num = num + 1
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
alphapat(n)
#########################################################################
#########################################################################
# Python code 3.x to demonstrate star pattern

# Function to demonstrate printing pattern of alphabets


def contalpha(n):

	# initializing value corresponding to 'A'
	# ASCII value
	num = 65


	# outer loop to handle number of rows
	for i in range(0, n):

	# inner loop to handle number of columns
	# values changing acc. to outer loop
		for j in range(0, i+1):

			# explicitly converting to char
			ch = chr(num)

			# printing char value
			print(ch, end=" ")

			# incrementing at each column
			num = num + 1

		# ending line after each row
		print("\r")

# Driver code
n = 5
contalpha(n)











